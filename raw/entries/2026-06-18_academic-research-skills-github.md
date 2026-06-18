---
id: github-imbad0202-academic-research-skills-2026-06-18
date: 2026-06-18
source_type: url
source_url: https://github.com/Imbad0202/academic-research-skills
title: Academic Research Skills for Claude Code
domain: llm-agents
tags: [llm, agents, prompt-engineering, eval, workflow, research]
---

# Academic Research Skills for Claude Code — raw ingest

Source repository: https://github.com/Imbad0202/academic-research-skills

Fetched/inspected on 2026-06-18:
- README.md
- POSITIONING.md
- QUICKSTART.md
- MODE_REGISTRY.md
- docs/ARCHITECTURE.md
- LICENSE
- top-level repository structure
- GitHub repository metadata via API

Durable source facts:
- Project name: Academic Research Skills for Claude Code, abbreviated ARS in the repository.
- Purpose: a Claude Code skill suite for the academic research-to-publication workflow: research → write → review → revise → finalize.
- Version visible in README and architecture docs: v3.13.0.
- Distribution: Claude Code plugin marketplace install is the recommended path for v3.7.0+ (`/plugin marketplace add Imbad0202/academic-research-skills`, then `/plugin install academic-research-skills`). Traditional symlink/copy install into `.claude/skills/` is also documented.
- Core skill directories: `deep-research/`, `academic-paper/`, `academic-paper-reviewer/`, `academic-pipeline/`.
- Command files include `ars-plan`, `ars-lit-review`, `ars-reviewer`, `ars-revision`, `ars-citation-check`, `ars-disclosure`, `ars-format-convert`, `ars-rebuttal-audit`, and cache/read-state commands.
- MODE_REGISTRY.md records 27 modes: 8 deep-research modes, 11 academic-paper modes, 6 academic-paper-reviewer modes, and the academic-pipeline orchestrator/resume path.
- Architecture: 10-stage pipeline with human checkpoints, Stage 2.5 and Stage 4.5 integrity gates, quality gates, data-access levels (`raw`, `redacted`, `verified_only`), and an optional claim-audit gate.
- Design stance from POSITIONING.md: source-available noncommercial academic copilot, not autonomous paper writing; human researcher controls state transitions.
- Explicitly rejected: end-to-end autonomous research pipeline, idea-generation agent that substitutes/ranks hypotheses, Paper2X auto-generation, autonomous experiment execution/coding, wet-lab automation API.
- License file and positioning text state Creative Commons Attribution-NonCommercial 4.0 International / CC BY-NC 4.0. The positioning document says this is not an open-source license because it restricts commercial use.
- Optional dependencies: Python for optional hooks/features, Pandoc/tectonic/fonts for DOCX/PDF/APA rendering, Claude Code as primary runtime.
- GitHub metadata fetched 2026-06-18: repository `Imbad0202/academic-research-skills`, default branch `main`, topics include academic-pipeline, academic-writing, ai-research, claude, claude-code, literature-review, peer-review, prompt-engineering.

Interpretive notes for wiki integration:
- Closest local neighbors: Research org code, Prompts.chat, Agents.md, Autoresearch, Evolve.
- ARS belongs in `llm-agents`: it is a skill/prompt/policy system for structured academic agent workflows, not a generic tool or infrastructure service.
- Main distinction from Autoresearch: ARS is human-in-the-loop and checkpoint-heavy; Autoresearch is a compact autonomous experiment loop.
- Main distinction from Prompts.chat: ARS is not only a prompt library; it packages roles, commands, modes, contracts, gates, and artifacts into a procedural research system.
