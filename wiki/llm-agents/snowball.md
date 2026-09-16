---
title: Snowball — обучающийся агент скидок FMCG
type: technology
created: 2026-09-16
last_updated: 2026-09-16
domain: llm-agents
related: ["Evolve", "Reasoning effort в LLM", "Autoresearch"]
sources: ["github-bums83-snowball-2026-09-16"]
tags: [llm, agents, eval, workflow, automation, open-source]
---

# Snowball — обучающийся агент скидок FMCG

[Snowball](https://github.com/bums83/snowball) — Kotlin/JVM 21 прототип, в котором LLM выбирает одну скидку (`0%`, `10%`, `20%`, `30%`), а накопленная структурированная память должна улучшать последующие решения. Это не general-purpose pricing system: рынок синтетический, один магазин — London Central, а baseline подготовлен офлайн из датасета dunnhumby.

## Замкнутый контур

```text
Scenario → решение агента → outcome симулятора → replay 4 действий
→ immutable PromotionCase → детерминированный Lesson → retrieval → следующее решение
```

Сценарий валидируется JSON Schema. Агент читает максимум три наиболее специфичных `Lesson`, получает от модели одно допустимое действие и валидирует ответ; после одной повторной попытки неисправный ответ заменяется детерминированным `0%` с отдельной маркировкой источника. Симулятор скрыт от агента: он не может сам перебрать варианты и узнать oracle-ответ.

## Что именно хранится и почему

`xmemory` содержит три сущности: стабильный `SKU`, неизменяемый `PromotionCase` и производный `Lesson`. В case сохраняются прибыли для всех четырёх контрфактических скидок, лучший вариант и regret. Поэтому lesson можно пересчитать из доказательств без повторного запуска скрытого симулятора.

Рекомендацию не выбирает LLM: для каждого lesson bucket код суммирует replay-profit по действиям и выбирает максимум; tie-break — меньшая скидка. Confidence строится из объёма evidence, согласованности case с рекомендацией и преимущества по прибыли. Это полезный паттерн: модель формулирует решение в ограниченном интерфейсе, а доказательства и агрегирование остаются детерминированными.

## Как измеряется эффект памяти

Корректный benchmark сравнивает две изолированные xmemory-инстанции на тех же 50 held-out сценариях: одна пустая, другая предварительно обучена. Модель, prompt, simulator version, коэффициенты, округление и `scenario_id` одинаковы; learning выключен, чтобы измерение не создавало новые уроки. Метрики: доля oracle-optimal действий, regret и gross profit.

README проекта сообщает: без памяти — 44% optimal decisions и 44.04 total regret; с exact-key memory — 76% и 12.17; с fallback-key memory — 80% и 7.18. Это узкое upstream-утверждение о конкретном симуляторе и split, не доказательство эффективности подхода на реальном ценообразовании. Локально CI не был выполнен: `./gradlew spotlessCheck build` остановился до запуска, потому что на хосте нет Java/JAVA_HOME.

## Инженерные компромиссы

- Транспорт намеренно in-process, не Kafka: границы заданы портами, но отказоустойчивого брокерного контура нет.
- Decision journal хранится в памяти процесса: он даёт idempotency внутри запуска, но restart начинает незавершённый прогон заново.
- xmemory writes идут через `structured_mutations`, без модели; reads всё ещё могут вызывать модель, стоят quota и имеют cache-effect. Репозиторий документирует, что conversational reads ненадёжны для key lookup.
- Схемы и примеры в `docs/` являются source of truth; committed diagrams могут отставать от runtime-кода.

## Связи в Wiki

[ Evolve ]({{ '/wiki/llm-agents/evolve' | relative_url }}) измеряет конфигурации AI-assistant в реальных coding sessions; Snowball измеряет другой объект — влияние ранее накопленного evidence на решение в контролируемом симуляторе. Общий принцип: не путать правдоподобную историю с измеренным outcome.

[Reasoning effort в LLM]({{ '/wiki/llm-agents/reasoning-effort' | relative_url }}) задаёт policy для model/budget. Snowball показывает практическую границу: увеличенный reasoning не заменяет корректные data, counterfactual evaluation, schema validation и evidence trace.

[Autoresearch]({{ '/wiki/llm-agents/autoresearch' | relative_url }}) автоматизирует цикл «изменение → короткий эксперимент → метрика». Snowball применяет похожую дисциплину к policy agent: фиксированный simulator, разделённые train/benchmark и observable artefacts вместо самооценки модели.

## Источники

- [bums83/snowball](https://github.com/bums83/snowball), проверенный revision `b055f34b781def1400bf05845b91118c4fa36e4d`
- `docs/benchmark/README.md`, `docs/xmemory/README.md`, `GOTCHAS.md`, исходный код и тестовая структура этого revision
