---
title: cmux-ssh-here
type: technology
created: 2026-06-29
last_updated: 2026-08-11
domain: tools
related: ["ASSH", "Coolify", "OculiX", "agent-aget", "Croc"]
sources: ["telegram-deksden-notes-909-cmux-ssh-here-2026-06-29"]
tags: ["tools", "cli", "automation", "shell", "ssh"]
---

# cmux-ssh-here

`cmux-ssh-here` — маленькая CLI-утилита для одноразового SSH-доступа к текущей машине по локальной сети. Она запускается одной командой:

```bash
npx cmux-ssh-here
```

После запуска инструмент поднимает временный SSH-сервер с token-auth, печатает `cmux` deep link, `ssh://` ссылку, QR-коды и обычную `ssh` команду. Когда процесс остановлен через `Ctrl-C`, временный сервер, token и host key исчезают.

## Что делает

Основная идея: быстро открыть shell на соседнем Mac/Linux host без постоянной настройки `sshd`, `authorized_keys`, паролей и ручной firewall/SSH-конфигурации.

Из README и Telegram-поста:

- запускает собственный SSH server на `ssh2`;
- генерирует ephemeral host key и одноразовый bearer token;
- печатает cmux deep link для macOS-приложения `cmux`;
- дополнительно печатает обычную `ssh` команду и `ssh://` ссылку для других SSH clients;
- token по умолчанию ротируется каждые 3 минуты;
- `--once` ограничивает доступ первым подключившимся клиентом;
- поддерживает full PTY shell, `scp`/`sftp` и exec channel;
- если установлен `tmux`, может сохранять и шарить сессии между reconnects.

## Чем отличается от обычного SSH

Обычный SSH предполагает заранее поднятый `sshd`, пользователей, ключи, firewall rules и поддержку долгоживущей конфигурации. `cmux-ssh-here` рассчитан на обратный сценарий: разовая локальная сессия, когда нужен быстрый временный доступ к shell без превращения машины в постоянно открытый SSH-host.

Это не замена нормальному SSH для серверов. Это disposable access pattern: запустил, дал ссылку/команду, сделал работу, остановил процесс.

## Связь с ASSH

С [ASSH]({{ '/wiki/tools/assh' | relative_url }}) связь прямая, но уровни разные.

- ASSH управляет устойчивой SSH-конфигурацией: aliases, gateway chains, templates, hooks и `~/.ssh/config`.
- `cmux-ssh-here` не управляет постоянной конфигурацией вообще; он создаёт временный SSH endpoint для локальной сети.

Практически: ASSH полезен для регулярного доступа к серверам, bastion routes и gateway-heavy инфраструктуре. `cmux-ssh-here` полезен для «дай мне shell на соседней машине на пару минут».

## Связь с self-hosted/deployment инструментами

С [Coolify]({{ '/wiki/tools/coolify' | relative_url }}) общий слой — SSH как operational transport. Но Coolify использует SSH для управления remote Docker hosts и деплоя приложений, а `cmux-ssh-here` создаёт одноразовый локальный SSH endpoint для человека или lightweight remote workflow.

С [OculiX]({{ '/wiki/tools/oculix' | relative_url }}) связь менее прямая: оба инструмента работают с доступом к чужой/удалённой машине, но OculiX автоматизирует GUI/remote sessions, а `cmux-ssh-here` даёт shell-level доступ.

С [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) сходство в CLI-first модели: capability упакована в простую команду, которую можно использовать вручную, в скрипте или как step внутри более крупного workflow.

## Где уместен

`cmux-ssh-here` подходит для:

- быстрого доступа к shell соседнего Mac/Linux в одной Wi-Fi/LAN сети;
- парного debugging или помощи коллеге в офисной сети;
- временного доступа с телефона через SSH client;
- ситуации, где поднимать постоянный `sshd` ради пары команд избыточно;
- локального troubleshooting, когда нужна одноразовая дверь, а не новый постоянный сервис.

[Croc]({{ '/wiki/tools/croc' | relative_url }}) закрывает соседнюю, но другую задачу: одноразово передать selected artifact code phrase-ом через encrypted relay, не создавая SSH endpoint. `cmux-ssh-here` лучше, когда нужен временный shell/`scp`/SFTP в доверенной LAN; Croc — когда нужен только file handoff между двумя peers, включая разные сети.

## Ограничения и безопасность

Главный риск: token в ссылке — bearer secret, который даёт shell под текущим пользователем. README прямо предупреждает: использовать только в доверенной локальной сети и не публиковать ссылку.

Особенно важно:

- сервер слушает `0.0.0.0`, то есть доступен всем в локальной сети;
- любой, кто получил актуальный token, может подключиться до истечения срока;
- token rotation снижает риск утечки, но не делает ссылку безопасной для публичных каналов;
- `--once` полезен, когда нужно ограничить доступ первым клиентом;
- Windows host не поддерживается; нужен macOS/Linux host и Node.js 18+.

## Практический вывод

`cmux-ssh-here` — хороший пример disposable operator tool: не строит инфраструктуру, не заменяет SSH inventory и не пытается быть PaaS. Он закрывает узкую боль: быстро и временно открыть shell на локальной машине без постоянной настройки SSH.

Его ценность именно в малом масштабе. Для серверной инфраструктуры лучше использовать нормальный SSH setup, [ASSH]({{ '/wiki/tools/assh' | relative_url }}) или deployment/control plane вроде [Coolify]({{ '/wiki/tools/coolify' | relative_url }}). Для разового LAN-доступа — это проще и чище.

## Источники

- https://t.me/deksden_notes/909
- https://github.com/viktor-silakov/cmux-ssh-here
- https://www.npmjs.com/package/cmux-ssh-here
