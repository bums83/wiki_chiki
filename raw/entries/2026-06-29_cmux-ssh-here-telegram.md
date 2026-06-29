---
id: telegram-deksden-notes-909-cmux-ssh-here-2026-06-29
date: 2026-06-29
source_type: url
source_url: https://t.me/deksden_notes/909
title: cmux-ssh-here Telegram post + GitHub repository
domain: tools
tags: [tools, cli, automation, shell, ssh]
---

# cmux-ssh-here — Telegram post + GitHub repository

Primary source: https://t.me/deksden_notes/909

Telegram post text extracted from public `t.me` embed on 2026-06-29:

> cmux-ssh-here — шелл другого Mac по локалке, одной командой, установка - не нужна.
>
> Нужно зайти в терминал соседнего Mac в той же сети, но поднимать sshd ради пары команд - лень. Эта тулза делает всё за один запуск:
>
> `npx cmux-ssh-here`
>
> Поднимает одноразовый SSH-сервер с токен-авторизацией и печатает ссылку с QR + готовую команду ssh. Открываешь ссылку в cmux на другом Mac (или заходишь любым SSH-клиентом) - и ты в шелле. Нажал Ctrl-C - сервер и токен исчезли.
>
> - ноль настройки, никакого sshd
> - вход по одноразовому токену, без паролей и ключей
> - токен живёт 3 минуты, потом ротируется на новый
> - открывается в cmux (терминал для macOS); с телефона / Linux / Windows - любым SSH-клиентом
>
> GitHub: https://github.com/viktor-silakov/cmux-ssh-here
>
> Лицензия: MIT

GitHub source inspected: https://github.com/viktor-silakov/cmux-ssh-here

Durable repository facts observed on 2026-06-29:

- Package name: `cmux-ssh-here`
- Version in `package.json`: `0.7.6`
- Runtime: Node.js >= 18
- Language: JavaScript
- License: MIT
- Dependencies: `ssh2`, `node-pty`, `qrcode-terminal`
- Command: `npx cmux-ssh-here`
- Purpose: spin up a throwaway token-authenticated SSH server and print a cmux deep link, `ssh://` link and plain `ssh` command for LAN access.
- Token rotates every 3 minutes by default; configurable via `CMUX_SSH_TTL`.
- `--once` locks the link to the first device that connects.
- Host support: macOS and Linux; Windows host unsupported because it needs a POSIX shell and cmux remote daemon has no Windows build.
- Optional `tmux` support gives persistent/shared sessions.
- Security note: token in the link is a bearer secret that grants shell access as the current user; server binds to `0.0.0.0`, so it should be used only on trusted local networks.
