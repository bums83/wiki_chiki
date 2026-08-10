---
title: The Agency / Agency Agents
type: technology
created: 2026-06-19
last_updated: 2026-08-10
domain: llm-agents
related: ["Agents.md", "Academic Research Skills", "Research org code", "Prompt Master", "Prompts.chat", "ProcessForge", "AI Factory"]
sources: ["github-msitarzewski-agency-agents-2026-06-19"]
tags: ["llm", "agents", "prompt-engineering", "workflow", "automation"]
---

# The Agency / Agency Agents

`The Agency` (`msitarzewski/agency-agents`) — большой каталог специализированных AI-agent personas, упакованных как Markdown-файлы с frontmatter, инструкциями, ролью, стилем, workflow и expected deliverables.

Проект позиционирует себя как «AI agency»: не один универсальный ассистент, а набор профильных специалистов — engineering, design, marketing, product, security, testing, sales, finance, GIS, game development и другие направления. На момент ingest в репозитории было 232 agent-файла в 16 divisions.

## Что это такое

В отличие от [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}), который обычно задаёт правила для одной кодовой базы или команды, `agency-agents` поставляет готовый roster ролей. Каждый агент — отдельный markdown-документ с:

- именем, описанием, emoji/color metadata;
- identity/personality блоком;
- mission и critical rules;
- рабочими процессами;
- deliverables и success criteria;
- стилем коммуникации.

Это ближе к библиотеке организационных ролей для LLM, чем к одному системному промпту. Пользователь выбирает не абстрактный режим «помоги», а конкретного специалиста: frontend developer, backend architect, UI designer, SEO specialist, incident responder, reality checker, multi-agent systems architect и т.д.

## Divisions

`divisions.json` фиксирует 16 source divisions:

- academic;
- design;
- engineering;
- finance;
- game-development;
- gis;
- marketing;
- paid-media;
- product;
- project-management;
- sales;
- security;
- spatial-computing;
- specialized;
- support;
- testing.

По состоянию на ingest самые крупные группы — `specialized`, `marketing`, `engineering`, `game-development`, `gis` и `security`. Это делает проект шире типичной prompt library: он покрывает не только software engineering, но и коммерческие, операционные, маркетинговые, геопространственные и игровые роли.

## Multi-tool packaging

Сильная сторона проекта — не только сами Markdown-агенты, но и packaging layer. Репозиторий содержит `scripts/convert.sh` и `scripts/install.sh`, которые адаптируют один source corpus под разные agentic tools.

Поддерживаемые targets включают:

- Claude Code;
- GitHub Copilot;
- Antigravity;
- Gemini CLI;
- OpenCode;
- OpenClaw;
- Cursor;
- Aider;
- Windsurf;
- Qwen Code;
- Kimi Code;
- Codex.

Конвертация меняет формат под runtime: например, Antigravity получает `SKILL.md`, Cursor — `.mdc` rules, Aider/Windsurf — consolidated rule files, OpenClaw — workspaces с `SOUL.md`/`AGENTS.md`/`IDENTITY.md`, Codex — TOML custom agents.

Это важное отличие от [Prompts.chat]({{ '/wiki/llm-agents/prompts-chat' | relative_url }}): там основной объект — prompt library, здесь объект — переносимая агентная workforce library с install/convert layer.

## NEXUS strategy layer

В `strategy/` лежит NEXUS — попытка превратить набор агентов в координированную operational model. Executive brief описывает NEXUS как «Network of EXperts, Unified in Strategy»: pipeline с phases, playbooks, handoff templates, activation prompts и scenario runbooks.

Ключевые идеи NEXUS:

- агентные проекты ломаются на handoff boundaries;
- нужны стандартизированные handoff templates;
- quality gates должны требовать evidence, а не «fantasy approvals»;
- parallel workstreams сокращают сроки, но требуют orchestration;
- Dev↔QA loop должен иметь retry limits и явный pass/fail.

Это делает проект близким к [Research org code]({{ '/wiki/llm-agents/research-org-code' | relative_url }}): объектом проектирования становится не только отдельный prompt, а агентная организация — роли, порядок активации, контракты, gates и recovery paths.

## Примеры agent design

Инспектированные agent-файлы показывают две линии дизайна.

`Multi-Agent Systems Architect` описывает multi-agent pipelines как distributed systems: topology selection, context architecture, failure mode engineering, least privilege, human-in-the-loop gates, observability, evals и prompt-injection defense.

`Agents Orchestrator` описывает более директивный pipeline manager: PM → architecture → dev/QA loop → integration, с task-by-task validation, retry limit и evidence-based decisions.

Эта часть пересекается с [Academic Research Skills]({{ '/wiki/llm-agents/academic-research-skills' | relative_url }}): оба проекта уходят от «одного промпта» к процедурной упаковке ролей, gates и artifacts. Разница в домене: Academic Research Skills глубоко сфокусирован на academic research workflow, а The Agency — широкий cross-functional агентный каталог.

## Где уместен

`agency-agents` полезен, когда нужно:

- быстро дать AI-ассистенту специализированную роль;
- собрать команду агентов для продукта, маркетинга, QA, security или operations;
- перенести одни и те же роли между Claude Code, Cursor, Codex, OpenClaw и другими tools;
- использовать готовые role definitions как reference для собственных agents;
- построить multi-agent pipeline с handoff и quality gates.

Проект может быть особенно полезен как сырьё для внутренней агентной библиотеки: взять не все 232 роли, а выбрать несколько divisions или конкретные agents через `--division`, `--agent` или `--agents-file`.

## Ограничения

Большой каталог агентных ролей не решает автоматически проблему качества. Риски очевидны:

- слишком много ролей повышает сложность выбора;
- agent personas могут конфликтовать, если нет orchestration layer;
- широкая библиотека требует отбора под конкретный workflow;
- установка «всего сразу» может перегрузить runtime или пользователя;
- готовые роли всё равно нужно проверять на реальных задачах и адаптировать под контекст.

Поэтому The Agency лучше рассматривать не как magic workforce, а как source corpus для агентной операционной системы. Без правил активации, handoff, evals и наблюдаемости каталог превращается в набор красивых персонажей.

## Практический вывод

`agency-agents` — это масштабная библиотека специализированных AI-agent ролей плюс tooling для переноса между agentic runtimes. Её ценность не в том, что «агентов много», а в том, что роли структурированы, разделены по divisions и снабжены install/convert механизмом.

Сильный сценарий — выбрать небольшой набор ролей под конкретный workflow и встроить их в дисциплинированный pipeline. Слабый сценарий — установить всё и надеяться, что сама масса агентов создаст порядок.


[ProcessForge]({{ '/wiki/llm-agents/processforge' | relative_url }}) закрывает недостающий operational слой для такого roster: он фиксирует assignment scope, context capsule, expected outputs, evidence и handoff. При этом ProcessForge не поставляет широкую библиотеку персонажей, а Agency не становится scheduler или доказательством корректного handoff только из-за наличия ролей.
[AI Factory]({{ '/wiki/llm-agents/ai-factory' | relative_url }}) — другой масштаб: не широкий roster personas, а CLI, который кладёт выбранный workflow skill-set и несколько runtime-native helper agents в один проект. Его bundled Codex support сам описан как baseline, поэтому не следует выдавать его за универсальную замену каталога ролей Agency.

## Источники

- [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- [Integrations README](https://github.com/msitarzewski/agency-agents/blob/main/integrations/README.md)
- [NEXUS Executive Brief](https://github.com/msitarzewski/agency-agents/blob/main/strategy/EXECUTIVE-BRIEF.md)
