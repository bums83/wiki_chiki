---
title: Croc
type: technology
created: 2026-08-11
last_updated: 2026-08-11
domain: tools
related: ["cmux-ssh-here", "ASSH", "Cobalt"]
sources: ["telegram-becaps-1956-2026-08-11", "github-schollz-croc-2026-08-11"]
tags: ["tools", "cli", "open-source", "self-hosted"]
---

# Croc

`croc` — open-source Go CLI для передачи выбранных файлов, каталогов или короткого текста между двумя участниками. Отправитель запускает `croc send`, получает code phrase и передаёт её получателю; тот запускает `croc` с этой фразой. Обычный режим не требует регистрации и не создаёт постоянное файловое хранилище, но это **не** означает отсутствие сетевой инфраструктуры: оба клиента используют relay, если не могут соединиться локально.

Проверенная ветка `main` на момент ingest: `3878cca` от 2026-08-11, сразу после release `v11.0.3` от 2026-08-10. Само source version значение и собранный CLI показывают `11.0.3`. Поэтому описание относится к текущему checkout, который уже включает post-release fix `make serve`.

## Базовый сценарий

```bash
# На отправителе
croc send ./report.pdf ./assets/

# На получателе — code phrase из вывода отправителя
croc <code-phrase>
```

CLI умеет передавать несколько файлов, папки, stdin/stdout, короткий текст и QR-код для browser receive flow. Для явной фразы есть `croc send --code <phrase> <file>`, но на Linux/macOS source намеренно предлагает передавать секрет через `CROC_SECRET`, а не командную строку: иначе другие локальные пользователи могут увидеть его в process list. `--classic` возвращает старое удобное поведение, и сам CLI маркирует его insecure для multi-user host.

Code phrase — не «просто красивый ID». Source разделяет из неё room и PAKE secret, затем запускает password-authenticated key agreement и выводит ключи канала с identity/session/transcript binding. Транспорт шифруется; утечка полной фразы всё равно опасна: получивший её может попытаться присоединиться к передаче. Передавать код надо отдельным приватным каналом, а не в общем чате или логе CI.

## Relay, NAT и реальная топология

Telegram-пост верно передаёт пользу: croc снимает необходимость поднимать `sshd`, открывать входящий порт или создавать аккаунт в чужом файлообменнике. Но формулировку «пробивает NAT» лучше понимать точно.

| Слой | Что происходит |
|---|---|
| Normal live transfer | оба peer подключаются к relay; `send` в CLI прямо описан как отправка через relay |
| Local-only | `--local` требует только локальные соединения; `--no-local` отключает локальный relay discovery |
| Default relay | адрес задаётся флагами/env и по умолчанию резолвится из публичных croc relay hosts |
| Self-hosted relay | `croc relay` запускает собственный TCP relay; default диапазон — порты `9009–9013`, нужно минимум два |
| Proxy | доступны SOCKS5 и HTTP CONNECT options |

То есть это не обещание прямого device-to-device соединения в любой сети. Relay позволяет обоим участникам сделать исходящее соединение и переносит зашифрованный поток. Для частного контура можно назначить `--relay relay.example:9009`; у своего relay нужно задать отдельный пароль, ограничить сеть/firewall и не путать relay access control с защитой code phrase.

## Шифрование, целостность и возобновление

В проверенном source:

- peer channel опирается на PAKE v2, HKDF-SHA-256 и role-specific mutual confirmation; traffic key имеет 32 байта;
- `src/crypt` использует AEAD: AES-GCM для legacy/general helpers и XChaCha20-Poly1305 через Argon2-derived key там, где это требуется форматом;
- протокол передаёт file metadata и chunk ranges, а tests/docs содержат отдельный сценарий для reconnect после разрыва data/control socket;
- CLI поддерживает выбор hash algorithm и хранит progress/chunk state для resume.

Это сильнее, чем пересылка файла через случайный публичный upload endpoint, но не отменяет endpoint risk: заражённый sender/recipient, скомпрометированная машина, утекшая фраза и подмена уже до шифрования остаются вне защиты протокола. Не следует отключать confirmation prompts и включать `--overwrite` в автоматизации без явного контроля пути назначения.

## Отдельный режим `--store`

Normal transfer требует, чтобы sender и recipient были online. `croc send --store` — другой, opt-in режим для asynchronous передачи:

1. клиент локально шифрует files и загружает ciphertext в storage service;
2. выдаёт browser link и CLI token;
3. transfer истекает через 24 часа или после первой полностью проверенной загрузки;
4. sender может удалить неполученную передачу через локальный revoke receipt.

