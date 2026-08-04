---
id: github-vakovalskii-searcharvester-2026-08-04
title: "Searcharvester — GitHub source review"
source_type: github_repository
url: https://github.com/vakovalskii/searcharvester
canonical_url: https://github.com/vakovalskii/searcharvester
author: vakovalskii
published: 2026-04-27
retrieved: 2026-08-04
status: reviewed
related: ["Searcharvester"]
---

# Searcharvester — первичный разбор репозитория

## Источник и revision

- Canonical URL: https://github.com/vakovalskii/searcharvester
- Проверенная shallow revision `main`: `5afa68b1a3f601fdb959940a383e3c7ee3f4d0cb`.
- Commit timestamp: `2026-04-27T11:00:55+03:00`.
- Commit subject: `Detect hallucinated URLs by cross-checking extracts/ on disk`.
- В репозитории найден root `LICENSE` GNU Affero General Public License v3.0.

## Подтверждённая реализация

Текущий `docker-compose.yaml` объявляет Valkey, SearXNG, `tavily-adapter` и frontend. Adapter image наследуется от Hermes Agent и запускает FastAPI на 8000; frontend опубликован на 9762; SearXNG опубликован на 8999. Adapter имеет RW bind mounts для `jobs/` и `hermes-data/`.

`simple_tavily_adapter/main.py` реализует `/search`, `/extract`, pagination `/extract/{id}/{page}`, async `/research`, status/logs/SSE/snapshot/cancel routes и `/health` со строкой версии `2.2.0`. Поиск использует SearXNG и формирует позиции с фиксированной synthetic score формулой; extract использует trafilatura и in-memory cache.

`orchestrator.py` запускает `hermes acp` subprocess в самом adapter container, связывает ACP по stdin/stdout и пишет job artifacts на host-mounted directory. В bundled deep-research skill описаны research agents, critic, fact-checker, `report.md` и проверка URL against stored extracts.

## Документация и риски

- `docs/ru` описывают более старую схему и API без текущего research/frontend/event surface; operational source of truth здесь — compose и код.
- README-схема с ephemeral containers/socket proxy расходится с текущей реализацией subprocess без per-job container isolation.
- `config.example.yaml` содержит placeholder secret, `limiter: false`, bind `0.0.0.0`; эти defaults нельзя считать безопасными для публичного endpoint.
- Adapter принимает URL для server-side fetch, а research/log/event routes не имеют встроенной user-level auth. Для production нужны private networking/auth, egress policy, rate limits, filesystem retention и secret management.
- Root AGPL-3.0 противоречит формулировке README «MIT on our code». В ingest зафиксирована более консервативная интерпретация: до уточнения maintainer весь репозиторий рассматривается как AGPL-3.0.

## Проверки ingest

- `docker compose config --no-interpolate`: passed.
- `python3 -m compileall`: passed.
- Isolated Python environment с `simple_tavily_adapter/requirements.txt`: `17 passed, 1 skipped`; warning-only deprecations от pytest-asyncio/httpx.
- Пропущенный E2E требует `RUN_E2E=1`, реальный Docker stack, Hermes и model endpoint; production service не поднимался в рамках ingest.

## Связь с Wiki

Создана [[Searcharvester]]. Рядом: [[Research org code]], [[Academic Research Skills]], [[Antfarm]], [[Coolify]].
