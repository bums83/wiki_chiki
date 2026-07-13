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

## [2026-04-22] cleanup | Full graph pass across current wiki articles
- Обновлено: [[Windows Shell]], [[Оптимизация рабочего стола Windows]], [[Легаси-железо]], [[Poka-yoke и Andon]], [[Неогностицизм]], [[Validation bits per byte]], [[VoxCPM2 Portable]], `wiki/_backlinks.json`
- Основание: убрать orphan и weak-link узлы, усилить смысловые связи внутри infra, management, llm-agents и tools кластеров

## [2026-04-23] ingest | OpenAI Privacy Filter
- Создано: `raw/entries/2026-04-23_openai-privacy-filter.md`, [[OpenAI Privacy Filter]]
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: Telegram post from user, репозиторий https://github.com/openai/privacy-filter

## [2026-04-25] ingest | Prompts.chat
- Создано: `raw/entries/2026-04-25_prompts-chat-github.md`, [[Prompts.chat]]
- Обновлено: [[Вайб-кодинг]], [[Research org code]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/f/prompts.chat

## [2026-04-26] ingest | Evolve
- Создано: [[Evolve]]
- Обновлено: [[Вайб-кодинг]], [[Prompts.chat]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: forwarded Telegram post from channel `Only GitHub`, https://github.com/Frostbyte-Devs/evolve

## [2026-04-27] ingest | PowerInfer
- Создано: `raw/entries/2026-04-27_powerinfer-tiiny-ai.md`, [[PowerInfer]]
- Обновлено: [[PostgreSQL + VectorChord]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/Tiiny-AI/PowerInfer

## [2026-04-30] ingest | Mermaid
- Создано: [[Mermaid]]
- Обновлено: [[Вайб-кодинг]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: Telegram post from user

## [2026-04-30] ingest | ThreatSwarm
- Создано: [[ThreatSwarm]]
- Обновлено: [[Asynchronous research swarms]], [[Evolve]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: forwarded Telegram post from channel `Only Hack`, https://github.com/mukul975/Threatswarm

## [2026-04-30] ingest | Claude-OSINT
- Создано: [[Claude-OSINT]]
- Обновлено: [[ThreatSwarm]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: forwarded Telegram post from channel `Only GitHub`, https://github.com/elementalsouls/Claude-OSINT

## [2026-04-30] ingest | Prompt Master
- Создано: [[Prompt Master]]
- Обновлено: [[Prompts.chat]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: forwarded Telegram post from channel `Only GitHub`, https://github.com/nidhinjs/prompt-master

## [2026-05-01] ingest | RTK
- Создано: [[RTK]]
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/rtk-ai/rtk

## [2026-05-01] ingest | Agents.md
- Создано: [[Agents.md]]
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: forwarded from channel `Teamlead Good Reads` (Egor Tolstoy), https://x.com/augmentcode/status/2047164534310494709
- Обогащено: best practices с agentsmd.io, Augment guidelines docs
## [2026-05-01] ingest | PocketBase
- Создано: [[PocketBase]]
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: forwarded from channel `Only GitHub`, https://github.com/pocketbase/pocketbase

## [2026-05-03] ingest | Penpot
- Создано: `raw/entries/2026-05-03_penpot-github.md`, [[Penpot]]
- Обновлено: [[Mermaid]], [[HyperFrames]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источники:
  - https://github.com/penpot/penpot
  - forwarded Telegram post from channel `Only GitHub`

## 2026-05-26 ingest | Tolaria

Source: https://github.com/refactoringhq/tolaria

Created:
- `raw/entries/2026-05-26_tolaria-github.md`
- `wiki/tools/tolaria.md`

Updated:
- `wiki/master-index.md`
- `index.md`
- `wiki/_backlinks.json`
- `wiki/tools/gitnexus.md`
- `wiki/llm-agents/prompts-chat.md`
- `wiki/llm-agents/agents-md.md`
- `TAGS.md`

Notes: added Tolaria as files-first/git-first/offline-first markdown knowledge base for AI-friendly personal and team context.
## [2026-05-27] ingest | Trench + стратегия валидации торговых сигналов

Source:
- https://github.com/frigadehq/trench
- текущая постановка задачи crypto Telegram monitoring

Created:
- `raw/entries/2026-05-27_trench-github.md`
- `raw/entries/2026-05-27_trading-signal-validation-strategy.md`
- `wiki/tools/trench.md`
- `wiki/tools/trading-signal-validation.md`

Updated:
- `wiki/master-index.md`
- `index.md`
- `wiki/tools/directus.md`
- `wiki/_backlinks.json`

## [2026-05-28] delete | Валидация торговых сигналов
- Удалено: `wiki/tools/trading-signal-validation.md`, `raw/entries/2026-05-27_trading-signal-validation-strategy.md`
- Обновлено: `index.md`, `wiki/master-index.md`, `wiki/tools/trench.md`, `wiki/_backlinks.json`
- Основание: пользователь попросил удалить последнюю статью

## [2026-05-28] ingest | agent-aget
- Создано: `raw/entries/2026-05-28_agent-aget-github.md`, [[agent-aget]]
- Обновлено: [[Agents.md]], [[MCPorter]], [[Antfarm]], [[GitNexus]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/izzzzzi/agent-aget

## [2026-06-02] ingest | Magpie
- Создано: `raw/entries/2026-06-02_magpie-github.md`, [[Magpie]]
- Обновлено: [[Evolve]], [[Agents.md]], [[GitNexus]], [[agent-aget]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/liliu-z/magpie

## [2026-06-05] ingest | Tokentap
- Создано: `raw/entries/2026-06-05_tokentap-github.md`, [[Tokentap]]
- Обновлено: [[agent-aget]], [[Magpie]], [[RTK]], [[Evolve]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/jmuncor/tokentap

## [2026-06-05] ingest | OculiX
- Создано: `raw/entries/2026-06-05_oculix-github.md`, [[OculiX]]
- Обновлено: [[agent-aget]], [[Antfarm]], [[Mermaid]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/oculix-org/Oculix


## [2026-06-07] ingest | OpenScreen
- Создано: `raw/entries/2026-06-07_openscreen-github.md`, [[OpenScreen]]
- Обновлено: [[HyperFrames]], [[Penpot]], [[Mermaid]], [[OculiX]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/siddharthvaddem/openscreen

## [2026-06-18] ingest | Teable
- Создано: `raw/entries/2026-06-18_teable-github.md`, [[Teable]]
- Обновлено: [[Directus]], [[PocketBase]], [[SurrealDB]], [[Trench]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/teableio/teable

## [2026-06-18] ingest | Academic Research Skills
- Создано: `raw/entries/2026-06-18_academic-research-skills-github.md`, [[Academic Research Skills]]
- Обновлено: [[Research org code]], [[Prompts.chat]], [[Agents.md]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/Imbad0202/academic-research-skills

## [2026-06-18] refresh | agent-aget
- Создано: `raw/entries/2026-06-18_agent-aget-refresh-github.md`
- Обновлено: [[agent-aget]], `index.md`, `wiki/master-index.md`
- Источник: https://github.com/izzzzzi/agent-aget

## [2026-06-19] ingest | ASSH
- Создано: `raw/entries/2026-06-19_assh-github.md`, [[ASSH]]
- Обновлено: [[MCPorter]], [[Antfarm]], [[OculiX]], [[agent-aget]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/moul/assh

## [2026-06-19] ingest | The Agency / Agency Agents
- Создано: `raw/entries/2026-06-19_agency-agents-github.md`, [[The Agency / Agency Agents]]
- Обновлено: [[Agents.md]], [[Academic Research Skills]], [[Research org code]], [[Prompt Master]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/msitarzewski/agency-agents

## [2026-06-21] ingest | Coolify
- Создано: `raw/entries/2026-06-21_coolify-github.md`, [[Coolify]]
- Обновлено: [[Directus]], [[Teable]], [[PocketBase]], [[ASSH]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/coollabsio/coolify

## [2026-06-29] ingest | cmux-ssh-here
- Создано: `raw/entries/2026-06-29_cmux-ssh-here-telegram.md`, [[cmux-ssh-here]]
- Обновлено: [[ASSH]], [[Coolify]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://t.me/deksden_notes/909
- Дополнительный источник: https://github.com/viktor-silakov/cmux-ssh-here

## [2026-07-04] ingest | Video Summary
- Создано: `raw/entries/2026-07-04_video-summary-github.md`, [[Video Summary]]
- Сохранена копия репозитория: `raw/sources/github/NiiyazG/video-summary/` + `video-summary.source-metadata.json`
- Обновлено: [[HyperFrames]], [[OpenScreen]], [[VoxCPM2 Portable]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/NiiyazG/video-summary

## [2026-07-13] ingest | Boring Computers
- Создано: `raw/entries/2026-07-13_boring-computers-github.md`, [[Boring Computers]]
- Обновлено: [[OculiX]], [[agent-aget]], [[MCPorter]], [[Coolify]], [[Antfarm]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/michaelshimeles/boring-computers
