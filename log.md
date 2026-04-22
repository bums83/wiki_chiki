# Log

## [2026-04-12] ingest | Приручаем монстра: Windows 10 на диете из XP
- Создано: [[Windows Shell]], [[Оптимизация рабочего стола Windows]], [[Легаси-железо]]
- Обновлено: —
- Источник: https://habr.com/ru/articles/994440/

## [2026-04-12] ingest | Японские подходы в IT (8 статей)
- Создано: [[Кайдзен]], [[Toyota Production System]], [[Муда]], [[Poka-yoke и Andon]], [[Метод 5 Why]], [[Диаграмма Исикавы]], [[Методология A3]]
- Обновлено: —
- Источники:
  - https://habr.com/ru/articles/297004/ (Кайдзен — путь к совершенству)
  - https://habr.com/ru/articles/547592/ (Кайдзен: постоянно улучшаем все вокруг)
  - https://habr.com/ru/companies/selectel/articles/878782/ (Японские подходы. Часть 1)
  - https://habr.com/ru/companies/selectel/articles/882102/ (Японские подходы. Часть 2)
  - https://habr.com/ru/companies/selectel/articles/888486/ (Японские подходы. Часть 3)
  - https://habr.com/ru/companies/selectel/articles/897854/ (Японские подходы. Часть 4)
  - https://habr.com/ru/companies/selectel/articles/909404/ (Японские подходы. Часть 5)
  - https://habr.com/ru/companies/selectel/articles/914098/ (Японские подходы. Часть 6)

## [2026-04-13] ingest | Autoresearch + research org code
- Создано: [[Autoresearch]], [[Research org code]]
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источники:
  - https://github.com/karpathy/autoresearch?tab=readme-ov-file
  - https://x.com/hooeem/status/2030720614752039185
  - https://x.com/karpathy/status/2029701092347630069
  - https://x.com/karpathy/status/2031135152349524125
- Примечание: X-посты не отдались напрямую через fetch, поэтому для них использованы поисковые сниппеты как вспомогательный источник контекста.

## [2026-04-13] expand | Agentic research cluster
- Создано: [[Nanochat]], [[Validation bits per byte]], [[Overnight experimentation]], [[Asynchronous research swarms]]
- Обновлено: [[Autoresearch]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источники:
  - https://github.com/karpathy/nanochat
  - https://x.com/karpathy/status/2030705271627284816

## [2026-04-13] refine | Sources restored + homepage simplified
- Обновлено: все wiki-страницы получили явный блок `Источники` с внешними ссылками на первоисточники
- Обновлено: `index.md` возвращён к простому плоскому виду: раздел → статья → краткое описание
- Обновлено: добавлен `wiki/master-index.md` как единый мастер-индекс для GitHub Pages
- Основание: source ids были сохранены в frontmatter и raw history, но не выводились на самих страницах

## [2026-04-13] fix | Resolve broken Obsidian-style links
- Обновлено: все видимые `[[...]]` в `wiki/` и `index.md` переведены в обычные Markdown-ссылки
- Обновлено: `related:` в frontmatter нормализован до обычных названий статей
- Добавлено: `scripts/resolve_wikilinks.py` для автоматической нормализации ссылок
- Обновлено: GitHub Pages workflow теперь прогоняет нормализацию перед сборкой
- Обновлено: `SCHEMA.md` теперь запрещает Obsidian-синтаксис в опубликованных страницах

## [2026-04-13] fix | Make published links baseurl-aware
- Исправлено: публичные ссылки больше не используют жёсткий абсолютный путь `/wiki/...`
- Исправлено: ссылки теперь рендерятся через `relative_url`, чтобы работать на GitHub Pages project site
- Исправлено: убран хвостовой `/` в URL статей, потому что текущий Pages site отдаёт страницы как `/wiki/.../slug`, а не `/wiki/.../slug/`
- Обновлено: `_config.yml` получил `baseurl: "/wiki_chiki"`
- Обновлено: `scripts/resolve_wikilinks.py` теперь генерирует baseurl-aware ссылки

## [2026-04-13] ingest | Библиотека вайб-кодера: 50 промптов
- Создано: [[Вайб-кодинг]], `raw/entries/2026-04-13_vibe-coder-50-prompts.md`
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: приложенный PDF `50_промптов---fa9b0596-6cf1-48b7-a354-acc4d05f0cc5.pdf`

## [2026-04-19] ingest | VoxCPM2 Portable
- Создано: [[VoxCPM2 Portable]], `raw/entries/2026-04-19_voxcpm2-portable-github.md`
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источники:
  - https://github.com/timoncool/VoxCPM2_portable
  - forwarded Telegram post from channel `НЕЙРО-СОФТ ● РЕПАКИ И ПОРТАТИВКИ` with screenshots and video clips

## [2026-04-19] curate | Tools backlog with OpenClaw tag
- Обновлено: `index.md`, `wiki/master-index.md`
- Добавлено: список возможных tools-статей с явной пометкой `OpenClaw`
- Backlog:
  - MCPorter
  - Telegram Client Operator
  - Antfarm
  - ServiceDesk Plus Operator
  - Grizzly SMS MCP

## [2026-04-21] ingest | PostgreSQL + VectorChord = Гибридный поиск. Часть 2. Безоблачная
- Создано: `raw/entries/2026-04-21_postgresql-vectorchord-hybrid-search-part-2.md`
- Обновлено: [[PostgreSQL + VectorChord, часть 2]], `wiki/_backlinks.json`
- Источники:
  - https://habr.com/ru/articles/1024818/
  - https://habr.com/ru/articles/1024810/

## [2026-04-21] refactor | PostgreSQL + VectorChord merged into one wiki article
- Создано: [[PostgreSQL + VectorChord]]
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Убрано из навигации: разбиение на `часть 1` и `часть 2`
- Источники:
  - https://habr.com/ru/articles/1024810/
  - https://habr.com/ru/articles/1024818/

## [2026-04-22] structure | Added dedicated Tools section
- Создано: `wiki/tools/_index.md`
- Обновлено: `index.md`, `wiki/master-index.md`
- Основание: оформить `tools` как явный раздел wiki, а не только как список статей на главной

## [2026-04-22] ingest | Directus
- Создано: `raw/entries/2026-04-22_directus-github.md`, [[Directus]]
- Обновлено: `wiki/tools/_index.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источники:
  - https://github.com/directus/directus
  - https://docs.directus.io

## [2026-04-22] cleanup | Strengthen graph links around database and tools articles
- Обновлено: [[PostgreSQL + VectorChord]], [[Directus]], [[MCPorter]], [[Antfarm]], `wiki/_backlinks.json`
- Основание: убрать слабую и нерелевантную связность, встроить статьи про базы и tool/platform слой в более осмысленный knowledge graph
