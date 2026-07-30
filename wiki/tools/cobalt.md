---
title: Cobalt
type: technology
created: 2026-07-30
last_updated: 2026-07-30
domain: tools
related: ["Coolify", "OpenScreen", "Video Summary"]
sources: ["github-imputnet-cobalt-2026-07-30"]
tags: ["tools", "video", "self-hosted", "open-source", "docker", "api-platform"]
---

# Cobalt

`Cobalt` — self-hosted media downloader для ссылок на свободно доступный публичный контент. Пользователь передаёт URL, а система возвращает прямую ссылку, временный tunnel или набор объектов для выбора. Это не медиатека и не публичный API-as-a-service: исходный проект строится вокруг собственной processing instance и короткоживущей обработки файла.

Репозиторий охватывает API, статичный web-клиент и Docker-развёртывание. Проверенный source tree содержит API `11.7.1` и web `11.7`; набор сервисов и форматов следует сверять с конкретным release, потому что он меняется.

## Что умеет

`api/README.md` на проверенном commit перечисляет 21 площадку, включая YouTube, VK, RuTube, TikTok, Instagram, Reddit, SoundCloud, Twitch Clips и X/Twitter. Поддержка разная: где-то доступны video+audio, audio-only, metadata и rich filename, а где-то — лишь часть вариантов. Например, YouTube заявлен с роликами, music и Shorts, несколькими codec/container вариантами, 8K/4K/HDR/VR/high-FPS, metadata и dubs; это не означает, что каждый ролик или регион всегда отдаст нужный вариант.

Главный endpoint — `POST /`; обязательны JSON `Accept` и `Content-Type`. Тело содержит URL и необязательные параметры:

| Группа | Примеры |
|---|---|
| Media | `downloadMode`: `auto` / `audio` / `mute`; audio format/bitrate; target video quality |
| YouTube | codec `h264` / `av1` / `vp9`, `mp4` / `webm` / `mkv`, subtitle/dub language, better audio, HLS option |
| Output | filename style, отключение metadata, GIF conversion, TikTok original audio |
| Processing | `alwaysProxy`, `localProcessing`: `disabled` / `preferred` / `forced` |

Ответы имеют явную семантику:

- `redirect` — клиент получает URL origin-сервиса;
- `tunnel` — Cobalt проксирует и при необходимости remux/transcode файл;
- `local-processing` — клиент получает tunnel URLs и должен сделать merge/remux/audio/GIF операцию локально;
- `picker` — в публикации несколько фото/видео/GIF для выбора;
- `error` — машинный code и контекст ошибки.

## Как устроен processing layer

API написан на Node/Express. Сервисные модули распознают и нормализуют допустимые source URL, Zod schema запрещает лишние поля, а обработчик выбирает redirect, proxy tunnel, server-side FFmpeg или локальную работу клиента.

Tunnel — не постоянный storage. При создании Cobalt генерирует ID, expiry, signature, secret и IV; данные stream об origin URL, заголовках, параметрах файла и request IP шифруются и кладутся в краткоживущий store. По умолчанию это память процесса. При `API_REDIS_URL` используется Redis; для нескольких API-инстансов Redis необходим, иначе они не смогут разделить tunnel state.

Это совпадает с заявленной моделью «fancy proxy»: проект не обещает хранить пользовательский контент. Но оператор всё равно обрабатывает ссылки, временные tunnel tokens, IP-derived rate-limit keys и, при включении, cookies — поэтому privacy/security не исчезают.

## Self-hosting: сильные и слабые места

Официальный путь — Docker Compose с `ghcr.io/imputnet/cobalt:11`, `API_URL` и, при публичном доступе, reverse proxy. API по умолчанию слушает `0.0.0.0`; CORS wildcard включён по умолчанию. Rate limits — только базовый контроль нагрузки, не полноценная авторизация.

| Механизм | Назначение |
|---|---|
| Turnstile + JWT | выдаёт короткоживущий Bearer после challenge |
| API keys | доступ для известных клиентов; можно ограничить IP/CIDR, user-agent, rate limit и services |
| `API_AUTH_REQUIRED=1` | запрещает запросы без key или session auth |
| `DISABLED_SERVICES` | отключает ненужные платформы |
| duration/tunnel/request limits | ограничивают расход CPU, bandwidth и abuse surface |

