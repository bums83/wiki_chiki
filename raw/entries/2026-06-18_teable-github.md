---
id: github-teableio-teable-2026-06-18
date: 2026-06-18
source_type: url
source_url: https://github.com/teableio/teable
title: Teable GitHub repository
domain: tools
tags: [tools, database, backend, api-platform, admin-panel, postgresql]
---

# Teable GitHub repository

Source: https://github.com/teableio/teable

Repository metadata observed on 2026-06-18:

- Full name: `teableio/teable`
- Description: `The Next Gen Airtable Alternative: No-Code Postgres`
- Language: TypeScript
- Stars: 21k+
- Main app license model: Community Edition self-hosting under AGPL; repository structure also marks shared packages as MIT
- Deployment: Docker standalone with Teable app, PostgreSQL and Redis; one-click templates listed in README

## Extracted source notes

Teable describes itself as a platform to “Manage Your Data & Connect Your Team”. It uses a simple spreadsheet-like interface to create database applications, supports realtime team collaboration, and aims to scale to millions of rows.

Core README features:

- aggregation;
- attachments preview;
- batch editing;
- charts;
- comments;
- custom columns;
- field conversion;
- filtering;
- formatting;
- formula support;
- grouping;
- history;
- import/export;
- millions of rows;
- plugins;
- realtime;
- search;
- sorting;
- SQL Query;
- undo/redo;
- validation.

Supported views listed in README:

- Grid View;
- Form View;
- Kanban View;
- Gallery View;
- Calendar View.

Repository structure from README:

```text
.
├── apps (AGPL 3.0)
│   ├── nextjs-app          (front-end)
│   └── nestjs-backend      (backend)
├── packages (MIT)
│   ├── common-i18n         (locales)
│   ├── core                (share code and interface)
│   ├── sdk                 (sdk for extensions)
│   ├── db-main-prisma      (schema, migrations, prisma client)
│   ├── eslint-config-bases
│   └── ui-lib
└── plugins (AGPL 3.0)
```

Standalone Docker deployment from repository uses:

- `ghcr.io/teableio/teable:latest`;
- PostgreSQL 15.4;
- Redis 7.2;
- app assets volume;
- `.env` with Postgres, Redis, public origin and Prisma database URL settings.

Development flow from README:

```bash
corepack enable
pnpm install
make switch-db-mode
cd apps/nestjs-backend
pnpm dev
```

README rationale:

No-code tools are useful because non-technical users can build applications through spreadsheet-like interfaces, but many no-code platforms struggle with scale, data ownership, vendor lock-in, developer ergonomics and integration with normal software standards. Teable positions its answer as: easy UI, access to data, privacy/choice across cloud/on-prem/local, developer compatibility, scale, integration flexibility, and native AI integration in the broader product roadmap.

License note from README:

Teable Community Edition is free for self-hosting under the AGPL license. Enterprise Edition includes advanced features such as AI, authority matrix, automation and advanced admin.
