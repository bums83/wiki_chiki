---
title: Nanochat
type: technology
created: 2026-04-13
last_updated: 2026-04-13
domain: llm-agents
related: ["Autoresearch", "Validation bits per byte", "Overnight experimentation"]
sources: ["github-karpathy-nanochat"]
---

# Nanochat

`nanochat` — минималистичный training harness Андрея Карпаты для end-to-end работы с LLM на сравнительно небольшом бюджете. Это не «универсальный framework на все случаи жизни», а сильный, компактный baseline для быстрых экспериментов.

## Что в нём есть

Проект покрывает весь базовый контур:
- токенизация,
- pretraining,
- finetuning,
- evaluation,
- inference,
- chat UI.

То есть это не только pretraining sandbox, а почти полный учебно-исследовательский контур.

## Главный дизайн-принцип

`nanochat` строится вокруг одного dial-а сложности: `--depth`.

Пользователь задаёт глубину трансформера, а остальные гиперпараметры подстраиваются автоматически так, чтобы конфигурация оставалась compute-optimal. Это резко снижает когнитивную сложность и делает систему удобной для исследований.

## Почему проект важен

В LLM tooling часто есть две крайности:
- либо игрушечный минимализм без реальной ценности,
- либо огромный framework со слоями абстракций, фабриками и конфигами.

`nanochat` интересен тем, что старается удержать середину: минимальный код, но реальная исследовательская мощность.

## Метрики и speedrun

Вокруг проекта построен режим `GPT-2 speedrun` — гонка за минимальное wall-clock время, необходимое чтобы обогнать GPT-2 по метрике CORE.

Для этого обычно смотрят на:
- [Validation bits per byte](/wiki/llm-agents/validation-bits-per-byte/) (`val_bpb`),
- DCLM CORE score,
- throughput,
- VRAM utilization,
- time to GPT-2.

## Связь с autoresearch

[Autoresearch](/wiki/llm-agents/autoresearch/) — это по сути выделенный из `nanochat` автономный research-loop. Если `nanochat` — это общий research harness, то `autoresearch` — это агентная надстройка для автоматического поиска улучшений внутри этого контура.

## Практический вывод

`nanochat` полезно понимать как **базовую лабораторию**, а `autoresearch` — как её автоматизированного исследователя.

## Источники

- [karpathy/nanochat](https://github.com/karpathy/nanochat)
