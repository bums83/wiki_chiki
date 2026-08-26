---
title: Boring Computers
type: technology
created: 2026-07-13
last_updated: 2026-08-26
domain: llm-agents
related: ["OculiX", "agent-aget", "MCPorter", "Coolify", "Antfarm", "AI Factory", "Firecracker", "nuphus-mcp"]
sources: ["github-michaelshimeles-boring-computers-2026-07-13"]
tags: ["llm", "agents", "mcp", "automation", "virtualization", "self-hosted"]
---

# Boring Computers

`Boring Computers` — open-source self-hosted платформа для disposable Linux computers, которые можно отдавать AI-агентам как полноценную рабочую машину. Внутри это [Firecracker]({{ '/wiki/infra/firecracker' | relative_url }}) microVM: отдельное ядро, serial shell, опциональный desktop/VNC, coding agents, preview ports, volumes и API для запуска/остановки/fork.

Коротко: **не браузерный helper и не очередной контейнерный sandbox, а управляемый парк короткоживущих microVM-компьютеров для агентных задач**.

## Что даёт

По README и структуре репозитория проект закрывает несколько agent runtime задач:

- запуск полной Linux-машины с browser, terminal и приложениями;
- headless shell через WebSocket TTY или deterministic `exec`;
- desktop/VNC режим для computer-use агентов;
- предустановленные coding agents вроде `claude`, `codex`, `cursor`, `pi` в desktop image;
- file upload/download и persistent volumes;
- preview URL для сервисов, поднятых внутри гостевой машины;
- fork running computer через snapshot/CoW branch;
- TTL/self-destruct по умолчанию, persistent режим как opt-in;
- MCP server и TypeScript SDK для подключения из внешних AI clients.

Это делает Boring Computers ближе к execution substrate для агентов, чем к обычному remote desktop или CI runner.

## Архитектура

Главная модель из `docs/architecture.md`: **Machine** — базовый primitive, а **Computer** — Machine плюс display/action layer.

- `boringd/` — Go control plane, который запускает Firecracker, держит registry машин, TTL reaper, REST API и WebSocket bridges.
- Firecracker child process получает rootfs overlay и unix API socket; guest kernel boot идет через `console=ttyS0`.
- `boringd` владеет stdin/stdout процесса Firecracker, поэтому `/v1/machines/{id}/tty` становится byte pump между WebSocket client и guest serial shell.
- Snapshot restore и copy-on-write overlays дают быстрый boot/fork, а cold boot остаётся fallback path.
- Desktop layer добавляет VNC/screenshot/computer-use agent endpoints.
- `apps/web/` — SvelteKit interface/showcase.
- `packages/mcp/` — `boring-computers-mcp`, MCP server для AI clients.
- `packages/sdk/` — Effect-native TypeScript client.

По смыслу это похоже на «serverless computer», но self-hosted и построенный на KVM/Firecracker, а не на shared container boundary.

## API и agent surface

`boringd` публикует REST/WebSocket контракт:

| Capability | Пример поверхности |
|---|---|
| Health/list/create/delete | `/healthz`, `/v1/machines` |
| Shell | `/v1/machines/{id}/tty`, `/exec` |
| Desktop | `/screenshot`, `/vnc`, computer-use agent stream |
| Branching/templates | `/branch`, `/publish`, `/v1/templates` |
| Files/volumes | upload/download, S3-backed volumes |
| Previews | reverse proxy на guest port |
| Inference | OpenAI-compatible `/v1/chat/completions` gateway |

MCP package превращает эту поверхность в tools вроде `launch_computer`, `run_command`, `run_task`, `screenshot`, `preview_url`, `fork_computer`, `publish_computer`, `list_templates`, `stop_computer`. Для отладки такого слоя полезен [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}): Boring Computers даёт MCP capability, а MCPorter помогает разложить проблемы на transport/auth/schema/handler уровень.

## Связь с computer-use и automation tools

Boring Computers пересекается с [OculiX]({{ '/wiki/tools/oculix' | relative_url }}) и [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}), но находится на другом уровне.

