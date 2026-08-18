---
id: github-firecracker-microvm-firecracker-2026-08-18
date: 2026-08-18
source_type: url
source_url: https://github.com/firecracker-microvm/firecracker
title: Firecracker — secure and fast microVMs for serverless computing
domain: infra
tags: [virtualization, linux, hardware, rate-limiting, open-source]
---

# Firecracker — source review

## Граница источника

- Canonical upstream: https://github.com/firecracker-microvm/firecracker
- Default branch: `main`; examined commit: `95e08ae10bc0adcc0b2226d691ca413235e76b98` (`2026-07-28T20:42:00Z`, `vstate: bus: Decouple address ranges from device handles`).
- Latest published release observed via GitHub API: `v1.16.1`, published `2026-07-02T15:03:04Z`; пять assets, включая `aarch64`/`x86_64` archives, SHA-256 files и `test_results.tar.gz`.
- License: Apache-2.0. Rust workspace (`Cargo.toml`) с crates для Firecracker, jailer, VMM, seccompiler, snapshot-editor и сопутствующих tooling.
- Изолированный `researcher` profile был запущен по evidence task, но runner закончился timeout через 600 s без usable report. В качестве fallback использованы только direct official GitHub API и revision-pinned upstream files; web-search другой backend не подменялся.

## Наблюдаемые факты upstream

| Область | Первичный источник | Сохранённый факт |
|---|---|---|
| Модель исполнения | `docs/design.md` | Один Firecracker process encapsulates одну microVM; в нём API, VMM и vCPU threads. VMM использует KVM; API — host-facing in-process HTTP server. |
| Платформа | `docs/getting-started.md`, `docs/kernel-policy.md` | Linux host/guest, `x86_64` и `aarch64`; нужен KVM module и RW access к `/dev/kvm`. Поддерживаемые kernel matrices отделены от конфигураций, которые просто могут работать. |
| I/O | `docs/design.md`, OpenAPI | VirtIO net/block/vsock, TAP для host networking, file-backed block devices, rate limiting на operations/bandwidth; Firecracker сам не filter-ит egress. |
| Sandboxing | `docs/design.md`, `docs/jailer.md`, `docs/seccomp.md` | Default per-thread seccomp; production recommendation — matching statically linked `jailer`, который применяет cgroup/namespace/chroot/privilege drop. Inputs jailer считаются trusted. |
| Snapshots | `docs/snapshotting/snapshot-support.md` | Отдельные state/memory files; backing disks user-managed; full vs diff snapshots, где diff остаётся Developer Preview; snapshot trust/identity/network/vsock limits документированы явно. |
| Release/support | `docs/RELEASE_POLICY.md` | SemVer API, policy support; current policy lists `v1.16` as supported with min end date 2026-12-03. Developer-preview features не production supported. |
| Performance | `SPECIFICATION.md` | Указанные limits привязаны к M5D.metal/M6G.metal, kernel/rootfs и ресурсам. Некоторые I/O statements помечены `integration test pending`; они не перенесены как general benchmark. |

## Локальная проверка и её пределы

1. Bounded sparse clone `--depth 1 --filter=blob:none` произведён в `/tmp/firecracker-review` и закреплён на reviewed SHA. Первичная `git sparse-checkout set` без `--skip-checks` не приняла root-level files; повтор с `--skip-checks` успешно materialized 819 tracked paths. Это review tree, не сохранённая пользовательская копия.
2. `tools/devtool checkenv` был запущен. Он сообщил, что текущий пользователь не имеет доступ к `/dev/kvm`, а host security preflight выдал warnings `spec_rstack_overflow` и `spec_store_bypass`; поэтому запуск Firecracker и integration/performance tests не предпринимался.
3. Попытка `cargo metadata --no-deps --format-version 1 && cargo fmt --all -- --check` не началась: `cargo: command not found`. Это не failure upstream code.
4. GitHub API для `95e08ae` вернул четыре current check runs в `completed/success`: `Analyze (actions)`, `trigger_ab_test`, `DCO`, `no_dirty_cargo_locks_check`. Эти статусы не названы полной upstream integration-suite верификацией.

## Security и эксплуатационные границы

- Firecracker не является control plane: API socket, диски, TAP, cgroups, UID/GID, logs/metrics, cleanup, image lifecycle и policy делает интегратор.
- Jailer усиливает boundary, но не валидирует безопасность operator-controlled paths; при запуске multi-tenant workload нужны per-tenant process/UID, patched kernel/microcode, host firewall/egress controls, resource quotas и monitoring.
- Snapshot clone может продублировать identifiers, random state и tokens; VMGenID решает только часть guest kernel entropy behavior. Snapshot transport/storage нужны authentication/encryption и quota policy.
- `--no-seccomp`, debug builds, experimental GNU target и custom seccomp policy не считаются production baseline.

## Wiki integration

Создана [[Firecracker]] в `infra` как статья о VMM и operational boundary.

Семантические связи:

- [[Boring Computers]] — platform, которая использует Firecracker, но добавляет agent-computer control plane/MCP/desktop/TTL; не отождествлять уровни.
- [[Coolify]] — application deployment control plane, а не hypervisor/VMM.
- [[AI Factory]] — project/worktree workflow, а не OS/network isolation boundary.

Отдельный полный source snapshot не создан: пользователь не запрашивал локальную копию. Raw entry сохраняет revision, evidence ledger, exact checks и пределы локальной верификации.
