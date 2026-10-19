---
id: github-hordekiller-build-your-own-x-ru-2026-10-19
date: 2026-10-19
source_type: url
source_url: https://github.com/Hordekiller/build-your-own-x-ru
title: Build Your Own X — русский каталог
domain: tools
tags: ["tools", "knowledge-base", "self-hosted", "git"]
---

# Разбор источника

## Источник и границы

- Проверено 2026-10-19 по прямым first-party GitHub API/raw/codeload URL, без сторонней поисковой выдачи.
- Canonical URL: https://github.com/Hordekiller/build-your-own-x-ru
- Ветка `main`, SHA `405fedc956856069e661fd900abb8dab69fb9984`, дата commit `2026-08-18T03:42:39Z`.
- GitHub API: `fork: false`, `license: null`; releases endpoint вернул пустой список. Это отсутствие GitHub Releases на момент проверки, не отсутствие истории изменений.
- Скачан и извлечён архив точного SHA. Для статьи не сохранялась полная копия репозитория в Wiki: такого запроса не было.

## Извлечённые факты

README представляет BYOX как русскую версию каталога Build Your Own X с 359 материалами, 30 категориями и 41 языком. Список связан с `codecrafters-io/build-your-own-x`; автор поддерживает также английский и персидский сайты. Русские страницы — обзоры/переводы отдельных материалов со ссылками на оригиналы, не гарантированно полный перевод исходного курса.

Данные: `assets/js/tutorials-ru.js`, массив `window.TUTORIALS`; поля `id`, `category`, `lang`, `title`, `url`, `video`, `fa`, `done`, `file`. Метки языка составные: например, `C# / TypeScript / JavaScript`. Формулировка «41 язык программирования» не воспроизводит точно семантику подсчёта уникальных `lang`.

UI: нативный JS фильтрует по категории и ищет подстроку в `title + category + lang`. Русские заголовки из `ru_titles.json` этим поиском не используются. `done` отражает русскую страницу, а не прогресс учащегося. Отдельного backend, login, learner progress или общего тестирования учебных реализаций в проверенном дереве нет.

Примеры: `cstack-sqlite-c.html` — обзор SQLite-like базы с REPL/структурой записи и внешним оригиналом; `ai-llm-from-scratch.html` — введение в книгу/репозиторий Себастьяна Рашки с оглавлением и предпосылками. Эти наблюдения не являются аудитом качества всех переводов.

Развёртывание: статические HTML/CSS/JS; Pages workflow выполняет checkout, configure-pages, upload-pages-artifact и deploy-pages, без тестового gate. В HTML есть внешние Google Fonts. Локальный просмотр сайта не делает внешние уроки/видео доступными offline.

## Реально выполненные проверки

- JS-данные загружены через изолированный Node VM context (`window` без Node API); массив не является строгим JSON из-за допустимой в JS завершающей запятой.
- Записей: **359**, уникальных ID: **359**, категорий: **30**, уникальных строк `lang`: **41**.
- HTML-страниц уроков: **359**; отсутствующих страниц из индекса: **0**.
- `ru-done.json`: **359** записей; `ru_titles.json`: **359** ключей; оба набора ID совпали с индексом.
- Для каждой страницы проверены H1 и ссылка на URL оригинала, указанный в индексе: пропусков **0**.
- Внутренние `href` всех страниц уроков разрешены относительно файловой структуры: отсутствующих целей **0**. Это не проверка внешних URL или всех CSS/media references.
- `node --check` для `main.js` и `tutorials-ru.js`: passed.
- Четыре проверки `matches`: все записи без фильтра; категория БД — **13**; поиск Redis внутри неё даёт результат; несуществующий запрос даёт **0**. Passed, без браузерного DOM rendering.
- Временный loopback HTTP server: `index.html`, JS-индекс, LLM-страница и SQLite-страница вернули **200**; сервер остановлен после smoke-проверки.
- Размеры крупнейших категорий: веб-сервер **73**, языки программирования **41**, игры **34**, блокчейн **21**, ОС **19**, нейросети **17**, БД **13**.

## Расхождения и непроверенное

- README заявляет Python-генератор и audit `359/359`; в tree рассматриваемого SHA нет `.py` файлов. Наши проверки — независимые структурные проверки каталога, не воспроизведение отсутствующего авторского аудита.
- README заявляет MIT для собственного кода, но badge указывает на `LICENSE` в другом репозитории. В проверенном дереве отсутствуют LICENSE/LICENCE-файлы; GitHub не распознал лицензию. Права на исходные уроки остаются отдельным вопросом.
- Не выполнялись: массовая проверка внешних ссылок, сравнение переводов с каждым оригиналом, компиляция примеров, обучение моделей, браузерное E2E или визуальная проверка. Наличие всех страниц не доказывает корректность всего содержания.

## Ссылки evidence

- https://api.github.com/repos/Hordekiller/build-your-own-x-ru
- https://api.github.com/repos/Hordekiller/build-your-own-x-ru/commits/main
- https://api.github.com/repos/Hordekiller/build-your-own-x-ru/git/trees/405fedc956856069e661fd900abb8dab69fb9984?recursive=1
- https://api.github.com/repos/Hordekiller/build-your-own-x-ru/releases?per_page=3
- https://github.com/Hordekiller/build-your-own-x-ru/blob/405fedc956856069e661fd900abb8dab69fb9984/README.md
- https://github.com/Hordekiller/build-your-own-x-ru/blob/405fedc956856069e661fd900abb8dab69fb9984/assets/js/tutorials-ru.js
- https://github.com/Hordekiller/build-your-own-x-ru/blob/405fedc956856069e661fd900abb8dab69fb9984/assets/js/main.js
- https://github.com/Hordekiller/build-your-own-x-ru/blob/405fedc956856069e661fd900abb8dab69fb9984/.github/workflows/deploy-pages.yml
- https://github.com/Hordekiller/build-your-own-x-ru/blob/405fedc956856069e661fd900abb8dab69fb9984/tutorials-ru/cstack-sqlite-c.html
- https://github.com/Hordekiller/build-your-own-x-ru/blob/405fedc956856069e661fd900abb8dab69fb9984/tutorials-ru/ai-llm-from-scratch.html
