---
title: Tolaria
type: technology
created: 2026-05-26
last_updated: 2026-05-26
domain: tools
related: ["GitNexus", "Prompts.chat", "Agents.md"]
sources: ["github-refactoringhq-tolaria-2026-05-26"]
tags: ["tools", "markdown", "knowledge-base", "git", "offline-first", "agents"]
---

# Tolaria

`Tolaria` — desktop-приложение для macOS, Windows и Linux, предназначенное для управления markdown knowledge bases. Проект позиционируется как локальный, files-first и git-first слой для личных и командных баз знаний.

Главная идея: знания остаются обычными Markdown-файлами с YAML frontmatter, а приложение даёт удобный интерфейс, навигацию и workflow вокруг этих файлов без переноса данных в закрытую облачную модель.

## Что это за класс инструмента

Tolaria относится к классу personal/team knowledge base tools, но отличается от типичных заметочников несколькими принципами:

- **files-first** — заметки являются plain markdown files, которые можно открыть любым редактором;
- **git-first** — vault является git-репозиторием, поэтому история, remote и переносимость строятся на стандартном Git;
- **offline-first** — работа не зависит от аккаунта, подписки или серверов Tolaria;
- **standards-based** — используется Markdown и YAML frontmatter, без proprietary export step;
- **AI-first but not AI-only** — база знаний проектируется как контекст для AI-агентов, но остаётся пригодной для ручной работы.

Поэтому Tolaria полезно рассматривать не как «ещё одно приложение для заметок», а как desktop-оболочку вокруг переносимого knowledge repository.

## Основные сценарии

README проекта выделяет три практических use case:

1. **Second brain и personal knowledge** — личная база заметок, дневников, идей и справочных материалов.
2. **Company docs as AI context** — корпоративная документация, которую можно использовать как устойчивый контекст для ассистентов.
3. **OpenClaw / assistants memory and procedures** — хранение процедур, памяти и операционных знаний для агентных сценариев.

Третий сценарий особенно важен для agentic workflows: база знаний становится не просто архивом, а источником инструкций и процедур, которые могут читать AI-инструменты.

## Связь с AI-агентами

Tolaria поддерживает setup paths для Claude Code, Codex CLI и Gemini CLI. Также проект предоставляет `AGENTS`-файл, который помогает агентам понимать структуру vault и правила работы с ним.

В этом смысле Tolaria находится рядом с [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}): `Agents.md` описывает формат постоянного контекста для coding-агентов, а Tolaria даёт desktop-среду, где такой контекст и связанные markdown-документы могут жить как обычная git-база.

Для команд это означает, что процедурные знания можно хранить в форме, пригодной одновременно для людей, IDE, CLI-агентов и внешних automation-сценариев.

## Отличие от code knowledge graph tools

Tolaria не индексирует код как graph-based intelligence engine. Его объект — markdown vault, а не репозиторий исходников как архитектурная модель.

Поэтому он дополняет [GitNexus]({{ '/wiki/tools/gitnexus' | relative_url }}): GitNexus превращает кодовую базу в knowledge graph для понимания архитектуры, а Tolaria превращает документацию, процедуры и заметки в переносимую knowledge base.

В паре они закрывают разные слои agentic context:

- GitNexus — структурное понимание кода;
- Tolaria — человеко- и агентно-читаемая база знаний вокруг работы, процессов и памяти.

## Prompt и procedure library

Tolaria может использоваться как private knowledge base для prompts, procedures и reusable operational notes. Это пересекается с [Prompts.chat]({{ '/wiki/llm-agents/prompts-chat' | relative_url }}), но фокус другой.

Prompts.chat — публичная / self-hosted prompt library и tooling layer вокруг промптов. Tolaria шире: он хранит не только промпты, но и заметки, документацию, процедуры, memory-файлы, daily notes и любые markdown-артефакты.

Для AI-assisted работы это даёт практичный паттерн: промпты, правила, решения и контекст можно держать рядом, версионировать через Git и передавать агентам без vendor lock-in.

## Техническая база

Проект open-source и построен на Tauri, React и TypeScript. Для локальной разработки требуются Node.js 20+, pnpm 8+ и Rust stable.

Типовой dev loop:

```bash
pnpm install
pnpm dev
pnpm tauri dev
```

На Linux Tauri 2 требует WebKit2GTK 4.1 и GTK 3 зависимости. README отдельно отмечает, что bundled MCP server на Linux всё ещё запускает системный `node` binary во внешнем AI tooling flow.

## Установка

На macOS поддерживается Homebrew:

```bash
brew install --cask tolaria
```

Также доступны релизы для macOS, Windows и Linux через страницу загрузки проекта.

## Ограничения и трезвый взгляд

Tolaria особенно уместна там, где важны контроль над данными, Git-история и переносимость. Если команда уже живёт в закрытой SaaS-базе знаний и не планирует работать с markdown/git workflow, часть преимуществ может не окупиться.

AGPL-3.0-or-later лицензия также требует внимания перед коммерческим embedding или модификацией: это не permissive-лицензия, и условия распространения нужно проверять отдельно.

## Практический вывод

`Tolaria` — open-source desktop layer для markdown knowledge bases, который соединяет привычный UX заметочника с Git, offline-first подходом и AI-friendly структурой данных.

Её главная ценность — в том, что база знаний остаётся обычным репозиторием файлов, пригодным для людей, редакторов, CLI-инструментов и AI-агентов одновременно.

## Источники

- [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria)
- [Tolaria homepage](https://tolaria.md)
