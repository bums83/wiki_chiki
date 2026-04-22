# TAGS.md — Контролируемый словарь тегов для Wiki Chiki

Теги в Wiki Chiki — вспомогательный слой, а не основа навигации.

Использование:
- 3-6 тегов на статью
- теги помогают находить соседние статьи при ingest
- теги помогают находить слабосвязанные кластеры и missing links
- теги не заменяют domain, master-index и смысловые ссылки в тексте

## Правила

- Используй только теги из этого словаря, если нет явной причины добавить новый
- Не создавай синонимичные дубли (`rag` и `retrieval-augmented-generation` одновременно нельзя)
- Предпочитай короткие kebab-case теги
- Не используй слишком общие теги вроде `tech`, `software`, `system`, `article`
- Если нужен новый тег, проверь, не покрывается ли он уже существующим

## Infra

- postgresql
- mysql
- sqlite
- sql
- vector-search
- full-text-search
- hybrid-search
- rag
- retrieval
- embeddings
- reranker
- chunking
- llama-cpp
- docker
- kubernetes
- monitoring
- storage
- virtualization
- windows
- linux
- shell
- hardware
- legacy-hardware
- database
- backend
- api-platform
- admin-panel
- headless-cms

## Management

- kaizen
- tps
- lean
- waste
- root-cause-analysis
- process-improvement
- incident-management
- service-management
- triage
- reporting
- decision-making

## LLM / Agents

- llm
- agents
- prompt-engineering
- eval
- fine-tuning
- workflow
- automation
- research
- mcp
- async-research
- vibe-coding

## Tools / Platforms

- tools
- operator
- cli
- telegram
- mtproto
- servicedesk
- voice
- tts
- sms-verification
- directus
- openclaw
