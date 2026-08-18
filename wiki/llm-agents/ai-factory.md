---
title: AI Factory
type: technology
created: 2026-08-10
last_updated: 2026-08-18
domain: llm-agents
related: ["Agents.md", "ProcessForge", "The Agency / Agency Agents", "MCPorter", "Boring Computers", "Firecracker"]
tags: ["llm", "agents", "workflow", "automation", "mcp", "open-source"]
sources: ["github-lee-to-ai-factory-2026-08-10"]
---

# AI Factory

`AI Factory` — npm CLI и набор project-local skills/agent files для AI-assisted разработки. Он не является моделью, изолированной средой исполнения или самостоятельным autonomous developer. Его работа — положить в конкретный репозиторий контекст, workflow-артефакты, инструкции для выбранных coding agents и при необходимости MCP-конфигурацию.

На проверенной ветке `2.x` проект уже опережает последний GitHub release: HEAD `2a3b142` от 2026-08-08, `package.json` заявляет версию `2.18.0`, тогда как последний release/tag — `v2.17.0` от 2026-07-06. Ниже речь именно о checkout ветки `2.x`, не о гарантированно опубликованном npm/release артефакте.

## Что устанавливает CLI

Нужны Node.js `>=18` и глобальная установка пакета. Затем `ai-factory init` запускается **внутри проекта**. Это не безобидная команда просмотра: она создаёт и меняет файлы в рабочем дереве.

| Слой | Что появляется или меняется | Кто владеет |
|---|---|---|
| CLI-state | `.ai-factory.json`: выбранные runtimes, installed skills, managed hashes, MCP и extensions | пакет AI Factory |
| Рабочие артефакты | `.ai-factory/` с `DESCRIPTION.md`, architecture, roadmap, rules, plans, research, QA и другими путями из `config.yaml` | конкретные skills по ownership contract |
| Agent runtime | например, `.claude/skills/`, `.claude/agents/`, `.codex/skills/`, `.codex/agents/` | package-managed assets и пользовательские файлы разделены по metadata |
| MCP settings | runtime-specific JSON/TOML configuration с выбранными template servers | CLI для выбранных runtimes |
| Extensions | `.ai-factory/extensions/<name>/`, skills, agent files, MCP и marker-wrapped injections | extension lifecycle CLI |

`init` понимает много targets: Claude Code, Cursor, Windsurf, Roo/Kilo Code, Antigravity, OpenCode, Warp, Zencoder, Codex CLI/app, Copilot, Gemini CLI, Junie, Qwen Code и universal path. Но это **не одинаковая функциональность**: bundled native-agent support шире у Claude; у Codex есть baseline planning/implementation/review bundle. Для некоторых runtimes устанавливаются только преобразованные skills без auto-MCP.

## Рабочая модель: не один prompt, а цепочка артефактов

После setup основной workflow выглядит так:

```text
/aif → explore или grounded → plan → improve → implement → verify / review / security → commit → evolve
```

- `/aif` формирует базовый project context;
- `/aif-explore` исследует вопрос до реализации, а `/aif-grounded` заявлен как режим evidence-only ответа;
- `/aif-plan` создаёт fast, full или явно opt-in ultra plan; ultra — папка с `index.md` и фазовыми спецификациями;
- `/aif-implement` исполняет plan, а `/aif-verify`, `/aif-review`, `/aif-security-checklist` и `/aif-rules-check` возвращают финальный machine-readable `aif-gate-result` JSON;
- `/aif-loop` хранит phase-state и историю итераций в `.ai-factory/evolution/`.

Это полезно как дисциплина: request, исследовательский контекст, план, gates и QA-артефакты остаются в файловой системе вместо исчезающего чата. Но сами skills — это инструкции, которые исполняет внешний agent runtime. Наличие plan, gate schema или subagent role не доказывает, что задача понята верно, тесты релевантны или изменения безопасны.

## Subagents: где реальная граница multi-agent

В source tree есть runtime-native agent files: более широкий Claude bundle и ограниченный Codex bundle. Планирующие и implementation coordinators рассчитаны на top-level session: они могут вызывать bounded workers, строить dependency layers и при параллельных задачах использовать отдельные git worktrees. Read-only sidecars предназначены для review, security, rules, documentation и commit readiness.

У этого есть жёсткие ограничения:

- обычный subagent не может строить бесконечную вложенную иерархию; source прямо адаптирует workflow под это ограничение;
- Codex bundle — baseline, а не parity с Claude bundle;
- parallel worktrees снижают конфликты файлов, но **не** дают container/VM sandbox и не изолируют сеть или секреты;
- runtime model, доступные инструменты и реальная permission policy принадлежат выбранному внешнему агенту, не AI Factory.

Если требуется disposable execution environment, нужен отдельный слой вроде [Boring Computers]({{ '/wiki/llm-agents/boring-computers' | relative_url }}) поверх [Firecracker]({{ '/wiki/infra/firecracker' | relative_url }}), а не только worktree orchestration.

## MCP и extensions: полезно, но это supply-chain boundary

CLI умеет записывать templates для GitHub, PostgreSQL, filesystem, Chrome DevTools и Playwright в формат конкретного runtime. Некоторые шаблоны ожидают environment references, например `GITHUB_TOKEN` или `DATABASE_URL`; секреты не должны попадать в `.ai-factory.json`, git или agent prompts.

