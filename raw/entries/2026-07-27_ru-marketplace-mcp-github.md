---
id: github-vladimir-human-ru-marketplace-mcp-2026-07-27
date: 2026-07-27
source_type: url
source_url: https://github.com/Vladimir-Human/ru-marketplace-mcp
title: ru-marketplace-mcp GitHub repository
domain: tools
tags: [tools, mcp, marketplace, price-comparison, automation, self-hosted]
---

# ru-marketplace-mcp GitHub repository

Canonical source: https://github.com/Vladimir-Human/ru-marketplace-mcp

Observed repository state on 2026-07-27:

- Repository: `Vladimir-Human/ru-marketplace-mcp`.
- Version: `1.1.0`; Python `>=3.12`, uv workspace.
- License: MIT.
- Primary language: Python.
- Git HEAD inspected: `4a4aef9d8473f40c2cb2b79c93e7347869be1501` on branch `main`.
- GitHub topics observed: `claude`, `ecommerce`, `marketplace`, `mcp`, `model-context-protocol`, `ozon`, `price-comparison`, `russia`, `wildberries`, `yandex-market`.
- Repository test verification: `uv run pytest -q -m "not live and not cdp"` completed with **406 passed**.

## What the source provides

`ru-marketplace-mcp` is a read-only family of MCP servers for Russian marketplaces. It reads public catalogue data — prices, availability, ratings, reviews and, for Wildberries, seller legal identity — without marketplace API keys or account registration.

The release contains five stdio servers and 22 tools:

| Server | Scope |
|---|---|
| `wb-mcp` | Wildberries: search, cards, reviews/questions, seller details, catalog/categories, selfcheck |
| `yandex-mcp` | Yandex Market: search, seller prices, rating distribution, reviews, selfcheck |
| `detmir-mcp` | Detsky Mir: categories, category items, card, regional stock, selfcheck |
| `ozon-mcp` | Ozon: search, cards, reviews, selfcheck |
| `compare-mcp` | Cross-marketplace comparison and source availability |

The project intentionally does not claim a universal result when a source fails. `compare_prices` queries sources in parallel, returns `complete` plus per-source outcomes, and ranks ordinary prices only. Yandex Plus subscription prices are carried separately rather than compared against ordinary marketplace prices.

## Architecture and runtime

The repo is a uv workspace with six packages:

- `mcp-core` — shared error taxonomy, transport selection, cache, redaction, parsing helpers, process handling and selfcheck logic;
- marketplace connectors for Wildberries, Ozon, Yandex Market and Detsky Mir;
- `compare-connector` — parallel fan-out and normalized cross-market ranking.

Each connector follows the same shape: environment-backed settings, typed output models, FastMCP tools and a console-script entry point. `mcp-core` keeps stdout reserved for stdio JSON-RPC, writes diagnostics to stderr, defaults HTTP mode to loopback and gives errors machine-readable codes such as `rate_limited`, `transport_down`, `parser_drift` and `not_found`.

## Data-quality and anti-bot rules captured by the source

The project is explicit about source-specific limits:

- Wildberries search needs a valid destination; its public search is rate-limit prone, and stale endpoints are rejected rather than returned as plausible empty results.
- Yandex Market has ordinary and Plus-subscriber prices; only ordinary `price_rub` is used for comparison.
- Detsky Mir has no trustworthy public text search, so the connector uses categories instead of pretending search works; region must be passed to get meaningful stock.
- Ozon may reject datacenter traffic. The connector first tries TLS impersonation, then can fetch through a Chrome session controlled by the operator via DevTools Protocol.
- Missing values remain `null`, never `0`; a zero price would falsely win a cheapest-price ranking.
- Every connector has a tri-state selfcheck: `success`, `drift_detected`, or `inconclusive`. A geo/IP block is not misreported as a parser regression.

`docs/ANTI_BOT.md` also records rejected sources and why they were left out, which is important: an endpoint that cannot be searched reliably is not exposed as a deceptively confident tool.

## Transport and security posture

Default transport is stdio. HTTP/streamable-HTTP is opt-in through `MCP_TRANSPORT`; HTTP binds to `127.0.0.1` by default because the servers have no authentication of their own. The bundled Docker Compose setup publishes connectors only on host loopback and recommends an authenticating reverse proxy before deliberate external exposure.

The Ozon Chrome/CDP fallback must remain local to a dedicated browser profile. A reachable DevTools port grants full control of that profile, so it must not be exposed beyond loopback.

## Source snapshot

A working-tree snapshot of the inspected repository is saved at:

`raw/sources/github/Vladimir-Human/ru-marketplace-mcp/`

Snapshot metadata is saved at:

`raw/sources/github/Vladimir-Human/ru-marketplace-mcp.source-metadata.json`

The snapshot excludes nested Git metadata, the temporary uv virtual environment, Python bytecode and test caches.

## Wiki integration notes

Nearest Wiki Chiki neighbors:

- [[MCPorter]] — MCP transport/tool diagnostics.
- [[Trench]] — event/outcome storage for repeated price observations.
- [[Teable]] — operational table/UI for price snapshots and manual review.
- [[Coolify]] — deployment control plane for a private HTTP MCP layer.
- [[Antfarm]] — orchestration for scheduled checks and follow-up steps.
