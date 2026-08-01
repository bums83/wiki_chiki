---
title: Prompt Master
type: technology
created: 2026-04-30
last_updated: 2026-07-27
domain: llm-agents
related: ["Prompts.chat", "Вайб-кодинг", "Evolve", "The Agency / Agency Agents", "humanizer-ru", "UI/UX Pro Max"]
tags: ["prompt-engineering", "claude-skills", "ai-tools", "prompt-generation"]
sources: ["onlygithub-prompt-master-2026-04-30"]
---

# Prompt Master

`Prompt Master` — это open-source навык для Claude, который превращает размытые идеи в готовые к использованию промпты для любых AI-инструментов.

Пользователь описывает задачу обычными словами, Prompt Master самостоятельно определяет целевую платформу, выстраивает правильную архитектуру и выдаёт оптимизированный промпт с целью получить нужный результат с первой попытки.

## Что умеет

### Поддержка 20+ AI-инструментов

Категории:
- **LLM**: Claude, ChatGPT, Gemini, o1/o3, MiniMax
- **IDE-ассистенты**: Cursor, GitHub Copilot, Windsurf, Bolt, v0, Lovable, Devin
- **Генераторы изображений/видео**: Midjourney, DALL-E, Stable Diffusion, ComfyUI, Sora, Runway
- **Автоматизация**: Zapier, Make

Для инструментов вне списка используется Universal Fingerprint — механизм, который сам вычисляет логику любого API.

### Методика профессионального промпт-инжиниринга

Архитектура включает 12+ фреймворков: RTF, CO-STAR, Chain of Thought и другие.

Процесс:
1. Распознаёт тип задачи
2. Извлекает 9 измерений намерения: задача, входные/выходные данные, ограничения, контекст, аудитория, критерии успеха
3. Задаёт не более 3 уточняющих вопросов
4. Применяет нужный шаблон — от XML-структур до few-shot примеров

### Аудит токен-эффективности

Финальный этап — вырезание каждого слова, которое не влияет на результат. Остаётся лаконичный, «несущий» промпт без потери качества.

## Использование

Активируется по команде `/prompt-master` или простому описанию задачи в чате.

Примеры:
- «Напиши промпт для Midjourney: реалистичный самурай под дождём ночью» → готовый промпт с параметрами и negative-спейсом
- «Нужен промпт для Cursor, чтобы отрефакторить модуль авторизации» → готовый промпт для IDE-ассистента

## Связь с существующим кластером

Prompt Master логично дополняет уже существующие статьи:

- [Prompts.chat]({{ '/wiki/llm-agents/prompts-chat' | relative_url }}) — Prompts.chat это библиотека готовых промптов, Prompt Master это генератор новых промптов. Вместе покрывают и хранение, и создание.
- [Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }}) — Prompt Master генерирует промпты, вайб-кодинг описывает практику их использования. Генерация → применение.
- [Evolve]({{ '/wiki/llm-agents/evolve' | relative_url }}) — Prompt Master создаёт промпт, Evolve проверяет его эффективность эмпирически.
- [The Agency / Agency Agents]({{ '/wiki/llm-agents/agency-agents' | relative_url }}) — не генератор промптов, а каталог готовых agent personas; его можно использовать как источник ролевых шаблонов для дальнейшей настройки.

[humanizer-ru]({{ '/wiki/llm-agents/humanizer-ru' | relative_url }}) работает после Prompt Master: Prompt Master помогает подготовить instruction до вызова модели, а humanizer-ru проверяет готовую русскую прозу на штампы, чатовые артефакты и добавленные редактурой факты. Это разные контрольные точки одного content workflow.

[UI/UX Pro Max]({{ '/wiki/llm-agents/ui-ux-pro-max' | relative_url }}) — соседний design workflow: Prompt Master формулирует instruction, а UI/UX Pro Max добавляет локальный search по design/UX данным. Ни один слой не оценивает автоматически собранный интерфейс — для этого нужны browser/a11y/visual checks.

## Ограничения

- Работает только в рамках Claude
- Качество зависит от описания задачи пользователем
- Для специфических задач может потребоваться несколько итераций уточнения

## Источники

- forwarded Telegram post from channel `Only GitHub`
- https://github.com/nidhinjs/prompt-master
