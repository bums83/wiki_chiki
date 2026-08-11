---
id: mobbin-public-pages-2026-08-11
title: "Mobbin — публичные страницы продукта, тарифа, MCP и Terms"
source_type: url
source_url: https://mobbin.com/
canonical_url: https://mobbin.com/
retrieved_at: 2026-08-11
language: en
status: reviewed
related_article: "Mobbin"
---

# Mobbin — source review

## Граница источника

Проверены только публично доступные first-party pages: главная, pricing, MCP landing page, changelog, Terms of Service и Acceptable Use Policy. Account не создавался; защищённая библиотека, screen download, реальный MCP tool list, OAuth session и платные вызовы не запускались. Скриншоты, видео, flows и иные защищённые библиотечные материалы не сохранялись.

## Наблюдаемые сведения о продукте

- Главная описывает Mobbin как curated library mobile/web product interfaces; на snapshot отображались 1 428 apps, 621 500+ screens и 323 900 flows. Это vendor-supplied, изменяемые показатели, не независимый подсчёт.
- Публичный интерфейс заявляет поиск по screens, UI elements, flows и тексту в screenshots; flows могут быть доступны в video/prototype режиме.
- Changelog от 2026-08-05 описывает full-text search across screens/flows/sections и Deep Search; он также говорит, что same ordering applies to Chat and API. Это release note, а не независимая проверка качества/полноты поиска.
- Pricing snapshot: Free — latest four apps/sites и ограниченные search/flows/animations; Pro — $10/mo billed yearly; Team — $16/member/mo billed yearly. Цена и набор возможностей могут измениться.

## MCP/API

- MCP landing page приводит пример remote HTTP registration: `claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp`.
- Тот же page говорит "No API key", но следующим шагом требует browser authorization и вход в Mobbin; это означает отсутствие статического ключа в конфиге, а не отсутствие аутентификации.
- Лэндинг обозначает MCP как доступный на paid plans. Terms (§4.3) говорят, что API/MCP calls расходуют AI Credits и различают standard/basic и advanced/AI-enhanced calls; публичные страницы не дают стабильного tool/schema/quota contract.

## Лицензионные и операционные ограничения

Terms effective 2026-05-16 запрещают обходить auth/rate limits, copy/derivative/reverse-engineering материалов, mirror/cache/archive/re-host без express written consent и неавторизованные scraper/robot/bot/spider/crawler средства. Отдельно запрещено использовать content для train/test/index/benchmark/improve generative AI/LLM/ML без явно разрешённого случая.

Для API/MCP указаны personal/internal business use; запрещены resale/sublicense/lease, конкурентный продукт и standalone content repository из полученных материалов. Terms признают, что интерфейсные материалы могут содержать copyright/trademark IP third parties и называют их reference-only; Mobbin не гарантирует полноту/accuracy, включая AI outputs.

Pricing page заявляет платным планам screen downloads, но это не отменяет broad Terms restrictions. Публичных документов недостаточно, чтобы выводить право на публичное распространение, массовое хранение или обучение модели.

## Интеграционное решение

- Создана статья `wiki/tools/mobbin.md`: закрытая design-reference library, а не UI editor, open dataset или free asset source.
- Semantic neighbours: `UI/UX Pro Max` (локальные эвристики vs внешние референсы), `Penpot` (утверждённый design source of truth) и `MCPorter` (операционная проверка remote MCP).
- Source snapshot и protected-content archive не создавались: пользователь не просил копию, а Terms ограничивают массовое копирование/архивирование.

## Источники

- <https://mobbin.com/>
- <https://mobbin.com/pricing>
- <https://mobbin.com/mcp>
- <https://mobbin.com/changelog>
- <https://mobbin.com/terms>
- <https://mobbin.com/acceptable-use>
