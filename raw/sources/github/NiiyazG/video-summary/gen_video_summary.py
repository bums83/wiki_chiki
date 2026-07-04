#!/usr/bin/env python3
"""
Скрипт генерации видео-обзора: сценарий → PNG кадры → MP4.

Использование:
  python3 gen_video_summary.py --source "текст" [--title "Заголовок"] [--no-tts]

Зависимости: Pillow, numpy, requests, ffmpeg
"""

import argparse
import json
import os
import subprocess
import sys
import textwrap
import time
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ Установи Pillow: pip install --break-system-packages Pillow")
    sys.exit(1)

# ─── Конфигурация ────────────────────────────────────────────────────

WIDTH, HEIGHT = 1080, 1920  # 9:16 vertical
BG_COLOR = (13, 13, 15)  # #0D0D0F
TITLE_COLOR = (100, 181, 246)  # #64B5F6
TEXT_COLOR = (255, 255, 255)
MUTED_COLOR = (112, 116, 120)
ACCENT_LINE_COLOR = (100, 181, 246)

OUTPUT_DIR = Path.home() / "video-summary"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ─── Шрифты ──────────────────────────────────────────────────────────

FONT_DIRS = [
    "/usr/share/fonts/truetype/ubuntu/",
    "/usr/share/fonts/truetype/dejavu/",
    "/usr/share/fonts/",
]


def find_font(name_pattern):
    """Ищет шрифт по паттерну в системных директориях."""
    for d in FONT_DIRS:
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            # Ubuntu вариативные шрифты: имя[Bold][wdth,wght].ttf → проверяем без [ ]
            f_lower = f.lower().split("[")[0]
            if name_pattern in f_lower and f.endswith((".ttf", ".otf")):
                return os.path.join(d, f)
    return None


FONT_BOLD = find_font("dejavusans-bold") or find_font("bold") or find_font("b.ttf")
FONT_BOLD = FONT_BOLD or find_font("dejavuserif-bold")

FONT_REG = find_font("regular") or find_font("r.ttf")
FONT_REG = FONT_REG or find_font("dejavusans")

FONT_LIGHT = find_font("thin") or find_font("th.ttf") or find_font("light")
FONT_LIGHT = FONT_LIGHT or FONT_REG

print(f"  Font bold: {FONT_BOLD}")
print(f"  Font reg:  {FONT_REG}")
print(f"  Font light: {FONT_LIGHT}")


def get_font(path, size):
    """Загружает шрифт с fallback на дефолтный."""
    try:
        return ImageFont.truetype(path, size) if path else ImageFont.load_default()
    except (OSError, IOError):
        return ImageFont.load_default()


# ─── Рендер кадра ────────────────────────────────────────────────────

def render_scene(scene, scene_num, total_scenes):
    """Рисует один кадр сцены. Возвращает путь к PNG."""
    frame = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(frame)

    # Номер сцены (мелко, сверху)
    font_small = get_font(FONT_LIGHT, 32)
    scene_label = f"{scene_num:02d} / {total_scenes:02d}"
    draw.text((60, 50), scene_label, fill=MUTED_COLOR, font=font_small)

    # Заголовок (крупно, жирно)
    title = scene.get("title", "")
    font_title = get_font(FONT_BOLD, 64)
    title_y = 320

    # Разбиваем длинный заголовок на строки
    title_lines = textwrap.wrap(title, width=28) if len(title) > 28 else [title]
    for line in title_lines:
        draw.text((80, title_y), line, fill=TITLE_COLOR, font=font_title)
        title_y += 74

    # Акцентная линия под заголовком
    line_y = title_y + 16
    draw.rectangle([80, line_y, 220, line_y + 3], fill=ACCENT_LINE_COLOR)

    # Тезисы
    bullets = scene.get("bullets", [])
    font_text = get_font(FONT_REG, 44)
    text_y = line_y + 60

    for bullet in bullets[:4]:  # макс 4 тезиса
        # Перенос длинных тезисов
        wrapped = textwrap.wrap(bullet, width=38)
        for i, line in enumerate(wrapped[:2]):  # макс 2 строки на тезис
            prefix = "• " if i == 0 else "  "
            draw.text((80, text_y), prefix + line, fill=TEXT_COLOR, font=font_text)
            text_y += 52
        text_y += 16  # отступ между тезисами

        if text_y > HEIGHT - 120:
            break  # не вылезаем за край

    # Футер — бренд
    font_footer = get_font(FONT_LIGHT, 24)
    draw.text((80, HEIGHT - 70), "© Гарипов Нияз Варисович t.me/ML_DS_one", fill=MUTED_COLOR, font=font_footer)

    # Сохраняем
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"frame_{scene_num:03d}.png"
    filepath = OUTPUT_DIR / filename
    frame.save(filepath, "PNG")
    return str(filepath)


