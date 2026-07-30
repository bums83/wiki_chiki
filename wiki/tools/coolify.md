---
title: Coolify
type: technology
created: 2026-06-21
last_updated: 2026-07-30
domain: tools
related: ["Directus", "Teable", "PocketBase", "ASSH", "Antfarm", "cmux-ssh-here", "Boring Computers", "ru-marketplace-mcp", "Cobalt"]
sources: ["github-coollabsio-coolify-2026-06-21"]
tags: ["tools", "docker", "self-hosted", "paas", "deployment", "backend"]
---

# Coolify

`Coolify` — open-source self-hosted PaaS/control plane для развёртывания приложений, баз данных и готовых сервисов на собственных серверах. Проект позиционируется как альтернатива Heroku, Netlify и Vercel, но с другим владением: инфраструктура остаётся у пользователя, а Coolify даёт web UI и automation layer поверх Docker/SSH.

Коротко: **cloud-like deployment UX на своих VPS/bare metal/Raspberry Pi**. Для доступа к серверам Coolify использует SSH; для запуска ресурсов — Docker, Docker Compose и набор встроенных шаблонов.

## Что делает

По README и структуре репозитория Coolify закрывает несколько операционных задач:

- управление серверами через SSH;
- деплой static sites, full-stack apps и Docker/Docker Compose ресурсов;
- запуск standalone databases: PostgreSQL, MySQL, MariaDB, MongoDB, Redis, KeyDB, Dragonfly, ClickHouse и другие;
- one-click services через `templates/compose/*.yaml` — в репозитории сотни compose-шаблонов;
- управление переменными окружения, persistent volumes, storage и scheduled tasks;
- scheduled database backups и backup executions;
- webhooks, logs, metrics, terminal access и resource operations;
- notifications через email, Telegram, Discord, Slack, Pushover и webhooks;
- proxy/dynamic configuration layer, Cloudflare tunnel и server-side security/patch views.

В этом смысле Coolify — не приложение, которое пользователь разворачивает ради одной функции, а deployment/control plane для множества приложений.

## Архитектура

Репозиторий — Laravel/PHP application:

- `composer.json` указывает Laravel 12, Livewire 3, Horizon, Sanctum, Socialite, Sentry, Flysystem S3/SFTP и другие production-зависимости;
- frontend собирается через Vite/Tailwind;
- production compose stack включает Coolify app, PostgreSQL, Redis и `coolify-realtime`/Soketi;
- данные Coolify монтируются из `/data/coolify/...`, включая SSH keys, applications, databases, services и backups;
- модельный слой содержит `Application`, `Server`, `Project`, `Environment`, `Service`, `ServiceApplication`, `ServiceDatabase`, standalone database models, scheduled backups, private keys, storages и notification settings.

Установка из README выглядит как bootstrap-скрипт:

```bash
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```

Скрипт рассчитан на root/sudo, проверяет Docker/network pool/disk space, пишет конфигурацию в `/data/coolify/source/.env` и поддерживает параметры вроде `ROOT_USER_EMAIL`, `ROOT_USER_PASSWORD`, `DOCKER_ADDRESS_POOL_BASE`, `AUTOUPDATE`, `REGISTRY_URL`.

## Чем отличается от соседних инструментов

Coolify удобно ставить рядом с [Directus]({{ '/wiki/tools/directus' | relative_url }}), [Teable]({{ '/wiki/tools/teable' | relative_url }}) и [PocketBase]({{ '/wiki/infra/pocketbase' | relative_url }}), но слой другой.

- **Directus** — backend/admin/API layer поверх SQL.
- **Teable** — no-code spreadsheet-like application layer поверх PostgreSQL.
- **PocketBase** — single-binary backend для быстрых продуктов.
- **Coolify** — deployment platform, которая может запускать такие приложения и их инфраструктуру на пользовательских серверах.

