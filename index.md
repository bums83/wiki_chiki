---
title: Wiki Chiki — Главная
layout: home
---

# Wiki Chiki

База знаний: инфраструктура, менеджмент, LLM/агенты, tools.

## Инфраструктура

| Статья | О чём |
|--------|-------|
| [Windows Shell]({{ '/wiki/infra/windows-shell' | relative_url }}) | Компоненты оболочки Windows, потребление ресурсов, альтернативы |
| [Оптимизация рабочего стола Windows]({{ '/wiki/infra/windows-desktop-optimization' | relative_url }}) | Кейс: замена тяжёлых компонентов Win10, 70 МБ вместо 300+ |
| [Легаси-железо]({{ '/wiki/infra/legacy-hardware' | relative_url }}) | Стратегии продления жизни старого оборудования |
| [PostgreSQL + VectorChord]({{ '/wiki/infra/postgresql-vectorchord-hybrid-search' | relative_url }}) | Единая статья про локальный hybrid retrieval на PostgreSQL и VectorChord: модель данных, пайплайны, hybrid search, локальные embeddings, reranker и semantic chunking |
| [PowerInfer]({{ '/wiki/infra/powerinfer' | relative_url }}) | High-speed LLM inference engine для локального запуска больших моделей на обычном GPU: sparse activation, hot/cold нейроны, до 11x быстрее llama.cpp |
| [RTK]({{ '/wiki/infra/rtk' | relative_url }}) | CLI proxy, который сокращает потребление токенов LLM на 60-90% при dev-командах: smart filtering, grouping, truncation, deduplication |
| [PocketBase]({{ '/wiki/infra/pocketbase' | relative_url }}) | Open-source бэкенд на Go в одном файле: SQLite realtime, авторизация, файловый storage, админ-панель и REST API — для быстрых прототипов |
| [SurrealDB]({{ '/wiki/infra/surrealdb' | relative_url }}) | Multi-model database на Rust: document, graph, relational, time-series, geospatial и key-value модели с realtime, hybrid search и BaaS-подобным backend layer |
| [Прокси в веб-сборе данных]({{ '/wiki/infra/web-scraping-proxies' | relative_url }}) | Guide по выбору и честному тестированию outbound proxy для разрешённого web data collection: типы IP, valid-success, rate policy, cost per valid record и границы доступа |

## Менеджмент

| Статья | О чём |
|--------|-------|
| [Кайдзен]({{ '/wiki/management/kaizen' | relative_url }}) | Философия непрерывного совершенствования, PDCA, genchi gembutsu |
| [Toyota Production System]({{ '/wiki/management/toyota-production-system' | relative_url }}) | 9 принципов TPS, JIT, SMED, Kanban |
| [Муда]({{ '/wiki/management/muda' | relative_url }}) | Три вида потерь: муда, мура, мури + 7 потерь с IT-параллелями |
| [Poka-yoke и Andon]({{ '/wiki/management/poka-yoke-andon' | relative_url }}) | Защита от дурака, система оповещения, karakuri |
| [Метод 5 Why]({{ '/wiki/management/5-why' | relative_url }}) | Поиск корневых причин через последовательные «почему?» |
| [Диаграмма Исикавы]({{ '/wiki/management/ishikawa-diagram' | relative_url }}) | Fishbone-диаграмма, анализ 6M, сюхари |
| [Методология A3]({{ '/wiki/management/a3-methodology' | relative_url }}) | Визуальный документ для принятия решений, 5S для IT |
| [Неогностицизм]({{ '/wiki/management/neognosticism' | relative_url }}) | Конец трудового договора: AGI, цифровая дистилляция, парадокс добросовестности |

## LLM и агенты

