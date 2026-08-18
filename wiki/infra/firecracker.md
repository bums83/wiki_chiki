---
title: Firecracker
type: technology
created: 2026-08-18
last_updated: 2026-08-18
domain: infra
related: ["Boring Computers", "Coolify", "AI Factory"]
sources: ["github-firecracker-microvm-firecracker-2026-08-18"]
tags: [virtualization, linux, hardware, rate-limiting, open-source]
---

# Firecracker

`Firecracker` — open-source VMM для Linux/KVM, который запускает **одну microVM в одном процессе**. Он нужен как низкоуровневый execution substrate для container/function workloads: даёт VM boundary с небольшим device model, но не даёт готовый scheduler, multi-tenant control plane, network policy, образный registry или agent UX.

Это принципиально не «лёгкий Docker» и не облачный сервис. Firecracker создаёт виртуальную машину; её жизненным циклом, сетью, дисками, лимитами, образами, логами и tenant policy должен управлять оператор или отдельный control plane.

## Граница и устройство

| Слой | Роль Firecracker | Что остаётся снаружи |
|---|---|---|
| Host | Linux + KVM, доступ к `/dev/kvm`, TAP и file-backed block devices | patched kernel/microcode, firewall, ресурсные quotas, storage и host observability |
| Процесс | API thread, VMM thread и один или несколько vCPU threads через `KVM_RUN` | orchestration нескольких VM, placement, cleanup и billing |
| Guest | Linux kernel, rootfs, VirtIO net/block/vsock, serial console, MMDS | guest hardening, package lifecycle, application secrets и egress intent |
| API | HTTP/REST по Unix socket, спецификация в in-tree OpenAPI | authn/authz control plane и безопасное предоставление API пользователям |

Перед `InstanceStart` оператор задаёт kernel image, rootfs, vCPU/memory, network/block devices и другие ресурсы. В design document текущая граница явно описана так: одна Firecracker process encapsulates одну microVM. Это удобный primitive, но не готовая платформа управления флотом.

Firecracker поддерживает Linux hosts и Linux guests на `x86_64` и `aarch64`; рабочий prerequisite — KVM module и read/write доступ к `/dev/kvm`. Документация ведёт supported-kernel matrix отдельно: «может работать» не равнозначно «периодически валидируется upstream». Не следует выводить поддержку Windows/macOS host или обычной nested VM без конкретной проверки окружения.

## I/O и наблюдаемость

VMM даёт минимальный guest device model с VirtIO network, block и vsock. Network устройства опираются на host TAP, блоковые устройства — на files на host; host networking и подготовка файловой системы rootfs не выполняются за оператора автоматически.

Для network и block доступны token-bucket rate limiters: отдельные ограничения на bandwidth и operations. Это защита fair use на device boundary, **не** замена firewall или per-tenant egress policy. Firecracker прямо не фильтрует network traffic гостя: egress остаётся untrusted и должен ограничиваться на host (`nftables`/`iptables`, namespaces, маршрутизация и т. п.).

Логи и metrics отправляются в указанные оператором pipes/files. Гость способен влиять на объём serial/log output; нужно ставить bounded sink и следить за `lost-logs`/`lost-metrics`, а не считать логирование безлимитным и безопасным по умолчанию.

## Snapshots: быстрый lifecycle, но не snapshot-as-a-service

Snapshot состоит как минимум из state file и guest-memory file; backing disk files Firecracker не упаковывает и не управляет ими. При restore memory может подгружаться on-demand через `MAP_PRIVATE` и copy-on-write mapping — отсюда быстрый resume, но memory file обязан оставаться доступным и неизменяемым весь срок жизни restored VM.

| Возможность | Факт | Ограничение |
|---|---|---|
| Full snapshot | полноценные state + memory на paused VM | disks backup/consistency и место на host — ответственность оператора |
| Diff snapshot | записывает состояние и изменённые pages | **Developer Preview**; часто требует base + merge и dirty-page tracking имеет overhead |
| Restore | `LoadSnapshot` возможен до обычной конфигурации VM | TAP/disks/vsock должны быть подготовлены и доступны по ожидаемым paths |
| Клонирование | memory/read-only disks можно разделять | network/vsock connections могут потеряться; уникальные IDs, entropy и токены могут продублироваться |

Snapshot files, host и host/API communication считаются trusted boundary. CRC state file — лишь частичная проверка от случайной порчи, не механизм доверенной доставки. При перемещении/хранении snapshot нужны authentication, encryption, lifecycle и quota policy. VMGenID помогает Linux guest re-seed kernel PRNG при restore, но не делает автоматически уникальными cached identifiers, user-space random state или cryptographic tokens.

## Security posture

Firecracker — defense in depth, не один security switch:

1. KVM отделяет guest execution от host.
2. Default seccomp filters применяются per-thread до guest code и ограничивают host syscalls.
3. Для production upstream рекомендует запуск через `jailer` либо через эквивалентно строгие process constraints.
4. `jailer` строит chroot/mount namespace, настраивает cgroups, может войти в netns, задаёт resource limits, сбрасывает privileges и `exec`-ит Firecracker под отдельными uid/gid.
5. Host operator обязан защищать пути jailer, применять patches/microcode, задавать cgroups/quotas и фильтровать guest egress.