То есть Coolify не заменяет backend/application platform. Он отвечает на вопрос: где и как это всё развернуть, обновлять, проксировать, бэкапить и наблюдать без ручной сборки каждого Docker workflow.

## SSH и серверный контур

Так как Coolify управляет внешними серверами через SSH, он концептуально пересекается с [ASSH]({{ '/wiki/tools/assh' | relative_url }}). ASSH стабилизирует локальную SSH-конфигурацию, aliases и gateway chains; Coolify использует SSH как operational transport для управления remote Docker hosts. [cmux-ssh-here]({{ '/wiki/tools/cmux-ssh-here' | relative_url }}) закрывает другой SSH-сценарий: не управление серверным парком, а временный token-auth shell в локальной сети без постоянного `sshd`.

Это важная граница: Coolify упрощает деплой, но не отменяет дисциплину вокруг SSH keys, bastion routes, firewall, Docker daemon, backups и monitoring. Если серверный доступ хаотичен, PaaS-панель только частично скрывает проблему.

## Где уместен

Coolify полезен, когда нужно:

- заменить простые Heroku/Vercel/Netlify-сценарии self-hosted подходом;
- держать приложения и базы на своих VPS или bare metal;
- быстро поднимать open-source сервисы из compose templates;
- дать команде web UI для деплоя без ручного SSH/Docker Compose на каждый проект;
- сохранить больше контроля над конфигурацией, volumes и окружением;
- развернуть внутренние tools вроде Directus/Teable/Gitea/Grafana/Immich без отдельного платформенного проекта под каждый сервис.

Для длинных операционных процессов Coolify может быть deployment target внутри [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) или другого workflow engine: workflow решает, что и когда выкатывать, а Coolify держит инфраструктурный слой приложений и сервисов. [Boring Computers]({{ '/wiki/llm-agents/boring-computers' | relative_url }}) похож по self-hosted/control-plane ответственности, но управляет не приложениями, а disposable Firecracker microVM-компьютерами для AI-агентов.

[ru-marketplace-mcp]({{ '/wiki/tools/ru-marketplace-mcp' | relative_url }}) можно развернуть как private HTTP MCP stack через Docker/Compose, но это не повод открывать scraper port напрямую: у серверов нет встроенной auth. Coolify может держать app/process layer, а reverse proxy и network policy должны оставлять MCP endpoint за authentication и rate limits.

[Cobalt]({{ '/wiki/tools/cobalt' | relative_url }}) — ещё один уместный private Docker workload: Coolify может держать container/proxy/deployment lifecycle, но API нельзя открывать бездумно. Cobalt defaults к широкому listen/CORS и требует отдельно настроить reverse proxy, rate limits, Turnstile/API keys, secrets и cookies policy.

## Ограничения

Главный компромисс Coolify — ответственность возвращается владельцу серверов.

Нужно учитывать:

- Docker, volumes, networks и reverse proxy всё ещё требуют понимания;
- bootstrap через root install script удобен, но должен запускаться осознанно;
- backups и restore-процедуры нужно проверять, а не просто включить галочку;
- self-hosted PaaS не убирает задачи security updates, disk pressure, monitoring и incident response;
- при большом масштабе может потребоваться более строгий IaC/Kubernetes/platform-engineering слой.

README подчёркивает отсутствие vendor lock-in: конфигурации приложений и баз сохраняются на сервере. Это сильная сторона, но она же означает, что сервер становится реальным stateful asset, за который нужно отвечать.

## Практический вывод

`Coolify` полезен как middle path между “всё руками через SSH/Docker Compose” и “полностью уйти в облачный PaaS”. Он даёт self-hosted control plane для приложений, баз и сервисов, сохраняя инфраструктуру у владельца.

Его стоит рассматривать там, где нужны простота деплоя и контроль над серверами одновременно. Если же команда не готова обслуживать Docker hosts, backups и сетевой слой, hosted PaaS может быть честнее.

## Источники

- https://github.com/coollabsio/coolify
- https://coolify.io
- https://coolify.io/docs/installation
