---
id: habr-1071250-reasoning-effort-2026-08-18
date: 2026-08-18
source_type: article
source_url: https://habr.com/ru/articles/1071250/
title: Как управлять reasoning effort в LLM
domain: llm-agents
tags: [llm, agents, eval, workflow, automation]
---

# Как управлять reasoning effort в LLM — source review

Canonical article: https://habr.com/ru/articles/1071250/

## Метаданные retrieval

- Canonical URL получен 2026-08-18.
- JSON-LD `headline`: `Как управлять reasoning effort в LLM`.
- JSON-LD `datePublished` / `dateModified`: `2026-08-17T14:41:22+03:00`.
- В рендере Habr автор указан как `NeoTweetster`; также назван автор оригинального материала Sebastian Raschka, PhD. В JSON-LD поле `author` равно `null`.
- Это длинная объяснительная статья, а не upstream API-документация, model card, исходный код или независимо воспроизводимый бенчмарк.

## Что разбирает Habr-статья

Статья разделяет training-time и inference-time scaling и рассматривает механизмы управления reasoning у нескольких семейств моделей. Её основные тезисы:

- RL с проверяемой наградой (RLVR), SFT и distillation могут формировать reasoning/non-reasoning поведение;
- видимый разделитель вида `<think>` — элемент формата/протокола, а не самостоятельный источник способности рассуждать;
- effort, расход токенов, latency и качество результата образуют trade-off, а не универсальную монотонную гарантию;
- одни системы дают mode switch, другие budget, третьи — выученное поведение, выбираемое prompt/chat template;
- в перспективе router мог бы выбирать модель и reasoning budget по классу задачи, latency и token constraints.

Статья ссылается на DeepSeek-R1, Qwen3, gpt-oss, Thinking Machines Inkling, DeepSeek V4, NVIDIA Nemotron, Kimi и GLM. Наличие ссылки не делает каждое сравнение из Habr-текста независимо проверенным.

## Независимо проверенные источники для Wiki

| Источник | Наблюдаемый факт, перенесённый в Wiki |
|---|---|
| [OpenAI Reasoning models guide](https://platform.openai.com/docs/guides/reasoning) | Значения `reasoning.effort` model-dependent; lower effort ориентирован на скорость/token use, higher — может использовать больше работы; reasoning tokens занимают контекст и тарифицируются; `max_output_tokens` способен вернуть `incomplete` до видимого ответа. Для GPT-5.6 документация называет `mode` и `effort` независимыми. |
| [GPT-5.6 model reference](https://platform.openai.com/docs/models/gpt-5.6) | Текущая reference page показывает reasoning-token support и model-specific context/output limits. Это изменяемые продуктовые факты, не вечные свойства всех LLM. |
| [gpt-oss-120b model card](https://huggingface.co/openai/gpt-oss-120b) | Документирует `low`, `medium` и `high` reasoning levels, выбираемые через system prompt. Это свидетельство для данного семейства, а не универсальная API-конвенция. |
| [Qwen3 technical report](https://arxiv.org/abs/2505.09388) и [Qwen docs](https://qwen.readthedocs.io/en/latest/getting_started/quickstart.html) | Qwen3 документирует thinking/non-thinking behavior в единой модели и model-specific thinking budget. Docs различают soft prompt switch, hard chat-template switch и early-stop continuation pattern. |
| [DeepSeek-R1 upstream README](https://github.com/deepseek-ai/DeepSeek-R1) | R1-Zero описан как large-scale RL без предварительного SFT; полный R1 — как две RL- и две SFT-стадии. Upstream также указывает, что runtime setup и prompting влияют на наблюдаемое reasoning behavior. |

## Сохранённые границы достоверности

- Wiki не утверждает, что UI provider всегда сводит effort к одному system prompt, если это не документировано именно этим provider. В Habr-статье часть рассуждений о реализации GPT-5.6 прямо подана как предположение.
- Длинный chain-of-thought не перенесён как надёжное объяснение, audit trail или доказательство правильности.
- Дополнительные токены не объявлены гарантией улучшения. Решение нужно измерять на outcome gate конкретной задачи и модели.
- Детали DeepSeek V4, Nemotron, Kimi, GLM и Inkling не были изучены как единый совместимый набор во время этого ingest. Они остались указателями из статьи, а не консолидированным техническим фактом.
- Локальные модели не скачивались, не запускались, не обучались и не бенчмаркились. Результат ingest — проверенный operational synthesis публичной документации, не runtime comparison.

## Интеграция в Wiki

Создана [[Reasoning effort в LLM]] как `practice` в `llm-agents`.

Связанные статьи:

- [[Tokentap]] — измерять token/context pressure и защищать prompt archive;
- [[Evolve]] — проводить long-horizon A/B сравнение конфигураций вместо выбора по ощущению;
- [[RTK]] — уменьшать context/tool payload; это отдельная задача от internal reasoning work;
- [[ProcessForge]] — хранить mode/effort/budget и quality gates как явную assignment policy.

Полный source snapshot не создавался: пользователь попросил ingest Habr-статьи; raw entry сохраняет границы источника, retrieval metadata, independently checked sources и пределы верификации.
