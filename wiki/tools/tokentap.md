---
title: Tokentap
type: technology
created: 2026-06-05
last_updated: 2026-06-05
domain: tools
related: ["agent-aget", "Magpie", "RTK", "Evolve", "Agents.md"]
sources: ["github-jmuncor-tokentap-2026-06-05"]
tags: ["tools", "cli", "llm", "monitoring", "automation"]
---

# Tokentap

`Tokentap` — Python CLI-инструмент для отслеживания token usage у LLM CLI tools. Он поднимает локальный HTTP proxy и live terminal dashboard, перехватывает LLM API traffic, считает токены, показывает заполнение context window и сохраняет каждый prompt в markdown и JSON.

Внутри Wiki Chiki это tool-layer для наблюдаемости LLM-сессий. Если [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) делает браузерные действия агента воспроизводимыми, а [Magpie]({{ '/wiki/tools/magpie' | relative_url }}) структурирует multi-AI review, то Tokentap отвечает за прозрачность того, что реально уходит в LLM API и сколько это потребляет контекста.

## Что делает

Tokentap решает четыре практические задачи:

- показывает token usage каждого запроса в real time;
- визуализирует cumulative context usage через fuel gauge;
- сохраняет prompt archive в markdown и JSON для последующего разбора;
- запускает популярные LLM CLI tools через proxy-настройки без ручной конфигурации сертификатов.

Базовый сценарий состоит из двух терминалов: в первом запускается `tokentap start`, во втором пользователь запускает LLM tool через wrapper-команду вроде `tokentap claude`, `tokentap codex` или `tokentap run --provider minimax <cmd>`.

## Как работает proxy model

Tokentap стартует локальный HTTP proxy, по умолчанию на `localhost:8080`. Wrapper-команды выставляют переменные окружения для конкретного provider и запускают целевой CLI. Например, для Claude Code команда задаёт `ANTHROPIC_BASE_URL=http://localhost:8080`, после чего трафик идёт через Tokentap и дальше проксируется в upstream API.

Для OpenAI-compatible providers используется path-prefix routing. Например, MiniMax-сценарий выставляет `OPENAI_BASE_URL=http://localhost:8080/minimax/v1`; proxy принимает запросы на `/minimax/v1/chat/completions`, снимает prefix и отправляет их в upstream MiniMax API.

Такой подход делает инструмент похожим не на агентный runtime, а на observability shim между CLI-инструментом и LLM provider.

## Dashboard и prompt archive

Live dashboard показывает:

- provider и модель;
- время запроса;
- количество токенов;
- суммарное использование context window;
- цветной fuel gauge: зелёный до 50%, жёлтый 50–80%, красный выше 80%;
- последний prompt в сокращённом виде.

Каждый перехваченный запрос сохраняется в выбранный каталог. Markdown-версия удобна для человеческого разбора prompt history, а JSON сохраняет raw API request body для debugging. Это помогает выяснять, какие system/user prompts, tool outputs или history fragments реально попали в запрос.

## Поддерживаемые CLI и providers

На момент ingest README указывает поддержку:

- Anthropic / Claude Code через `tokentap claude`;
- OpenAI Codex через `tokentap codex`;
- MiniMax через `tokentap run --provider minimax <cmd>`;
- Gemini CLI через `tokentap gemini`, но с известным upstream issue: Gemini CLI игнорирует custom base URLs при OAuth authentication.

Для произвольных команд есть общий режим `tokentap run --provider <name> <cmd>`, где provider может быть `anthropic`, `openai`, `gemini` или `minimax`.

## Связь с agentic development

Tokentap полезен в AI-assisted development workflow, где важно понимать не только итоговый ответ модели, но и стоимость и состав контекста. Он дополняет [RTK]({{ '/wiki/infra/rtk' | relative_url }}): RTK уменьшает token load через filtering/grouping/truncation, а Tokentap показывает фактическое потребление и помогает увидеть, где контекст раздувается.

С [Evolve]({{ '/wiki/llm-agents/evolve' | relative_url }}) связь в feedback loop: Evolve оценивает качество конфигураций AI-coding сессий, а Tokentap даёт наблюдаемость по токенам и prompt archive, который можно использовать для ручного анализа причин успеха или неудачи.

Для практик из [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}) Tokentap важен как проверка реальности: даже хороший project instruction может разрастись или попасть в запрос в неожиданной форме. Prompt archive позволяет увидеть фактический payload, а не предполагать его по файлам правил.

## Ограничения и осторожность

Главный риск Tokentap — приватность prompt archive. Инструмент сохраняет raw prompts и JSON request bodies, поэтому туда могут попасть приватный код, секреты, user data, cookies из tool outputs или внутренние инструкции. Каталог archive нужно выбирать осознанно, не коммитить в репозитории и не отправлять в публичные отчёты без очистки.

Также важно учитывать:

- proxy model зависит от того, уважает ли конкретный CLI custom base URL;
- Gemini CLI имеет известное ограничение с OAuth base URL;
- token counting и cost interpretation зависят от provider/model;
- инструмент показывает traffic, но не заменяет policy layer для data minimization.

## Практический вывод

`Tokentap` делает LLM CLI sessions наблюдаемыми: показывает токены, context-window pressure и фактические prompts. Его ценность особенно высока в длинных coding/research сессиях, где пользователь хочет понимать, почему контекст растёт, где тратятся токены и что именно отправляется в модель.

## Источники

- https://github.com/jmuncor/tokentap
- https://tokentap.ai
