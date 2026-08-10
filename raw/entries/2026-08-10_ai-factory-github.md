---
id: github-lee-to-ai-factory-2026-08-10
title: "AI Factory — GitHub source review"
source_type: repository
source_url: https://github.com/lee-to/ai-factory
canonical_url: https://github.com/lee-to/ai-factory
retrieved_at: 2026-08-10
language: en
status: reviewed
related_article: "AI Factory"
---

# AI Factory — source review

## Scope

User supplied the repository `lee-to/ai-factory` for Wiki Chiki ingest. This entry records primary-source evidence from the default branch and a temporary local shallow clone. No source snapshot was requested or added to the wiki repository.

## Revision and release state

- Canonical repository: <https://github.com/lee-to/ai-factory>
- Default branch at review: `2.x`
- Inspected shallow-clone HEAD: `2a3b142ec0dfb1ce9db596584ae4ba5316c6fd9f`
- HEAD timestamp/subject: `2026-08-08T11:01:19+03:00` — `Merge pull request #148 from lee-to/feat/aif-transfer`
- `package.json` version: `2.18.0`; Node engine: `>=18.0.0`
- Latest GitHub release returned by API: `v2.17.0`, published `2026-07-06T08:09:26Z`; tag commit `0e83e98dc13f9a57c31288a7526e190967e571c6`
- Therefore branch source/package metadata is ahead of the latest GitHub release. This review does not assert that an npm package, release archive and current branch are identical.

GitHub API at retrieval returned no recognized repository license (`license: null`). README and `package.json` claim MIT, but the inspected tracked root tree has no `LICENSE` file. Article treats this as an unresolved licensing caveat rather than a fully verified MIT grant.

## Observed structure and operating model

The 306 tracked files separate a TypeScript CLI (`src/cli`, `src/core`), package assets (`skills`, `subagents`, `mcp/templates`), schemas, docs and shell/Node test scripts.

Observed primary mechanisms:

- `ai-factory init` writes project-local skills, agent files, `.ai-factory.json`, selected MCP settings and optional `.ai-factory/config.yaml` support. `src/cli/commands/init.ts` shows that it can remove selected AI Factory setup during runtime deselection, while trying to keep unmanaged user agent files separate.
- `.ai-factory.json` tracks installed/managed hashes; `.ai-factory/config.yaml` carries language, paths, workflow and git preferences. Source docs distinguish CLI-owned state from user-editable config.
- Project workflow is encoded in skills: explore/grounded → plan → improve → implement → verification, review, security, rules and commit. Quality-gate outputs have a defined final JSON contract `aif-gate-result`.
- Built-in agent files are runtime-specific. Documentation says Claude bundle is broader and Codex is baseline planning/implementation/review, not parity. Source contains 19 Claude Markdown agent files, 9 Codex TOML agent files and a Codex config file.
- Extension manifests can add commands, skills, agent files, MCP servers and marker-wrapped injections. `src/core/injections.ts` shows injections alter installed skill Markdown; `src/core/mcp.ts` writes runtime-specific MCP settings.
- `src/core/installer.ts` contains path traversal / symlink boundary guards for managed agent/config artifacts. This is a useful implementation control, not a guarantee that extensions or a runtime are benign.

## Security and operational boundaries

- Upstream documentation describes a static scanner plus semantic LLM review before external skill use. This is a stated process, not independent proof that all malicious or novel content is detected.
- Built-in MCP templates include services that may need sensitive environment values, including GitHub and Postgres. No secrets were inspected or copied.
- `ai-factory update` can prompt to self-update global npm package and can refresh extensions from npm/GitHub/local sources. `--force` broadens refresh/reinstall behavior; operators should review diff and source trust.
- Managed Codex config may be refreshed when source evolves and local tracked content is clean; source tests document distinct preservation behavior for user-owned or locally modified config.
- Worktree-based parallelism is not VM/container isolation. Real execution capabilities remain controlled by the selected external agent runtime.

## Local verification performed

Temporary clone: `/tmp/tmp.gMTEJ0YI9r/repo`. Node available locally: `v24.17.0`; source CI specifies Node 18.

Commands and results:

| Command | Result |
|---|---|
| `npm ci --ignore-scripts --no-audit --no-fund` | passed; dependencies installed in temporary clone |
| `npm run build` | passed |
| `npm run lint` | passed |
| `npm test` | passed: 145 passed, 0 failed; 11 warnings about oversized skill bodies |
| `npm run test:init` | passed |
| `npm run test:update` | passed |
| repository `git diff --check` / clean status after tests | passed |

`npm test` includes source-defined skill, integrity, subagent, extension, QA, rules, update/init, gate-contract and security scanner regression checks. Internal security self-scan reported 0 critical findings; it also reported 31 warnings with 28 ignored by the first-party allowlist. No real LLM provider, authenticated MCP, browser service, third-party extension, global install or production project was exercised.

## Article policy decisions

- Classified as `llm-agents` technology, not as a generic MCP tool or autonomous development platform.
- Article records the branch/release and root-license drift explicitly.
- Article does not repeat promotional claims such as “zero configuration” or “shipping quality code” as guarantees.
- Relevant connections: `Agents.md` (project instructions), `ProcessForge` (file-based process model), `The Agency / Agency Agents` (role catalog vs workflow package), `MCPorter` (MCP operations) and `Boring Computers` (execution isolation).

## Primary source paths consulted

- `README.md`; `package.json`; `.github/workflows/ci.yml`
- `docs/getting-started.md`, `docs/workflow.md`, `docs/quality-gates.md`, `docs/security.md`, `docs/configuration.md`, `docs/subagents.md`, `docs/extensions.md`, `docs/skills.md`
- `src/cli/commands/init.ts`, `update.ts`, `extension.ts`
- `src/core/installer.ts`, `mcp.ts`, `injections.ts`, `extension-ops.ts`
- `scripts/test-init.sh` and package test scripts

## Source URLs

- Repository: <https://github.com/lee-to/ai-factory>
- Current branch README: <https://github.com/lee-to/ai-factory/blob/2.x/README.md>
- Release: <https://github.com/lee-to/ai-factory/releases/tag/2.17.0>
