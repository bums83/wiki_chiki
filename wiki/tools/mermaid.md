---
title: Mermaid
type: technology
created: 2026-04-30
last_updated: 2026-08-15
domain: tools
related: ["Вайб-кодинг", "Диаграмма Исикавы", "Методология A3", "Penpot", "OculiX", "OpenScreen", "Slidev"]
tags: ["diagrams", "flowcharts", "mermaid", "documentation", "technical-graphics"]
sources: ["mermaideditor-com-2026-04-30"]
---

# Mermaid

`Mermaid` — это open-source инструмент для создания диаграмм, блок-схем и графиков из текстового описания, похожего на Markdown-синтаксис.

Вместо рисования в GUI или генерации картинок через визуальные ИИ-генераторы, вы описываете диаграмму текстом, а Mermaid рендерит её в PNG или SVG.

## Что это даёт

Mermaid решает несколько практических задач:

1. **Воспроизводимость** — диаграмма это код, её можно хранить в Git, версионировать, мержить
2. **LLM-friendly** — любой LLM без проблем превращает текстовое описание в Mermaid-код
3. **Интеграция в документацию** — встраивается в Markdown, GitHub, GitLab, Notion и другие платформы
4. **Консистентность** — не нужно перерисовывать вручную при изменении процесса

## Поддерживаемые типы диаграмм

Всего 21 тип, основные:
- блок-схемы (flowchart)
- диаграммы последовательностей (sequence diagram)
- диаграммы классов (class diagram)
- диаграммы состояний (state diagram)
- диаграммы Ганта (Gantt chart)
- диаграммы «сущность-связь» (ER diagram)
- пользовательские диаграммы через Mermaid JS

## Пример: блок-схема процесса

Процесс из описания превращается в код:

```
graph TD
 A[🚀 Начать проект] --> B{📋 Есть требования?}
 B -->|✅ Да| C[💻 Начать кодинг]
 B -->|❌ Нет| D[📝 Собрать требования]
 D --> B
 C --> E{🧪 Тесты пройдены?}
 E -->|✅ Да| F[🎉 Деплой!]
 E -->|❌ Нет| G[🔧 Исправить баги]
 G --> E
```

Результат — визуальная блок-схема, которую можно встроить в любую документацию.

## Практический workflow с LLM

Порядок работы:
1. Описываете процесс или структуру текстом
2. Просите LLM интерпретировать в нотации Mermaid
3. Вставляете код в документацию
4. Mermaid рендерит диаграмму

Это особенно удобно для:
- технической документации
- архитектурных диаграмм
- бизнес-процессов
- onboarding-описаний
- спецификаций

## Связь с существующим кластером wiki

Mermaid естественно дополняет несколько уже существующих статей:

- [Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }}) — LLM может генерировать Mermaid-код, что делает визуальную документацию частью agentic workflow
- [Диаграмма Исикавы]({{ '/wiki/management/ishikawa-diagram' | relative_url }}) — Mermaid умеет рисовать fishbone-диаграммы, хотя и не является специализированным инструментом для 6M-анализа
- [Методология A3]({{ '/wiki/management/a3-methodology' | relative_url }}) — A3-отчёты можно иллюстрировать через Mermaid-диаграммы

## Связь с design workflow

Для UI/UX-команд Mermaid не заменяет полноценный визуальный редактор, но хорошо дополняет [Penpot]({{ '/wiki/tools/penpot' | relative_url }}): в Penpot проектируют интерфейсы и design system, а в Mermaid фиксируют процессы, user flows, архитектурные схемы и сопроводительную документацию рядом с кодом.

[OculiX]({{ '/wiki/tools/oculix' | relative_url }}) даёт пример сценариев, где диаграммы особенно полезны: visual automation flows с несколькими GUI, ожиданиями, remote sessions и fallback-ветками удобнее проектировать и документировать через sequence или flowchart diagrams. [OpenScreen]({{ '/wiki/tools/openscreen' | relative_url }}) закрывает соседний формат объяснения: Mermaid даёт схему процесса, а OpenScreen — видео того же workflow.

[Slidev]({{ '/wiki/tools/slidev' | relative_url }}) использует Mermaid внутри developer presentation deck: диаграмма остаётся text-based и reviewable, но появляется рядом с narration, click steps, code и presenter notes. Для standalone docs Mermaid проще; для technical talk Slidev добавляет delivery/presenter layer.

## Редакторы

Бесплатные редакторы:
- https://mermaideditor.com/ru — онлайн-редактор с превью
- GitHub / GitLab — нативная поддержка Mermaid в Markdown
- VS Code — расширения для подсветки и превью

Документация на русском: https://mermaideditor.com/ru/cheatsheet

## Ограничения

- Сложные диаграммы требуют внимания к синтаксису
- Не все типы диаграмм одинаково удобны в Mermaid
- Для векторной графики высокого качества может потребоваться другой инструмент

## Источники

- https://mermaideditor.com/ru
- https://mermaideditor.com/ru/cheatsheet
