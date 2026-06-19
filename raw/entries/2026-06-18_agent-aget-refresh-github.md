---
id: github-izzzzzi-agent-aget-refresh-2026-06-18
date: 2026-06-18
source_type: url
source_url: https://github.com/izzzzzi/agent-aget
title: agent-aget repository refresh
domain: tools
tags: [tools, cli, agents, automation, workflow]
---

# agent-aget — repository refresh

Source repository: https://github.com/izzzzzi/agent-aget

Fetched/inspected on 2026-06-18:
- README.md
- AGENT_INSTRUCTIONS.md
- package.json
- CLAUDE.md
- top-level repository structure
- GitHub repository metadata via API

Current durable source facts:
- Project: `agent-aget`, command name `aget`.
- Description: CloakBrowser-backed browser workflow CLI for LLM agents.
- Language/runtime: Go CLI distributed through npm package `agent-aget`.
- npm package version in `package.json`: 0.6.0.
- License: MIT.
- GitHub metadata fetched 2026-06-18: stars 9, forks 1, default branch `main`, repo updated 2026-06-17T14:55:53Z.
- Topics include: agent, ai-agent-tools, automation, browser-automation, chrome-devtools-protocol, chromium, cli, cloakbrowser, developer-tools, devtools, go, golang, headless, llm-agents, npm-package, stealth, testing, web-automation, web-scraping.

New or strengthened capabilities visible in the current README / AGENT_INSTRUCTIONS:
- Device emulation via `aget open ... --device mobile|tablet`, with coherent viewport, user-agent and touch behavior for stealth-sensitive mobile/tablet pages.
- Cookie injection at open/profile creation time: Netscape file or inline cookie string through `--cookies`.
- Persistent named Chromium profiles: `aget profile create/list/show/delete`, then `aget open URL --profile NAME`. Profiles preserve cookies, localStorage and session data; one profile cannot be used by two sessions at the same time.
- Expanded page interaction commands: `select`, `check`, `uncheck`, `is`, `hover`, `focus`, `upload`, `dialog-accept`, `dialog-dismiss`, `js` fallback.
- Force click mode: `aget page click ... --force`, using CDP mouse events for custom React/jQuery components.
- Wait improvements: wait for text, selector, ref, load state, or DOM appearance.
- Agent instruction artifact: `AGENT_INSTRUCTIONS.md`, also exposed through `aget prompt` / `aget agent-instructions`, gives a compact command playbook for terminal agents.
- Repository includes architecture images under `docs/aget-architecture-*.png`, managed-browser install scripts/tests, and Go internal modules for sessions, browser resolver/launcher, CDP, cookies, profiles, snapshot store, doctor and CLI commands.

Integration note:
- Existing Wiki Chiki article `wiki/tools/agent-aget.md` already exists from 2026-05-28. This refresh should update the article rather than creating a duplicate.
