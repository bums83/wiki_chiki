---
title: Teable
type: technology
created: 2026-06-18
last_updated: 2026-06-21
domain: tools
related: ["Directus", "PocketBase", "SurrealDB", "Trench", "Coolify"]
sources: ["github-teableio-teable-2026-06-18"]
tags: ["tools", "database", "backend", "api-platform", "admin-panel", "postgresql"]
---

# Teable

`Teable` — open-source no-code database platform с spreadsheet-like интерфейсом поверх PostgreSQL. Проект позиционируется как Airtable alternative: пользователи работают с данными через привычную таблицу, views и collaborative UI, а под капотом остаётся нормальный backend/data stack.

Ключевая формула проекта: **no-code UX + Postgres scale**. Teable пытается дать нетехническим пользователям удобство Airtable, но без полного vendor lock-in и с возможностью self-hosted развёртывания.

## Что делает

Из README видно, что Teable закрывает сразу несколько уровней:

- spreadsheet-like работа с таблицами и записями;
- realtime collaboration для команды;
- views: Grid, Form, Kanban, Gallery, Calendar;
- filtering, sorting, grouping, formatting, formulas, validation;
- aggregation, charts, comments, history, undo/redo;
- attachments preview, import/export и batch editing;
- plugins и SQL Query;
- работа с большими объёмами данных, включая demo на 1M rows.

Практически это не просто spreadsheet clone, а no-code слой для построения data-driven приложений: таблицы становятся операционной базой, а views — интерфейсами для разных ролей и процессов.

## Архитектура и стек

Репозиторий организован как TypeScript monorepo:

- `apps/nextjs-app` — frontend;
- `apps/nestjs-backend` — backend;
- `packages/core`, `sdk`, `db-main-prisma`, `ui-lib` и другие общие пакеты;
- `plugins` — custom plugins.

Standalone Docker example поднимает три основных сервиса:

- Teable application image;
- PostgreSQL 15.4 как основную базу;
- Redis 7.2 как cache layer.

Разработка идёт через `pnpm`, backend запускается из `apps/nestjs-backend`, а база и миграции завязаны на Prisma/Postgres. Это делает Teable ближе к полноценной web application platform, чем к лёгкому single-binary backend.

## Чем отличается от соседних инструментов

Teable находится рядом с [Directus]({{ '/wiki/tools/directus' | relative_url }}), [PocketBase]({{ '/wiki/infra/pocketbase' | relative_url }}) и [SurrealDB]({{ '/wiki/infra/surrealdb' | relative_url }}), но решает другую задачу.

- **Directus** накладывает API/admin слой поверх SQL и силён как backend/control plane.
- **PocketBase** даёт маленький single-binary backend с SQLite, auth, files и realtime для быстрых продуктов.
- **SurrealDB** пытается быть multi-model database/backend layer.
- **Teable** делает акцент на spreadsheet-like no-code приложениях поверх Postgres, где бизнес-пользователь может сам работать с таблицами, views и командными процессами.

То есть Teable важен не как ещё один backend generator, а как рабочий UI-слой над данными, который сохраняет связь с инженерно понятной базой.

## Где уместен

Teable полезен для:

- внутренних операционных баз: CRM-lite, inventory, контент-планы, project trackers;
- командных таблиц, которые переросли Google Sheets/Airtable-подобный SaaS;
- self-hosted no-code сценариев, где данные нельзя или не хочется держать у внешнего провайдера;
- продуктов, где нетехническим пользователям нужен UI, а разработчикам — доступ к Postgres/API;
- прототипов data-driven приложений, которые потенциально должны вырасти до более серьёзной архитектуры.

С [Trench]({{ '/wiki/tools/trench' | relative_url }}) граница простая: Teable управляет сущностями и таблицами, а Trench пишет append-only events и аналитику. В одной системе Teable может быть операционным UI, а Trench — журналом действий и outcome-аналитикой.

[Coolify]({{ '/wiki/tools/coolify' | relative_url }}) закрывает соседний deployment layer: Teable — приложение/операционная база, а Coolify — self-hosted PaaS, через который такие Postgres-backed сервисы можно разворачивать и обслуживать на собственных серверах.

## Лицензия и editions

README указывает, что Teable Community Edition доступен для self-hosting под AGPL. В структуре репозитория также явно разделены `apps` как AGPL 3.0 и `packages` как MIT. Enterprise Edition содержит дополнительные функции вроде AI, authority matrix, automation и advanced admin.

Это важно учитывать до внедрения: Teable открыт и self-hosted, но не является полностью permissive MIT-проектом как единое приложение.

## Ограничения

Teable не отменяет проектирование данных. Если таблицы используются как хаотичный spreadsheet без модели, Postgres сам по себе не спасёт систему.

Также нужно учитывать:

- monorepo и web-app стек сложнее в эксплуатации, чем single binary;
- Postgres и Redis требуют нормального backup/upgrade/monitoring процесса;
- no-code слой удобен, но сложная бизнес-логика всё равно может потребовать custom backend;
- AGPL/EE-разделение требует юридической проверки для коммерческих сценариев.

## Практический вывод

`Teable` закрывает нишу между Airtable-like user experience и нормальным self-hosted database stack. Его стоит рассматривать там, где таблица уже стала операционным приложением, но закрытый SaaS, слабый масштаб или vendor lock-in больше не устраивают.

Главная ценность Teable — не «таблица в браузере», а возможность дать бизнесу удобный no-code интерфейс, сохранив для инженеров Postgres, API и контролируемое развёртывание.

## Источники

- https://github.com/teableio/teable
- https://teable.ai
- https://help.teable.ai
