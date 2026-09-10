---
title: Invidious
type: technology
created: 2026-09-10
last_updated: 2026-09-10
domain: tools
related: ["Cobalt", "Coolify", "Прокси в веб-сборе данных"]
sources: ["github-iv-org-invidious-2026-09-10"]
tags: ["tools", "video", "self-hosted", "open-source", "docker", "api-platform"]
---

# Invidious

`Invidious` — open-source альтернативный web frontend и API для YouTube. Он даёт просмотр, поиск, каналы, подписки, плейлисты и JSON API без использования официальных YouTube API, по заявлению upstream. Это **не независимая видеоплатформа**: сервер всё равно получает метаданные и video streams через инфраструктуру YouTube; доступность зависит от внешней платформы, IP/region/rate limits и текущих механизмов YouTube.

Проект написан на Crystal, лицензирован под **AGPL-3.0-only** и распространяется как self-hosted сервис. Локальные Invidious-аккаунты могут хранить подписки и плейлисты без Google account, но это переносит доверие к оператору конкретного instance, а не устраняет его.

## Контур сервиса

| Слой | Наблюдаемая роль | Операционная граница |
|---|---|---|
| Invidious | Crystal/Kemal приложение, web UI и `/api/v1/*` | Нужны domain/reverse-proxy settings и случайный `hmac_key`; конфигурация читается из файла либо `INVIDIOUS_CONFIG`. |
| PostgreSQL | Основное stateful storage для users, subscriptions, playlists и кэшей | `db` или `database_url` обязательны; backup и restore остаются задачей оператора. |
| Invidious companion | Отдельный сервис для загрузки video streams с YouTube | Reviewed config предупреждает: без companion просмотр и playback не работают. Для связи нужен отдельный 16-символьный secret. |
| Reverse proxy | TLS, public routing и при необходимости direct companion path | При внешнем HTTPS upstream требует корректно выставить `https_only`, `domain` и `external_port`. |

В актуальной инструкции companion заменяет `inv-sig-helper` и `youtube-trusted-session-generator`. Это важнее, чем выглядит: обычный «поднять один frontend container» уже не описывает полный working playback path.

## Пользовательские функции и API

README перечисляет themes, subscriptions, notifications, audio-only mode, import/export данных из YouTube/NewPipe/FreeTube, embedded player и комментарии YouTube/Reddit. Это возможности проекта, не обещание, что каждая функция будет одинаково доступна у любого public instance.

Документация API фиксирует, например, `GET /api/v1/stats`, `/api/v1/videos/:id`, `/api/v1/search`, `/api/v1/captions/:id`, `/api/v1/comments/:id`, `/api/v1/trending` и endpoints для playlists/mixes. Ответ video endpoint включает metadata, форматы, captions и URLs streams. Поэтому публичный API — не безобидный read-only widget: он создаёт заметный upstream/bandwidth/abuse surface.

В `config.example.yml` есть `disable_abusable_api`: он отключает `/api/v1/videos`, `/api/v1/clips` и `/api/v1/transcripts`. Это полезный защитный предохранитель, но не полноценная authorization model. В reviewed configuration нет общего переключателя API-authentication; если API должен быть private, его следует закрывать на network/reverse-proxy уровне и добавлять rate/quota policy.

## Privacy: где заканчивается обещание

Upstream заявляет «no tracking» и Google-independent subscriptions. Технически это означает отсутствие обязательного Google account для локальной модели подписок; это **не** универсальная гарантия приватности.

- На public instance оператор является стороной, которой пользователь доверяет соединение, cookies, локальный account state и серверные журналы/политику хранения.
- В self-hosted deployment эту ответственность берёт владелец сервиса: минимизация logs, доступ к PostgreSQL, backup encryption, retention и уведомление пользователей не появляются автоматически из репозитория.
- Настройки `statistics_enabled` и `/api/v1/stats` могут раскрывать агрегированную информацию об instance; для public instance upstream просит включать statistics, чтобы status мог обновляться.
- Инструмент PII-redaction решает другую задачу: он не делает доверенным public Invidious instance и не заменяет сетевую/retention policy.

## Сеть, egress и публичный instance

По умолчанию config допускает `host_binding: 0.0.0.0`; пример development Compose при этом публикует приложение только на `127.0.0.1:3000`. Эти два факта не стоит смешивать: production exposure задаёт конкретный compose/reverse-proxy deployment.

Для outbound path доступны `force_resolve` (IPv4/IPv6) и HTTP/SOCKS5 proxy. Документация прямо отделяет этот proxy от video-stream path: для streams прокси настраивается у companion. Смена IP может помочь диагностировать rate-limit ситуацию, но не делает доступ гарантированным и не является основанием обходить ограничения платформы. Общие принципы легитимного egress и rate policy — в [Прокси в веб-сборе данных]({{ '/wiki/infra/web-scraping-proxies' | relative_url }}).

