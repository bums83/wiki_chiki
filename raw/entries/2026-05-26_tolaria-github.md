---
id: github-refactoringhq-tolaria-2026-05-26
date: 2026-05-26
source_type: url
source_url: https://github.com/refactoringhq/tolaria
title: Tolaria — desktop app to manage markdown knowledge bases
domain: tools
tags: [tools, markdown, knowledge-base, git, offline-first, agents]
---

# Tolaria — source capture

Source: https://github.com/refactoringhq/tolaria
Homepage: https://tolaria.md
Repository: `refactoringhq/tolaria`

GitHub metadata at ingest time:
- description: Desktop app to manage markdown knowledge bases
- language: TypeScript
- license: AGPL-3.0-or-later
- stars: 11516
- forks: 820
- default branch: main
- created: 2026-02-14T19:43:14Z
- pushed: 2026-05-26T15:09:02Z

README facts captured:
- Tolaria is a desktop app for macOS, Windows, and Linux for managing markdown knowledge bases.
- Use cases: second brain / personal knowledge, company docs as AI context, OpenClaw/assistants memory and procedures.
- Principles: files-first, git-first, offline-first, zero lock-in, open source, standards-based markdown + YAML frontmatter, types as lenses, AI-first but not AI-only, keyboard-first.
- AI tooling: setup paths for Claude Code, Codex CLI, and Gemini CLI; an AGENTS file is provided for agents.
- Installation: Homebrew cask on macOS (`brew install --cask tolaria`) or downloads from releases.
- Development stack: Tauri, React, TypeScript; prerequisites include Node.js 20+, pnpm 8+, Rust stable, and Linux WebKit/GTK dependencies for Tauri 2.
- Local dev commands: `pnpm install`, `pnpm dev`, `pnpm tauri dev`.

Relevant docs in repo:
- `docs/ARCHITECTURE.md`
- `docs/ABSTRACTIONS.md`
- `docs/GETTING-STARTED.md`
- `docs/adr/`
- public docs under `site/`
