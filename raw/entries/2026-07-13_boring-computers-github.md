---
id: github-michaelshimeles-boring-computers-2026-07-13
date: 2026-07-13
source_type: url
source_url: https://github.com/michaelshimeles/boring-computers
title: boring computers GitHub repository
domain: llm-agents
tags: [llm, agents, mcp, automation, virtualization, self-hosted]
---

# boring computers GitHub repository

Canonical source: https://github.com/michaelshimeles/boring-computers

Observed repository state on 2026-07-13:

- Repository: `michaelshimeles/boring-computers`.
- Description: on-demand Linux computers for AI agents — Firecracker microVMs with browser, terminal, coding agents, and an AI driver.
- License: Apache-2.0.
- Primary language: Go; monorepo also contains SvelteKit/TypeScript web app, MCP server and SDK packages.
- Git HEAD inspected: `9752ac7e4d902e425ab0f4047a975ea5bfba7579` on branch `main`.
- GitHub topics observed: `ai-agents`, `computer-use`, `firecracker`, `golang`, `mcp`, `microvm`, `sandbox`, `svelte`.

## What the source claims

`boring computers` packages disposable Linux machines as an agent primitive. Each machine is a Firecracker microVM with its own kernel. It can boot quickly, expose a shell or desktop, run code, serve preview ports, and be destroyed on TTL. The project positions the machine as the core primitive:

- **Sandbox = Machine**: a microVM created over API and driven through shell/exec.
- **Computer = Machine + display**: the same microVM with framebuffer/desktop and action layer for computer-use agents.

The README frames the hosted site as a showcase, not a required SaaS endpoint: users run `boringd` themselves with their own keys.

## Repository structure

Key files and directories inspected:

- `README.md` — positioning, self-hosted setup, MCP snippet and monorepo map.
- `docs/architecture.md` — thesis, Machine/Computer model, Firecracker snapshot/CoW design and prototype limits.
- `boringd/` — Go control plane for Firecracker microVM lifecycle, VNC/TTY, agents, volumes, previews and inference gateway.
- `boringd/README.md` — REST/WebSocket endpoint reference and environment variables.
- `packages/mcp/` — `boring-computers-mcp`, an MCP server exposing launch/run/fork/screenshot/template tools to AI clients.
- `packages/sdk/` — Effect-native TypeScript client for `boringd`.
- `apps/web/` — SvelteKit UI/site.
- `infra/latitude/` — one-box Latitude.sh bare-metal runbook.
- `infra/local/` — local Mac/Lima nested-virtualization path; Windows 11/WSL2 is described as designed but not fully wired.

## Technical model

`boringd` starts Firecracker child processes and owns their stdin/stdout. The guest kernel boots with `console=ttyS0`; `boringd` pumps bytes between the child process and WebSocket clients. The API supports machine creation/list/delete, shell exec, live TTY WebSocket, VNC desktop, screenshot, upload/download, preview URLs, branching/forking, published templates, volumes and agent runs.

Important implementation points:

- Firecracker/KVM gives stronger isolation than containers for arbitrary code.
- Snapshot restore and copy-on-write overlays make fast boot/fork possible.
- Machines are TTL-bound by default; persistent mode is opt-in.
- Built-in caps include max live machines, memory reserve, template/fork limits, inference/agent rate limits and volume quotas.
- The MCP server lets Claude Desktop, Cursor and other MCP clients launch and drive computers via `BORING_URL`.

## Security and maturity notes

The repo explicitly treats arbitrary code execution as hostile-tenant territory. The Latitude runbook says the prototype should stay behind localhost/SSH tunnel, use a token, and not expose `:8080` publicly. Hardening items before public exposure include jailer/seccomp confinement, stronger egress controls, multi-host scheduling, persistent volume hardening and metering/billing.

The local Mac path is described as built/proven on Apple Silicon through Lima nested virtualization; Windows 11/WSL2 support is designed but not yet wired. Linux hosts need `/dev/kvm`, typically Ubuntu 24.04 on x86_64 or arm64.

## Wiki integration notes

Nearest Wiki Chiki neighbors:

- [[OculiX]] — visual automation layer for desktop/remote screens.
- [[agent-aget]] — CLI/browser automation surface for agents.
- [[MCPorter]] — operator/debug layer for MCP integrations.
- [[Coolify]] — self-hosted control plane, but for apps/services rather than disposable agent machines.
- [[Antfarm]] — workflow orchestration layer that could use disposable machines as execution steps.
