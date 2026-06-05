---
title: Magpie
type: technology
created: 2026-06-02
last_updated: 2026-06-02
domain: tools
related: ["Agents.md", "Evolve", "GitNexus", "agent-aget", "MCPorter", "Tokentap"]
sources: ["github-liliu-z-magpie-2026-06-02"]
tags: ["tools", "cli", "agents", "automation", "workflow"]
---

# Magpie

`Magpie` — TypeScript CLI-инструмент для adversarial code review, где несколько AI-моделей независимо ревьюят PR, затем спорят о находках, а отдельный code-aware verifier проверяет каждую проблему по реальной кодовой базе.

В отличие от простого «LLM прочитал diff», Magpie строит полный pipeline ревью: context gathering, анализ PR, параллельные раунды reviewers, convergence check, structurizer, verify+audit и опциональный summarizer. Поэтому внутри Wiki Chiki он ближе к tool-layer для инженерного качества, чем к обычной prompt-библиотеке.

## Что делает

Основной сценарий — PR review:

- принимает номер PR или GitHub URL;
- может ревьюить local changes, current branch vs base или конкретные файлы;
- поддерживает full repository review с feature-based analysis;
- запускает несколько reviewers в одинаковых условиях;
- собирает дискуссию в несколько раундов;
- извлекает issues в структурированный JSON;
- проверяет находки по исходникам и фильтрует false positives;
- формирует итоговый вывод и, при необходимости, inline comments для GitHub PR.

Дополнительно есть команда `magpie discuss`, которая использует тот же multi-reviewer debate подход для технических обсуждений: архитектурные решения, миграции, выбор между microservices/monolith и другие спорные темы.

## Adversarial review model

Ключевая идея Magpie — fair debate model. В первом раунде reviewers дают независимое мнение, не видя ответы друг друга. В последующих раундах каждый видит все предыдущие сообщения и может подтвердить, оспорить или уточнить чужие находки. Reviewers одного раунда получают одинаковую информацию и выполняются параллельно.

Такой подход использует естественное различие моделей как механизм cross-validation. Если одна модель нашла проблему, другие могут её подтвердить или указать, что это false positive. После дискуссии verify+audit слой читает реальные файлы и перепроверяет evidence.

Это роднит Magpie с [Evolve]({{ '/wiki/llm-agents/evolve' | relative_url }}): оба инструмента используют несколько AI-систем для повышения качества результата, но Evolve пассивно A/B-тестирует ассистентов в фоне, а Magpie явно организует debate вокруг конкретного PR или технического вопроса.

## Code-aware reviewers

Magpie делает акцент на CLI-based reviewers: Claude Code, Codex CLI, Gemini CLI и Qwen Code. Такие reviewers могут читать исходники через свои tools, искать callers, смотреть surrounding context и проверять гипотезы до того, как сформулировать issue.

Это важно для практик из [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}): качество AI-review зависит не только от модели, но и от правил, контекста, review dimensions и того, насколько явно описан workflow проверки. Magpie выносит эти элементы в `~/.magpie/config.yaml`: providers, reviewers, analyzer, summarizer и contextGatherer.

## Поддерживаемые провайдеры

Проект поддерживает два класса providers:

- CLI providers: `claude-code`, `codex-cli`, `gemini-cli`, `qwen-code` — используют существующие подписки или логины и не требуют API key;
- API providers: Anthropic, OpenAI, Google Gemini, MiniMax и compatible endpoints через custom `base_url`.

Также есть `mock` provider для debug mode, чтобы тестировать workflow без реальных AI-вызовов.

## Контекст и проверка

Перед debate Magpie может собрать system context:

- affected modules;
- related PRs из истории;
- call-chain analysis для Go, C++, Python, Java, Scala, TypeScript/JavaScript, Rust и Proto;
- релевантные docs вроде README, ARCHITECTURE, DESIGN.

Здесь полезна связь с [GitNexus]({{ '/wiki/tools/gitnexus' | relative_url }}): GitNexus строит knowledge graph репозитория, а Magpie использует context gathering и tool-equipped reviewers для конкретного review/debate процесса. Оба инструмента уменьшают риск blind edits и поверхностных выводов по diff.

## Workflow и automation

Типовой запуск:

```bash
magpie init
magpie review 12345
magpie review https://github.com/owner/repo/pull/12345
magpie discuss "Should we use microservices or monolith?"
```

В более автоматизированных сценариях Magpie может быть review step внутри CI, bot flow или agent workflow. Флаги `--no-post`, `--no-conclusion`, `--fail-fast`, `--plan-only`, `--skip-context`, `--reviewers` и `--all` позволяют переключать режим между интерактивным ревью, ботом и диагностическим запуском.

В связке с [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) и другими CLI capabilities Magpie показывает общий паттерн: агентный workflow становится надёжнее, когда сложные действия упакованы в инструмент с явными командами, форматами вывода и режимами восстановления.

[Tokentap]({{ '/wiki/tools/tokentap' | relative_url }}) добавляет к таким CLI workflows слой наблюдаемости: сколько токенов ушло в reviewers или coding agents, насколько заполнено context window и какие prompts реально были отправлены.

## Ограничения

У Magpie есть несколько практических ограничений:

- качество зависит от настроенных reviewers и их доступа к исходникам;
- CLI providers требуют установленного и залогиненного Claude Code, Codex CLI, Gemini CLI или Qwen Code;
- API providers требуют ключей и корректного `base_url`;
- multi-round debate может быть дорогим по токенам, хотя convergence detection помогает остановиться раньше;
- adversarial debate не заменяет человеческую ответственность за merge decision.

Также важно не воспринимать consensus моделей как доказательство корректности: Magpie снижает риск false positives через verify+audit, но финальное решение всё равно должно опираться на code evidence, severity и контекст проекта.

## Практический вывод

`Magpie` — полезный слой для команд, которые хотят превратить AI code review из одиночного комментария модели в проверяемый debate pipeline. Его сильная сторона — комбинация нескольких reviewers, fair parallel rounds, code-aware verification и структурированного post-processing для PR comments.

## Источники

- https://github.com/liliu-z/magpie
