---
title: agent-aget
type: technology
created: 2026-05-28
last_updated: 2026-05-28
domain: tools
related: ["Agents.md", "MCPorter", "Antfarm", "GitNexus"]
sources: ["github-izzzzzi-agent-aget-2026-05-28"]
tags: ["tools", "cli", "agents", "automation", "workflow"]
---

# agent-aget

`agent-aget` — CLI-помощник для браузерных сценариев LLM-агентов. Он запускает управляемый stealth Chromium на базе CloakBrowser, хранит локальные браузерные сессии и возвращает машинно-читаемый JSON, чтобы terminal agents могли выполнять web workflow без отдельного GUI-оператора.

Внутри Wiki Chiki это практический tool-layer рядом с [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}) и [GitNexus]({{ '/wiki/tools/gitnexus' | relative_url }}): не «агент сам по себе», а повторяемый интерфейс к capability, которую агент может использовать в ходе работы.

## Что делает

`aget` закрывает базовые операции browser automation для агентного CLI:

- открыть URL и получить `sid` браузерной сессии;
- прочитать страницу как текст через `page read`;
- получить accessibility/snapshot refs вроде `@e1` и `@i1`;
- кликать, заполнять поля, нажимать клавиши и ждать текст;
- делать screenshots, scroll, `get` URL/text и выполнять batch-сценарии;
- закрывать сессии и диагностировать установку через `aget doctor`.

Ключевой момент — JSON-контракт. Операционные команды выводят один JSON-объект в stdout, а ошибки имеют структурированный вид с `ok:false`, `code`, `message` и `details`. Это снижает неоднозначность для LLM-агента: результат можно парсить, передавать между шагами и использовать как состояние workflow.

## Браузерный runtime

При установке через npm пакет скачивает native `aget` и пытается установить pinned CloakBrowser в пользовательский cache. CloakBrowser описан как stealth Chromium с source-level fingerprint patches и Playwright-like применением. Если сеть недоступна, установка пакета не падает: браузер можно поставить позже командами `aget browser install`, `aget browser status` и `aget browser path`.

Порядок выбора браузера устроен как fallback chain:

1. явный `--browser-path`;
2. переменная `AGET_BROWSER_PATH`;
3. managed CloakBrowser из cache;
4. legacy managed Chrome for Testing из cache;
5. системный Chrome/Chromium.

Такой порядок делает инструмент полезным и в локальной разработке, и на агентных хостах, где браузер может быть предустановлен или, наоборот, должен жить в изолированном cache.

## Как агент использует workflow

Типовой цикл выглядит так:

1. `aget open URL -n NAME` создаёт сессию и возвращает `sid`;
2. агент читает страницу через `aget page read -s SID --limit 80` или делает `page snapshot`;
3. действия выполняются через refs (`click`, `fill`, `press`) либо CSS-селекторы;
4. ожидания и проверки делаются командами `wait`, `get`, `scroll`, `screenshot`;
5. многошаговый сценарий можно отправить в `aget batch -s SID --stdin`;
6. после завершения агент закрывает сессию через `aget session close -s SID`.

Это хорошо сочетается с практиками из [Agents.md]({{ '/wiki/llm-agents/agents-md' | relative_url }}): вместо длинной неформальной инструкции агент получает короткий стабильный playbook и команды, которые возвращают предсказуемый формат.

## Отличие от MCP и встроенных browser tools

По смыслу `agent-aget` ближе к CLI-оператору, чем к MCP-серверу. [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}) помогает проверять MCP-интеграции, а `agent-aget` даёт агенту прямой terminal интерфейс к браузеру. Это удобно для сред, где агент уже умеет запускать shell-команды, но не имеет нативного browser tool или должен работать одинаково в Codex, Claude Code, OpenCode и других CLI.

От встроенного browser tool отличие в переносимости: `aget` можно описать в prompt, установить через npm и использовать как внешнюю capability. От Playwright-скриптов отличие в том, что команды уже упакованы как агентный UX: `prompt`, `agent-instructions`, snapshot refs, JSON help и batch-команды.

## Где уместен

`agent-aget` полезен для:

- web research, где нужно открыть страницы, читать текст и переходить по ссылкам;
- заполнения форм и UI-проверок в browser workflow;
- headless/headful проверки сайтов в агентных задачах;
- инструментальных пайплайнов, где браузерный шаг является частью более длинной цепочки;
- CLI-агентов, которым нужен общий браузерный протокол без привязки к конкретному агентному runtime.

Для долгих цепочек такой браузерный шаг можно рассматривать как task capability внутри [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) или похожего workflow-движка: `aget` выполняет конкретное действие в браузере, а orchestration layer хранит состояние процесса и решает, какой шаг запускать дальше.

## Ограничения и осторожность

Браузерная автоматизация остаётся чувствительной к состоянию страницы, fingerprinting, сессиям и приватным данным. Поэтому важно:

- не смешивать `sid` разных задач;
- не печатать в логи cookies, tokens и приватные данные из форм;
- закрывать сессии после работы;
- использовать screenshot только когда текстового чтения недостаточно;
- запускать `aget doctor`, если проблема похожа на runtime/browser failure, а не на ошибку сценария.

Stealth Chromium помогает с совместимостью сайтов, но не отменяет необходимость соблюдать правила сервисов и не превращает browser automation в универсальный обход ограничений.

## Практический вывод

`agent-aget` превращает браузер из «ручного окна» в воспроизводимый CLI-инструмент для LLM-агентов. Его ценность — в стабильном JSON-контракте, session id, snapshot refs и коротком наборе команд, которые можно вставить в agent prompt или использовать как часть более крупного workflow.

## Источники

- https://github.com/izzzzzi/agent-aget
- https://www.npmjs.com/package/agent-aget
- https://github.com/CloakHQ/CloakBrowser
