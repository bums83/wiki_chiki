# Wiki Chiki

Это **knowledge map** по текущим областям wiki.

Не курс. Не каталог подряд. Не «что читать шаг 1, шаг 2».

Здесь важны три вещи:
- какие кластеры знаний уже есть,
- из каких статей они состоят,
- как эти кластеры связаны между собой.

Для полного перечня страниц есть [мастер-индекс](wiki/master-index.md).

## Карта верхнего уровня

Сейчас в wiki есть три основных кластера:

1. **Менеджмент и операционное управление**  
   Про улучшение процессов, поиск причин, устранение потерь, оформление решений.

2. **LLM и агентный research**  
   Про training harnesses, автономные циклы экспериментов, метрики и организацию research через агентов.

3. **Инфраструктура и ресурсная эффективность**  
   Про легаси, стоимость системной оболочки, оптимизацию рабочего окружения под слабые ресурсы.

## Кластер 1. Менеджмент и операционное управление

### Внутренняя структура кластера

**Системный каркас**
- [Toyota Production System](wiki/management/toyota-production-system.md)
- [Кайдзен](wiki/management/kaizen.md)
- [Муда](wiki/management/muda.md)

**Разбор причин**
- [Метод 5 Why](wiki/management/5-why.md)
- [Диаграмма Исикавы](wiki/management/ishikawa-diagram.md)

**Внедрение и контроль качества процесса**
- [Poka-yoke и Andon](wiki/management/poka-yoke-andon.md)
- [Методология A3](wiki/management/a3-methodology.md)

### Логика кластера

Это самый собранный раздел wiki.

Его внутренняя схема уже читается так:
- [Toyota Production System](wiki/management/toyota-production-system.md) задаёт рамку системы,
- [Кайдзен](wiki/management/kaizen.md) задаёт режим постоянного улучшения,
- [Муда](wiki/management/muda.md) показывает, что именно надо убирать,
- [Метод 5 Why](wiki/management/5-why.md) и [Диаграмма Исикавы](wiki/management/ishikawa-diagram.md) дают инструменты анализа,
- [Poka-yoke и Andon](wiki/management/poka-yoke-andon.md) и [Методология A3](wiki/management/a3-methodology.md) переводят анализ в устойчивое изменение процесса.

## Кластер 2. LLM и агентный research

### Внутренняя структура кластера

**Базовая лаборатория**
- [Nanochat](wiki/llm-agents/nanochat.md)
- [Autoresearch](wiki/llm-agents/autoresearch.md)

**Метрика и режим экспериментов**
- [Validation bits per byte](wiki/llm-agents/validation-bits-per-byte.md)
- [Overnight experimentation](wiki/llm-agents/overnight-experimentation.md)

**Организация research-системы**
- [Research org code](wiki/llm-agents/research-org-code.md)
- [Asynchronous research swarms](wiki/llm-agents/asynchronous-research-swarms.md)

### Логика кластера

Это уже не набор ссылок про Карпаты, а связанный кусок карты:
- [Nanochat](wiki/llm-agents/nanochat.md) даёт минимальную экспериментальную среду,
- [Autoresearch](wiki/llm-agents/autoresearch.md) превращает её в автономный цикл поиска улучшений,
- [Validation bits per byte](wiki/llm-agents/validation-bits-per-byte.md) даёт локальную метрику сравнения,
- [Overnight experimentation](wiki/llm-agents/overnight-experimentation.md) описывает operational pattern,
- [Research org code](wiki/llm-agents/research-org-code.md) поднимает уровень абстракции до проектирования самой исследовательской организации,
- [Asynchronous research swarms](wiki/llm-agents/asynchronous-research-swarms.md) показывает, как этот подход масштабируется из одного loop в распределённую систему.

## Кластер 3. Инфраструктура и ресурсная эффективность

### Внутренняя структура кластера

**Ограничения среды**
- [Легаси-железо](wiki/infra/legacy-hardware.md)

**Цена системной оболочки**
- [Windows Shell](wiki/infra/windows-shell.md)

**Практическая оптимизация**
- [Оптимизация рабочего стола Windows](wiki/infra/windows-desktop-optimization.md)

### Логика кластера

Это пока самый маленький кластер, но он уже имеет форму:
- [Легаси-железо](wiki/infra/legacy-hardware.md) задаёт контекст ограничений,
- [Windows Shell](wiki/infra/windows-shell.md) объясняет, где именно сидит стоимость среды,
- [Оптимизация рабочего стола Windows](wiki/infra/windows-desktop-optimization.md) показывает прикладной способ сократить этот overhead.

Пока это локальный подкластер про ресурсную дисциплину, а не полная карта инфраструктуры.

## Связи между кластерами

Ниже не просто соседство тем, а **смысловые мосты** между областями.

### 1. Менеджмент ↔ LLM и агентный research

Это сейчас самая сильная межкластерная связь во всей wiki.

**Непрерывное улучшение**
- [Кайдзен](wiki/management/kaizen.md) и [Autoresearch](wiki/llm-agents/autoresearch.md) описывают один и тот же паттерн на разных уровнях.
- В одном случае улучшается производственный или управленческий процесс.
- В другом случае улучшается training loop.
- Общая идея: не разовый «гениальный ход», а поток маленьких проверяемых улучшений.

