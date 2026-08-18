---
title: ProcessForge
type: technology
created: 2026-08-07
last_updated: 2026-08-10
domain: llm-agents
related: ["Agents.md", "Research org code", "The Agency / Agency Agents", "Antfarm", "AI Factory"]
tags: ["llm", "agents", "workflow", "automation", "mcp", "open-source"]
sources: ["habr-1066916-2026-08-07", "github-webtolk-process-forge-2026-08-07"]
---

# ProcessForge

`ProcessForge` — файловый framework для воспроизводимых AI-assisted процессов. Он не подменяет агента, модель или scheduler. Его предмет — явный контракт работы: процесс, назначение, входные и выходные артефакты, scope, quality gates, handoff и контекст, который был выдан конкретному исполнителю.

Это разумный ответ на типичную проблему agentic-разработки: правила, состояние, результаты и решения живут в переписке или в головах людей, а после смены сессии всё приходится собирать заново. ProcessForge переносит эти вещи в versioned files, прежде всего в проектную папку `.pf/`.

По состоянию на проверенный тег `v1.0.2` это Python CLI (рекомендован Python 3.11+, зависимость — `PyYAML`), лицензированный Apache-2.0. Публичная статья на Habr описывает замысел; технические утверждения ниже сверены по репозиторию `WebTolk/process-forge` и локальному checkout тега.

## Что именно он формализует

| Слой | Где лежит | Зачем нужен |
|---|---|---|
| Дистрибутив ProcessForge | отдельная стабильная папка | CLI, схемы, builtin-процессы, templates, validators и docs |
| Workplace | отдельный machine-level root | общие knowledge packages, tools, MCP registrations, templates и platform contracts |
| Проект | `.pf/` в репозитории проекта | manifest, assignments, runs, artifacts, reviews, handoffs, snapshots и logs |
| Private runtime | `.pf/runtime/`, `.pf/cache/`, `.pf/private-notes/`, local config | machine-local paths, worker state, outbox и чувствительные данные; не коммитятся |

Ключевой принцип: не копировать весь framework, зеркала документации и общие toolchains в каждый проект. Дистрибутив и workplace — общие, в проекте остаётся выбранный контекст и след конкретной работы.

## Файловая модель вместо «магической» оркестрации

Минимальная единица — **assignment**. В нём зафиксированы цель, роль, input artifacts, разрешённые и запрещённые файлы, требуемый output, gates, logs и handoff. Один process definition можно применять к разным assignments; результатом становятся проверяемые записи, а не лишь устное «агент закончил».

Основные объекты разделены намеренно:

- process definition описывает stages, roles, artifacts, gates и capabilities;
- run фиксирует один рабочий запуск;
- task связывает конкретную работу с run;
- iteration записывает `work`, `debug`, `fix`, `review`, `test`, `research`, `handoff` или `note`;
- review и handoff несут решение о качестве и передаче, а не только текстовый отчёт.

`handoff-return` требует реальные возвращённые артефакты. Наличие красивого сообщения от worker не равняется завершению работы — expected files проверяются отдельно.

## Контекст: каскад, provenance и lock model

ProcessForge собирает execution context из уровней `core → workplace → organization → direction → specialization → platform → toolchain → project → process → stage → task → agent profile`. У правил есть типы: `hard`, `locked`, `preference`, `gate`, `tool`, `template`. Нижний слой может уточнять локальное поведение, но не ослабляет locked policy.

Важная граница с обычным `AGENTS.md`: Markdown-инструкции остаются human/agent guidance, но не парсятся как машинные parameters. Machine-readable `parameters` имеют отдельный merge с provenance и conflict report. Это снижает риск случайно превратить произвольный текст правила в активную конфигурацию.

`context_requirements` в `.pf/process-forge.yaml` похож на dependency declaration. `project-context-refresh` строит versioned snapshot, а assignment capsule закрепляет его id и SHA-256. Если позже knowledge resource меняется, новые tasks получают новую генерацию, но уже созданная capsule не переписывается тихо.

Статусы freshness: `fresh`, `fresh_with_updates`, `stale`, `broken`. Для external live resources воспроизводимость прямо признана best-effort: lock file улучшает auditability, но не превращает изменившийся внешний URL в неизменяемый источник.

## Режимы работы и выполнение worker'ов

### Garage mode

Базовый режим — `1-1-1-1`: один оператор, одна primary agent session, один проект и один активный run. Это default для обычной разработки. Worker и Inspector здесь могут быть фазами той же сессии, а не театром из множества «персон».

### Forge / factory mode

Для независимых workstreams есть `multi-agent-task-orchestration`: orchestrator делает task plan, валидирует scope, создаёт isolated assignments/capsules и собирает результаты. Worker по умолчанию не получает весь project context: только назначение, capsule, разрешённые read/write scopes, forbidden files и output contract. Пересекающиеся write scopes запрещены, пока policy явно не разрешит их.

### Runtime drivers

Core не привязан к конкретной модели. Default driver `manual` только готовит launch material и ничего не запускает. Встроены также `generic-shell`, `codex-exec` и тестовые drivers. `codex-exec` умеет подготавливать capsule, worker prompt, heartbeat/exit paths и private workspace-access file, но модель должен выбрать operator или orchestration plan. Это не «встроенный Codex cloud» и не гарантия запуска без корректно настроенного внешнего runtime.

