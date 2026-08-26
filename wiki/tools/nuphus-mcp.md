---
title: nuphus-mcp
type: technology
created: 2026-08-26
last_updated: 2026-08-26
domain: tools
related: ["MCPorter", "agent-aget", "OculiX", "Boring Computers"]
sources: ["github-mrpulor-gh-nuphus-mcp-2026-08-26"]
tags: ["tools", "mcp", "automation", "computer-vision", "ocr", "open-source"]
---

# nuphus-mcp

`nuphus-mcp` — локальный stdio MCP-сервер для computer use: он даёт MCP-клиенту инструменты управления экраном, окнами, мышью/клавиатурой и Chrome. Это **не удалённый sandbox и не безопасный browser helper**: процесс, которому клиент передаёт команды через stdin, действует на той машине и в той desktop-сессии, где запущен сервер.

На 2026-08-26 upstream `master` зафиксирован на `9817ef7` (2026-08-21); актуальные GitHub release и npm-пакет — `v0.1.13` / `0.1.13`. Репозиторий MIT, Rust workspace из трёх crates: `nuphus-mcp`, `nuphus-browser` и `desktop-api`.

## Поверхность и transport

Сервер читает newline-delimited JSON-RPC 2.0 из stdin и пишет ответы **только** в stdout; logging идёт в stderr. Поддерживаются стандартные методы MCP `initialize`, `notifications/initialized`, `ping`, `tools/list`, `tools/call`. В entrypoint есть лимит 4 MiB на одну request line: oversized запрос получает protocol error, а процесс продолжает обслуживать следующий ввод.

Документация заявляет 38 tools: desktop-операции и browser-операции через Chrome DevTools Protocol. На практике важнее не число, а capability boundary:

- screen/window screenshot, список и активация окон, перемещение/resize;
- mouse, keyboard и системный clipboard;
- browser navigation, accessibility snapshot с refs, click/type/press, DOM evaluation, cookies, file upload/drag и downloads;
- `desktop_vision`: отправка screenshot в выбранный пользователем vision endpoint;
- `desktop_perceive`: local OCR и optional YOLO icon detection с координатами элементов.

Для browser layer `nuphus-browser` использует CDP (`chromiumoxide`). По умолчанию он управляет отдельным Chrome profile; при `NUPHUS_MCP_BROWSER_CDP_URL` подключается к внешнему CDP endpoint и, по документации, не должен тихо переключаться на свой browser при ошибке attach. Это полезная предсказуемость, но внешний CDP endpoint и его сессии — чувствительный credential/control surface.

## Две разные vision-модели

Не смешивать OCR и удалённую vision-модель:

1. `desktop_perceive` запускает PaddleOCR локально, может дополнительно применить YOLO и при первом вызове пытается скачать модели. В закрытых сетях это нужно сделать явным policy: `NUPHUS_MCP_NO_MODEL_DOWNLOAD=1` даёт fast-fail, а не неявный network egress.
2. `desktop_vision` передаёт screenshot в BYOK vision API — OpenAI-compatible либо Anthropic Messages API. Значит screenshot и prompt уходят туда, куда указывает конфигурация; это не local-only capability.

Упоминание «локальный OCR» не делает весь server локальным: browser может ходить в сеть, vision — отправлять изображения провайдеру, а модели OCR/YOLO имеют отдельную supply chain загрузки.

## Подтверждение действий — обязательный режим

Это главный operational point. В `tools/list` write-capabilities отмечаются MCP-аннотацией `destructiveHint`; она лишь даёт клиенту возможность показать предупреждение. Блокировка на стороне сервера появляется только при `--confirm-write` или `NUPHUS_MCP_CONFIRM_WRITE=1`: тогда write tool требует явное `"confirm": true`, иначе сервер возвращает `isError` без side effect.

Код `SecurityPolicy::from_env()` устанавливает этот режим в `false`, если переменная не задана. Поэтому базовая конфигурация с пустыми `args` — слабая. Для любого агента, которому нельзя безусловно доверять, нужен минимум:

```json
{
  "mcpServers": {
    "nuphus-mcp": {
      "command": "nuphus-mcp",
      "args": ["--confirm-write"]
    }
  }
}
```

