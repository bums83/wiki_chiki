---
id: github-frigadehq-trench-2026-05-27
date: 2026-05-27
source_type: url
source_url: https://github.com/frigadehq/trench
title: Trench — Open-Source Analytics Infrastructure
domain: tools
tags: [tools, database, backend, api-platform, monitoring]
---

# Trench — Open-Source Analytics Infrastructure

Trench — open-source analytics infrastructure от Frigade. Проект представляет собой event tracking system поверх Apache Kafka и ClickHouse, предназначенный для real-time analytics и обработки больших потоков событий.

Ключевые факты из README и GitHub metadata:

- GitHub: https://github.com/frigadehq/trench
- Homepage: https://trench.dev
- Documentation: https://docs.trench.dev
- License: MIT
- Language: TypeScript
- Core stack: Kafka, ClickHouse, Node.js
- Deployment: single production-ready Docker image; self-hosted и managed cloud варианты
- API: совместимость с Segment Track / Group / Identify
- Возможности: real-time querying, webhooks, event replay / event tracking, no-cookie GDPR/PECR-friendly tracking

Базовый self-hosted quickstart из README:

```sh
git clone https://github.com/frigadehq/trench.git
cd trench/apps/trench
cp .env.example .env
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build --force-recreate --renew-anon-volumes
```

Пример записи события через `/events` использует Bearer public key и JSON-массив `events`. Пример чтения событий использует `/events?event=...` с private key. Также есть endpoint `/queries` для raw SQL-запросов к данным.

Для production Kafka поддерживаются SASL и SSL/TLS настройки через переменные окружения; для ClickHouse Kafka authentication требуется серверная конфигурация ClickHouse.
