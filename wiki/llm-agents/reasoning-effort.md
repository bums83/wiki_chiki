---
title: Reasoning effort в LLM
type: practice
created: 2026-08-18
last_updated: 2026-08-18
domain: llm-agents
related: ["Tokentap", "Evolve", "RTK", "ProcessForge"]
tags: [llm, agents, eval, workflow, automation]
sources: ["habr-1071250-reasoning-effort-2026-08-18", "openai-reasoning-docs-2026-08-18", "qwen3-docs-2026-08-18", "gpt-oss-model-card-2026-08-18", "deepseek-r1-readme-2026-08-18"]
---

# Reasoning effort в LLM

`Reasoning effort` — это не «уровень интеллекта» и не универсальная кнопка качества. Это provider- и model-specific способ выделить больше или меньше вычислений на один запрос. Практически он меняет trade-off между качеством, latency и стоимостью; для некоторых моделей — ещё и режим работы или допустимый reasoning budget.

Нормальная цель — не поставить максимум везде, а получить **минимальную конфигурацию, стабильно проходящую нужную проверку**. Всё остальное — перерасход времени и токенов.

## Не смешивать четыре ручки

| Ручка | Что меняет | Что не гарантирует |
|---|---|---|
| Модель / model tier | возможности и профиль ошибок самого чекпойнта | что больше параметров всегда выгоднее |
| Thinking / reasoning mode | включает, выключает или меняет режим исполнения там, где модель это поддерживает | единый API между providers |
| `reasoning.effort` / budget | объём работы модели при инференсе | правильный факт, корректное действие или доступ к данным |
| `max_output_tokens` и context budget | жёсткий предел на сгенерированные токены и доступное место в контексте | что модель успеет завершить мысль до лимита |

В актуальном OpenAI Responses API `reasoning.mode` и `reasoning.effort` названы независимыми параметрами; поддерживаемые значения effort зависят от модели. Reasoning-токены тарифицируются как output tokens, занимают context window и могут закончиться до появления видимого ответа. Следовательно, `max_output_tokens` — это не безобидный «лимит длины текста», а часть надёжности workflow.

У переносимых open-weight моделей механика другая. `gpt-oss` документирует `low` / `medium` / `high` через system prompt. Qwen3 документирует soft/hard switch thinking mode и отдельный thinking budget; в open-source runtimes budget может требовать двухэтапного продолжения генерации. Нельзя переносить имена параметров или поведение из одного стека в другой без проверки конкретной model card и chat template.

## Что подтверждают источники, а что нет

