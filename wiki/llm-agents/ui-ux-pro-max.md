---
title: UI/UX Pro Max
type: technology
created: 2026-08-01
last_updated: 2026-08-11
domain: llm-agents
related: ["Agents.md", "Вайб-кодинг", "Penpot", "Prompt Master", "Mobbin"]
sources: ["github-nextlevelbuilder-ui-ux-pro-max-skill-2026-08-01"]
tags: ["agents", "design", "workflow", "prompt-engineering", "vibe-coding"]
---

# UI/UX Pro Max

`UI/UX Pro Max` — не визуальный редактор и не модель, которая «сама делает хороший дизайн». Это cross-platform skill suite для coding-агентов: локальная база UI/UX-эвристик, Python-поиск по ней и инструкция, как превращать результат в дизайн-систему, а затем в код. Репозиторий упаковывает эти материалы для Claude Code, Codex, Cursor, Copilot и других agentic IDE.

Практический смысл простой: вместо общего промпта «сделай красивый dashboard» агент сначала получает структурированную подборку паттернов, палитр, типографики, UX-ограничений, motion-советов и stack-specific правил. Это полезный *вход в инженерный дизайн-процесс*, но не замена бренду, исследованию пользователей, макетам и проверке готового интерфейса.

Проверенный commit `14ddef5` соответствует release `v2.12.0` от 1 августа 2026 года.

## Что здесь реально работает

| Слой | Что делает | Чего не делает |
|---|---|---|
| Skill-инструкция | Подсказывает агенту, когда анализировать требования, запускать локальный поиск и фиксировать design system | Не знает фактов о конкретном продукте без контекста команды |
| Python engine | Ищет по CSV через BM25, выбирает рекомендации и строит текст/JSON design system | Не вызывает LLM, не ходит в сеть, не рендерит интерфейс |
| Данные | Хранят паттерны, цвета, типографику, UX, charts, motion и правила для стеков | Не являются доказательством, что конкретный совет подходит бизнесу или пользователю |
| CLI `uipro` | Генерирует skill-файлы для выбранной agent platform и кладёт bundled assets | Не делает безопасный merge локальных кастомизаций автоматически |

Ядро в `src/ui-ux-pro-max/` использует только Python standard library. В нём нет cloud API key, модели или фонового web search. Это означает воспроизводимость и offline-режим, но также жёсткую границу качества: ответ ограничен данными и эвристиками, записанными авторами репозитория.

## Из чего состоит база

На проверенном source tree валидатор нашёл 35 runtime CSV-файлов. Несколько ключевых наборов выглядят так:

| Набор | Строк данных |
|---|---:|
| UI styles | 84 |
| Color palettes | 192 |
| Typography pairs | 74 |
| Product categories | 192 |
| UX guidelines | 99 |
| UI reasoning rules | 161 |
| Chart recommendations | 25 |
| Motion recipes | 16 |
| Icon recommendations | 105 |
| Stack-specific files | 22 |

Это справочник с поиском, а не обученная экспертная система. Набор правил может подсказать «data-dense dashboard», контрастную палитру, типографическую иерархию, допустимый motion или a11y fallback для chart, но не понимает экономику продукта, юридические ограничения, текущий brand book и результаты UX-исследований.

## Рабочий поток

### 1. Получить design system

Основной сценарий — локальный вызов:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py \
  "saas analytics dashboard" \
  --design-system \
  --variance 8 --motion 7 --density 8 \
  --json
```

Результат включает product pattern, style, colors, typography, spacing scale, key effects, anti-patterns и decision rules. У трёх «dials» диапазон `1–10`:

| Параметр | Что меняет |
|---|---|
| `--variance` | от более центрированного/minimal к смелому/asymmetric стилю |
| `--motion` | от спокойных микроинтеракций до сложных GSAP-сценариев |
| `--density` | от просторной маркетинговой компоновки до плотного dashboard layout |

Skill template утверждает, что сначала выполняются пять «параллельных» поисков. В текущем `design_system.py` это обычный последовательный `for` по `product`, `style`, `color`, `landing`, `typography`. Правильнее считать это multi-domain lookup, а не реальной concurrent-обработкой.

### 2. Дополнить конкретным доменом или стеком

```bash
# UX и accessibility
python3 skills/ui-ux-pro-max/scripts/search.py \
  "keyboard contrast loading" --domain ux

# Правила для стека
python3 skills/ui-ux-pro-max/scripts/search.py \
  "performance suspense cache" --stack nextjs