Extensions имеют широкие права на интеграцию: могут добавлять commands, skills, runtime definitions, agent files, MCP servers и injection blocks в установленные skills. AI Factory проверяет manifest/path boundaries и пытается сохранить user-owned files; package-managed Codex config может обновляться, если tracked file чисто соответствует предыдущему managed hash. Поэтому перед `extension add` или `update --force` нужен обычный supply-chain review и diff, а не вера в название расширения.

Для внешних skills upstream описывает two-level screening: статический Python scanner плюс semantic review агентом. Это хорошая защита от известных prompt-injection и exfiltration patterns, но не доказательство безопасности неизвестного кода или инструкций. В частности, repo self-scan применяет allowlist только для собственного trusted content; переносить её на чужие skills нельзя.

## Верификация checkout

В чистом temporary checkout под Node `v24.17.0` были выполнены `npm ci --ignore-scripts --no-audit --no-fund`, build, lint и наборы, соответствующие CI. Результат:

| Проверка | Результат |
|---|---|
| TypeScript build | passed |
| `npm run lint` (`tsc --noEmit` + `knip`) | passed |
| `npm test` | **145 passed, 0 failed**, 11 предупреждений о слишком длинных `SKILL.md` |
| `npm run test:init` | passed: Claude/Codex init, managed-config ownership, path boundaries, extension conflicts |
| `npm run test:update` | passed: update/migration/managed asset cases |
| internal security self-scan | 0 critical; 31 warnings, из них 28 исключены first-party allowlist |

Это проверяет исходный checkout и его test contracts, но не запускает реальные LLM-сессии, GitHub/Postgres MCP с учётными данными, browser automation, произвольные сторонние extensions или production codebase. Официальный CI использует Node 18; локальная проверка на Node 24 не заменяет его matrix.

## Лицензия и release caveat

README и `package.json` указывают `MIT`. При этом в проверенном root tree отсутствует файл `LICENSE`, а GitHub API возвращает `license: null`. До появления явного license text в репозитории или опубликованном пакете это следует трактовать как **лицензионную неопределённость**, а не как полностью подтверждённую MIT-лицензию для downstream use.

Разрыв между `package.json` `2.18.0` на ветке и последним release `v2.17.0` — отдельный operational caveat: для команды лучше pin-ить exact npm version или commit и тестировать именно выбранный артефакт, а не предполагать, что README ветки и опубликованный package совпадают.

## С чем не путать

| Рядом | Разница |
|---|---|
| [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}) | `AGENTS.md` — компактные правила репозитория. AI Factory генерирует и раскладывает более широкий набор skills, config и workflow artifacts; это полезно только если их ownership действительно поддерживается. |
| [ProcessForge]({{ '/wiki/llm-agents/processforge' | relative_url }}) | ProcessForge формализует context snapshots, assignments и handoffs без обязательного runtime setup. AI Factory ориентирован на bootstrapping конкретных coding-agent runtimes и их project-local assets. |
| [The Agency / Agency Agents]({{ '/wiki/llm-agents/agency-agents' | relative_url }}) | Agency — большой каталог personas. AI Factory — более узкий workflow package с CLI, selected native bundles и generated project state; не заменяет широкий roster. |
| [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}) | AI Factory записывает ограниченный набор MCP templates во время setup. MCPorter — отдельный operator для конфигурирования, auth и прямой диагностики MCP tool calls. |
| [Boring Computers]({{ '/wiki/llm-agents/boring-computers' | relative_url }}) | Worktrees из AI Factory изолируют git-ветки, не операционную среду. Boring Computers изолирует сам execution substrate через disposable microVM. |

## Практический вывод

AI Factory оправдан для команд, которые готовы поддерживать project-local agent instructions как часть кода: проверять generated diff, pin-ить package version, отдельно утверждать MCP/extension sources и запускать настоящие tests после реализации. Он сокращает стартовую рутину и делает workflow заметнее.

Он слабый выбор, если нужна «одна команда — автономная безопасная разработка», универсальная parity всех IDE или sandbox только за счёт multi-agent roles. В этих местах source сам оставляет границы: разные runtimes поддержаны по-разному, managed assets могут обновляться, а качество работы остаётся ответственностью модели, оператора и настоящих CI/QA.

## Источники

- [lee-to/ai-factory — проверенная ветка `2.x`](https://github.com/lee-to/ai-factory)
- [README](https://github.com/lee-to/ai-factory/blob/2.x/README.md), [workflow](https://github.com/lee-to/ai-factory/blob/2.x/docs/workflow.md), [configuration](https://github.com/lee-to/ai-factory/blob/2.x/docs/configuration.md)
- [security](https://github.com/lee-to/ai-factory/blob/2.x/docs/security.md), [subagents](https://github.com/lee-to/ai-factory/blob/2.x/docs/subagents.md), [CI](https://github.com/lee-to/ai-factory/blob/2.x/.github/workflows/ci.yml)
- [latest GitHub release `v2.17.0`](https://github.com/lee-to/ai-factory/releases/tag/2.17.0)