Habr-статья [«Как управлять reasoning effort в LLM»](https://habr.com/ru/articles/1071250/) — хороший обзор нескольких подходов: RL с проверяемой наградой, SFT на reasoning/non-reasoning примерах, budget-aware reward, chat templates и внешнее ограничение reasoning trace.

Для Wiki сохранены только опорные, проверяемые части:

- upstream DeepSeek-R1 описывает R1-Zero как модель с RL без предварительного SFT, а полный R1 — как pipeline с двумя RL- и двумя SFT-этапами;
- отчёт Qwen3 подтверждает единый checkpoint с thinking/non-thinking mode, post-training на данных обоих форматов и thinking budget;
- model card `gpt-oss-120b` подтверждает три документированных уровня reasoning;
- официальная OpenAI-документация подтверждает, что effort — параметр исполнения, а не универсальная шкала между моделями.

Конкретные механизмы других моделей, перечисленных в Habr (например, DeepSeek V4, Nemotron, Kimi, GLM и Inkling), не перенесены в статью как единый установленный факт: это отдельные технические отчёты и версии, которым нужна самостоятельная проверка перед проектным решением.

## Рабочая policy для агента

### 1. Классифицировать задачу до вызова модели

Не спрашивать «какой effort лучше вообще». Сначала определить:

- есть ли проверяемый результат: тест, schema, calculation, source citation, acceptance check;
- цена ошибки и цена задержки;
- нужны ли tools и несколько dependent steps;
- можно ли безопасно повторить выполнение;
- есть ли внешний side effect: публикация, удаление, платеж, отправка сообщения.

Факты, которые нельзя получить из контекста, не становятся достовернее от высокого effort. Им нужен поиск, первоисточник или инструмент проверки. Внешнее действие не становится безопасным от длинного reasoning — ему нужны scope, подтверждение и precondition check.

### 2. Выбирать минимальный рабочий режим

Ниже — **стартовая policy**, а не переносимая спецификация API:

| Класс задачи | Старт | Когда повышать |
|---|---|---|
| Классификация, extraction, короткий ответ без tool chain | `none` или `low`, только после eval | если рушится format/schema или растёт ложная классификация |
| Один ограниченный tool call, анализ таблицы, черновик | `low` | если не проходит явную проверку результата |
| Coding, поиск с верификацией, план из нескольких шагов | `medium` | если baseline не проходит тесты, evidence gate или reviewer check |
| Сложный debugging, архитектурный выбор, долгий research workflow | `high` | только когда измеримый выигрыш окупает latency и cost |
| `xhigh` / `max` | не default | только для изолированной сложной задачи с заранее заданным eval и достаточным budget |

Провайдерные метки различаются. Например, у модели может не быть `none`, `xhigh` или `max`; тогда policy должна выбрать ближайший поддерживаемый режим, а не подменять его произвольным system prompt.

### 3. Эскалировать только проигравший кейс

Правильный loop:

1. Запустить baseline на выбранном классе задач.
2. Проверить outcome: тесты, schema, citations, diff, acceptance criteria.
3. Если outcome не прошёл — сначала выяснить причину: плохой контекст, недостающий tool, неверная задача, недостаточный budget или предел модели.
4. Увеличить **одну** переменную: effort, model tier, context budget либо quality of evidence.
5. Сохранить результат эксперимента и сравнить cost per accepted outcome.

Нельзя автоматически повторять side effect только потому, что был поднят effort. Сначала нужно отделить reasoning/review от исполнения и определить, допустима ли новая попытка без человека.

## Наблюдаемость вместо ощущения

Для каждой policy нужны хотя бы:

- model, snapshot/version, mode и effort;
- входной, output и — если API показывает — reasoning token usage;
- latency, retries и `incomplete`/timeout state;
- outcome gate: test pass, валидный JSON, source coverage, reviewer acceptance;
- стоимость **принятого** результата, а не стоимость одного запроса.

[Tokentap]({{ '/wiki/tools/tokentap' | relative_url }}) полезен как слой наблюдаемости traffic, prompt archive и context pressure, но его архив может содержать приватные prompts, tool outputs и секреты. Не коммитить его как evidence без redaction.

[Evolve]({{ '/wiki/llm-agents/evolve' | relative_url }}) полезен для медленного A/B-сравнения конфигураций AI-coding сессий. Он не доказывает, что одинаковая настройка будет лучшей для research, support или внешних операций. [RTK]({{ '/wiki/infra/rtk' | relative_url }}) решает другую задачу: сжимает входящий tool/context payload, но не заменяет управление reasoning budget.

## Границы

- Больше reasoning не лечит ложный source, устаревшие данные, неверные права доступа или отсутствующий инструмент.
- Не считать скрытый reasoning trace аудит-логом. Для аудита нужны observable artifacts: запросы, источники, tool outputs, tests, diff и финальная проверка.
- Жёстко обрезанный budget может вернуть незавершённый или менее надёжный результат; это нужно обрабатывать явно, а не интерпретировать как успех.
- Параметры и дефолты меняются быстрее, чем статьи. Перед внедрением сверять API/model documentation на конкретные дату, model ID и snapshot.

[ProcessForge]({{ '/wiki/llm-agents/processforge' | relative_url }}) даёт подходящее место для такой policy: фиксировать выбранные model/effort/budget, expected output и gate в assignment. Сам ProcessForge не выбирает reasoning mode и не заменяет экспериментальную проверку.

## Практический вывод

`Reasoning effort` следует использовать как **измеряемый routing parameter**. Низкий effort — не признак халтуры, а нормальный baseline для простых и проверяемых задач. Высокий — не «безопасный максимум», а дорогой режим, который оправдан только тогда, когда прошёл на ваших задачах и не вытеснил более важные меры: хороший контекст, tools, source validation и quality gates.

## Источники

- [Habr: «Как управлять reasoning effort в LLM»](https://habr.com/ru/articles/1071250/)
- [OpenAI API: Reasoning models](https://platform.openai.com/docs/guides/reasoning)
- [OpenAI: GPT-5.6 model reference](https://platform.openai.com/docs/models/gpt-5.6)
- [OpenAI gpt-oss-120b model card](https://huggingface.co/openai/gpt-oss-120b)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)
- [Qwen: Quickstart / thinking budget](https://qwen.readthedocs.io/en/latest/getting_started/quickstart.html)
- [DeepSeek-R1 upstream README](https://github.com/deepseek-ai/DeepSeek-R1)
