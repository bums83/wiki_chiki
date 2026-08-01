---
id: github-nextlevelbuilder-ui-ux-pro-max-skill-2026-08-01
date: 2026-08-01
source_type: url
source_url: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
title: nextlevelbuilder/ui-ux-pro-max-skill GitHub repository
domain: llm-agents
tags: [agents, design, workflow, prompt-engineering, vibe-coding]
---

# nextlevelbuilder/ui-ux-pro-max-skill GitHub repository

Canonical source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

## Observed repository state

- Inspected shallow clone: `14ddef5c05e52d7c253b8f0129de7bcd1045ae5b`, branch `main`.
- Commit title: `feat(gallery): add Style Detail Modal with phone UI controls preview (#155)`; commit date `2026-08-01`.
- Official GitHub latest release queried on 2026-08-01: `v2.12.0`, published `2026-08-01T01:29:59Z`.
- Repository shape: source data/search engine in `src/ui-ux-pro-max/`; installed Claude-form skill in `.claude/skills/ui-ux-pro-max/`; distributable CLI in `cli/`; additional installed sibling skills under `.claude/skills/`; a gallery and example projects.
- Root `LICENSE` is MIT.

## Core architecture

The core is a Python 3 standard-library-only local recommendation engine:

- CSV data is loaded by `core.py` and searched with BM25-like ranking, domain detection, synonyms and suggestions for zero matches.
- `design_system.py` combines `product`, `style`, `color`, `landing`, and `typography` searches with `ui-reasoning.csv`, then emits text/JSON fields for category, pattern, style, colors, typography, effects, anti-patterns, decision rules, spacing scale and optional motion snippet.
- `search.py` exposes domain search, stack search, JSON, output format, dials (`variance`, `motion`, `density`) and opt-in persistence.
- No LLM API, API key, network access or browser automation is required by these core commands.

The template documentation calls the five design-system searches “parallel”; current code instead loops sequentially over `SEARCH_CONFIG`. This is multi-domain search, not true parallel execution.

## Data and supported platform facts

`python scripts/validate-csv.py` reported 35 runtime CSV files. Direct CSV row counts in the source data were:

| Dataset | Rows |
|---|---:|
| styles | 84 |
| colors | 192 |
| typography | 74 |
| products | 192 |
| UX guidelines | 99 |
| UI reasoning | 161 |
| charts | 25 |
| motion | 16 |
| icons | 105 |
| stack datasets | 22 |

`cli/src/utils/template.ts` maps 19 configured targets: Claude, Cursor, Windsurf, Antigravity, Copilot, Kiro, OpenCode, Roo Code, Codex, Qoder, Gemini, Trae, Continue, CodeBuddy, Droid, Kilo Code, Warp, Augment and CodeWhale. The Codex template places the main skill at `.agents/skills/ui-ux-pro-max/SKILL.md`.

A regular current CLI install is template based and copies bundled data/scripts. `--offline` is a compatibility flag for this default. `--legacy` can query/download GitHub releases and then falls back to bundled assets. `--force` overwrites existing generated files; `--global` targets the home directory.

The current installer also copies six sibling sub-skills beside `ui-ux-pro-max`: `banner-design`, `brand`, `design`, `design-system`, `slides`, and `ui-styling`.

## Source consistency caveats

- The inspected current tag/release is `v2.12.0`, while `.claude-plugin/plugin.json` reports `version: 2.11.0`.
- Platform-template descriptions claim older dataset sizes such as 67 styles and 161 palettes, while validated source data currently holds 84 styles and 192 colors.
- The source and bundled asset datasets have content-equivalent but line-ending-different copies. `npm --prefix cli run check:assets` passed, so this was not treated as an asset-sync failure.
- Root LICENSE is MIT; the repository also contains sub-skill-specific license material (for example `ui-styling/LICENSE.txt`). A team distributing or modifying individual sub-skills should inspect their local notices rather than infer every asset's terms solely from root MIT.

## Local verification actually run

All commands ran against the shallow clone above, without installing the project into a user workspace:

```text
python3 scripts/validate-csv.py
# CSV validation passed: 35 runtime CSV files checked.

bash scripts/smoke-domains.sh
# OK: 12/12 domains returned >=1 result

bash scripts/smoke-stacks.sh
# OK: 22/22 stacks returned >=1 result

python3 -m unittest discover -s src/ui-ux-pro-max/scripts/tests -v
# Ran 36 tests ... OK

python3 src/ui-ux-pro-max/scripts/search.py \
  'saas analytics dashboard' --design-system --variance 8 --motion 7 --density 8 --json
# produced full design_system contract; persistence=None

npm --prefix cli run check:assets
# Assets are in sync.
```

Not run: Node CLI build, package publish flow, Playwright e2e, or an installation into an existing repository. The tests verify data/search logic and selected output coherence; they do not validate a generated interface visually, measure end-user usability or guarantee integration safety with a project's custom agent rules.

## Wiki integration notes

Article belongs in `wiki/llm-agents/`: although it ships a CLI, its primary deliverable is an instruction/data/search layer installed into AI coding-agent runtimes.

Direct related pages:

- [[Agents.md]] — project-local instructions and source-of-truth rules must override imported general recommendations.
- [[Вайб-кодинг]] — applies the generated design brief inside a disciplined build/review loop.
- [[Penpot]] — visual collaboration/design-system environment; it should own approved screens and tokens.
- [[Prompt Master]] — prompt formulation can precede the skill's structured local lookup; neither validates real UI on its own.