## Что инструмент **не** делает

Это важно сильнее, чем список возможностей.

- Core — короткоживущий CLI; daemon, watch-events service, network API, web UI и database-backed scheduler не реализованы.
- Run/task records сохраняют состояние, но сами не планируют и не исполняют работу в фоне.
- Hooks по умолчанию только observational/outbox; `webhook` и local `command` зарезервированы на будущее, `--send` сейчас должен завершаться ошибкой.
- Для multi-agent есть assignments, capsules и optional shell workers, но полноценная claim/lease coordination ещё не реализована.
- External documentation mirroring не становится реальностью без явного импортирования ресурсов.
- Framework не даёт права на сетевой доступ, внешние MCP, запуск subprocess или работу с секретами: это границы конкретного workplace/runtime policy.

Итог: ProcessForge полезен как **контур дисциплины**, а не как обещание автономной фабрики, которая сама планирует, запускает и доставляет работу.

## Установка и безопасный rollout

Upstream предлагает установить инструмент отдельно от project/workplace, затем создать workplace и подключить проект. Для production-профиля предусмотрена явная схема `workplace-init` → `project-onboard`; после этого doctor запускается из `.pf/runtime/bin/pf.py` в самом проекте.

Практический порядок:

1. Сначала прогнать release/cleanliness checks на конкретном пинованном архиве или revision.
2. Держать mutable workplace и проекты вне replaceable distribution directory.
3. Начать с Garage mode и одного реального процесса; не включать Director/multi-agent только ради названия.
4. Явно разделить public `.pf/` files и private local files. Public не должны содержать absolute paths, hostnames, secrets или local knowledge roots.
5. Добавлять runtime drivers, network capability, hooks и MCP только после отдельного review их scopes и secret handling.

## Проверка текущего `v1.0.2`: что прошло, что нет

В чистом shallow checkout revision `647c650` выполнены:

| Проверка | Результат |
|---|---|
| `python -m compileall -q bin tools` | passed |
| schema validation | passed |
| public cleanliness validation | passed |
| `release-check` | passed |
| checksum validation (`--root . --check`) | **failed** |
| `release-test --public --fail-fast` | **failed** на checksum step |

Проблема не косметическая: `checksums/processforge.sha256` расходится с текущим деревом по множеству `expected only` / `actual only` entries. Поэтому у репозитория есть working CLI checks, но проверенная на момент ingest release цепочка **не зелёная**. Нельзя считать archive integrity подтверждённой, пока maintainer не обновит manifest или не объяснит, какой exact tree он должен описывать.

## С чем не путать

| Рядом | Разница |
|---|---|
| [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}) | `AGENTS.md` задаёт правила конкретного репозитория; ProcessForge добавляет typed context, snapshots, task scopes и evidence trail. Его не нужно использовать ради ещё одного файла инструкций. |
| [Research org code]({{ '/wiki/llm-agents/research-org-code' | relative_url }}) | Это идея проектировать агентную организацию. ProcessForge — конкретная file-first механика для процессов, ресурсов, capsules и checks. |
| [The Agency / Agency Agents]({{ '/wiki/llm-agents/agency-agents' | relative_url }}) | Agency даёт roster ролей; ProcessForge задаёт contract, scope и handoff для реальной работы. Роли без работающего процесса остаются каталогом. |
| [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) | Antfarm нужен для durable scheduler и self-advancing цепочек. ProcessForge хранит process state и bounded supervision, но не заменяет background workflow engine. |

## Практический вывод

Использовать ProcessForge имеет смысл, если нужно превратить повторяющиеся AI-задачи в Git-аудируемые файлы: чётко фиксировать context, approvals, expected outputs, handoffs и провалы. Особенно полезно в командах, где агентные сессии сменяются, а ответственность не должна исчезать вместе с чатом.

Не стоит выбирать его как готовый «AI operating system» для полностью автономных процессов. На текущем `v1.0.2` не хватает scheduler/daemon/network delivery, и release checksum gate уже не проходит. Сначала починить release integrity, затем внедрять маленьким ограниченным процессом, а не раздувать `.pf/` в новую бюрократию.

[AI Factory]({{ '/wiki/llm-agents/ai-factory' | relative_url }}) решает соседнюю задачу: bootstrap конкретных coding-agent runtimes, project-local skills и MCP templates. ProcessForge сильнее в provenance, assignment/capsule и file-first process contracts; AI Factory не заменяет эти границы одной установкой workflow assets.

[Reasoning effort в LLM]({{ '/wiki/llm-agents/reasoning-effort' | relative_url }}) добавляет runtime policy: в assignment разумно явно фиксировать model/snapshot, mode, effort, context/output budget, ожидаемый output и quality gate. ProcessForge хранит этот контракт и evidence trail, но сам не выбирает режим и не доказывает, что высокий effort лучше baseline.

## Источники

- [Habr: «Process Forge — фреймворк для создания AI-процессов»](https://habr.com/ru/articles/1066916/)
- [WebTolk/process-forge](https://github.com/WebTolk/process-forge)
- [Release v1.0.2](https://github.com/WebTolk/process-forge/releases/tag/v1.0.2)
- [Known limitations](https://github.com/WebTolk/process-forge/blob/main/docs/known-limitations.md)
- [Runtime drivers](https://github.com/WebTolk/process-forge/blob/main/docs/concepts/runtime-drivers.md)