`jailer` не защищает от небезопасного оператора: его paths и размещённые в jail ресурсы считаются trusted inputs. Custom seccomp filter — advanced override; upstream предупреждает, что неверный filter может оборвать процесс или отключить security boundary. `--no-seccomp`, debug binaries и experimental GNU targets — не production baseline.

Для multi-tenant threat model upstream рекомендует один Firecracker process на workload одного tenant. Аппаратные side channels, swap/remanence, SMT/KSM, host kernel vulnerabilities и image supply chain не исчезают от выбора microVM вместо container.

## Релизы, спецификация и проверка

На 2026-08-18 reviewed `main` — [`95e08ae`](https://github.com/firecracker-microvm/firecracker/commit/95e08ae10bc0adcc0b2226d691ca413235e76b98). Последний опубликованный release — [`v1.16.1`](https://github.com/firecracker-microvm/firecracker/releases/tag/v1.16.1) от 2026-07-02, Apache-2.0. Release policy использует SemVer; `v1.16` в текущей policy поддерживается минимум до 2026-12-03. Для production нужно pin-ить release binary, его checksum и matching statically linked `jailer`, а не произвольный `main` snapshot.

`SPECIFICATION.md` содержит контекстные SLA-like показатели, которые upstream привязывает к M5D.metal/M6G.metal, заданным kernel/rootfs и свободным ресурсам: например, API socket start до 8 CPU ms, VMM overhead до 5 MiB для 1 vCPU/128 MiB и boot до `/sbin/init` до 125 ms. Это **не** переносимый benchmark любого host; ряд I/O утверждений в том же документе помечен `integration test pending`.

Проверка для этого ingest:

- GitHub check-runs reviewed `main` SHA: `Analyze (actions)`, `trigger_ab_test`, `DCO`, `no_dirty_cargo_locks_check` — completed/success 2026-08-18.
- Локально выполнен bounded sparse checkout этого SHA и `tools/devtool checkenv`; host не дал текущему пользователю доступ к `/dev/kvm`, поэтому microVM/integration suite не запускались.
- Локальный `cargo metadata` / `cargo fmt --check` не выполнен: Rust `cargo` отсутствует в окружении. Ни upstream full integration suite, ни performance claims локально не воспроизводились.

## Место в Wiki

[Boring Computers]({{ '/wiki/llm-agents/boring-computers' | relative_url }}) использует Firecracker как VMM substrate, но добавляет поверх него control plane, TTL, desktop/VNC, files, previews, SDK и MCP. Эти возможности не принадлежат Firecracker.

[Coolify]({{ '/wiki/tools/coolify' | relative_url }}) — deployment PaaS/control plane для приложений и Docker services; Firecracker — VMM, который может быть частью иной platform, но сам не выполняет Git→build→deploy workflow.

[AI Factory]({{ '/wiki/llm-agents/ai-factory' | relative_url }}) изолирует работу агентных проектов через worktrees и runtime assets, а не OS/network boundary. Для запуска untrusted workload нужен отдельный integration layer над Firecracker, а не прямой доступ агента к `/dev/kvm` и jailer paths.

## Практический вывод

Firecracker уместен, когда нужен управляемый Linux/KVM substrate для short-lived isolated workloads и команда готова взять на себя image pipeline, network/egress, host hardening, quotas, cleanup, snapshot identity и observability. Если нужна готовая agent-computer поверхность, искать следует platform над ним. Если нужна только доставка приложения, Firecracker добавит сложность без выгоды.

## Источники

- [Upstream repository](https://github.com/firecracker-microvm/firecracker) — reviewed SHA `95e08ae`
- [Design](https://github.com/firecracker-microvm/firecracker/blob/95e08ae10bc0adcc0b2226d691ca413235e76b98/docs/design.md)
- [Production host setup](https://github.com/firecracker-microvm/firecracker/blob/95e08ae10bc0adcc0b2226d691ca413235e76b98/docs/prod-host-setup.md)
- [Jailer](https://github.com/firecracker-microvm/firecracker/blob/95e08ae10bc0adcc0b2226d691ca413235e76b98/docs/jailer.md) и [seccomp](https://github.com/firecracker-microvm/firecracker/blob/95e08ae10bc0adcc0b2226d691ca413235e76b98/docs/seccomp.md)
- [Snapshotting](https://github.com/firecracker-microvm/firecracker/blob/95e08ae10bc0adcc0b2226d691ca413235e76b98/docs/snapshotting/snapshot-support.md)
- [Specification](https://github.com/firecracker-microvm/firecracker/blob/95e08ae10bc0adcc0b2226d691ca413235e76b98/SPECIFICATION.md), [release policy](https://github.com/firecracker-microvm/firecracker/blob/95e08ae10bc0adcc0b2226d691ca413235e76b98/docs/RELEASE_POLICY.md), [v1.16.1](https://github.com/firecracker-microvm/firecracker/releases/tag/v1.16.1)
