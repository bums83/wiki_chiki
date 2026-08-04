---
title: Searcharvester
type: technology
created: 2026-08-04
last_updated: 2026-08-04
domain: tools
related: ["Research org code", "Academic Research Skills", "Antfarm", "Coolify"]
sources: ["github-vakovalskii-searcharvester-2026-08-04"]
tags: ["tools", "self-hosted", "web-search", "research", "api-platform"]
---

# Searcharvester

`Searcharvester` — self-hosted стек для поиска в вебе, извлечения основного текста страниц и запуска исследовательской задачи через Hermes Agent. Он объединяет SearXNG, Valkey, FastAPI-адаптер с частичной совместимостью с Tavily API, React/Vite UI и набор Hermes skills.

Главная ценность не в «ещё одном поиске», а в воспроизводимом внутреннем контуре: результаты можно искать, извлекать в Markdown, сохранять artifacts job и передавать агенту для исследовательского отчёта. Но это **не готовый публичный API и не безопасная sandbox-среда**. Текущий compose открывает сервисы наружу и не добавляет аутентификацию.

## Что есть в текущем репозитории

В `docker-compose.yaml` на рассмотренной ревизии определены четыре постоянно работающих сервиса:

| Слой | Роль |
|---|---|
| `searxng` + Valkey | Метапоиск по включённым поисковым движкам и служебный storage SearXNG. |
| `tavily-adapter` | FastAPI API: поиск, извлечение HTML в Markdown и research jobs. Внутри этого же контейнера запускается Hermes CLI. |
| `frontend` | React/Vite UI для работы с API и отображения jobs. |
| bind mounts/volumes | `config.yaml`, `jobs/`, `hermes-data/`, а также persistent data SearXNG и Valkey. |

Это важное уточнение к старой архитектурной схеме в репозитории. В текущем compose research-job **не поднимает отдельный Docker-контейнер** и не использует Docker socket proxy: адаптер создаёт `hermes acp` как subprocess и общается с ним по ACP JSON-RPC через stdin/stdout. Значит, агент выполняется в том же контейнерном и сетевом контексте, что и адаптер; отдельной изоляции для каждого research-запроса здесь нет.

## API: что реально делает

API близок к Tavily по форме запросов, но не эквивалентен Tavily по охвату или качеству данных.

| Endpoint | Реальное поведение | Практическая оговорка |
|---|---|---|
| `POST /search` | Отправляет запрос в SearXNG и нормализует ответ в Tavily-подобную структуру. При `include_raw_content` параллельно получает содержимое выдачи. | Поле `score` в коде синтетическое: `0.9 - 0.05 × позиция`. Это не relevance score поисковой системы и не метрика достоверности. |
| `POST /extract` | Загружает указанный HTML URL и извлекает основной текст через `trafilatura`; доступна нарезка длинного текста. | Cache хранится в памяти около 30 минут: после рестарта он исчезает. HTML-only: PDF, изображения и тяжёлые JS-приложения не являются гарантированным случаем. |
| `POST /research` | Возвращает `202` и создаёт job, который запускает Hermes ACP с bundled skills. | Результат — отчёт агента, не доказательство. Его ссылки и claims нужно проверять по первоисточникам. |
| `GET /research/{job_id}`, `/logs`, `/events`, `/snapshot` | Возвращают status/report, log, SSE-события и накопленные события job. `DELETE /research/{job_id}` отменяет job. | Эти routes раскрывают содержание запросов и artifacts любому, кто имеет доступ к API, если отдельно не поставлена auth-граница. |

`/research` ограничивает длину query до 2 000 символов. В compose для research выставлен timeout 1 200 секунд. Это предел ожидания процесса, а не гарантия качества, полноты или актуальности отчёта.

## Исследовательский контур

Поставляемый skill `searcharvester-deep-research` задаёт двухраундовую роль-модель:

1. lead декомпозирует вопрос;
2. 2–3 sub-agent исследуют разные под-вопросы и сохраняют extracts;
3. critic ищет контраргументы к конкретным утверждениям;
4. fact-checker проверяет числа, даты и имена;
5. lead собирает `report.md`.

Код дополнительно сверяет URL из sub-agent summary с файлами в `extracts/`, чтобы помечать ссылки без соответствующего извлечённого artifact как непроверенные. Это полезный guardrail против выдуманных URL, но не полноценная верификация содержания: файл extract доказывает факт чтения страницы, а не корректность интерпретации, датировку источника или надёжность самого сайта.

Поэтому Searcharvester — практическая реализация части идеи [Research org code]({{ '/wiki/llm-agents/research-org-code' | relative_url }}): procedure, роли и артефакты становятся кодом. В отличие от [Academic Research Skills]({{ '/wiki/llm-agents/academic-research-skills' | relative_url }}), он не добавляет человеческие gates для академической целостности, disclosure или финальной ответственности за цитаты.

## Безопасный deployment: обязательные границы

По текущему compose наружу публикуются SearXNG на `8999`, adapter на `8000` и UI на `9762`; adapter и SearXNG по умолчанию слушают все интерфейсы. CORS, даже если ограничен localhost, **не является аутентификацией**.

