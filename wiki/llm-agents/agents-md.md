---
title: Agents.md
type: best practices
created: 2026-05-01
last_updated: 2026-05-01
domain: llm-agents
related: ["Вайб-кодинг", "Evolve", "Prompt Master", "CLAUDE.md"]
tags: ["ai-coding", "team-lead", "coding-standards", "prompting", "development-tooling"]
sources: ["augmentcode-2026-05-01", "agentsmd-io-2026-05-01"]
---

# Agents.md

`Agents.md` — markdown-файл с правилами, рекомендациями и ограничениями для AI coding-агентов. Служит постоянным контекстом, который подсказывает агенту стандарты кодовой базы, архитектурные паттерны и воркфлоу. Это зона ответственности тимлида.

Agents.md стал де-факто открытым стандартом, принятым более чем 20 000 репозиториями. В августе 2025 года формат формализовали совместно OpenAI, Google, Cursor, Factory и Sourcegraph. Поддерживается напрямую в Augment, Cursor, Claude Code (через CLAUDE.md) и других IDE.

## Зачем нужен

Без Agents.md AI-агент работает на общих знаниях о программировании, которые могут конфликтовать с конкретной кодовой базой. Agents.md даёт:

- **Консистентность** — все агенты (и люди) работают по одним правилам
- **Скорость** — меньше итераций и переделок
- **Контроль** — явные разрешения и запреты вместо "агенты делают что хотят"
- **Передаваемость** — правила живут в репозитории, а не в голове тимлида

## Структура и рекомендации

### Progressive disclosure

Самая эффективная структура — **skill-like**: на верхнем уровне держать общие рекомендации, детали и примеры — в отдельных файлах.

**Оптимальный размер: 100–150 строк.** Очень подробные файлы работают хуже — агенту сложнее удержать всё в контексте. Файл должен быть достаточно компактным, чтобы его можно было прочитать за один проход и не потерять фокус.

### Пронумерованные шаги для воркфлоу

Один из самых эффективных паттернов — описывать задачу или сложный воркфлоу как серию пронумерованных шагов:

```markdown
### Как добавить новый API endpoint

1. Создай файл `api/clients/{resource}.ts` — используй `api/clients/template.ts` как образец
2. Добавь типы запроса и ответа в `api/types/{resource}.ts`
3. Напиши unit-тест в `api/{resource}.test.ts`
4. Обнови `api/index.ts` — экспортируй новый клиент
5. Добавь документацию в `api/docs/{resource}.md`
```

### Decision tables

Когда в кодовой базе несколько способов решить одну задачу, помогает набор вопросов с весами в пользу того или иного варианта:

```markdown
## Decision table: какой тип компонента выбрать?

| Ситуация | Действие |
|---|---|
| Нужен интерактивный UI с состоянием | `app/components/Form.tsx` — functional component + hooks |
| Одноразовая статическая секция | Inline в родительском компоненте |
| Переиспользуемый UI-примитив | `app/components/ui/` — atomic components |
| Сложный Data grid | `app/components/Table.tsx` — проверенный паттерн |
| Чарты | `app/components/Charts/Bar.tsx` — copy-paste, не пиши с нуля |
```

### Do / Don't с парами

Каждый `don't` должен сопровождаться соответствующим `do`:

```markdown
### Do
- используй functional components с hooks
- используй `app/api/client.ts` для HTTP-запросов
- предпочитай small, focused modules

### Don't
- не используй class components → используй functional components с hooks
- не делай fetch напрямую в компонентах → используй `app/api/client.ts`
- не создавай god components → разбивай на focused modules
```

### Примеры из реальной кодовой базы

Короткие сниппеты из реального кода сильно повлияли на переиспользуемость кода:

```markdown
## Примеры

- хорошие формы: copy `app/components/DashForm.tsx`
- хорошие чарты: copy `app/components/Charts/Bar.tsx`
- data grids: copy `app/components/Table.tsx`
- не используй `Admin.tsx` как образец — это legacy
```

Указывайте конкретные файлы и явно говорите, какие образцы **не** стоит использовать.

### Архитектурные детали — дозированно

Не нужно слишком детально описывать архитектуру, особенно во вложенных файлах. Агент не должен погружаться в 5 уровней документации, чтобы сделать простое изменение. Лучше: ссылка на один файл со структурой, чем описание всей системы.

