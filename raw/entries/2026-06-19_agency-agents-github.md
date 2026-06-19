---
id: github-msitarzewski-agency-agents-2026-06-19
date: 2026-06-19
source_type: url
source_url: https://github.com/msitarzewski/agency-agents
title: The Agency / agency-agents
domain: llm-agents
tags: [llm, agents, prompt-engineering, workflow, automation]
---

# The Agency / agency-agents — raw ingest

Source repository: https://github.com/msitarzewski/agency-agents

Fetched/inspected on 2026-06-19:
- README.md
- divisions.json
- integrations/README.md
- strategy/EXECUTIVE-BRIEF.md
- scripts/install.sh
- scripts/convert.sh
- engineering/engineering-multi-agent-systems-architect.md
- specialized/agents-orchestrator.md
- top-level repository structure
- GitHub repository metadata via API

Durable source facts:
- Repository: `msitarzewski/agency-agents`.
- Project name in README: `The Agency`.
- Description: complete AI agency / growing collection of specialized AI agent personalities.
- License: MIT.
- GitHub metadata fetched 2026-06-19: stars 114547, forks 18704, default branch `main`, created 2025-10-13, updated 2026-06-19, pushed 2026-06-18, not archived.
- Repository has 16 source divisions in `divisions.json`: academic, design, engineering, finance, game-development, gis, marketing, paid-media, product, project-management, sales, security, spatial-computing, specialized, support, testing.
- Counted agent markdown files with frontmatter across those divisions on 2026-06-19: 232.
- Largest inspected divisions by count: specialized 53, marketing 36, engineering 33, game-development 20, gis 13, security 10.
- README positions each agent as specialized, personality-driven, deliverable-focused and production-ready.
- Native install path: copy/installer for Claude Code agents under `~/.claude/agents/`.
- `scripts/install.sh` supports tool targets: claude-code, copilot, antigravity, gemini-cli, opencode, openclaw, cursor, aider, windsurf, qwen, kimi, codex, all.
- `scripts/convert.sh` converts source markdown agents into tool-specific formats: Antigravity `SKILL.md`, Gemini CLI agents, OpenCode agents, Cursor `.mdc`, Aider `CONVENTIONS.md`, Windsurf rules, OpenClaw workspaces, Qwen SubAgents, Kimi YAML specs, Codex TOML custom agents.
- Installer supports filtering by `--division`, `--agent`, `--agents-file`, plus `--dry-run`, `--link`, `--path`, interactive wizard and parallel install.
- `divisions.json` is the source of truth for divisions and is checked by CI against directories and scripts.
- `strategy/` contains NEXUS materials: strategy, playbooks, runbooks, activation prompts, handoff templates and executive brief. NEXUS frames the catalog as an orchestrated intelligence network with phases, pipelines and quality gates.
- Example inspected agent `Multi-Agent Systems Architect` focuses on topology selection, context architecture, failure modes, trust/permissions, human-in-the-loop gates, observability and evals.
- Example inspected agent `Agents Orchestrator` describes a full PM → architecture → dev/QA loop → integration pipeline with retry limits and evidence gates.

Integration note:
- Wiki Chiki had no existing `agency-agents` article or raw entry before this ingest.
- Closest local neighbors: Agents.md, Academic Research Skills, Research org code, Prompt Master, Prompts.chat.
- The project belongs in `llm-agents`: it is a reusable agent roster / instruction corpus plus multi-tool packaging and orchestration materials.