`disable_proxy`, `local` и companion `public_url` влияют на то, проходит ли stream через instance или приходит к пользователю напрямую. Проксирование video по умолчанию выключено; включение увеличивает bandwidth ответственность оператора. Для public deployment это расчёт трафика и abuse policy, а не переключатель «лучшей приватности».

## Развёртывание и эксплуатация

Официальный production path — Docker Compose с prebuilt образом на Quay, PostgreSQL и companion; репозиторий всё ещё нужно клонировать для SQL/init files. Документация не поддерживает PaaS/SaaS как штатный путь и называет сервис bandwidth-intensive proxy, который может вызвать проблемы или блокировку у провайдера.

Maintainer guidance задаёт минимум 20 GB disk и 2 GB free RAM для Invidious+companion, а для public instance — ориентир 60 GB, 4 GB RAM, 2 vCPU, 200 Mbps и 20 TB traffic. Это planning guidance upstream, не независимый benchmark. Отдельно upstream рекомендует регулярный restart: как минимум ежедневно, предпочтительно каждый час.

[Coolify]({{ '/wiki/tools/coolify' | relative_url }}) может быть control plane для private Compose deployment, но не отменяет PostgreSQL backup, secret management, reverse proxy, egress, bandwidth limits и monitoring. HMAC key, companion key, DB password и proxy credentials должны храниться вне Git как секреты; в примерах документации значения-заглушки намеренно не переносятся в рабочую конфигурацию.

## Версии и проверяемость

Проверенная sparse checkout ревизия `master`: `049d591d294e2a43cb32b97a0bb018c2093e5beb` (2026-09-04). `shard.yml` на ней содержит development version `2.20260804.1-dev`; последний GitHub release на момент проверки — `v2.20260804.1` от 2026-08-05, без release assets, с исправлением debug information OCI image.

CI запускает `crystal spec`, build по Crystal matrix и Docker build/run на AMD64/ARM64. На reviewed head были успешны Docker checks и stable Crystal 1.14–1.20, но **stable Crystal 1.21.0 failed**; nightly также failed и marked non-stable. Поэтому некорректно писать «CI полностью green». Local sparse checkout совпал с reviewed SHA, но Crystal toolchain отсутствовал; source build, tests, PostgreSQL migration, companion и playback локально не запускались.

Есть documentation drift: `shard.yml` допускает Crystal `>=1.10.0,<2.0.0`, CI включает 1.20/1.21, а manual-install page всё ещё перечисляет 1.14–1.19. Для deploy следует сверять конкретный image/release и текущие CI, а не брать одну старую таблицу как окончательную совместимость.

## Лицензия и границы использования

AGPL-3.0 предназначена для network service: при публичном предоставлении модифицированной версии пользователям требуется предоставить Corresponding Source модификаций (license section 13). Это факт лицензии, не юридическая консультация; для коммерческого или публичного deployment нужна собственная юридическая оценка.

README отдельно отказывается от ответственности за внешние instances и напоминает соблюдать применимые правила. Invidious не является разрешением на загрузку или распространение content, игнорирование условий платформы либо обход региональных/доступных ограничений.

## Сравнение с соседними tools

[Cobalt]({{ '/wiki/tools/cobalt' | relative_url }}) обрабатывает ссылки на свободно доступные public media и возвращает файл/redirect/tunnel; Invidious даёт interactive frontend/API поверх YouTube. Оба зависят от внешних platform paths и требуют ограничивать публичный abuse, но Cobalt не заменяет subscriptions/UI, а Invidious не является general media-downloader.

## Когда уместен

Подходит для private/team instance, когда нужны YouTube UI/API без обязательного Google account и есть готовность обслуживать stateful, bandwidth-sensitive сервис с внешней зависимостью от YouTube.

Не стоит выбирать его как гарантированный permanent access layer, как полностью anonymous service без доверия к оператору или как «одноконтейнерную» замену YouTube без database, companion, reverse proxy и operational policy.

## Источники

- [iv-org/invidious](https://github.com/iv-org/invidious)
- [README](https://github.com/iv-org/invidious/blob/master/README.md)
- [Configuration example](https://github.com/iv-org/invidious/blob/master/config/config.example.yml)
- [Configuration loader](https://github.com/iv-org/invidious/blob/master/src/invidious/config.cr)
- [CI workflow](https://github.com/iv-org/invidious/blob/master/.github/workflows/ci.yml)
- [Installation](https://docs.invidious.io/installation/)
- [API reference](https://docs.invidious.io/api/)
- [Release v2.20260804.1](https://github.com/iv-org/invidious/releases/tag/v2.20260804.1)