| Статья | О чём |
|--------|-------|
| [Autoresearch]({{ '/wiki/llm-agents/autoresearch' | relative_url }}) | Single-GPU framework для автономного research-цикла: агент меняет `train.py`, человек задаёт `program.md` |
| [Research org code]({{ '/wiki/llm-agents/research-org-code' | relative_url }}) | Идея проектирования исследовательской организации через prompt/policy layer |
| [Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }}) | Практика разработки, где человек управляет агентом через рамки, контекст и stage-specific промпты |
| [Nanochat]({{ '/wiki/llm-agents/nanochat' | relative_url }}) | Базовый LLM training harness Карпаты, из которого вырос autoresearch |
| [Video Summary]({{ '/wiki/llm-agents/video-summary' | relative_url }}) | Hermes Agent skill/tool для коротких вертикальных видео-обзоров: источник → JSON-сценарий → Pillow-кадры → TTS → FFmpeg MP4 |
| [Boring Computers]({{ '/wiki/llm-agents/boring-computers' | relative_url }}) | Self-hosted Firecracker microVM-компьютеры для AI-агентов: shell, desktop/VNC, MCP, fork/snapshot и disposable execution substrate |
| [Validation bits per byte]({{ '/wiki/llm-agents/validation-bits-per-byte' | relative_url }}) | Метрика `val_bpb` для быстрых и сравнительно честных research-сравнений |
| [Overnight experimentation]({{ '/wiki/llm-agents/overnight-experimentation' | relative_url }}) | Ночной режим пакетных агентных экспериментов |
| [Asynchronous research swarms]({{ '/wiki/llm-agents/asynchronous-research-swarms' | relative_url }}) | Переход от одного автономного исследователя к распределённому сообществу агентов |
| [Prompts.chat]({{ '/wiki/llm-agents/prompts-chat' | relative_url }}) | Open-source prompt library и prompt tooling layer с self-hosting, dataset и MCP-интеграцией |
| [Academic Research Skills]({{ '/wiki/llm-agents/academic-research-skills' | relative_url }}) | Claude Code skill suite для academic research workflow: research → write → review → revise → finalize, с human checkpoints и integrity gates |
| [The Agency / Agency Agents]({{ '/wiki/llm-agents/agency-agents' | relative_url }}) | Cross-functional библиотека AI-agent ролей: 232 Markdown agents в 16 divisions плюс convert/install tooling для Claude Code, Cursor, OpenClaw, Codex и других runtimes |
| [Evolve]({{ '/wiki/llm-agents/evolve' | relative_url }}) | Пассивное A/B-тестирование AI-ассистентов в фоне: эмпирический подбор лучшего промпта и модели |
| [ThreatSwarm]({{ '/wiki/llm-agents/threatswarm' | relative_url }}) | Claude Code plugin с 27 AI-агентами для полной автоматизации пентеста: разведка → эксплуатация → закрепление → отчёт |
| [Claude-OSINT]({{ '/wiki/llm-agents/claude-osint' | relative_url }}) | SKILL.md-набор для LLM с 90+ OSINT-модулями, 48 паттернами поиска секретов и 80+ dorks для профессиональных расследований |
| [Prompt Master]({{ '/wiki/llm-agents/prompt-master' | relative_url }}) | Claude skill для генерации оптимизированных промптов под 20+ AI-инструментов: Midjourney, Cursor, ChatGPT, Gemini и другие |
| [humanizer-ru]({{ '/wiki/llm-agents/humanizer-ru' | relative_url }}) | Agent Skill для осторожной проверки и правки русской прозы: 37 паттернов, class A/B артефакты, запрет на дописывание фактов и offline eval/validators |
| [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}) | Best practices для написания Agents.md файлов: progressive disclosure, decision tables, numbered steps, dos/donts pairs, file-scoped commands, safety boundaries |
| [UI/UX Pro Max]({{ '/wiki/llm-agents/ui-ux-pro-max' | relative_url }}) | Local BM25-backed design-recommendation skill suite для coding-агентов: CSV data, design-system output, stack guides, template CLI и строгие границы валидации UI |

## Tools

