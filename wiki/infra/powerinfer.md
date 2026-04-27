---
title: PowerInfer
type: technology
created: 2026-04-27
last_updated: 2026-04-27
domain: infra
related: ["PostgreSQL + VectorChord"]
tags: ["llm-inference", "local-llm", "gpu-optimization", "powerinfer", "llm-serving"]
sources: ["github-tiiny-ai-powerinfer"]
---

# PowerInfer

`PowerInfer` — это high-speed LLM inference engine для локального развёртывания больших языковых моделей на обычном PC с одной consumer-grade GPU.

Проект разработан в SJTU-IPADS (Shanghai Jiao Tong University). Основная идея — использование power-law распределения нейронных активаций: небольшое количество «hot» нейронов активируется стабильно, а большинство «cold» нейронов зависят от конкретного входа. PowerInfer загружает hot-нейроны на GPU для быстрого доступа, а cold-нейроны вычисляет на CPU, что драматически снижает GPU memory demands и CPU-GPU data transfers.

## Как это устроено

Ключевой инсайт —稀疏激活 (sparse activation) в LLM:

- LLM показывают power-law распределение активаций нейронов
- Небольшое подмножество нейронов («hot») активируются стабильно для разных входов
- Большинство нейронов («cold») варьируются в зависимости от конкретного входа
- Это присуще ReLU-моделям, где часть нейронов может быть практически неактивной

PowerInfer эксплуатирует это через:

1. **GPU-CPU hybrid engine** — hot-нейроны прединицируются на GPU, cold вычисляются на CPU
2. **Adaptive predictors** — предсказывают, какие нейроны будут hot/cold для конкретного входа
3. **Neuron-aware sparse operators** — оптимизируют эффективность активаций и вычислительной sparsity

## Производительность

На одной RTX 4090 (24GB VRAM) PowerInfer показывает:
- **OPT-175B**: ~13.20 tokens/s в среднем (пик 29.08 tokens/s) — всего на 18% медленнее, чем server-grade A100
- **Falcon(ReLU)-40B**: до 11.69x быстрее llama.cpp при сопоставимой точности

PowerInfer-2 (2024):
- TurboSparse-Mixtral-47B на смартфонах: 11.68 tokens/s — до 22x быстрее state-of-the-art решений

## Поддерживаемые модели

PowerInfer работает с ReLU-sparse моделями:
- **Falcon(ReLU)-40B**
- **LLaMA(ReLU) family** (7B, 13B, 70B)
- **ProSparse Llama2** (7B, 13B)
- **Bamboo-7B** (рекомендуемая авторская модель, отличная производительность и скорость)
- **TurboSparse-Mixtral-47B** (PowerInfer-2)
- **SmallThinker** (21B и 4B, on-device inference фреймворк)

## Платформы

- Linux (NVIDIA GPU + CUDA, AMD GPU + ROCm)
- Windows (NVIDIA GPU)
- macOS (Apple M chips, CPU only — Metal backend в разработке)

## Архитектура и формат

PowerInfer использует специальный формат **PowerInfer GGUF**, основанный на GGUF:
- содержит и веса LLM, и веса предиктора
- горячие нейроны offloadятся на GPU, cold хранятся в CPU memory

Для крупных моделей (>=40B нe квантованных) конвертация из оригинальных весов доступна через `convert.py`.

## Практический смысл

PowerInfer важен для сценариев локального LLM inference:

1. **Персональные AI-ассистенты** — запуск больших моделей на обычном железе без cloud
2. **Edge deployment** — PowerInfer-2 оптимизирован для смартфонов
3. **Экономия ресурсов** — один consumer GPU вместо server-grade A100
4. **Приватность** — все данные обрабатываются локально, ничего не уходит в cloud

## Связь с существующим кластером

PowerInfer — это инфраструктурный инструмент для LLM serving, поэтому он связан с:

- [PostgreSQL + VectorChord]({{ '/wiki/infra/postgresql-vectorchord-hybrid-search' | relative_url }}) — оба проекта про локальный AI-стек: VectorChord для semantic search, PowerInfer для inference. Вместе могут формировать локальную RAG-систему без зависимости от cloud-провайдеров.

PowerInfer также показывает общую тенденцию: sparse, locality-aware подходы к оптимизации нейросетей, что релевантно для anyone building local AI systems.

## Ограничения

- Работает эффективно только с ReLU-sparse моделями, не со всеми архитектурами
- Требует специфическую подготовку модели (PowerInfer GGUF формат)
- CPU-only режим на Mac пока не оптимизирован (Metal backend в разработке)

## Источники

- https://github.com/Tiiny-AI/PowerInfer
- https://arxiv.org/abs/2406.06282 (PowerInfer-2)
- https://arxiv.org/abs/2406.05955 (Turbo Sparse)