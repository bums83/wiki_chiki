---
title: Academic Research Skills
type: technology
created: 2026-06-18
last_updated: 2026-08-04
domain: llm-agents
related: ["Research org code", "Prompts.chat", "Agents.md", "The Agency / Agency Agents", "Autoresearch", "humanizer-ru", "Searcharvester"]
sources: ["github-imbad0202-academic-research-skills-2026-06-18"]
tags: ["llm", "agents", "prompt-engineering", "eval", "workflow", "research"]
---

# Academic Research Skills

`Academic Research Skills` (ARS) — source-available suite of Claude Code skills for academic research workflows: research, paper writing, peer review, revision, integrity checking and final formatting.

It is best understood as a procedural layer for human-led academic work, not as an autonomous paper factory. The repository repeatedly draws the boundary: AI assists with search, structure, verification, citation work and review pressure; the researcher keeps control of the research question, method, evidence interpretation and state transitions.

## What it contains

The repository is organized as four main Claude Code skill packages:

| Skill | Role |
|---|---|
| `deep-research` | Literature search, source verification, systematic review, Socratic research framing and synthesis. |
| `academic-paper` | Paper planning, drafting, revision, citation work, disclosure and format conversion. |
| `academic-paper-reviewer` | Multi-perspective peer review with editorial decision, rubrics, re-review and calibration modes. |
| `academic-pipeline` | Orchestrator that connects research → writing → integrity gate → review → revision → finalization. |

The project also ships command files such as `ars-plan`, `ars-lit-review`, `ars-reviewer`, `ars-revision`, `ars-citation-check`, `ars-disclosure` and `ars-format-convert`. In Claude Code plugin installs, these commands become the practical entrypoints.

## Pipeline model

ARS uses a 10-stage research-to-publication pipeline:

1. research;
2. writing;
3. Stage 2.5 integrity verification;
4. peer review;
5. revision coaching;
6. revision;
7. re-review;
8. final integrity verification;
9. final formatting;
10. process summary.

The key design choice is the checkpoint structure. Every completed stage requires user confirmation, while Stage 2.5 and Stage 4.5 are stronger integrity gates. This differs from [Autoresearch]({{ '/wiki/llm-agents/autoresearch' | relative_url }}), where the value is autonomous overnight iteration. ARS is deliberately slower and more controlled because scholarly authorship, evidence quality and citation responsibility cannot be delegated blindly.

## Quality and integrity mechanisms

ARS is built around visible failure modes rather than silent confidence. The architecture docs describe:

- data-access levels: `raw`, `redacted`, `verified_only`;
- anti-leakage rules for unsupported manuscript content;
- Semantic Scholar / source verification patterns;
- claim verification and citation-faithfulness checks;
- reviewer calibration and quality rubrics;
- artifact provenance via Material Passport and optional `repro_lock`;
- explicit AI disclosure generation for venues.

This makes ARS adjacent to [Research org code]({{ '/wiki/llm-agents/research-org-code' | relative_url }}): the researcher is not only asking for outputs, but designing the operating system of the research process — roles, gates, artifacts, constraints and acceptance criteria.

## Prompt system vs prompt library

ARS overlaps with [Prompts.chat]({{ '/wiki/llm-agents/prompts-chat' | relative_url }}) only at the surface. Both preserve reusable LLM instructions, but ARS goes further than a prompt catalog:

- it defines multi-agent roles;
- it separates modes by task type;
- it carries state through named artifacts;
- it uses gates and contracts;
- it encodes what the system must refuse to automate.

That puts it closer to a domain-specific operating procedure for academic work than to a loose library of good prompts.

## Relationship to agent instruction files

ARS also illustrates the same discipline described in [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}): instructions are useful when they are structured, scoped and attached to repeatable workflows. The difference is level:

- `Agents.md` usually governs one software repository or team workflow;
- ARS packages a domain workflow as installable Claude Code skills, commands, agents, references, templates and checks.

This is the skill-pattern version of repository rules: a controlled instruction tree with progressive disclosure and task-specific entrypoints.

[The Agency / Agency Agents]({{ '/wiki/llm-agents/agency-agents' | relative_url }}) занимает более широкий слой: там нет одного academic workflow, зато есть большой cross-functional roster ролей и convert/install tooling для разных agent runtimes.

## Style integrity

[humanizer-ru]({{ '/wiki/llm-agents/humanizer-ru' | relative_url }}) закрывает узкий соседний риск: AI-style artefacts, ложные срабатывания и редактура, которая может дописать в текст новые факты. Это не заменяет ARS citation/claim integrity, но хорошо показывает тот же принцип: проверяемые gates и явные границы важнее уверенного, но неаудируемого вывода.

## Boundaries and license

The project is explicit about what it is not:

- not an autonomous paper-writing system;
- not a replacement for the researcher;
- not a mechanism for hiding AI usage;
- not a commercial SaaS component under the shipped license;
- not an autonomous experiment runner or wet-lab automation layer.

The repository is licensed under CC BY-NC 4.0. Its positioning document states plainly that this is not an open-source license because commercial use is restricted. That matters operationally: ARS may be useful as a reference design or noncommercial academic tool, but it is not a permissive building block for paid products without separate licensing.

## Practical use

The recommended installation path in the README is Claude Code plugin install:

```text
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

Older/manual setup copies or symlinks the four skill directories into `.claude/skills/`. Optional tooling such as Python, Pandoc and tectonic is only needed for specific hooks or document rendering paths; the core skills are prompt-driven.

## When it is useful

ARS is strongest when the goal is disciplined academic workflow support:

- turning a vague research area into a framed research question;
- building a literature review or systematic review process;
- checking citations and claim support;
- forcing a draft through adversarial peer review;
- documenting how AI assistance was used;
- keeping human checkpoints visible instead of pretending the agent can own the work.

It is weaker if the actual need is quick generic summarization, commercial paper-production automation, or fully autonomous research. In those cases its gate-heavy design is intentional friction, not overhead.

[Searcharvester]({{ '/wiki/tools/searcharvester' | relative_url }}) близок по части search/extract и role-based research, но его storage URL/extract artifacts не заменяет ARS integrity gates: существование extract-файла не доказывает корректную интерпретацию, академическую пригодность источника или ответственность автора за citation.

## Источники

- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
- [ARS architecture](https://github.com/Imbad0202/academic-research-skills/blob/main/docs/ARCHITECTURE.md)
- [ARS positioning](https://github.com/Imbad0202/academic-research-skills/blob/main/POSITIONING.md)
- [ARS mode registry](https://github.com/Imbad0202/academic-research-skills/blob/main/MODE_REGISTRY.md)