Даже strict confirm не равен human approval: агент или MCP-клиент всё ещё может передать `confirm: true`. Он предотвращает случайный вызов по протоколу, но не заменяет trust boundary, отдельную OS account/desktop session, least privilege и review policy для клиента.

Документы upstream сейчас расходятся в точном числе write tools: `TOOLS.md` указывает 27 destructive и 11 read-only, тогда как `SECURITY.md` говорит о 23 write tools. Код классифицирует операции по имени и отдельно по `desktop_mouse.action`. В production нужно читать реальный `tools/list` установленной версии, а не строить permission policy по числу из README.

## Платформа, installation и tests

Рекомендуемый путь — `npm install -g @nuphus/nuphus-mcp`: meta package выбирает prebuilt binary для Windows x64/arm64, macOS arm64 или Linux x64/arm64. Source build требует Rust stable. В проверенном release `v0.1.13` есть десять platform/npm assets; `nuphus-mcp` crate имеет версию `0.1.13`.

Поддержка не одинаковая:

| Платформа | Browser | Desktop boundary |
|---|---|---|
| Windows | full | Win32 API, полный заявленный desktop control |
| macOS | full | input требует Accessibility permission |
| Linux | available | window/input capabilities заявлены как partial |

На reviewed SHA GitHub показывает восемь успешных checks: `cargo check` на Ubuntu/macOS/Windows, `cargo test` на Windows/macOS, `cargo fmt`, advisory `cargo audit` и real-Chrome integration на Windows. Это upstream CI, не локальный rerun. В workflow Chrome integration помечен `continue-on-error`, а `cargo audit` исключает две конкретные advisory как build-dependency-only по rationale в `.cargo/audit.toml`; ни один из этих фактов не является доказательством отсутствия уязвимостей.

Локально source workspace был клонирован и revision совпал с `9817ef7`, но Cargo в текущем окружении отсутствует. Поэтому `cargo check`, unit/integration tests и запуск управления desktop здесь **не выполнялись**.

## Где применять и где не путать уровни

- [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}) помогает проверить stdio transport, схему и список tools. Он не превращает high-impact computer-control capability в безопасную.
- [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) — CLI-first browser workflow с profiles/sessions; `nuphus-mcp` добавляет desktop control и доставляет browser surface через MCP.
- [OculiX]({{ '/wiki/tools/oculix' | relative_url }}) автоматизирует видимый GUI через image matching/OCR. Nuphus сочетает OCR/vision с MCP и CDP, но не заменяет устойчивый visual test design.
- [Boring Computers]({{ '/wiki/llm-agents/boring-computers' | relative_url }}) выделяет disposable microVM-компьютер. Nuphus управляет desktop/browser той машины, где запущен; он не даёт сам по себе VM isolation.

## Практический вывод

`nuphus-mcp` — удобный способ дать агенту реальную desktop/browser поверхность через один stdio MCP server. Цена этой простоты — сильное доверие к MCP client и к окружению запуска. Использовать его стоит в отдельной неповышенной desktop-сессии, с включённым strict confirmation, явной egress/model-download policy и без секретов в screenshots, clipboard или CDP-сессиях. Если требуется isolation, сначала выделяется disposable machine/sandbox; затем в ней подключается этот tool layer.

## Источники

- https://github.com/mrpulor-gh/nuphus-mcp
- https://github.com/mrpulor-gh/nuphus-mcp/releases/tag/v0.1.13
- https://raw.githubusercontent.com/mrpulor-gh/nuphus-mcp/master/README.md
- https://raw.githubusercontent.com/mrpulor-gh/nuphus-mcp/master/TOOLS.md
- https://raw.githubusercontent.com/mrpulor-gh/nuphus-mcp/master/SECURITY.md
- https://raw.githubusercontent.com/mrpulor-gh/nuphus-mcp/master/crates/nuphus-mcp/src/security.rs
- https://raw.githubusercontent.com/mrpulor-gh/nuphus-mcp/master/.github/workflows/ci.yml
- https://registry.npmjs.org/@nuphus/nuphus-mcp/latest