| Статья | О чём |
|--------|-------|
| [VoxCPM2 Portable]({{ '/wiki/tools/voxcpm2-portable' | relative_url }}) | Portable Windows-обвязка вокруг VoxCPM2: TTS, voice cloning, voice design и авто-пайплайн обучения LoRA из видео/аудио |
| [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}) | CLI-оператор для MCP-серверов: конфиг, auth, прямые вызовы tools и отладка интеграций |
| [ru-marketplace-mcp]({{ '/wiki/tools/ru-marketplace-mcp' | relative_url }}) | Read-only MCP-серверы для WB, Ozon, Яндекс Маркета и Детского мира: цены, наличие, отзывы и честное cross-marketplace сравнение |
| [ASSH]({{ '/wiki/tools/assh' | relative_url }}) | Advanced SSH config manager: YAML для `~/.ssh/config`, aliases, gateway chains, hooks, Graphviz и control sockets |
| [cmux-ssh-here]({{ '/wiki/tools/cmux-ssh-here' | relative_url }}) | Одноразовый token-auth SSH-сервер для LAN: `npx` запуск, cmux/ssh ссылки, QR, auto-rotation token и shell без постоянного sshd |
| [Coolify]({{ '/wiki/tools/coolify' | relative_url }}) | Self-hosted PaaS/control plane: деплой приложений, баз данных и 280+ Docker Compose сервисов на своих серверах через SSH/Docker |
| [Telegram Client Operator]({{ '/wiki/tools/telegram-client-operator' | relative_url }}) | MTProto-слой для чтения диалогов, тем, сообщений и поиска внутри агентных сценариев |
| [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) | Workflow-движок поверх cron и agent jobs для многошаговых автоматизаций и self-advancing цепочек |
| [ServiceDesk Plus Operator]({{ '/wiki/tools/servicedesk-plus-operator' | relative_url }}) | Локальный toolkit для отчётов, triage и category-check по ManageEngine ServiceDesk Plus |
| [Grizzly SMS MCP]({{ '/wiki/tools/grizzly-sms-mcp' | relative_url }}) | MCP-обёртка для SMS verification через API-провайдера внутри допустимых registration/login workflow |
| [Directus]({{ '/wiki/tools/directus' | relative_url }}) | Платформа, которая накладывает REST/GraphQL API и админку поверх SQL-базы без переноса данных в собственную CMS-модель |
| [Teable]({{ '/wiki/tools/teable' | relative_url }}) | Open-source no-code Postgres/Airtable alternative: spreadsheet-like UI, realtime collaboration, multiple views, plugins, SQL query и self-hosted Docker deployment |
| [OpenAI Privacy Filter]({{ '/wiki/tools/openai-privacy-filter' | relative_url }}) | Open-source модель для обнаружения и маскировки PII в тексте |
| [Mermaid]({{ '/wiki/tools/mermaid' | relative_url }}) | Open-source инструмент для создания диаграмм и блок-схем из текстового описания: LLM-friendly, Git-версионирование, 21 тип диаграмм |
| [GitNexus]({{ '/wiki/tools/gitnexus' | relative_url }}) | Client-side code intelligence engine и knowledge graph creator для репозиториев: CLI + MCP, Web UI, Graph RAG Agent и bridge mode |
| [Tolaria]({{ '/wiki/tools/tolaria' | relative_url }}) | Desktop-приложение для markdown knowledge bases: files-first, git-first, offline-first vaults и AI-friendly контекст для людей и агентов |
| [Penpot]({{ '/wiki/tools/penpot' | relative_url }}) | Open-source платформа для UI/UX-дизайна и прототипирования: self-hosted, открытые стандарты, design tokens, collaboration и design-to-code handoff |
| [Trench]({{ '/wiki/tools/trench' | relative_url }}) | Self-hosted event analytics infrastructure на Kafka, ClickHouse и Node.js; подходит как журнал событий для проверки сигналов и outcome-аналитики |
| [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) | CLI-помощник для браузерных сценариев LLM-агентов: stealth Chromium, persistent profiles/cookies, device emulation, snapshot refs, batch-команды и JSON-ответы |
| [Magpie]({{ '/wiki/tools/magpie' | relative_url }}) | Multi-AI adversarial PR review tool: параллельные AI-reviewers, debate rounds и code-aware verify+audit для PR findings |
| [Tokentap]({{ '/wiki/tools/tokentap' | relative_url }}) | Token tracker для LLM CLI tools: proxy, live dashboard, context-window fuel gauge и prompt archive в markdown/JSON |
| [OculiX]({{ '/wiki/tools/oculix' | relative_url }}) | Visual automation IDE/runtime: GUI-автоматизация по screenshots, OpenCV matching, OCR, VNC/remote desktop и JVM scripting |
| [OpenScreen]({{ '/wiki/tools/openscreen' | relative_url }}) | Open-source recorder/editor для polished product demos: screen/window capture, webcam PiP, auto-zooms, cursor effects, captions, annotations и MP4/GIF export |
| [Cobalt]({{ '/wiki/tools/cobalt' | relative_url }}) | Self-hosted media downloader для свободно доступного публичного контента: API с redirect/tunnel/local processing, Svelte frontend, Docker, rate limits и access controls |
| [Searcharvester]({{ '/wiki/tools/searcharvester' | relative_url }}) | Private research stack: SearXNG + extract-to-Markdown + Tavily-shaped API + Hermes ACP jobs; требует auth, egress policy и review artifacts |

## Полный список

- [Мастер-индекс статей]({{ '/wiki/master-index' | relative_url }})

---

Как добавить знания: отправь URL, файл или текст — я обработаю и обновлю wiki.
