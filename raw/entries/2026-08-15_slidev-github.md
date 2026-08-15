---
id: github-slidevjs-slidev-2026-08-15
title: "slidevjs/slidev — source and documentation review"
source_type: url
source_url: https://github.com/slidevjs/slidev
canonical_url: https://github.com/slidevjs/slidev
retrieved_at: 2026-08-15
language: en
status: reviewed
related_article: "Slidev"
---

# Slidev — source review

## Repository and release state

- Repository: <https://github.com/slidevjs/slidev>
- Default branch: `main`
- Reviewed branch HEAD: `1877b3014ecc8f256e8c4df799035252a1968fc2`, 2026-08-14T11:37:40Z, docs-only commit `docs(skills): fix broken draggable link in core-components reference (#2700)`.
- Latest GitHub release API result: `v52.19.0`, published 2026-08-03T00:56:26Z; tag commit `6b540d3a20c311a21702d59201ba7785dbcaf1a5`.
- `packages/slidev/package.json` names the distributable CLI `@slidev/cli` at `52.19.0`, with Node `>=20.12.0` and bin `slidev`.
- The root private workspace manifest still says `52.16.0`; use package/release metadata rather than root workspace version as the CLI version source.
- Root `LICENSE`, package manifest and GitHub metadata state MIT.

## Inspected structure and mechanics

GitHub Contents API shows a pnpm monorepo: `packages/slidev` (CLI/runtime), `client`, `parser`, `types`, `create-app`, `create-theme`, `vscode`, docs, demo, Cypress and Vitest tests, plus official agent skill `skills/slidev`.

Direct raw-source review covered root/package manifests, `packages/slidev/node/{cli,commands/{serve,build,export},mcp/{server,operations}}`, parser manifest, official skill, workflows `test.yml`, `smoke.yml`, `release.yml`, and official documentation for getting started, syntax, export, hosting, UI, remote access, Mermaid, AI and MCP.

Confirmed implementation-level points:

- CLI exports `createServer`, parser/options and Vite plugin; serve creates a Vite server.
- Build executes `viteBuild`, creates static SPA artifacts, copies `index.html` to `404.html` and writes SPA `_redirects` if absent.
- Export imports `playwright-chromium`; PDF/PNG/Markdown/PPTX are supported. PPTX is built from PNG data URLs, with notes added per slide.
- MCP server is available both on dev-server HTTP `__mcp` and stdio. Mutation tools save formatted Markdown files; remove has `destructiveHint`; move rejects cross-file source moves and entry headmatter moves/removals.
- Remote access documentation explicitly provides `--remote`, optional presenter password, and Cloudflare Quick Tunnel flag. It does not make this a public production hosting/security model.

## CI and validation matrix

| Evidence | Result | Scope / limit |
|---|---|---|
| GitHub Actions `Test`, run `31796984635` on reviewed SHA | success | Workflow defines pnpm install, build/test on Ubuntu/Windows/macOS, Linux typecheck, and Cypress job. GitHub success is upstream CI evidence, not an independent local rerun. |
| GitHub Actions `Production Smoke Test`, run `31796984629` on reviewed SHA | success | Workflow builds/packs packages, creates fresh projects with npm/pnpm and smoke-tests build/E2E across declared Linux/Windows matrix. |
| Local shallow clone `git clone --depth=1` | timed out after 300 s | No usable checked-out source tree. |
| Local partial clone `--filter=blob:none --no-checkout`, sparse checkout | timed out after 600 s | Partial `.git` was 3.6 MB but checkout remained unusable; no install/build/test result may be claimed. |

No source snapshot was requested or created. No local package installation, dev server, browser export, MCP connection, tunnel or write action was run.

## Integration decision

- New `wiki/tools/slidev.md` article: developer-oriented presentation runtime, not a generic presentation methodology.
- Semantic neighbours: `Mermaid` (deck diagrams), `MCPorter` (MCP transport/tool validation), `HyperFrames` (code-driven video output) and `OpenScreen` (product/demo recording).
- Article explicitly distinguishes interactive SPA from non-interactive PDF/PPTX delivery, local MCP from agent safety, and upstream CI from local verification.

## Sources

- <https://github.com/slidevjs/slidev>
- <https://api.github.com/repos/slidevjs/slidev>
- <https://api.github.com/repos/slidevjs/slidev/commits/main>
- <https://api.github.com/repos/slidevjs/slidev/actions/runs?branch=main&per_page=12>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/package.json>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/packages/slidev/package.json>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/packages/slidev/node/mcp/server.ts>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/packages/slidev/node/mcp/operations.ts>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/packages/slidev/node/commands/build.ts>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/packages/slidev/node/commands/export.ts>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/.github/workflows/test.yml>
- <https://raw.githubusercontent.com/slidevjs/slidev/main/.github/workflows/smoke.yml>
- <https://sli.dev/>
