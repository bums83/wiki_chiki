---
id: github-iv-org-invidious-2026-09-10
date: 2026-09-10
source_type: url
source_url: https://github.com/iv-org/invidious
title: Invidious — альтернативный frontend и API для YouTube
domain: tools
tags: ["tools", "video", "self-hosted", "open-source", "docker", "api-platform"]
---

# Source review: iv-org/invidious

## Граница источника

- Canonical source: https://github.com/iv-org/invidious
- Default branch: `master`.
- Reviewed revision: `049d591d294e2a43cb32b97a0bb018c2093e5beb`, commit date `2026-09-04T20:46:52Z`.
- Доступ проверен: 2026-09-10.
- Последний release на момент проверки: `v2.20260804.1`, опубликован 2026-08-05; GitHub API показывает zero attached assets. В `shard.yml` master имеет development version `2.20260804.1-dev`.
- Лицензия: `AGPL-3.0-only`; текст LICENSE содержит network-interaction obligation section 13.

## Наблюдаемые факты

1. README называет Invidious open-source alternative frontend to YouTube; заявляет no official YouTube APIs, локальные subscriptions без Google и developer API.
2. `shard.yml`: Crystal project, target `src/invidious.cr`, требования `>= 1.10.0, < 2.0.0`; среди зависимостей Kemal, PostgreSQL и SQLite drivers.
3. `config/config.example.yml` и `src/invidious/config.cr`: требуются `db` либо `database_url` и non-empty `hmac_key`; config можно передать через file/`INVIDIOUS_CONFIG_FILE` или YAML `INVIDIOUS_CONFIG`.
4. Config описывает отдельный `invidious_companion` для получения video streams с YouTube. При пустом списке исходный код печатает warning, что companion required to view/playback; при включённом companion ключ обязателен и должен быть длиной 16 символов.
5. Inbound default в source — `host_binding: 0.0.0.0`, port `3000`; reverse proxy требует согласованных `https_only`, `domain` и `external_port`. Config содержит HTTP/SOCKS5 outbound proxy, но явно исключает video-stream path: proxy для него настраивается у companion.
6. В config есть `disable_abusable_api` для `/api/v1/videos`, `/api/v1/clips`, `/api/v1/transcripts`; общего API-auth setting в reviewed config не найдено.
7. API docs описывают versioned endpoints для stats, video metadata/formats, search, captions, comments, trending, playlists и др.
8. Production docs требуют Compose/Quay image, PostgreSQL и companion, называют PaaS/SaaS unsupported and risky для bandwidth-intensive technical proxy; дают planning guidance и рекомендуют регулярный restart.
9. `Makefile` предоставляет `test` (`crystal spec`) и `verify` compile without binary. CI запускает Crystal matrix, tests/build, Docker build/run AMD64/ARM64; lint is `continue-on-error: true`.

## CI и локальная проверка

- GitHub check-runs для reviewed head: Docker AMD64/ARM64 success; stable Crystal 1.14–1.20 success; stable Crystal 1.21.0 failure; nightly failure marked non-stable. Нельзя описывать current CI как полностью зелёный.
- Выполнен shallow sparse checkout в `/tmp/invidious-review`; `git rev-parse HEAD` совпал с reviewed SHA.
- Локальный `crystal` отсутствует. Docker Compose V2 доступен, но compose/build/run не запускались: это затронуло бы внешние зависимости, PostgreSQL и YouTube-dependent workflow. Локальные source tests, migration, companion и playback не подтверждены.
- `SECURITY.md` по raw GitHub URL вернул HTTP 404; отдельная repository security policy в рассматриваемом tree не зафиксирована.

## Ограничения интерпретации

- «No tracking» — README claim о проекте, не аудит public instances. Оператор instance определяет network/log/retention policy и является доверенной стороной для локальных accounts/cookies/state.
- Работа UI/API не делает Invidious независимым от YouTube: config/docs прямо показывают upstream data/video-stream dependency. Доступность может меняться из-за платформы, региона, IP и limits.
- Документация Crystal версий расходится: manual installation перечисляет 1.14–1.19, CI уже включает 1.20/1.21, а manifest шире. Текущий image/release и CI следует проверять перед deploy.
- Исследовательский профиль был вызван с тем же scope, но превысил timeout 600 секунд; его отсутствующий отчёт не использовался. Этот review основан на прямых first-party GitHub/docs/API sources.

## Использованные источники

- https://github.com/iv-org/invidious
- https://raw.githubusercontent.com/iv-org/invidious/master/README.md
- https://raw.githubusercontent.com/iv-org/invidious/master/shard.yml
- https://raw.githubusercontent.com/iv-org/invidious/master/config/config.example.yml
- https://raw.githubusercontent.com/iv-org/invidious/master/src/invidious/config.cr
- https://raw.githubusercontent.com/iv-org/invidious/master/.github/workflows/ci.yml
- https://docs.invidious.io/installation/
- https://docs.invidious.io/api/
- https://github.com/iv-org/invidious/releases/tag/v2.20260804.1
