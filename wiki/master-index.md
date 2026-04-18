# Wiki Chiki — Мастер-индекс

## Инфраструктура

### [Windows Shell]({{ '/wiki/infra/windows-shell' | relative_url }})
- **type:** technology
- **domain:** infra
- **summary:** Графическая оболочка Windows: компоненты, потребление ресурсов, альтернативы
- **also:** shell, explorer, панель задач

### [Оптимизация рабочего стола Windows]({{ '/wiki/infra/windows-desktop-optimization' | relative_url }})
- **type:** case-study
- **domain:** infra
- **summary:** Замена тяжёлых shell-компонентов Win10 на легковесные альтернативы — 70 МБ вместо 300+
- **also:** windows optimization, retrobar, модульный shell

### [Легаси-железо]({{ '/wiki/infra/legacy-hardware' | relative_url }})
- **type:** concept
- **domain:** infra
- **summary:** Стратегии продления жизни старого оборудования
- **also:** legacy hardware, старое железо

## Менеджмент

### [Кайдзен]({{ '/wiki/management/kaizen' | relative_url }})
- **type:** concept
- **domain:** management
- **summary:** Японская философия непрерывного совершенствования: малые улучшения, PDCA, genchi gembutsu
- **also:** kaizen, непрерывное улучшение, рацпредложение

### [Toyota Production System]({{ '/wiki/management/toyota-production-system' | relative_url }})
- **type:** technology
- **domain:** management
- **summary:** Производственная система Toyota: 9 принципов, JIT, SMED, Kanban
- **also:** TPS, TBP, Toyota, производственная система

### [Муда]({{ '/wiki/management/muda' | relative_url }})
- **type:** concept
- **domain:** management
- **summary:** Три вида потерь: муда (действия без ценности), мура (неравномерность), мури (перегрузка)
- **also:** muda, mura, muri, потери, waste, 7 потерь

### [Poka-yoke и Andon]({{ '/wiki/management/poka-yoke-andon' | relative_url }})
- **type:** technology
- **domain:** management
- **summary:** Защита от дурака (poka-yoke), система оповещения (andon), автоматизация (karakuri)
- **also:** poka-yoke, andon, karakuri, защита от ошибок, error-proofing

### [Метод 5 Why]({{ '/wiki/management/5-why' | relative_url }})
- **type:** practice
- **domain:** management
- **summary:** Техника поиска корневых причин через последовательные «почему?»
- **also:** 5 почему, five whys, root cause analysis, RCA

### [Диаграмма Исикавы]({{ '/wiki/management/ishikawa-diagram' | relative_url }})
- **type:** practice
- **domain:** management
- **summary:** Fishbone-диаграмма для визуализации причин проблемы, анализ 6M, сюхари
- **also:** Ishikawa, рыбьи кости, fishbone, 6M, сюхари, shuhari

### [Неогностицизм]({{ '/wiki/management/neognosticism' | relative_url }})
- **type:** essay-analysis
- **domain:** management
- **summary:** Конец 250-летнего договора «труд=ценность», AGI как готовая функция, инструменты цифровой дистилляции и парадокс добросовестности
- **also:** AGI, digital clone, colleague.skill, AI policy, future of work, civilization shift

### [Методология A3]({{ '/wiki/management/a3-methodology' | relative_url }})
- **type:** practice
- **domain:** management
- **summary:** Визуальный документ для принятия решений: структура из 8 блоков, альтернатива презентациям
- **also:** A3, Toyota A3, A3 report, P3.Express, 5S

## LLM и агенты

### [Autoresearch]({{ '/wiki/llm-agents/autoresearch' | relative_url }})
- **type:** technology
- **domain:** llm-agents
- **summary:** Минималистичный single-GPU framework Карпаты для автономных research-циклов, где человек программирует `program.md`, а агент меняет `train.py`
- **also:** autoresearch, nanochat, autonomous research, overnight experiments, karpathy

### [Research org code]({{ '/wiki/llm-agents/research-org-code' | relative_url }})
- **type:** concept
- **domain:** llm-agents
- **summary:** Подход, где человек проектирует исследовательскую организацию через prompt/policy layer, а агент исполняет search loop
- **also:** program.md, agentic research, prompt as policy, research organization

### [Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }})
- **type:** practice
- **domain:** llm-agents
- **summary:** Практика AI-assisted разработки, где человек управляет агентом через ограничения, контекст, этапы работы и критерии приёмки
- **also:** vibe coding, вайб-кодинг, prompt library, cursor prompts, agentic development

### [Nanochat]({{ '/wiki/llm-agents/nanochat' | relative_url }})
- **type:** technology
- **domain:** llm-agents
- **summary:** Минималистичный LLM training harness Карпаты: один dial сложности, speedrun до GPT-2, база для autoresearch
- **also:** nanochat, GPT-2 speedrun, CORE, llm harness

### [Validation bits per byte]({{ '/wiki/llm-agents/validation-bits-per-byte' | relative_url }})
- **type:** concept
- **domain:** llm-agents
- **summary:** Исследовательская метрика качества `val_bpb`, удобная для быстрых сравнений между токенизаторами и архитектурами
- **also:** val_bpb, bits per byte, validation metric, bpb

### [HyperFrames]({{ '/wiki/llm-agents/hyperframes' | relative_url }})
- **type:** technology
- **domain:** llm-agents
- **summary:** HTML-ориентированный video framework для AI-агентов, где сцены, анимации и тайминг описываются через HTML, CSS, JavaScript и data-атрибуты
- **also:** hyperframes, html video, agentic video, heygen, gsap video

### [Overnight experimentation]({{ '/wiki/llm-agents/overnight-experimentation' | relative_url }})
- **type:** practice
- **domain:** llm-agents
- **summary:** Режим, в котором агент прогоняет серию коротких экспериментов ночью, а человек утром получает журнал и лучшие изменения
- **also:** overnight loop, autonomous experiments, sleep while it runs

### [Asynchronous research swarms]({{ '/wiki/llm-agents/asynchronous-research-swarms' | relative_url }})
- **type:** concept
- **domain:** llm-agents
- **summary:** Следующий шаг после одиночного autoresearch: множество агентов асинхронно исследуют гипотезы параллельно
- **also:** agent swarms, parallel research, distributed research community