Перед использованием вне доверенной локальной сети нужны как минимум:

1. **Private network или reverse proxy с authentication.** Не публиковать adapter напрямую в интернет. API умеет принять URL для `/extract`, запускать agent job и отдавать логи/reports без встроенного user-level auth.
2. **Egress policy для adapter.** `/extract` выполняет HTTP-fetch адреса, переданных клиентом. Без ограничений это создаёт риск доступа к нежелательным внутренним адресам и расхода ресурсов. Фильтровать destinations на сетевом уровне и запрещать доступ к внутренним сетям/metadata endpoints.
3. **Rate limits, quotas и timeouts.** В `config.example.yaml` у SearXNG `limiter: false`; это приемлемо только для закрытого, ограниченного контура. Public endpoint без лимитов быстро станет abuse surface.
4. **Секреты и filesystem.** Заменить примерный `server.secret_key`; не хранить ключи модели в Git. `jobs/` и `hermes-data/` монтируются RW: там могут остаться запросы, extracts, отчёты, логи и конфигурация agent runtime. Нужны владельцы файлов, retention и резервное удаление.
5. **Явный Linux UID/GID.** Compose defaults ориентированы на UID/GID `501:20`; на Linux их следует задать под владельца bind mounts, иначе entrypoint будет пытаться менять ownership и можно получить нечитабельные artifacts.
6. **Pin images и проверять обновления.** Compose/Dockerfile используют `latest` для части образов. Плюс Dockerfile патчит внутренний файл Hermes для отключения streaming как workaround. Такой build зависит от конкретной структуры upstream image; обновление может сломать build или изменить поведение без review.

Для запуска private compose-инстанса можно использовать [Coolify]({{ '/wiki/tools/coolify' | relative_url }}) как deployment/control plane, но не как замену этим ограничениям: firewall, auth, secrets, image pinning, disk limits и backup/retention остаются ответственностью владельца.

## Наблюдаемость и устойчивость

Плюс проекта — job workspace оставляет `plan.md`, `notes.md`, `report.md`, `hermes.log` и events на host mount. Это делает разбор неудачного исследования возможным. Минус — API job registry живёт в процессе; artifacts на диске не превращают перезапуск сервиса в полноценное продолжение job с durable state.

Если research должен жить днями, зависеть от retry policy или входить в цепочку `collect → review → publish`, Searcharvester лучше использовать как один data/research step, а state и schedule держать в [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) или другом workflow engine.

## Documentation и licence: есть drift

Перед внедрением нельзя слепо копировать все инструкции из репозитория:

- русские `docs/ru/overview.md` и `docs/ru/api.md` описывают более старый, трёхсервисный контур и не покрывают текущий `/research`, frontend и event routes;
- README содержит схему с ephemeral Docker containers/socket proxy, тогда как актуальный compose и `orchestrator.py` используют subprocess `hermes acp` в одном adapter container;
- `/health` в коде сообщает `2.2.0`, а части README/image references отстают;
- README говорит «MIT on our code» и «AGPL on upstream SearXNG artifacts», однако root `LICENSE` репозитория — GNU AGPL v3. До письменного уточнения от maintainer безопасно считать публикацию и модификации всего дерева подчинёнными AGPL-3.0, а не полагаться на фразу в README для проприетарного использования.

Проверенная ревизия `main`: `5afa68b1a3f601fdb959940a383e3c7ee3f4d0cb` от 2026-04-27. Для неё были выполнены `docker compose config`, Python `compileall` и isolated test suite: **17 passed, 1 skipped**. Пропущенный E2E-тест намеренно требует реальный Docker stack, Hermes и model endpoint; он не был имитирован и не подтверждает production research quality.

## Когда выбирать

Подходит, если нужен собственный закрытый контур для:

- discovery URL через self-hosted SearXNG;
- извлечения readable HTML в Markdown;
- агентного exploratory research с видимыми artifacts и review;
- Tavily-подобной интеграции в внутренние tools без передачи каждого запроса в сторонний search API.

Не подходит, если требуется:

- публичный multi-tenant API без отдельного security-проекта;
- гарантированная полнота или авторитетность источников;
- изолированное выполнение недоверенных prompts/URL;
- durable orchestration и recovery долгих jobs из коробки;
- замена юридической оценки условий источников, robots policy или прав на данные.

## Источники

- [vakovalskii/searcharvester](https://github.com/vakovalskii/searcharvester)
- [README](https://github.com/vakovalskii/searcharvester/blob/main/README.md)
- [Docker Compose](https://github.com/vakovalskii/searcharvester/blob/main/docker-compose.yaml)
- [FastAPI adapter](https://github.com/vakovalskii/searcharvester/blob/main/simple_tavily_adapter/main.py)
- [Research orchestrator](https://github.com/vakovalskii/searcharvester/blob/main/simple_tavily_adapter/orchestrator.py)
- [Configuration example](https://github.com/vakovalskii/searcharvester/blob/main/config.example.yaml)
- [AGPL-3.0 LICENSE](https://github.com/vakovalskii/searcharvester/blob/main/LICENSE)