[Coolify]({{ '/wiki/tools/coolify' | relative_url }}) может быть удобным deployment layer для private Cobalt instance, но не заменяет эту конфигурацию. Важно держать ключи, JWT/Turnstile secrets и `cookies.json` вне Git, закрыть API reverse proxy/auth policy и не оставлять сервис открытым лишь потому, что в нём уже есть rate limiter.

API для сторонних проектов не предоставляется публично: docs предлагают развернуть свой instance или получить явное разрешение владельца другого. Hosted endpoints защищаются от бот-использования и не предназначены как общая зависимость приложений.

## Лицензии и допустимое использование

Лицензирование неоднородно:

- API и основная часть репозитория — **AGPL-3.0**: публичное предоставление модифицированного сервиса влечёт обязанности AGPL по исходникам модификаций;
- frontend — **CC-BY-NC-SA-4.0**, то есть с non-commercial и share-alike ограничениями;
- branding, mascot и связанные визуальные активы отдельно copyrighted: для форка их надо заменить или убрать.

Авторы прямо ограничивают назначение Cobalt свободно доступным публичным контентом и перекладывают ответственность за загрузку, использование и распространение на пользователя. Это не отменяет прав правообладателей, правил платформ и локального законодательства. Auth cookies допустимы только там, где они нужны для просмотра публичного контента, а не как основание для обхода приватности или ограничений сервиса.

## Cobalt рядом с media-инструментами

[OpenScreen]({{ '/wiki/tools/openscreen' | relative_url }}) и Cobalt не дублируют друг друга. OpenScreen записывает и редактирует собственный экранный demo; Cobalt сохраняет уже опубликованный публичный медиа-объект. Один производит оригинальный evidence/demo artifact, другой получает доступный исходный artifact.

[Video Summary]({{ '/wiki/llm-agents/video-summary' | relative_url }}) идёт в другую сторону: превращает текст, URL или PDF в короткий объясняющий MP4. Cobalt может дать локальный видеофайл для отдельного шага транскрибации или извлечения фрагментов, но текущий Video Summary напрямую принимает не video input, а текстовый источник и готовый JSON-сценарий. Связка требует явного промежуточного шага, а не магического «скачай и суммируй».

## Ограничения

- Поддержка сервисов внешняя и хрупкая: rate limits, регион, формат публикации и изменения платформ могут ломать загрузку.
- End-to-end тесты проекта сами обращаются к живым сервисам; они не дают стабильной offline-гарантии.
- `API_URL` должен быть корректным, иначе tunnel URLs не работают.
- Документы о защите говорят о совместимости с Cobalt 10, тогда как inspected package metadata сообщает API 11.7.1/web 11.7. Перед публичным запуском security config нужно проверить на конкретном image version.
- Root README заявляет отсутствие trackers для cobalt.tools, но self-hosted web содержит optional `WEB_PLAUSIBLE_HOST`; analytics у собственного deploy определяет оператор.

## Практический вывод

Cobalt полезен как self-hosted сервис получения публичных media files с прозрачным API-контрактом, client-side/server-side processing и контролем того, где проходят файлы. Его сильная сторона — не «скачивать всё», а отделять redirect, short-lived tunnel и local processing, не превращая себя в persistent media storage.

Разворачивать его стоит как частный сервис с ограничениями доступа. Без reverse proxy, rate limits, Turnstile/API keys и аккуратного обращения с cookies публичный Cobalt станет не удобством, а чужой bandwidth/CPU проблемой.

## Источники

- https://github.com/imputnet/cobalt
- https://github.com/imputnet/cobalt/blob/main/api/README.md
- https://github.com/imputnet/cobalt/blob/main/docs/api.md
- https://github.com/imputnet/cobalt/blob/main/docs/run-an-instance.md
- https://github.com/imputnet/cobalt/blob/main/docs/protect-an-instance.md
