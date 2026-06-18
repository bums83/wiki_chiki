---
title: SurrealDB
type: technology
created: 2026-05-07
last_updated: 2026-06-18
domain: infra
related: ["PostgreSQL + VectorChord", "Directus", "PocketBase", "Teable"]
tags: ["surrealdb", "database", "graph-db", "document-db", "realtime", "multi-model", "backend"]
sources: ["github-surrealdb-surrealdb-2026-05-07"]
---

# SurrealDB

`SurrealDB` — это multi-model database на Rust, которая пытается собрать в одном движке document, graph, relational, time-series, geospatial и key-value модели.

На практике это выглядит как одна база для систем, где нужны одновременно:
- структурированные данные,
- граф связей,
- realtime-обновления,
- гибкие запросы,
- permissions на уровне строк,
- и возможность использовать базу как backend layer.

## Что это за класс системы

SurrealDB стоит между классической SQL-базой, graph database и backend platform.

Её сильная сторона — не просто хранение данных, а попытка дать один unified layer для приложений, где смешиваются разные типы сущностей и связей.

Поэтому она особенно интересна для:
- knowledge graphs,
- AI-agent backends,
- realtime приложений,
- data-intensive продуктов,
- embedded и edge-сценариев.

## Что она даёт

По README у SurrealDB есть несколько важных свойств:
- multi-model storage;
- SurrealQL как SQL-like язык;
- full-text, vector и hybrid search;
- GraphQL, WebSocket и SQL-ориентированные способы доступа;
- row-level permissions;
- встроенная auth-модель;
- возможность работать как BaaS-подобный backend.

Именно сочетание этих свойств делает её интересной не только как базу, но и как часть application platform.

## Где она полезна

SurrealDB особенно уместна там, где обычная связка "SQL + отдельный graph layer + realtime service" начинает расползаться по стеку.

Она может быть хорошим выбором, если нужно:
- быстро поднять backend для продукта с разными типами данных,
- хранить графовые связи без отдельной graph DB,
- дать приложению realtime поведение,
- упростить инфраструктуру для AI-сценариев,
- уменьшить количество отдельных сервисов.

В этом смысле она хорошо дополняет [PostgreSQL + VectorChord]({{ '/wiki/infra/postgresql-vectorchord-hybrid-search' | relative_url }}): там акцент на локальном retrieval-стеке поверх PostgreSQL, а здесь — на более широком multi-model backend.

## Сравнение с соседними инструментами

С точки зрения wiki SurrealDB удобно ставить рядом с [Directus]({{ '/wiki/tools/directus' | relative_url }}) и [PocketBase]({{ '/wiki/infra/pocketbase' | relative_url }}), но они решают разные задачи.

- **Directus** — это control layer и админка поверх SQL-базы.
- **PocketBase** — лёгкий single-binary backend для быстрых прототипов.
- **SurrealDB** — база, которая пытается сама быть и storage, и query layer, и частью backend experience.
- **Teable** — no-code application layer поверх PostgreSQL, где главным интерфейсом становится spreadsheet-like UI и набор views для команды.

То есть это не замена всем сразу, а отдельный класс системы: более амбициозный, чем лёгкий embedded backend, но и более цельный, чем чисто админский слой поверх SQL.

## Ограничения

Важно учитывать и обратную сторону:
- multi-model базы сложнее в освоении, чем обычный PostgreSQL;
- перенос архитектуры в одну систему не всегда упрощает реальную эксплуатацию;
- BSL 1.1 требует отдельной проверки для коммерческого использования;
- для части задач PostgreSQL + специализированные инструменты могут оказаться проще и надёжнее.

## Практический вывод

`SurrealDB` — интересный вариант, когда нужен один backend-движок для смешанных данных, графов и realtime-сценариев.

Если задача — собрать быстрый, гибкий и сравнительно цельный data layer, SurrealDB заслуживает внимания. Если же нужен более консервативный и предсказуемый путь, то PostgreSQL-ориентированный стек остаётся сильной альтернативой.

## Источники

- https://github.com/surrealdb/surrealdb
- https://surrealdb.com/docs