def render_all_scenes(scenes):
    """Рендерит все сцены, возвращает список путей к PNG."""
    total = len(scenes)
    paths = []
    print(f"\n🎬 Рендеринг {total} кадров...")
    for i, scene in enumerate(scenes, 1):
        path = render_scene(scene, i, total)
        paths.append(path)
        print(f"  [{i}/{total}] ✓ {os.path.basename(path)}")
    return paths


# ─── Сборка видео ────────────────────────────────────────────────────

def build_video_from_segments(scene_audio_paths, frame_paths, output_path):
    """
    Собирает видео из кадров с посценовой озвучкой.
    Каждый кадр идёт столько, сколько длится его аудио-сегмент.
    """
    if not frame_paths:
        return None
    
    n = len(frame_paths)
    if not scene_audio_paths or len(scene_audio_paths) != n:
        # Фолбэк на старый метод
        return build_video(frame_paths, None, 6)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    segments = []
    
    try:
        for i, (frame, audio) in enumerate(zip(frame_paths, scene_audio_paths)):
            seg_video = OUTPUT_DIR / f"seg_{timestamp}_{i:03d}.mp4"
            
            if audio and os.path.exists(audio):
                # Получаем длительность аудио
                result = subprocess.run(
                    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "default=noprint_wrappers=1:nokey=1", audio],
                    capture_output=True, text=True, timeout=10
                )
                dur = float(result.stdout.strip())
                
                # Кадр длится ровно столько же, сколько аудио (но не меньше 2 сек)
                dur = max(2, dur)
                
                # Собираем сегмент: кадр + аудио
                subprocess.run([
                    "ffmpeg", "-y",
                    "-loop", "1", "-i", frame,
                    "-i", audio,
                    "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-t", str(dur),
                    "-r", "30",
                    "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2",
                    "-c:a", "aac",
                    "-shortest",
                    str(seg_video)
                ], check=True, capture_output=True, text=True)
            else:
                # Без звука — просто кадр на 5 сек
                subprocess.run([
                    "ffmpeg", "-y",
                    "-loop", "1", "-i", frame,
                    "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-t", "5",
                    "-r", "30",
                    "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2",
                    str(seg_video)
                ], check=True, capture_output=True, text=True)
            
            segments.append(str(seg_video))
        
        # Склеиваем все сегменты
        concat_list = OUTPUT_DIR / f"concat_seg_{timestamp}.txt"
        with open(concat_list, "w") as f:
            for seg in segments:
                f.write(f"file '{seg}'\n")
        
        subprocess.run([
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(concat_list),
            "-c:v", "copy",
            "-c:a", "aac",
            output_path
        ], check=True, capture_output=True, text=True)
        
        total_dur = 0
        for seg in segments:
            r = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", seg],
                capture_output=True, text=True, timeout=5
            )
            total_dur += float(r.stdout.strip())
        
        print(f"  ✓ Видео собрано из {n} сегментов, общая длительность {total_dur:.1f} сек")
        
        # Чистим временные сегменты
        for seg in segments:
            try: os.remove(seg)
            except OSError: pass
        try: os.remove(concat_list)
        except OSError: pass
        
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"  ✓ Видео готово: {output_path} ({size_mb:.1f} MB)")
        return output_path
        
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg ошибка при сборке сегментов: {e.stderr[-500:] if e.stderr else ''}")
        return None


# ─── TTS (заглушка) ──────────────────────────────────────────────────

