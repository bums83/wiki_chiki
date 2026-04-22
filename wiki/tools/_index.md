---
title: Tools
layout: page
---

# Tools

Раздел `tools` собирает статьи про прикладные инструменты, operator-слои, CLI-утилиты и вспомогательные системы, которые используются рядом с агентами, workflow и автоматизациями.

Это не общий каталог софта, а curated-раздел про инструменты, которые важны как рабочие слои в реальных сценариях: интеграции, orchestration, client access, triage, voice tooling и verification workflow.

## Статьи

| Статья | О чём |
|--------|-------|
| [VoxCPM2 Portable]({{ '/wiki/tools/voxcpm2-portable' | relative_url }}) | Portable Windows-обвязка вокруг VoxCPM2: TTS, voice cloning, voice design и авто-пайплайн обучения LoRA из видео/аудио |
| [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}) | CLI-оператор для MCP-серверов: конфиг, auth, прямые вызовы tools и отладка интеграций |
| [Telegram Client Operator]({{ '/wiki/tools/telegram-client-operator' | relative_url }}) | MTProto-слой для чтения диалогов, тем, сообщений и поиска внутри агентных сценариев |
| [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) | Workflow-движок поверх cron и agent jobs для многошаговых автоматизаций и self-advancing цепочек |
| [ServiceDesk Plus Operator]({{ '/wiki/tools/servicedesk-plus-operator' | relative_url }}) | Локальный toolkit для отчётов, triage и category-check по ManageEngine ServiceDesk Plus |
| [Grizzly SMS MCP]({{ '/wiki/tools/grizzly-sms-mcp' | relative_url }}) | MCP-обёртка для SMS verification через API-провайдера внутри допустимых registration/login workflow |

## Что сюда попадает

В этот раздел стоит класть статьи, если инструмент:
- решает прикладную операционную задачу,
- используется как отдельный рабочий слой,
- встраивается в agent workflow или automation pipeline,
- заслуживает отдельного описания как reusable capability.
