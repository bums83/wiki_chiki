---
title: RTK
type: technology
created: 2026-05-01
last_updated: 2026-05-01
domain: infra
related: ["PowerInfer", "Вайб-кодинг"]
tags: ["llm-optimization", "token-saving", "cli-proxy", "development-tooling"]
sources: ["github-rtk-ai-rtk-2026-05-01"]
---

# RTK

`RTK` (RTK-ai/rtk) — это high-performance CLI proxy, который фильтрует и сжимает вывод команд перед отправкой в контекст LLM, сокращая потребление токенов на 60-90% при типичных dev-операциях.

Это не ещё один AI-инструмент — это инфраструктурный слой между вашими командами и LLM-контекстом.

## Как это работает

RTK перехватывает вывод shell-команд и применяет четыре стратегии фильтрации:

1. **Smart Filtering** — убирает шум: комментарии, whitespace, boilerplate
2. **Grouping** — агрегирует похожие элементы (файлы по директориям, ошибки по типу)
3. **Truncation** — оставляет релевантный контекст, убирает избыточность
4. **Deduplication** — сворачивает повторяющиеся строки логов с подсчётом

Установка — одна команда:
```bash
brew install rtk
# или
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
```

## Типичные результаты

| Команда | Без RTK | С RTK | Экономия |
|---------|---------|-------|----------|
| `ls / tree` | ~2,000 | ~400 | -80% |
| `cat / read` | ~40,000 | ~12,000 | -70% |
| `git status` | ~3,000 | ~600 | -80% |
| `cargo test` | ~25,000 | ~2,500 | -90% |
| `pytest` | ~8,000 | ~800 | -90% |
| `git add/commit/push` | ~1,600 | ~120 | -92% |

Общая оценка: ~118,000 токенов → ~23,900 токенов при типичном рабочем дне (-80%).

## Поддерживаемые инструменты

RTK поддерживает 100+ команд и интегрируется с 12 AI coding tools:
- Claude Code (pre-tool hook)
- GitHub Copilot
- Cursor
- Windsurf
- Cline / Roo Code
- Gemini CLI
- Codex (OpenAI)
- и другие

## Установка и интеграция

```bash
# Установка
brew install rtk

# Инициализация для Claude Code
rtk init -g

# Перезапустить AI-инструмент — и всё работает
git status  # автоматически → rtk git status
```

RTK transparently перехватывает Bash-команды и переписывает их в rtk-эквиваленты перед выполнением. LLM получает уже сжатый вывод.

## Практический смысл

### Экономия токенов

При активной работе с AI-coding инструментами типичный dev workflow генерирует десятки тысяч токенов в день. RTK сокращает это на 60-90% без потери полезной информации.

### Совместимость с локальными стеками

RTK работает с локальными LLM-инструментами, что важно для приватных workflow. В связке с [PowerInfer]({{ '/wiki/infra/powerinfer' | relative_url }}) (локальный inference) это даёт полностью приватный AI-coding контур.

### Совместимость с LLM-оптимизацией

В контексте [Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }}) RTK добавляет ещё один слой эффективности: помимо правильной постановки задач агенту, вы ещё и оптимизируете сам контекстный поток.

## Ограничения

- На Windows работает в fallback-режиме (CLAUDE.md injection) без auto-rewrite hook
- Только Bash tool calls перехватываются — встроенные инструменты Claude Code (Read, Grep, Glob) обходятся напрямую
- Экономия зависит от размера проекта

## Источники

- https://github.com/rtk-ai/rtk
- https://www.rtk-ai.app