- [OculiX]({{ '/wiki/tools/oculix' | relative_url }}) автоматизирует уже существующий экран через screenshots, OCR и visual matching.
- [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) даёт CLI/JSON-интерфейс к управляемому браузеру.
- [nuphus-mcp]({{ '/wiki/tools/nuphus-mcp' | relative_url }}) даёт MCP surface для desktop/browser control внутри той machine/session, где он запущен; strict confirmation полезен, но не заменяет сам disposable execution boundary.
- Boring Computers создаёт саму disposable машину, внутри которой может жить браузер, терминал, VNC desktop, coding agent и артефакты задачи.

То есть Boring Computers отвечает на вопрос «где безопасно и быстро дать агенту реальный компьютер?», а OculiX/agent-aget — «как агенту управлять конкретной GUI/browser поверхностью?».

## Deployment и эксплуатация

Проект self-hosted. README описывает два основных пути:

- Linux host с `/dev/kvm`, обычно Ubuntu 24.04 на x86_64/arm64 bare metal или VM с nested virtualization;
- Apple Silicon Mac через Lima nested virtualization, где `boringd` доступен локально через forwarded port.

Windows 11/WSL2 описан как designed, но ещё не полностью wired. Для внешнего bare-metal сценария есть Latitude.sh runbook: bootstrap Firecracker/kernel/rootfs, deploy `boringd`, открыть SSH tunnel, прогнать demo, затем teardown чтобы не платить за idle host.

С [Coolify]({{ '/wiki/tools/coolify' | relative_url }}) связь не в функциональной замене, а в self-hosted control plane модели. Coolify управляет приложениями, базами и Docker services на серверах; Boring Computers управляет короткоживущими microVM-computers для агентных задач. Оба требуют дисциплины вокруг SSH, firewall, secrets, health checks и стоимости инфраструктуры.

## Где уместен

Boring Computers уместен, когда агенту нужен не один tool call, а целая рабочая среда:

- безопасно выполнить untrusted code с более сильной изоляцией, чем container;
- дать агенту browser + terminal + files как единый stateful workspace;
- параллельно пробовать несколько веток решения через fork/snapshot;
- запускать code-generation задачи с live preview;
- строить MCP capability, где AI client сам просит выделить disposable computer;
- делать workflow step внутри [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) или другого orchestrator, когда шаг требует отдельной машины, а не просто shell-команды в текущем окружении.

## Ограничения

Главный риск — это не «сложно поставить», а **сложность безопасной эксплуатации произвольного кода**.

Нужно учитывать:

- нужен Linux/KVM или рабочая nested virtualization среда;
- [Firecracker]({{ '/wiki/infra/firecracker' | relative_url }}) даёт VM boundary сильнее shared containers, но production posture всё равно требует jailer/seccomp/cgroups/network policy;
- README/runbook прямо рекомендуют держать prototype за localhost/SSH tunnel и включать token;
- публичное multi-tenant использование требует egress controls, quotas, billing/metering и наблюдаемости;
- bare-metal host стоит денег даже когда microVMs простаивают;
- desktop/browser image может быть тяжелее и медленнее cold boot, чем headless shell.

## Практический вывод

`Boring Computers` — сильная идея для agent infrastructure: агентам всё чаще нужен не абстрактный sandbox, а настоящая временная машина с shell, browser, display, files и preview URL. [Firecracker]({{ '/wiki/infra/firecracker' | relative_url }}) даёт VMM boundary, а MCP/SDK Boring Computers превращают microVM lifecycle в reusable capability.

Пока это стоит рассматривать как перспективный self-hosted substrate для AI-компьютеров и sandboxed execution, а не как готовый публичный multi-tenant cloud без дополнительного hardening.

[AI Factory]({{ '/wiki/llm-agents/ai-factory' | relative_url }}) может распараллеливать задачи через git worktrees и runtime-native helpers, но это не isolation boundary. Когда агенту требуется disposable OS, сеть и процессная изоляция, нужен execution substrate вроде Boring Computers, а не только project-local skills.

## Источники

- https://github.com/michaelshimeles/boring-computers
- https://boringcomputers.com
