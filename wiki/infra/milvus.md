---
title: Milvus
type: technology
created: 2026-09-20
last_updated: 2026-09-20
domain: infra
related: ["PostgreSQL + VectorChord", "SurrealDB", "PocketBase", "Teable"]
sources: ["github-milvus-io-milvus-2026-09-20"]
tags: [database, vector-search, hybrid-search, full-text-search, kubernetes, open-source]
---

# Milvus

`Milvus` — специализированная vector database для retrieval-нагрузок: хранит dense и sparse vectors вместе со scalar/JSON-полями, строит ANN-индексы и выполняет vector, full-text и hybrid search с filtering. Это не embedding-модель, не готовый RAG-продукт и не универсальная OLTP-база.

## Место в архитектуре

Milvus рассчитан на путь от локального prototyping до распределённого сервиса. В лёгком варианте Python SDK `pymilvus` может открыть локальный файл через Milvus Lite. Для сервера доступны standalone deployment и кластерный режим; managed-вариант — Zilliz Cloud.

В распределённом режиме upstream разделяет compute и storage: query nodes обслуживают чтение, data nodes — ingestion, а stateless services рассчитаны на горизонтальное масштабирование и восстановление в Kubernetes. Это сильнее обычной embedded vector extension, но покупается отдельным operational контуром.

| Слой | Роль | Что нужно эксплуатировать |
|---|---|---|
| Метаданные/service discovery | etcd | HA, backup, изоляция namespace/root path |
| Persistent data | S3-compatible object storage / MinIO | bucket, credentials, lifecycle, durability |
| Mutation/WAL | RocksMQ, Pulsar, Kafka или Woodpecker | выбор backend и capacity; RocksMQ — только standalone |
| Query/data services | Milvus nodes | ресурсы, replicas, scaling, observability |

## Retrieval-возможности

Upstream документирует HNSW, IVF, FLAT, SCANN и DiskANN, включая вариации с quantization, `mmap` и GPU-indexing. Выбор индекса зависит от размера корпуса, latency/recall target, памяти и write/read profile; «лучшего индекса» без workload benchmark нет.

Помимо dense semantic retrieval Milvus поддерживает sparse vectors, BM25 full-text search и hybrid search. Dense и sparse представления можно держать в одной collection и затем объединять/переранжировать кандидатов. Это удобно для RAG, semantic/image search и recommendation, но quality всё равно определяется corpus, chunking, embedding model, filtering и evaluation, а не одной установкой базы.

В этом классе задач Milvus близок к [PostgreSQL + VectorChord]({{ '/wiki/infra/postgresql-vectorchord-hybrid-search' | relative_url }}): обе системы умеют hybrid retrieval. Граница другая: Postgres-стек оставляет документы, транзакционные данные и retrieval в знакомой SQL-системе; Milvus — отдельный специализированный search service, оправданный когда объём/throughput/tenant isolation начинают давить на общий Postgres-контур.

## API, безопасность и deployment boundary

Python quickstart использует `MilvusClient`: создать collection с размерностью, insert records, затем выполнить `search`. Внешнее приложение должно само строить embeddings, управлять schema, ingestion/reindexing и измерять качество выдачи.

Milvus заявляет authentication, TLS и RBAC. Но checked `configs/milvus.yaml` содержит development defaults, включая `etcdadmin` и `minioadmin`, а TLS у внешних зависимостей выключен. Это исходный пример, не безопасный production baseline: credentials, TLS, object-storage IAM, network segmentation и доступ к management endpoints должны быть заданы оператором.

Standalone не означает «один бинарник без зависимостей»: конфигурация использует etcd и S3-compatible storage; журнал в standalone по умолчанию может быть локальным RocksMQ. Cluster mode добавляет orchestration, node placement, replicas, monitoring и backup/restore policy. Upstream `docker-compose.yml` — developer/test compose с builder, etcd, MinIO, Pulsar и дополнительными test services, не production reference.

## Сравнение с соседними страницами

- [PostgreSQL + VectorChord]({{ '/wiki/infra/postgresql-vectorchord-hybrid-search' | relative_url }}) — рациональный путь, если retrieval должен жить рядом с реляционными данными и SQL; Milvus — отдельная search база для самостоятельного масштабирования.
- [SurrealDB]({{ '/wiki/infra/surrealdb' | relative_url }}) — multi-model database/backend с vector и graph capabilities; Milvus жертвует широтой модели ради специализированного vector-search слоя.
- [PocketBase]({{ '/wiki/infra/pocketbase' | relative_url }}) — лёгкий SQLite backend для MVP; это другой масштаб и не замена search cluster.
- [Teable]({{ '/wiki/tools/teable' | relative_url }}) — operational/no-code UI поверх Postgres, а не retrieval engine. Он может быть интерфейсом данных вокруг pipeline, но не конкурентом Milvus.

## Проверенная граница фактов

Для статьи просмотрен upstream SHA [`9fcbbec`](https://github.com/milvus-io/milvus/commit/9fcbbec31bba4958e6642f7c0109257207e591fe) и release `v3.0.2` от 2026-09-20. Локально успешно выполнен `docker compose config -q` для upstream compose. Полная сборка и `make unittest` не запускались: это тяжёлая C++/Go сборка с несколькими сервисными зависимостями. Следовательно, утверждения о производительности и feature-completeness взяты из первичной документации, а не из локального benchmark.

## Практический вывод

Milvus уместен, когда retrieval — отдельный масштабируемый subsystem: много векторов, независимый read/write scaling, hybrid dense+sparse search и понятная команда, готовая эксплуатировать etcd, object storage, WAL и кластер. Для небольшого продукта или retrieval, тесно связанного с SQL-данными, отдельная distributed база часто добавит больше operational cost, чем пользы. Начинать стоит с измеримого retrieval baseline и migration threshold, а не с «векторной БД по умолчанию».

## Источники

- [Upstream repository](https://github.com/milvus-io/milvus/tree/9fcbbec31bba4958e6642f7c0109257207e591fe)
- [README at reviewed SHA](https://github.com/milvus-io/milvus/blob/9fcbbec31bba4958e6642f7c0109257207e591fe/README.md)
- [Configuration at reviewed SHA](https://github.com/milvus-io/milvus/blob/9fcbbec31bba4958e6642f7c0109257207e591fe/configs/milvus.yaml)
- [Release v3.0.2](https://github.com/milvus-io/milvus/releases/tag/v3.0.2)
- [Milvus documentation](https://milvus.io/docs)
