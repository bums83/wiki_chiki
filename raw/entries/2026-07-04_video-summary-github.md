---
id: github-niiyazg-video-summary-2026-07-04
date: 2026-07-04
source_type: url
source_url: https://github.com/NiiyazG/video-summary
title: NiiyazG/video-summary GitHub repository
domain: llm-agents
tags: [llm, video, tts, automation, workflow]
---

# NiiyazG/video-summary GitHub repository

Source: https://github.com/NiiyazG/video-summary

Repository snapshot saved locally in Wiki Chiki:

- `raw/sources/github/NiiyazG/video-summary/`
- metadata: `raw/sources/github/NiiyazG/video-summary.source-metadata.json`
- commit: `467846ec742951d86f742a77dd4e1e7baee4deeb`
- branch: `main`

Repository metadata observed on 2026-07-04:

- Full name: `NiiyazG/video-summary`
- Description: генератор коротких видео-обзоров для Hermes Agent, аналог NotebookLM Short Video Overviews: текст/PDF/ссылка → вертикальное видео 9:16 с TTS-озвучкой.
- Language: Python
- Default branch: `main`
- License metadata from GitHub API: none. README states MIT with attribution/footer preservation.
- Top-level files: `README.md`, `SKILL.md`, `deepseek-prompt.md`, `example_script.json`, `gen_video_summary.py`.

Durable source facts:

- The project is packaged as a Hermes Agent skill named `video-summary`, category `creative`.
- Trigger phrases include “сделай видео-обзор”, “сгенерируй видео по ссылке/тексту”, “как NotebookLM, но в Hermes”.
- Target output: vertical MP4 1080×1920, 9:16, about 60 seconds.
- Pipeline: source text/URL/PDF → LLM-generated JSON scenario → Pillow renders PNG frames → gTTS/edge-tts produces per-scene audio → FFmpeg assembles segments and final MP4.
- Runtime dependencies: Python 3.8+, Pillow, gTTS, FFmpeg; script also imports/mentions numpy and requests in docs, but the visible main script primarily uses Pillow, subprocess/FFmpeg and TTS providers.
- Script output defaults to `~/video-summary/`.
- Frame style: Dark Material, black background, blue accent, white text, 1080×1920 dimensions, footer `© Гарипов Нияз Варисович t.me/ML_DS_one`.
- Important implementation decision: each scene gets its own `audio` field and its own audio file; FFmpeg then creates scene-level segments and concatenates them. This avoids the “last slide has no sound” problem caused by one shared audio file and `-shortest`.
- Caveat: `deepseek-prompt.md` still describes an older `overall_audio` schema and says not to add per-scene `audio`; `SKILL.md`, `example_script.json` and `gen_video_summary.py` require per-scene `audio`. The prompt needs synchronization before operational use.
- The repository has no `LICENSE` file in the inspected snapshot; README says “MIT с указанием авторства” and asks to preserve the footer.