def generate_tts(text, output_path):
    """Генерирует аудио через TTS провайдер.
    Приоритет: gTTS → edge-tts → OpenAI.
    Возвращает путь к аудиофайлу или None."""
    
    # 1. gTTS (Google, работает из РФ, бесплатно)
    try:
        from gtts import gTTS
        tts = gTTS(text, lang='ru', slow=False)
        # Сохраняем во временный файл, потом переименовываем в output_path
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            tmp_path = f.name
        tts.save(tmp_path)
        os.rename(tmp_path, output_path)
        print(f"  ✓ TTS: gTTS (ru, {os.path.getsize(output_path)} bytes)")
        return output_path
    except Exception as e:
        print(f"  ⚠️ gTTS не сработал: {e}")

    # 2. edge-tts
    try:
        result = subprocess.run(
            ["which", "edge-tts"], capture_output=True, text=True
        )
        if result.returncode == 0:
            cmd = [
                "edge-tts",
                "--text", text,
                "--voice", "ru-RU-DariyaNeural",
                "--write-media", output_path
            ]
            subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=120)
            print("  ✓ TTS: edge-tts (ru-RU-DariyaNeural)")
            return output_path
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        print(f"  ⚠️ edge-tts не сработал: {e}")

    print("  ⚠️ TTS недоступен: ни gTTS, ни edge-tts не сработали")
    return None


# ─── Генерация сценария через DeepSeek ──────────────────────────────

def generate_script_from_source(source_text, title=None):
    """Передаёт текст в DeepSeek и получает JSON сценарий.
    Заглушка — реальный вызов делает агент.
    Возвращает dict со сценарием."""
    # Этот метод вызывается агентом, который передаёт результат DeepSeek
    # Реализация — в навыке (агент генерирует JSON через LLM)
    print("ℹ️ Генерация сценария выполняется агентом Hermes (DeepSeek)")
    print("   Этот скрипт принимает готовый JSON через --script-file")
    return None


# ─── Главная ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Генерация видео-обзора")
    parser.add_argument("--source", type=str, help="Текст статьи/источника")
    parser.add_argument("--title", type=str, help="Заголовок видео")
    parser.add_argument("--script-file", type=str, help="Готовый JSON-файл сценария")
    parser.add_argument("--no-tts", action="store_true", help="Без озвучки")
    parser.add_argument("--duration", type=int, default=6, help="Секунд на кадр (по умолч. 6)")
    parser.add_argument("--output", type=str, help="Путь к выходному MP4")
    args = parser.parse_args()

    print("🎥 Video Summary Generator")
    print("=" * 50)

    # 1. Загружаем сценарий
    scenes = None
    overall_audio_text = ""

    if args.script_file:
        with open(args.script_file, "r", encoding="utf-8") as f:
            script = json.load(f)
        scenes = script.get("scenes", [])
        overall_audio_text = script.get("overall_audio", "")
        title = script.get("title", args.title or "Видео-обзор")
    elif args.source:
        print("\n📝 Пожалуйста, передайте сценарий через --script-file")
        print("   Сценарий генерируется агентом (DeepSeek).")
        print("   Запустите в Hermes: сделай видео-обзор по тексту")
        return
    else:
        print("❌ Укажите --source или --script-file")
        parser.print_help()
        return

    if not scenes:
        print("❌ Пустой сценарий")
        return

    # 2. Рендерим кадры
    frame_paths = render_all_scenes(scenes)

    # 3. TTS — для каждой сцены отдельно
    scene_audio_paths = []
    if not args.no_tts:
        print("\n🔊 Генерация озвучки (посценово)...")
        for i, scene in enumerate(scenes):
            audio_text = scene.get("audio", "")
            if not audio_text:
                scene_audio_paths.append(None)
                print(f"  [{i+1}/{len(scenes)}] ⚠️ нет текста для озвучки")
                continue
            
            audio_path = str(OUTPUT_DIR / f"audio_scene_{i+1:02d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3")
            result = generate_tts(audio_text, audio_path)
            scene_audio_paths.append(result)
            if result:
                r = subprocess.run(
                    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "default=noprint_wrappers=1:nokey=1", result],
                    capture_output=True, text=True, timeout=10
                )
                dur = float(r.stdout.strip()) if r.stdout.strip() else 0
                print(f"  [{i+1}/{len(scenes)}] ✓ {dur:.1f}сек")
            else:
                print(f"  [{i+1}/{len(scenes)}] ❌ TTS не сработал")

    # 4. Сборка видео из сегментов
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = str(OUTPUT_DIR / f"output_{timestamp}.mp4")
    print(f"\n🎞️ Сборка видео: {output_path}")
    video_path = build_video_from_segments(scene_audio_paths, frame_paths, output_path)

    # 5. Чистим временные PNG (опционально)
    clean_png = False
    if clean_png:
        for fp in frame_paths:
            try:
                os.remove(fp)
            except OSError:
                pass

    if video_path:
        print(f"\n✅ Готово: {video_path}")
        return video_path


if __name__ == "__main__":
    main()
