---
id: github-moul-assh-2026-06-19
date: 2026-06-19
source_type: url
source_url: https://github.com/moul/assh
title: assh — advanced ssh config
domain: tools
tags: [tools, cli, automation, shell, linux]
---

# assh — raw ingest

Source repository: https://github.com/moul/assh

Fetched/inspected on 2026-06-19:
- README.md
- doc.go
- pkg/commands/commands.go
- pkg/config/config.go
- top-level repository structure
- GitHub repository metadata via API

Durable source facts:
- Project name: `assh`.
- Import path/module visible in code: `moul.io/assh/v2`.
- CLI description from code: `assh - advanced ssh config`.
- Repository description from GitHub API: `:computer: make your ssh client smarter`.
- Language/runtime: Go CLI.
- License: MIT.
- GitHub metadata fetched 2026-06-19: stars 3208, forks 162, default branch `master`, created 2011-12-25, updated 2026-06-18, pushed 2026-06-18, not archived.
- Topics: automation, config, config-management, devops, proxy, ssh.

README facts:
- `assh` is a transparent wrapper around SSH that adds regex, aliases, gateways, dynamic hostnames, Graphviz, JSON output, YAML configuration and more.
- It works by wrapping SSH via ProxyCommand, so it can be used with `ssh`, `scp`, `rsync`, `git` and desktop apps relying on SSH/libssh behavior.
- Gateway shorthand supports command-line chains such as `ssh hosta/hostb` and `ssh hosta/hostb/hostc` instead of manual nested `ProxyCommand` strings.
- YAML configuration is stored by default in `~/.ssh/assh.yml` and can contain `hosts`, `templates`, `defaults`, `includes`, `ASSHBinaryPath` and related SSH options.
- `assh` manages/regenerates `~/.ssh/config`; README warns to keep a backup.
- Configuration features include aliases, gateway fallbacks, includes, local command execution, templates, inheritance, environment variable expansion, smart ProxyCommand, rate limits, JSON output and Graphviz host graph output.
- Hooks include `BeforeConnect`, `OnConnect`, `OnConnectError`, `OnDisconnect`, `BeforeConfigWrite`, `AfterConfigWrite`; hook drivers include `exec`, `write`, `notify`.
- Commands visible in README/code include `config build`, `config list`, `config graphviz`, `config search`, `info`, `sockets list`, `sockets flush`, `sockets master`, `ping`.
- Install paths include `go install moul.io/assh/v2@latest` and Homebrew (`brew install assh`).

Integration note:
- ASSH belongs in Wiki Chiki `tools` domain as a practical CLI/operator around SSH configuration and gateway/proxy workflows.
- Closest neighbors: MCPorter, Antfarm, OculiX, agent-aget. It is not an agent tool by itself, but it is useful as a stable shell capability inside agent or ops workflows that need SSH access.
