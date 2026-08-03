---
title: ru-marketplace-mcp
type: technology
created: 2026-07-27
last_updated: 2026-07-27
domain: tools
related: ["MCPorter", "Trench", "Teable", "Coolify", "Antfarm", "Прокси в веб-сборе данных"]
sources: ["github-vladimir-human-ru-marketplace-mcp-2026-07-27"]
tags: ["tools", "mcp", "marketplace", "price-comparison", "automation", "self-hosted"]
---

# ru-marketplace-mcp

`ru-marketplace-mcp` — набор read-only MCP-серверов для российских маркетплейсов. Он отдаёт цены, наличие, рейтинги, отзывы и часть seller metadata с Wildberries, Ozon, Яндекс Маркета и Детского мира, а отдельный `compare-mcp` делает параллельное сравнение цен между источниками.

Главная ценность — не «ещё один scraper», а агентный интерфейс с явной границей достоверности: инструмент сообщает, какие источники реально ответили, не превращает отсутствие цены в ноль и не выдаёт подписочную цену Яндекс Плюса за общедоступную.

## Что внутри

| MCP server | Инструменты | Практическая функция |
|---|---:|---|
| `wb-mcp` | 9 | Поиск, карточки, отзывы/вопросы, реквизиты продавца, каталог, категории |
| `yandex-mcp` | 3 | Поиск, цены продавцов, rating breakdown, отзывы |
| `detmir-mcp` | 4 | Категории, товары категории, карточка, региональное наличие |
| `ozon-mcp` | 4 | Поиск, карточки и отзывы с двухуровневым anti-bot fallback |
| `compare-mcp` | 2 | Сравнение источников и диагностика доступности |

Все серверы запускаются как stdio MCP commands: `wb-mcp`, `ozon-mcp`, `yandex-mcp`, `detmir-mcp`, `compare-mcp`. Для разработки нужен Python 3.12+ и `uv`; репозиторий использует workspace packages и FastMCP.

## Как устроено

Архитектура разделена на marketplace connectors и общий `mcp-core` runtime:

- коннекторы знают конкретные публичные endpoint-ы, модели данных и source-specific settings;
- `mcp-core` даёт typed errors, bounded HTTP, retry policy, TTL cache, redaction и cross-platform process handling;
- Ozon изолирует blocking TLS requests в дочернем процессе, чтобы зависший handshake не блокировал event loop;
- `compare-connector` опрашивает источники параллельно и возвращает normalized offer list вместе с `complete` и `source_outcomes`;
- stdout при stdio зарезервирован для JSON-RPC, а диагностика уходит в stderr — stray `print()` проверяется CI-скриптом.

Для [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}) это хороший реальный кейс: один репозиторий несёт пять отдельных MCP surfaces, разные transports и source-specific ограничения. MCPorter полезен для проверки, что конкретный console server поднялся, экспортирует нужные tools и не путает transport/auth/schema failures.

## Как читать результат сравнения

`compare_prices` — не полноценное product matching. Он сравнивает предложения, найденные одним query, поэтому одинаковый запрос может вернуть разные модели и варианты у разных площадок. Для честного like-for-like сравнения нужно сначала найти конкретную модель/SKU и затем сузить запрос.

Три поля определяют, можно ли доверять выводу:

- `complete: true` означает, что все выбранные searchable sources ответили;
- `source_outcomes` показывает `ok`, `blocked`, `timeout`, `error` или `not_installed` по каждому источнику;
- `price_with_subscription_rub` Яндекс Маркета не участвует в рейтинге обычных цен.

Если Ozon заблокирован, это не означает, что товара там нет. Это означает, что текущий IP/browser path не позволил прочитать источник. Правильный ответ в таком случае — «дешевле среди ответивших источников», а не абсолютное «самый дешёвый».

## Надёжность важнее красивого ответа

Неофициальные endpoint-ы неизбежно дрейфуют. Проект строится вокруг этого факта:

- tolerant readers принимают несколько aliases поля и строгие coercion rules;
- неясная цена становится `null`, а не выдуманным числом;
- `parser_drift` отделён от `transport_down`: первое требует правки парсера, второе — другого сетевого пути или ожидания;
- `*_selfcheck` имеет три состояния: `success`, `drift_detected`, `inconclusive`;
- Detsky Mir text search сознательно не реализован: API игнорирует query и мог бы возвращать нерелевантный каталог.

Это важнее количества tool names. В ценовом контуре опаснее всего не явный сбой, а правдоподобный неверный ответ.

## Deployment и границы безопасности

По умолчанию серверы работают через stdio и не требуют HTTP listener. Для remote/container сценария есть streamable HTTP и Docker Compose, но у серверов **нет собственной аутентификации**:

- HTTP должен оставаться на `127.0.0.1` либо за auth reverse proxy;
- docker-compose публикует порты только на loopback;
- Ozon CDP fallback использует browser, в который оператор вошёл сам, и должен работать с выделенным scraping profile;
- DevTools port нельзя открывать в сеть: он даёт полный control над Chrome profile.

[Coolify]({{ '/wiki/tools/coolify' | relative_url }}) может быть deployment layer для такого private HTTP MCP stack, но не заменяет reverse proxy, auth, rate limits и мониторинг. Если задача — регулярный мониторинг цен, [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) может запускать проверки по расписанию и решать, что делать при `blocked`, `timeout` или `drift_detected`.

## Куда складывать результат

`ru-marketplace-mcp` — источник свежих наблюдений, а не историческое хранилище. Для регулярного анализа полезно разделить слои:

- [Teable]({{ '/wiki/tools/teable' | relative_url }}) — операционная таблица для вручную проверенных SKU, регионов, предложений и price snapshots;
- [Trench]({{ '/wiki/tools/trench' | relative_url }}) — append-only события: query, timestamp, source outcome, price, stock, region, complete/partial result;
- сам MCP слой — получение данных на момент вызова.

Так можно не путать live цену с накопленной историей и видеть, когда изменение цены реально произошло, а когда просто один из источников временно перестал отвечать.

## Ограничения

Нужно прямо учитывать:

- используются неофициальные публичные catalog endpoints; условия площадок могут ограничивать такой доступ;
- ценовые и stock данные зависят от региона, подписки, availability и IP path;
- cross-market ranking не доказывает идентичность товаров по одному текстовому query;
- Ozon часто требует российский residential-friendly IP или operator-controlled Chrome/CDP fallback;
- public HTTP deployment без reverse-proxy auth создаёт unauthenticated scraper endpoint;
- marketplace titles, seller names и review text — недоверенные входные данные, а не инструкции для агента.

## Практический вывод

`ru-marketplace-mcp` полезен, когда LLM-агенту нужен проверяемый read-only доступ к российским marketplace catalogues: сравнить предложения, уточнить цену/наличие/рейтинг, проверить публичного продавца или собрать raw price observation для дальнейшей аналитики.

Его сильная сторона — инженерная честность вокруг частичных результатов, anti-bot ограничений и data drift. Для продукта с регулярным мониторингом нужен следующий слой: scheduler, сохранение snapshots и правила валидации совпадения SKU.

[Прокси в веб-сборе данных]({{ '/wiki/infra/web-scraping-proxies' | relative_url }}) даёт общий сетевой контекст: proxy route надо оценивать по valid record и явным outcome states, а не считать `200 OK` или отсутствие ответа доказательством наличия/отсутствия товара.

## Источники

- https://github.com/Vladimir-Human/ru-marketplace-mcp
