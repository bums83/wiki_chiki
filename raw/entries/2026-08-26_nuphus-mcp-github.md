---
id: github-mrpulor-gh-nuphus-mcp-2026-08-26
date: 2026-08-26
source_type: url
source_url: https://github.com/mrpulor-gh/nuphus-mcp
title: nuphus-mcp — Desktop automation MCP server
domain: tools
tags: [tools, mcp, automation, computer-vision, ocr, open-source]
---

# nuphus-mcp — source review

## Граница источника

- Canonical upstream: https://github.com/mrpulor-gh/nuphus-mcp
- Default branch: `master`; examined commit: `9817ef74619235e710932e8d9d7a5ad68abb6891` (`2026-08-21T18:32:40Z`, `fix(browser): upgrade resident headless instance to headed on headed request`).
- Metadata observed through GitHub API 2026-08-26: MIT, JavaScript/Rust, created `2026-08-01T08:02:34Z`, last push `2026-08-21T18:33:01Z`.
- Latest release observed through GitHub API: `v0.1.13`, published `2026-08-21T12:37:29Z`; ten release assets for Linux/macOS/Windows and npm packages.
- npm registry `@nuphus/nuphus-mcp@0.1.13` matches release version and publishes a meta package with optional platform binaries.
- Изолированный `researcher` profile был запущен по evidence task, но runner завершился timeout через 600 s без usable report. Fallback ограничен прямыми official GitHub raw/API и npm registry URLs; другой web-search backend не подменялся.

## Наблюдаемые факты upstream

| Область | Первичный источник | Сохранённый факт |
|---|---|---|
| Transport | `crates/nuphus-mcp/src/main.rs` | Stdio JSON-RPC: newline-delimited requests, responses only to stdout, logs to stderr; request line capped at 4 MiB and server continues after oversized-line protocol error. |
| Workspace | root и crate `Cargo.toml` | Workspace содержит `nuphus-mcp`, `nuphus-browser`, `desktop-api`; main server package version `0.1.13`, MIT. |
| Browser | README, `nuphus-browser/Cargo.toml` | Browser tools используют CDP через `chromiumoxide`; может быть managed Chrome или `NUPHUS_MCP_BROWSER_CDP_URL` для external endpoint. |
| Desktop/vision | `TOOLS.md`, `desktop-api/Cargo.toml` | Desktop APIs, local PaddleOCR/optional YOLO и BYOK vision существуют как разные paths; `desktop_perceive` может загрузить модели при первом вызове. |
| Strict confirmation | `security.rs`, README | Default `strict_confirm=false`, если env не задан; при `--confirm-write`/env write tools требуют boolean `confirm:true`. |
| Path controls | `security.rs` | screenshot paths reject `..`/system paths; upload needs existing regular file; drag paths must be absolute/existing and canonicalized. |
| CI | `.github/workflows/ci.yml`, GitHub checks | Current SHA has eight successful checks. Browser integration job uses `continue-on-error`; audit job is hard gate but has two documented ignored advisories. |

## Security и эксплуатационные границы

- Любой process/client, способный писать в stdin server, получает возможность управлять той desktop/browser surface, где server запущен. Stdio означает отсутствие HTTP daemon, а не отсутствие privilege boundary.
- `destructiveHint` — MCP annotation, не enforcement. Strict confirm полезен, но client может сознательно передать `confirm:true`; это protocol guard, не substitute для OS isolation и trusted client policy.
- Screenshots могут уходить к BYOK provider при `desktop_vision`; OCR/YOLO artifacts могут скачиваться из указанных upstream mirrors. Нужны data-egress и model-artifact policy.
- CDP даёт control над browser session; external attach и cookies не следует размещать в shared/multi-tenant agent context. Chrome restriction на default profile, описанный в README, не является обходом security model браузера.
- Tool documentation расходится в number of write/destructive tools. Runtime `tools/list` на установленной версии — source of truth для permission inventory.
- Windows/macOS/Linux capability layers различаются; на macOS нужны Accessibility permissions, Linux desktop support ограничен. Не переносить Windows claims на Linux.

## Локальная проверка и её пределы

1. Bounded sparse clone `--depth 1 --filter=blob:none` создан в `/tmp/nuphus-mcp-review`; `git rev-parse HEAD` вернул reviewed SHA `9817ef7`.
2. В текущем окружении `cargo` отсутствует (`cargo: command not found`), поэтому `cargo check`, `cargo test`, real Chrome integration и desktop actions не запускались.
3. Не выполнялась `npm install` и не запускался downloaded binary: установка/исполнение computer-control server без отдельного user request не являются необходимыми для source review.
4. GitHub CI status не объявлен локальной верификацией; он приведён строго как upstream evidence.

## Wiki integration

Создана [[nuphus-mcp]] в `tools` как MCP desktop/browser automation layer.

Семантические связи:

- [[MCPorter]] — проверяет MCP transport/schema/tools, но не заменяет authorization boundary.
- [[agent-aget]] — CLI browser automation с profiles/sessions; Nuphus отдаёт browser + desktop через MCP.
- [[OculiX]] — visual GUI automation/OCR; различие между pixel-based automation и CDP/MCP surface.
- [[Boring Computers]] — execution/isolation substrate; Nuphus — control layer внутри конкретной machine/session.

Отдельный полный source snapshot не создан: пользователь запрашивал Wiki ingest, не локальную копию репозитория. Raw entry фиксирует reviewed revision, direct evidence, CI и ограничения локальной проверки.
