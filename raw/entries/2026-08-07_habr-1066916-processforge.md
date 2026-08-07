---
id: habr-1066916-processforge-2026-08-07
date: 2026-08-07
source_type: article
source_url: https://habr.com/ru/articles/1066916/
title: Process Forge — фреймворк для создания AI-процессов
domain: llm-agents
tags: [llm, agents, workflow, automation, open-source]
---

# Process Forge — первичный разбор Habr-статьи и upstream

Canonical article: https://habr.com/ru/articles/1066916/

Статья представляет Process Forge как framework для формализованных процессов работы AI-агентов. Из HTML canonical page извлечена прямая upstream-ссылка автора: https://github.com/WebTolk/process-forge. В Wiki Chiki предметом статьи стала не рекламная оценка, а проверяемая механика и границы upstream на конкретном release.

## Habr: что заявляет автор

- Процесс включает роли, этапы, входы/выходы, policies, state и decision points, а не только один prompt.
- Контекст предлагается собирать из project/local/shared sources через каскад, оставляя human-readable configuration в файлах.
- Описаны Garage mode для одного оператора/агента и Forge/Factory mode для разбиения работы между workers.
- Автор сопоставляет подход с AI Factory, GSD Core и Serena. Эти сравнения не перенесены как доказанные feature/quality claims: они требуют отдельной совместимой методики и проверки каждого продукта.

## Upstream и revision

- Canonical repository: https://github.com/WebTolk/process-forge
- Default branch: `main`.
- Shallow revision inspected: `647c650eccf7b0974621778caf42261b8d601549`.
- Commit: `Release ProcessForge 1.0.2`, timestamp `2026-08-05T09:16:35+04:00`.
- GitHub release: `v1.0.2`, published `2026-08-05T05:17:35Z`.
- Root `VERSION`: `1.0.2`.
- Root license and GitHub metadata: Apache-2.0.
- Runtime requirement from `requirements.txt`: `PyYAML>=6.0`; upstream recommends Python 3.11+.

## Подтверждённая механика

`README`, Russian README и `docs/concepts/*` подтверждают file-first model:

- shared distribution root и separate workplace;
- project-local `.pf/` for manifests, context snapshots, assignments, runs, tasks, artifacts, reviews, handoffs, logs and runtime records;
- typed cascade resolution and immutable assignment capsules pinned to snapshot id/checksum;
- public/private config split; `.pf/runtime/**`, cache, private notes and local config are private;
- default `manual` runtime driver prepares files only; optional `generic-shell` and `codex-exec` use external worker execution;
- simple `1-1-1-1` flow plus bounded multi-agent assignments/capsules.

Implementation notes checked in current docs:

- launcher `bin/pf.py` is a cross-platform wrapper around `tools/processforge.py`;
- core commands are short-lived and write files/events, then exit;
- no daemon/background scheduler/network API/web UI/database scheduler in core;
- hook delivery is outbox-only; network send and command execution are future semantics;
- multi-agent claim/lease coordination remains unimplemented.

## Local verification during ingest

Executed in clean shallow checkout using the available Python environment:

| Command / check | Result |
|---|---|
| `python -m compileall -q bin tools` | passed |
| `tools/validate-process-forge-schemas.py` | passed |
| `tools/validate-public-cleanliness.py --root .` | passed |
| `bin/pf.py release-check --root .` | passed |
| `tools/validate-process-forge-checksums.py --root . --check` | failed |
| `bin/pf.py release-test --root . --public --fail-fast` | failed at checksum step |

The failed checksum validator reports a large difference between `checksums/processforge.sha256` and the current repository tree (`expected only` and `actual only` entries). `release-test` therefore returns `RESULT: FAIL`, even though schema/public-cleanliness/release-surface checks passed. The checkout remained clean after verification. No worker runtime, external AI provider, network delivery or production ProcessForge workplace was started.

## Wiki integration

Created [[ProcessForge]] as `technology` in `llm-agents`.

Direct conceptual links:

- [[Agents.md]] — instructions versus structured runtime context;
- [[Research org code]] — framework as concrete operational mechanics for policy/context/artifacts;
- [[The Agency / Agency Agents]] — agent roles require task scope and handoff contracts;
- [[Antfarm]] — ProcessForge file state versus durable background workflow scheduling.

No source snapshot was created: the user asked to add the Habr article to the wiki, not archive the upstream repository.
