---
title: Video Summary
type: technology
created: 2026-07-04
last_updated: 2026-07-30
domain: llm-agents
related: ["HyperFrames", "OpenScreen", "VoxCPM2 Portable", "Вайб-кодинг", "Cobalt"]
sources: ["github-niiyazg-video-summary-2026-07-04"]
tags: ["llm", "video", "tts", "automation", "workflow"]
---

# Video Summary

`Video Summary` — Hermes Agent skill/tool для генерации коротких вертикальных видео-обзоров из текста, ссылок или PDF. По замыслу это локальный аналог NotebookLM Short Video Overviews: агент извлекает смысл источника, пишет сценарий, рендерит кадры и собирает MP4 с озвучкой.

Практический результат — вертикальное видео `1080×1920` в формате 9:16: несколько статичных сцен с крупными заголовками, тезисами и посценовой TTS-озвучкой.

## Что делает

Репозиторий `NiiyazG/video-summary` содержит:

- `SKILL.md` — описание навыка для Hermes Agent;
- `gen_video_summary.py` — основной Python-скрипт рендера и сборки;
- `deepseek-prompt.md` — промпт для генерации JSON-сценария;
- `example_script.json` — пример сценария с посценовым `audio`;
- `README.md` — установка и ручной запуск.

Целевой пользовательский запрос выглядит так:

```text
Сделай видео-обзор по статье https://...
Сгенерируй видео по этому тексту
Как NotebookLM, сделай шортс
```

Агент должен загрузить источник, сжать его в сценарий, сохранить JSON и передать его в скрипт:

```bash
python3 gen_video_summary.py --script-file script.json
```

## Pipeline

Операционная схема проекта:

1. **Источник** — текст, URL или PDF.
2. **LLM-сценарий** — JSON с `title` и массивом `scenes`.
3. **Pillow-render** — каждая сцена превращается в PNG-кадр 1080×1920.
4. **TTS** — для каждой сцены создаётся отдельный audio file.
5. **FFmpeg segments** — каждый кадр + его audio собираются в отдельный MP4-сегмент.
6. **Concat** — сегменты склеиваются в финальный MP4.

Ключевое инженерное решение: **не делать один общий audio file на всё видео**. Скрипт ждёт `scene["audio"]` на каждой сцене, генерирует отдельные MP3 и длительность каждого кадра привязывает к длительности его аудио. Это чинит типовую ошибку, где последний слайд остаётся без звука из-за `-shortest`.

## Стиль вывода

Визуальная модель простая и воспроизводимая:

- вертикальный кадр `1080×1920`;
- тёмный фон `#0D0D0F`;
- голубой accent color для заголовков и линии;
- крупные заголовки и 2–4 коротких тезиса;
- нумерация сцены сверху;
- footer: `© Гарипов Нияз Варисович t.me/ML_DS_one`.

Это не генеративное видео в смысле Sora/Veo. Это deterministic slide-video pipeline: сценарий + типографика + voiceover + FFmpeg.

## Связь с HyperFrames и OpenScreen

С [HyperFrames]({{ '/wiki/llm-agents/hyperframes' | relative_url }}) связь по общей идее: видео становится артефактом, который агент может собрать через код. Но уровень другой:

- HyperFrames делает HTML/CSS/JS composition и motion pipeline;
- Video Summary делает статичные объясняющие кадры через Pillow и FFmpeg.

С [OpenScreen]({{ '/wiki/tools/openscreen' | relative_url }}) граница тоже чёткая: OpenScreen записывает реальный продукт и полирует screen demo, а Video Summary генерирует объясняющий ролик из текста или документа. Один инструмент начинается с экрана, другой — с источника знания.

## Связь с TTS

[Вокс/TTS-инструменты вроде VoxCPM2 Portable]({{ '/wiki/tools/voxcpm2-portable' | relative_url }}) находятся рядом по аудиослою, но Video Summary решает более узкую задачу: не управление голосовой моделью, а включение TTS в автоматический video-summary pipeline.

В текущей реализации приоритет TTS такой:

1. `gTTS` — основной вариант, бесплатный, русский язык;
2. `edge-tts` — fallback, если установлен;
3. без TTS — видео можно собрать без звука, но ценность заметно ниже.

## Где уместен

Video Summary полезен для:

- быстрых видео-выжимок из статей, PDF и заметок;
- коротких вертикальных роликов для Telegram/Shorts/Reels;
- объясняющих summary по research/documentation материалам;
- превращения текстового дайджеста в медиа-артефакт;
- agentic content workflows, где нужно не просто пересказать источник, а собрать файл.

Это хорошо ложится в практику [Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }}): человек задаёт формат, ограничения и критерии, агент генерирует сценарий и исполняет pipeline до готового артефакта.

[Cobalt]({{ '/wiki/tools/cobalt' | relative_url }}) может предоставить локальный файл свободно доступного публичного видео для отдельного transcript/extraction шага, но не является входом Video Summary сам по себе: текущий Video Summary начинается с текста, URL/PDF и готового JSON-сценария. Между ними нужен явный слой извлечения содержания и проверка прав на использование media.

## Ограничения и риски

У проекта пока видны признаки раннего состояния:

- GitHub API не показывает license metadata, а `LICENSE` файла в snapshot нет; README говорит MIT с сохранением авторства/footer.
- `deepseek-prompt.md` описывает старую схему `overall_audio` и прямо запрещает per-scene `audio`, но `SKILL.md`, `example_script.json` и текущий скрипт требуют `scene["audio"]`. Перед реальным использованием prompt нужно привести к актуальной схеме.
- `generate_script_from_source()` в коде — заглушка; LLM-сценарий должен создать сам агент, скрипт принимает готовый JSON через `--script-file`.
- gTTS требует сеть; без сети/провайдера остаётся fallback на silent video.
- Кадры статичны: нет motion graphics, timing-анимаций и сложного визуального сторителлинга.

## Практический вывод

`Video Summary` ценен как минимальный локальный pipeline для “source → short vertical explainer video”. Он не конкурирует с полноценными video frameworks и редакторами. Его сила — в простоте: JSON-сценарий, Pillow, TTS и FFmpeg дают воспроизводимый путь от текста к MP4.

Главное, что нужно доработать перед стабильным использованием: синхронизировать prompt schema с реальным скриптом, явно оформить лицензию и проверить TTS/FFmpeg окружение на целевой машине.

## Локальная копия источника

Snapshot репозитория сохранён внутри Wiki Chiki:

- `raw/sources/github/NiiyazG/video-summary/`
- commit: `467846ec742951d86f742a77dd4e1e7baee4deeb`
- metadata: `raw/sources/github/NiiyazG/video-summary.source-metadata.json`

## Источники

- https://github.com/NiiyazG/video-summary
- `raw/sources/github/NiiyazG/video-summary/README.md`
- `raw/sources/github/NiiyazG/video-summary/SKILL.md`
- `raw/sources/github/NiiyazG/video-summary/gen_video_summary.py`
