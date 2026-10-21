---
id: remade-wiki-explore-2026-10-21
date: 2026-10-21
source_type: url
source_url: https://remade.wiki/explore/
title: Remade — каталог независимых реализаций ПО
domain: tools
tags: ["tools", "knowledge-base", "research", "design"]
---

# Source review: Remade

## Scope и происхождение

Запрос — добавить обзор https://remade.wiki/explore/ в Wiki Chiki. Полная выгрузка/зеркало базы и проверка всех программ не запрашивались. Проверено 2026-10-21: прямые HTTP-запросы к Explore/About/Disclaimer, двум карточкам и официальному JSON; first-party GitHub API/raw для `replicraft/remade`.

Reviewed repository revision: `2c61c92847ace6947a91c8713c82c8e67c836b06`, commit date `2026-10-20T12:58:21Z`. Прочитаны README, POLICY, CONTRIBUTING, LICENSE, docs/CATALOG.md, schemas.ts и root package.json. README после transient URLError успешно получен повторно; отдельный frontend package.json не получен из-за SSL timeout, его содержимое не восстанавливалось догадками.

Исследовательский профиль вызван для evidence report, но завершился `RESEARCHER_ROUTING_ERROR: timed out after 300s`, exit 124. Его отсутствующий отчёт не использовался. Review основан на прямо полученных первоисточниках.

## Извлечённые факты

- Каталог независимых reimplementations, отдельных supporting tools, originals, suites и project requests. Сайт ссылается на внешние проекты, не сопровождает и не сертифицирует их.
- Current policy ориентирована преимущественно на closed-source originals; open-source-target exceptions и broader alternatives требуют maintainer approval. Fork/port самого оригинала и оболочка над его движком не являются обычной независимой reimplementation; supporting tools имеют отдельную категорию допуска.
- Explore содержит category/language/platform/status/compatibility controls и сортировку Recently added/Alphabetical/GitHub stars. Все записи присутствуют в HTML; фильтрация/сортировка/indexed search требуют JS. Браузерные действия не выполнялись.
- Шкалы: planned/experimental/alpha/beta/stable/archived и targeting/partial/high/claimed-complete. Compatibility не оценивается каталогом, claimed-complete не сертифицировано; status self-reported, кроме наблюдаемого GitHub archive flag.
- Карточка BeamCraft описывает planned scaffolding, прямо предупреждает об отсутствии usable application. PhotoCraft на странице имеет Alpha, Partial (claimed), ограничения typography/AI/pro workflows/plugin compatibility. Это заявления карточек, не наш тест программ.
- Данные — YAML в `apps/frontend/remade-wiki/src/content/catalog/`; Valibot strict schemas и проверки связей в source. Readable exports build-generated; `schemaVersion: 1` у проверенного catalog.json. Документирован также requests.json, отдельно не получен.
- Root package.json: pnpm `12.10.1`, Node `>=22.12.0`, команды делегируют frontend app. Локальные install/build/test не выполнялись; это не мешает обзору публичного каталога, но не подтверждает его reproducible build.

## Проверки структуры

Публичные HTML и JSON сохранены во временном source-review workspace и разобраны Python-кодом:

- Projects: **123**; tools: **13**; unique Explore entry URLs: **136**.
- Уникальность slug внутри originals/projects/tools/suites и непересечение slug projects/tools: passed.
- project.originals ссылаются на существующие originals: passed.
- tool.projects и suite.projects ссылаются на существующие projects: passed.
- Featured ссылается только на известные projects/tools: passed.
- Набор уникальных `/projects/<slug>/` и `/tools/<slug>/` в Explore совпал с JSON: passed.

SHA-256 сохранённых ответов:
- Explore HTML: `c58e69358ca631ae7373cb5c711ec805a7d7e55b23e6c41c5cb327dd85d282e1`.
- catalog.json: `cbfbbbf9a86416e72289d59a35f056c68e547c211c792c87f227553020bb401e`.

Это проверка состава индекса и ссылочной целостности export, не correctness/security/compatibility тест приложений. Числа датированы и не обещают постоянного размера каталога.

## Лицензии, policy drift и непроверенное

- Root LICENSE — MIT, copyright 2026 replicraft. Она не перелицензирует third-party projects.
- README описывает open-source directory, однако POLICY допускает approved `Unlicensed`, а в export запись AgeSkeleton явно source-available, not OSI open source, с собственной ограничительной лицензией. Обобщение «все проекты свободные» неверно.
- CONTRIBUTING говорит об отсутствии votes/assignment в Requests, тогда как POLICY уже допускает reversible signed-in upvotes/“I'm building this”. Поэтому конкретная runtime-семантика запросов не выводилась из одного CONTRIBUTING; auth/counters не проверялись.
- Disclaimer не сертифицирует clean-room methodology и не даёт blanket legality. Условия лицензирования, безопасность и происхождение кода каждого приложения требуют отдельного review.
- Отдельные Terms/Privacy страницы не исследовались; отсутствие таких страниц или отсутствие tracking не заявляется. Регистрация, отправка предложений/PR и внешние социальные действия не выполнялись.

## Источники

- https://remade.wiki/explore/
- https://remade.wiki/about/
- https://remade.wiki/disclaimer/
- https://remade.wiki/data/catalog.json
- https://remade.wiki/projects/beamcraft/
- https://remade.wiki/projects/photocraft/
- https://github.com/replicraft/remade/tree/2c61c92847ace6947a91c8713c82c8e67c836b06
- https://github.com/replicraft/remade/blob/2c61c92847ace6947a91c8713c82c8e67c836b06/POLICY.md
- https://github.com/replicraft/remade/blob/2c61c92847ace6947a91c8713c82c8e67c836b06/CONTRIBUTING.md
- https://github.com/replicraft/remade/blob/2c61c92847ace6947a91c8713c82c8e67c836b06/docs/CATALOG.md
- https://github.com/replicraft/remade/blob/2c61c92847ace6947a91c8713c82c8e67c836b06/apps/frontend/remade-wiki/src/lib/schemas.ts
- https://github.com/replicraft/remade/blob/2c61c92847ace6947a91c8713c82c8e67c836b06/LICENSE