**Поиск потерь**
- [Муда](wiki/management/muda.md) из management-кластера естественно связывается с [Overnight experimentation](wiki/llm-agents/overnight-experimentation.md) и [Validation bits per byte](wiki/llm-agents/validation-bits-per-byte.md).
- В agentic research потери, по сути, принимают форму бесполезных прогонов, шумных гипотез, плохих метрик и лишнего compute.

**Разбор причин**
- [Метод 5 Why](wiki/management/5-why.md) и [Диаграмма Исикавы](wiki/management/ishikawa-diagram.md) концептуально связаны с [Research org code](wiki/llm-agents/research-org-code.md).
- Если research-loop деградирует, нужен не просто новый запуск, а разбор: проблема в данных, метрике, организационном policy layer, search space или execution discipline.

**Защита от ошибок и сигнализация**
- [Poka-yoke и Andon](wiki/management/poka-yoke-andon.md) хорошо ложатся на agentic tooling.
- Guardrails, лимиты, sandboxing, review gates и сигналы деградации, по сути, являются современными аналогами poka-yoke и andon для агентных систем.

**Оформление решений**
- [Методология A3](wiki/management/a3-methodology.md) связана с [Research org code](wiki/llm-agents/research-org-code.md) как способ вынести логику решения наружу.
- A3 делает это для управленческой задачи.
- Research org code делает это для исследовательской организации.

### 2. Инфраструктура ↔ LLM и агентный research

Эта связь слабее, но уже реальна.

**Ограниченный ресурс как дизайн-фактор**
- [Легаси-железо](wiki/infra/legacy-hardware.md) и [Nanochat](wiki/llm-agents/nanochat.md) встречаются в одной точке: вычислительный бюджет ограничен, значит система должна быть спроектирована экономно.
- В одном случае это старое железо и слабая машина.
- В другом случае это ограниченный GPU budget и необходимость выжимать максимум из коротких циклов.

**Цена среды выполнения**
- [Windows Shell](wiki/infra/windows-shell.md) и [Nanochat](wiki/llm-agents/nanochat.md) концептуально связаны через вопрос overhead.
- В одном случае overhead сидит в UI-обвязке и системной оболочке.
- В другом, в training stack, runtime и неэффективной конфигурации.
- Общий вопрос один: сколько ресурса уходит не на полезную работу, а на обслуживание среды.

**Практика оптимизации**
- [Оптимизация рабочего стола Windows](wiki/infra/windows-desktop-optimization.md) и [Overnight experimentation](wiki/llm-agents/overnight-experimentation.md) связаны как две формы прагматичной оптимизации.
- Не «идеальная архитектура с нуля», а последовательное улучшение реальной рабочей системы под жёсткие ограничения.

### 3. Менеджмент ↔ Инфраструктура

Эта связь сейчас скрыта в статьях, но её полезно сделать явной.

**Устранение потерь в технической среде**
- [Муда](wiki/management/muda.md) напрямую читается через [Windows Shell](wiki/infra/windows-shell.md) и [Оптимизация рабочего стола Windows](wiki/infra/windows-desktop-optimization.md).
- Тяжёлая оболочка, лишние компоненты, неиспользуемые слои UI и лишнее потребление памяти, это техническая форма потерь.

**Кайдзен как режим эксплуатации**
- [Кайдзен](wiki/management/kaizen.md) связан с [Легаси-железо](wiki/infra/legacy-hardware.md) и [Оптимизация рабочего стола Windows](wiki/infra/windows-desktop-optimization.md) через маленькие практические улучшения среды вместо дорогой тотальной замены всего.

**Документирование изменений**
- [Методология A3](wiki/management/a3-methodology.md) естественно применима к инфраструктурным кейсам, когда нужно зафиксировать: проблема, ограничения, варианты, выбранное решение и эффект.

## Что это значит для всей wiki

Сейчас карта читается так:

- **Менеджмент** даёт язык улучшений, диагностики и организационной дисциплины.
- **LLM/агенты** показывают, как эти же принципы начинают работать в research-системах.
- **Инфраструктура** даёт материальный слой ограничений, стоимости среды и прикладной оптимизации.

То есть кластеры не изолированы.

Они сходятся в трёх общих темах:
- **непрерывное улучшение**,
- **работа в условиях ограничений**,
- **снижение потерь и overhead**.

## Слабые места карты

Пока не хватает нескольких важных мостов:
- между инфраструктурой и наблюдаемостью,
- между management и ServiceDesk/ITSM,
- между LLM/агентами и MCP/tooling/evals,
- между инфраструктурой и автоматизацией эксплуатации.

Когда эти области появятся, карта станет не просто набором кластеров, а уже нормальной рабочей онтологией.

## Справка

- [Полный мастер-индекс](wiki/master-index.md)

---

Как пополнять wiki: пришли URL, текст или файл. Я встрою материал в нужный кластер, обновлю связи и, если потребуется, перестрою всю карту знаний.