Ключ дешифрования в browser URL находится после `#`, поэтому не уходит на HTTP server и в стандартный proxy/access log. Но полный link/token — bearer secret: любой, кто его прочитает, может расшифровать и занять единственную загрузку. Storage видит connection metadata, timing, ciphertext sizes и quota-related totals; source прямо не обещает скрыть эти данные. Для приватной эксплуатации можно указать `--store-url` и поднять `croc-web --store-dir`, но понадобятся HTTPS reverse proxy, private persistent directory, quota/rate limits и исключение ciphertext из backups, иначе «удаление после download» будет фикцией.

## Browser и self-hosting

Репозиторий содержит отдельный `croc-web`: React/Vite UI + WebAssembly implementation протокола, упакованный в самостоятельный Go binary. Он совместим с обычными CLI peers, отдаёт UI, health check и allowlisted WebSocket-to-TCP bridge. `croc-web` по умолчанию bind-ится на `127.0.0.1:9014`; публичный deploy предполагает HTTPS reverse proxy.

Web client — не универсальная замена CLI. Upstream перечисляет границы: один peer/transfer за раз, отсутствие browser-to-browser direct mode, ограничения directory UX и невозможность resume stored download после закрытия вкладки. Для больших файлов и automation CLI остаётся предсказуемее.

## Проверка исходника

| Проверка в temporary clone | Результат |
|---|---|
| Revision / license | HEAD `3878cca`; root `LICENSE` — MIT; GitHub metadata также MIT |
| `go vet ./...` | passed |
| Static Linux CLI build | passed; собранный `/tmp/croc-verify --version` вывел `croc version 11.0.3` |
| `go test ./...` под Go `1.25.0` | **не прошёл полностью**: все пакеты кроме `src/models` passed; `TestRemoteLookupIPTimeout` ожидал ошибку от DNS `192.0.2.1`, но в этой сети lookup завершился успешно |
| Targeted retry | тот же тест падал 3/3 за `0.00–0.02 s`; это environment-dependent тестовое предположение, а не доказанный defect transfer protocol |

Официальный GitHub CI использует Go `^1.26`, запускает `go test -v ./...`, cross-platform static builds и отдельно собирает `croc-web` с Node 24. Локально не запускались browser Playwright suite, два реальных peer, public relay, self-hosted relay/storage или cross-platform binaries. Поэтому статья не выдаёт полную E2E верификацию за выполненную.

## С чем не путать

| Инструмент | Граница |
|---|---|
| [cmux-ssh-here]({{ '/wiki/tools/cmux-ssh-here' | relative_url }}) | создаёт временный LAN SSH endpoint для shell, `scp`/SFTP. Croc передаёт выбранный artifact без SSH server и не даёт remote shell. |
| [ASSH]({{ '/wiki/tools/assh' | relative_url }}) | обслуживает устойчивые SSH aliases, gateways и config. Для регулярного доступа к серверам `scp`/`rsync` поверх SSH часто лучше; Croc хорош для разового передачи между любыми двумя peers. |
| [Cobalt]({{ '/wiki/tools/cobalt' | relative_url }}) | Cobalt получает публичный media artifact по URL; Croc переносит уже выбранный локальный artifact между участниками. Ни один не заменяет другой. |

## Практический вывод

Croc — хороший инструмент для «передать файл человеку/другой машине сейчас» без подготовки SSH account, cloud drive или port forwarding. Его сильная сторона — простой handoff плюс криптографически связанная code phrase и возобновление передачи.

Для постоянного server-to-server data flow, прав доступа, аудита, многопользовательского storage или массового обмена это не замена SFTP/rsync/object storage. Для этого нужны отдельные identity, retention, monitoring и access-policy слои. А `--store` следует включать лишь когда действительно нужен asynchronous режим и понятны последствия bearer link, metadata и self-hosted storage.

## Источники

- [Telegram: Бэкап, сообщение 1956](https://t.me/becaps/1956)
- [schollz/croc](https://github.com/schollz/croc), [release v11.0.3](https://github.com/schollz/croc/releases/tag/v11.0.3)
- [README: usage, relay и browser](https://github.com/schollz/croc/blob/main/README.md)
- [stored transfers: protocol and operator guide](https://github.com/schollz/croc/blob/main/src/docs/STORED_TRANSFERS.md)
- [CI workflow](https://github.com/schollz/croc/blob/main/.github/workflows/ci.yml)