### Dos/Donts — не больше 15

Избегайте слишком длинных секций dos/donts. Когда количество уходит за 15, всё становится плохо — агенту сложно удержать всё в голове и приоритеты теряются. Фокусируйтесь на самых важных 5–10 правилах.

## Файл-скрипты для быстрой валидации

Вместо запуска полного билда на каждое изменение — настройте file-scoped команды:

```markdown
### Команды

# Type check одного файла
npm run tsc --noEmit path/to/file.tsx

# Format одного файла
npm run prettier --write path/to/file.tsx

# Lint одного файла
npm run eslint --fix path/to/file.tsx

# Unit-тесты одного файла
npm run vitest run path/to/file.test.tsx

# Полный билд — только когда явно попросили
yarn build:app

Note: всегда линтуй, типеконтрольь и тестируй изменённые файлы.
Полный билд — только явно по запросу.
```

## Safety и permissions

Явно определите, что агенту можно делать без спроса, а что требует подтверждения:

```markdown
### Safety и permissions

**Можно без спроса:**
- read files, list files
- tsc single file, prettier, eslint
- vitest single test

**Сначала спросить:**
- npm install
- git push
- удаление файлов
- запуск полного билда или e2e-тестов
```

## Иерархические Agents.md

Для больших репозиториев поддерживаются вложенные `AGENTS.md` / `CLAUDE.md` в поддиректориях. Агент автоматически находит файлы от текущей директории до корня:

```
my-project/
  AGENTS.md                  # всегда загружается
  src/
    AGENTS.md                # загружается для src/**
    components/
      AGENTS.md              # загружается для src/components/**
      Button.tsx
```

**Use cases:**
- framework-specific guidelines (React rules в `frontend/`, Node.js rules в `backend/`)
- модульные конвенции (API design patterns в `api/`)
- границы команд (разные команды поддерживают свои стандарты)

## PR checklist

```markdown
### PR checklist

- title: `feat(scope): short description`
- lint, type check, unit tests — всё зелёное перед коммитом
- diff small и focused, есть краткое описание что и почему изменилось
- убраны лишние логи и комментарии перед PR
```

## Когда агент не уверен

Дайте агенту выход:

```markdown
### Когда не уверен

- спроси уточняющий вопрос, предложи краткий план или открой draft PR с заметками
- не делай больших спекулятивных изменений без подтверждения
```

Это заменяет потенциально неправильные повороты на маленькие уточнения.

## Test-first mode

Для сложных фич:

```markdown
### Test first mode

- при добавлении новой функциональности: сначала тесты, потом код
- предпочитай component tests для UI state changes
- для регрессий: сначала failing test, потом fix
```

## Типичные ошибки

| Ошибка | Почему плохо | Что делать |
|---|---|---|
| "Пиши чистый код" | Слишком абстрактно | "Используй functional components с hooks" |
| Слишком много dos/donts (>15) | Теряется фокус | Топ-10 самых важных |
| Противоречивые правила | Агент не может определиться | Проверяйте консистентность |
| Файл не обновляется | Правила устаревают | Рефайн на каждом ретро |
| Очень длинный файл | Теряется в контексте | 100–150 строк, детали в референсах |

## Типичная структура

```markdown
# AGENTS.md — {название проекта}

## TL;DR (3-5 строк)
## Dos / Don'ts (до 10 пар)
## Как сделать X (пронумерованные шаги)
## Decision table: ...
## Примеры (конкретные файлы)
## Команды (file-scoped)
## Safety
## PR checklist
## Когда не уверен
```

## Инструменты

- [agentsmd.io](https://agentsmd.io) — генератор Agents.md, шаблоны, best practices
- [agents.md](https://agents.md) — открытый стандарт, поддерживается Cursor, Sourcegraph, Augment, OpenAI
- [Augment Guidelines](https://docs.augmentcode.com/setup-augment/guidelines) — иерархические правила, workspace-level и user-level guidelines

## Источники

- https://x.com/augmentcode/status/2047164534310494709
- https://docs.augmentcode.com/setup-augment/guidelines
- https://agentsmd.io/agents-md-best-practices
- https://agents.md