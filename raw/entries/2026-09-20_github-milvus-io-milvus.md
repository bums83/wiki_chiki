---
id: github-milvus-io-milvus-2026-09-20
date: 2026-09-20
source_type: url
source_url: https://github.com/milvus-io/milvus
title: Milvus — distributed vector database
domain: infra
tags: [database, vector-search, hybrid-search, full-text-search, kubernetes, open-source]
reviewed_revision: 9fcbbec31bba4958e6642f7c0109257207e591fe
reviewed_release: v3.0.2
---

# Milvus — исходный материал

- Upstream: `milvus-io/milvus`, default branch `master`; локально просмотрен shallow clone SHA `9fcbbec31bba4958e6642f7c0109257207e591fe`.
- GitHub API на 2026-09-20: 46 171 stars, 4 256 forks, 1 485 open issues. Последний release: `v3.0.2`, опубликован 2026-09-20.
- Проект под Apache-2.0, относится к LF AI & Data Foundation; Zilliz указан основным контрибьютором.
- Кодовая база на Go и C++; `go.mod` требует Go 1.26.6. Полная сборка требует Linux, Go >=1.21, CMake >=3.26.4 и <4, GCC >=11, Python >3.8 и <=3.11.
- В standalone конфигурации метаданные хранятся в etcd, persistent data — в S3-compatible object storage (MinIO по умолчанию), журнал мутаций — в local RocksMQ либо внешнем Pulsar/Kafka/Woodpecker. В cluster mode Rocksmq не поддержан.
- Upstream описывает distributed/Kubernetes-native разделение compute и storage: query nodes масштабируются для read-heavy, data nodes — для write-heavy. Коллекции хранят dense/sparse vectors вместе со scalar/JSON fields; доступны scalar filtering, HNSW/IVF/FLAT/SCANN/DiskANN, BM25/full-text и hybrid search.
- Простой Python path: `pymilvus`, Milvus Lite для локального файла либо Milvus server/Zilliz Cloud по URI+token. Milvus Lite не следует выдавать за совместимый production substitute для cluster deployment без отдельной проверки feature parity.
- Security capabilities заявлены как authentication, TLS и RBAC; проверенная `configs/milvus.yaml` содержит development defaults и явные примеры учётных данных (`etcdadmin`, `minioadmin`). Их нельзя переносить в production.
- Локальная валидация: `docker compose config -q` на upstream `docker-compose.yml` успешна. Это compose для developer/test environment (builder + etcd + MinIO + Pulsar и др.), не production deployment. Full build/test не запускались: требуют тяжёлого C++/Go dependency build и сервисов; upstream make targets включают `verifiers` и `unittest`.

## Первичные источники

- https://github.com/milvus-io/milvus/tree/9fcbbec31bba4958e6642f7c0109257207e591fe
- https://github.com/milvus-io/milvus/releases/tag/v3.0.2
- https://milvus.io/docs
