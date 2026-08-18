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

## [2026-07-27] ingest | ru-marketplace-mcp
- Создано: `raw/entries/2026-07-27_ru-marketplace-mcp-github.md`, [[ru-marketplace-mcp]]
- Сохранена копия репозитория: `raw/sources/github/Vladimir-Human/ru-marketplace-mcp/` + `ru-marketplace-mcp.source-metadata.json`
- Обновлено: [[MCPorter]], [[Trench]], [[Teable]], [[Coolify]], [[Antfarm]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источник: https://github.com/Vladimir-Human/ru-marketplace-mcp

## [2026-07-27] ingest | humanizer-ru
- Создано: `raw/entries/2026-07-27_humanizer-ru-github.md`, [[humanizer-ru]]
- Сохранена копия репозитория: `raw/sources/github/Vladimir-Human/humanizer-ru/` + `humanizer-ru.source-metadata.json`
- Обновлено: [[Prompt Master]], [[Agents.md]], [[Academic Research Skills]], [[OpenAI Privacy Filter]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Верифицированы: полный offline validation sequence; `blind_eval` selftest 27/27; deterministic release archive
- Источник: https://github.com/Vladimir-Human/humanizer-ru

## [2026-07-30] ingest | Cobalt
- Создано: `raw/entries/2026-07-30_cobalt-github.md`, [[Cobalt]]
- Обновлено: [[Coolify]], [[OpenScreen]], [[Video Summary]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Верифицированы: Node syntax checks для core API files и JSON manifest parsing; end-to-end service suite не запускался, так как обращается к live media services
- Источник: https://github.com/imputnet/cobalt

## [2026-08-01] ingest | UI/UX Pro Max
- Создано: `raw/entries/2026-08-01_ui-ux-pro-max-skill-github.md`, [[UI/UX Pro Max]]
- Обновлено: [[Agents.md]], [[Вайб-кодинг]], [[Penpot]], [[Prompt Master]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Верифицированы: 35 runtime CSV, 12/12 domain smoke, 22/22 stack smoke, 36 Python tests, design-system JSON smoke и CLI asset-sync check
- Источник: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

## [2026-08-03] ingest | Прокси в веб-сборе данных
- Создано: `raw/entries/2026-08-03_habr-1066200-proxy-scraping.md`, [[Прокси в веб-сборе данных]]
- Обновлено: [[agent-aget]], [[ru-marketplace-mcp]], [[ASSH]], [[OpenAI Privacy Filter]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Проверено: canonical Habr retrieval, publication metadata, semantic links, source claims separated from independently reproducible facts
- Источник: https://habr.com/ru/articles/1066200/

## [2026-08-04] ingest | Searcharvester
- Создано: `raw/entries/2026-08-04_searcharvester-github.md`, [[Searcharvester]]
- Обновлено: [[Research org code]], [[Academic Research Skills]], [[Antfarm]], [[Coolify]], `TAGS.md`, `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Верифицированы: `docker compose config`, Python compileall, isolated suite `17 passed, 1 skipped`; реальный E2E намеренно не запускался — он требует Docker stack, Hermes и model endpoint
- Зафиксированы: API/auth/egress риски, documentation drift и конфликт README-license statement с root AGPL-3.0
- Источник: https://github.com/vakovalskii/searcharvester

## [2026-08-07] ingest | ProcessForge
- Создано: `raw/entries/2026-08-07_habr-1066916-processforge.md`, [[ProcessForge]]
- Обновлено: [[Agents.md]], [[Research org code]], [[The Agency / Agency Agents]], [[Antfarm]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Верифицированы: Python compileall, schema validation, public cleanliness и release-check; checksum validator и `release-test --public --fail-fast` не прошли из-за рассинхронизации `checksums/processforge.sha256` с текущим tree
- Источники: https://habr.com/ru/articles/1066916/ ; https://github.com/WebTolk/process-forge

## [2026-08-10] ingest | AI Factory
- Создано: `raw/entries/2026-08-10_ai-factory-github.md`, [[AI Factory]]
- Обновлено: [[Agents.md]], [[ProcessForge]], [[The Agency / Agency Agents]], [[MCPorter]], [[Boring Computers]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Верифицированы: `npm ci --ignore-scripts`, TypeScript build, lint, `npm test` (145 passed, 0 failed), init/update smoke suites и internal security self-scan; реальные LLM/MCP/browser/extension paths не запускались
- Зафиксированы: package branch `2.18.0` опережает последний GitHub release `v2.17.0`; README/package MIT claim не подтверждён root `LICENSE` или GitHub license metadata
- Источник: https://github.com/lee-to/ai-factory

## [2026-08-11] ingest | Croc
- Создано: `raw/entries/2026-08-11_becaps-1956-croc.md`, [[Croc]]
- Обновлено: [[cmux-ssh-here]], [[ASSH]], [[Cobalt]], `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`
- Источники: публичный Telegram-пост `@becaps/1956` и проверенный upstream `schollz/croc`
- Верифицированы: `go vet`, static Linux build и CLI version `11.0.3`; полный `go test ./...` не прошёл из-за воспроизводимо environment-dependent DNS expectation в `src/models/TestRemoteLookupIPTimeout`, остальные пакеты прошли
- Зафиксированы: normal live transfer relay-based; `--store` — отдельный encrypted async storage mode с bearer link/token, а не обычный peer flow

## [2026-08-11] ingest | Mobbin public product pages

- **source:** https://mobbin.com/
- **created:** `wiki/tools/mobbin.md`, `raw/entries/2026-08-11_mobbin-public-pages.md`
- **updated:** `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`, `wiki/llm-agents/ui-ux-pro-max.md`, `wiki/tools/penpot.md`, `wiki/tools/mcporter.md`
- **summary:** Mobbin is documented as a commercial design-reference library and paid account/OAuth MCP, not an open dataset or a visual editor. Terms boundaries on copying, repositories and ML use are explicit.

## [2026-08-15] ingest | slidevjs/slidev

- **source:** https://github.com/slidevjs/slidev
- **created:** `wiki/tools/slidev.md`, `raw/entries/2026-08-15_slidev-github.md`
- **updated:** `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`, `wiki/tools/mermaid.md`, `wiki/tools/mcporter.md`, `wiki/tools/openscreen.md`, `wiki/llm-agents/hyperframes.md`
- **summary:** Slidev is documented as a Markdown/Vite/Vue developer presentation runtime with interactive SPA/export/presenter workflows and a local file-mutating MCP surface; upstream CI succeeded at reviewed HEAD, while local clone/test was blocked by reproducible Git transport timeouts.

## [2026-08-18] ingest | Habr 1071250: Reasoning effort в LLM

- **source:** https://habr.com/ru/articles/1071250/
- **created:** `wiki/llm-agents/reasoning-effort.md`, `raw/entries/2026-08-18_habr-1071250-reasoning-effort.md`
- **updated:** `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`, [[Tokentap]], [[Evolve]], [[RTK]], [[ProcessForge]]
- **summary:** Reasoning effort is recorded as a model-specific routing parameter, not a universal quality slider: distinguish model/mode/effort/output budget, observe accepted outcome, escalate only failed cases and retain explicit external-action gates.
- **verified:** canonical Habr retrieval plus OpenAI reasoning/GPT-5.6 docs, gpt-oss model card, Qwen3 report/docs and DeepSeek-R1 upstream README; no local model runtime or benchmark was claimed.

## [2026-08-18] ingest | firecracker-microvm/firecracker

- **source:** https://github.com/firecracker-microvm/firecracker
- **created:** `wiki/infra/firecracker.md`, `raw/entries/2026-08-18_firecracker-microvm-firecracker.md`
- **updated:** `index.md`, `wiki/master-index.md`, `wiki/_backlinks.json`, [[Boring Computers]], [[Coolify]], [[AI Factory]]
- **summary:** Firecracker is documented as a Linux/KVM VMM for one microVM per process, not a ready-made control plane: the article distinguishes the VMM/API/jailer/seccomp/snapshot substrate from the image, egress, quota, lifecycle and observability responsibilities of an integrator.
- **verified:** revision-pinned sparse checkout at `95e08ae`; GitHub API current checks observed as success. Local `tools/devtool checkenv` found no `/dev/kvm` access for this user, and Rust `cargo` was absent, so no microVM/integration/performance test is claimed.