```

Поддерживаются отдельные домены для style, color, typography, chart, UX, landing, motion/GSAP, React performance, mobile app interface, icons и Google Fonts. Stack-guides покрывают 22 стека: от React/Next/Vue/Svelte до Flutter, SwiftUI, Jetpack Compose, Angular, Laravel и desktop UI frameworks.

### 3. Зафиксировать, но не потерять решения

`--persist` создаёт `design-system/<project-slug>/MASTER.md`; `--page` добавляет override в `pages/`. Без `--force` существующий master не переписывается. Это полезный pattern для многосессионной работы агента: сначала читается глобальный master, затем — override конкретной страницы.

Но это файловое изменение в репозитории. `--output-dir` нужно задавать явно на корень проекта, а `--force` использовать только после diff/review. Иначе удобный генератор design token-советов становится ещё одним неконтролируемым источником дрейфа.

## Установка и границы CLI

`uipro init --ai <platform>` по умолчанию создаёт файлы из bundled templates. Например, для Codex конфигурация указывает путь `.agents/skills/ui-ux-pro-max/SKILL.md`; для Claude Code — `.claude/skills/ui-ux-pro-max/SKILL.md`.

Это не устанавливает одну инструкцию. Актуальный CLI добавляет orchestrator `ui-ux-pro-max` и шесть sibling skills: `banner-design`, `brand`, `design`, `design-system`, `slides`, `ui-styling`. То есть scope заметно шире названия репозитория.

| Режим | Поведение |
|---|---|
| `uipro init` | По умолчанию template-based install из assets пакета |
| `--offline` | Compatibility flag: стандартный template install и так не зависит от сети |
| `--legacy` | Может получить release с GitHub; при ошибке берёт bundled assets |
| `--global` | Пишет в home directory, а не в текущий проект |
| `--force` | Перезаписывает существующий generated skill и assets; требует предварительного review |

Не стоит запускать global install «на всякий случай». Сначала нужен обычный project-local install в test repo, затем diff установленного `SKILL.md`, data и scripts. Для команды с собственными design rules её repo context должен стоять выше imported defaults.

## Где он полезен

- быстро зафиксировать начальную дизайн-гипотезу для нового продукта;
- дать coding-агенту конкретный vocabulary вместо «сделай современно»;
- получить checklist по a11y, motion, responsive layout и charts;
- держать design decisions в versioned `MASTER.md`, а не в разрозненных чатах;
- добавить stack-level reminders до реализации компонента.

[Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }}) описывает дисциплину постановки и приёмки задач агенту. UI/UX Pro Max может стать её design-слоем: сначала получить явно проверяемую спецификацию, затем реализовать маленькими шагами и проверить в реальном приложении.

[Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}) объясняет, почему imported skill нельзя считать конституцией репозитория. UI/UX Pro Max — переносимый baseline; `AGENTS.md`/`CLAUDE.md`, дизайн-токены продукта и реальные component examples должны иметь приоритет.

## Где он ломается

1. **Нельзя принимать рекомендации за дизайн-решение.** Правило «dark dashboard» или готовая палитра — гипотеза. Её всё ещё нужно проверить против brand, контраста, content density, локализации, данных и реальных задач пользователя.
2. **Нет оценки готового UI.** Core не открывает браузер, не сравнивает screenshot с макетом, не измеряет WCAG и не проверяет поведение на устройстве. Нужны отдельные lint/a11y/visual regression и ручной review.
3. **Данные и метаданные меняются несинхронно.** На release `v2.12.0` plugin metadata остаётся `2.11.0`, а platform templates рекламируют старые размеры датасета (например 67 styles/161 palettes), тогда как inspected runtime data содержит 84/192. Перед rollout следует пиновать release и проверять фактически установленный набор.
4. **Премиальный branding не подтверждён качеством.** В репозитории есть широкий набор sibling skills, но их наличие не доказывает, что они подходят продукту или что у них одинаковая лицензия/поддержка. Проверять надо каждый поставляемый артефакт.
5. **Есть риск «дизайн-театра».** Много токенов, рекомендаций и motion-snippets могут сделать результат визуально сложнее без улучшения понятности. Особенно опасно это для dashboards и workflow-интерфейсов.

[Penpot]({{ '/wiki/tools/penpot' | relative_url }}) решает другую задачу: это визуальная среда, где команда хранит реальные экраны, компоненты и handoff. Skill может помочь сформулировать начальный system brief, но Penpot или другой design source of truth должен удерживать утверждённые решения.

[Mobbin]({{ '/wiki/tools/mobbin' | relative_url }}) может добавить к локальным эвристикам реальные shipped references: не «сгенерируй красивый checkout», а «сопоставь механики checkout в нескольких существующих продуктах». Но это закрытая, account-bound библиотека с запретом на построение копий, dataset и ML-training из контента; агент должен сохранять собственные выводы и ссылки, а не выкачивать изображения в проект.

[Prompt Master]({{ '/wiki/llm-agents/prompt-master' | relative_url }}) работает на уровне формулировки instruction. UI/UX Pro Max добавляет локальные данные и search path после этой формулировки. Ни один из них сам по себе не заменяет проверку интерфейса в браузере.

## Проверка источника

На commit `14ddef5c05e52d7c253b8f0129de7bcd1045ae5b` были реально запущены dependency-free проверки:

- `scripts/validate-csv.py` — **35/35** runtime CSV валидны;
- `scripts/smoke-domains.sh` — **12/12** domains вернули результаты;
- `scripts/smoke-stacks.sh` — **22/22** stacks вернули результаты;
- `python3 -m unittest discover -s src/ui-ux-pro-max/scripts/tests -v` — **36 tests passed**;
- `--design-system --json` smoke test вернул полный contract без persistence;
- `npm --prefix cli run check:assets` — assets синхронизированы.

Не запускались Node CLI build и Playwright e2e, и tool не устанавливался в пользовательский проект. Это проверка source logic и bundled data, а не доказательство, что generated UI будет качественным или что installer безопасно сольётся с любым существующим репозиторием.

## Практический вывод

`UI/UX Pro Max` полезен как локальный, воспроизводимый *design-recommendation layer* для coding-агента. Его надо использовать для ускорения design brief и фиксирования решений, а не как генератор «правильного UI».

Сильный сценарий: product constraints и существующая design system → scoped local search → `MASTER.md` в Git → реализация компонента → a11y/visual/device review. Если пропустить последние два шага, получится аккуратно сгенерированная документация, а не проверенный интерфейс.

## Источники

- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Release v2.12.0](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases/tag/v2.12.0)
- [Core skill source](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/src/ui-ux-pro-max)
- [CLI source](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/cli)
