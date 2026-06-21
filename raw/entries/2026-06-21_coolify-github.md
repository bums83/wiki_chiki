---
id: github-coollabsio-coolify-2026-06-21
date: 2026-06-21
source_type: url
source_url: https://github.com/coollabsio/coolify
title: Coolify GitHub repository
domain: tools
tags: [tools, docker, self-hosted, paas, deployment, backend]
---

# Coolify GitHub repository

Source: https://github.com/coollabsio/coolify

Repository metadata observed on 2026-06-21:

- Full name: `coollabsio/coolify`
- Description: open-source, self-hostable PaaS alternative to Vercel, Heroku and Netlify for static sites, databases, full-stack applications and 280+ one-click services on user-owned servers.
- Language: PHP
- Framework/runtime: Laravel 12, Livewire, Horizon, Sanctum, Socialite, Sentry; frontend build via Vite/Tailwind.
- License: Apache-2.0
- Default branch: `v4.x`
- Stars: 57k+
- Topics include: coolify, deployment, docker, docker-compose, laravel, postgres, redis, self-hosted, self-hosting, server, static-site.

Durable source facts:

- Installation command from README: `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`.
- Coolify manages servers, applications and databases over SSH. README says it can manage VPS, bare metal, Raspberry Pi and other hosts with SSH access.
- Project goal: cloud-like deployment UX on user-owned infrastructure, without vendor lock-in; application/database configuration remains on the user’s server.
- Paid cloud version exists at `app.coolify.io`; README frames it as hosted Coolify with high availability, notifications, support and less maintenance.
- Production compose stack includes Coolify app, PostgreSQL, Redis and `coolify-realtime`/Soketi. Persistent data lives under `/data/coolify/...` and named Docker volumes.
- Install script is root/sudo-oriented, configures Docker networking, checks disk space, writes under `/data/coolify/source`, and supports environment variables such as `ROOT_USER_EMAIL`, `ROOT_USER_PASSWORD`, `DOCKER_ADDRESS_POOL_BASE`, `AUTOUPDATE`, `REGISTRY_URL`.
- Repository contains many `templates/compose/*.yaml` service definitions, including Directus, Dify, Grafana, Gitea, GitLab, Immich, Home Assistant, Postgres-backed apps and many other one-click services.
- Models and Livewire components show operational concepts: Application, Server, Project, Environment, Service, ServiceApplication, ServiceDatabase, standalone databases, scheduled backups, private keys, notifications, proxy, terminal, log drains, tags and storage.

Interpretive notes for wiki integration:

- Closest local neighbors: Directus, Teable, PocketBase, ASSH, Antfarm.
- Coolify belongs under `tools`: it is an operator/platform layer for deployments and self-hosted services, not a database engine or a single app backend.
- Main distinction from Directus/Teable/PocketBase: those are application/data platforms to run; Coolify is the deployment/control plane that can host them.
- Main risk: operational ownership moves to the user. Coolify reduces deployment friction, but Docker, servers, backups, upgrades, networking, SSH keys and proxy behavior remain real responsibilities.
