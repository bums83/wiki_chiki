---
title: ASSH
type: technology
created: 2026-06-19
last_updated: 2026-06-19
domain: tools
related: ["MCPorter", "Antfarm", "OculiX", "agent-aget"]
sources: ["github-moul-assh-2026-06-19"]
tags: ["tools", "cli", "automation", "shell", "linux"]
---

# ASSH

`assh` — Go CLI для управления расширенной SSH-конфигурацией. Он генерирует и обслуживает `~/.ssh/config`, добавляя поверх обычного OpenSSH удобные YAML-правила, алиасы, gateway chains, templates, inheritance, hooks, Graphviz и JSON-вывод.

Практически это не замена SSH, а слой конфигурации и проксирования над ним. `assh` использует `ProxyCommand`, поэтому остаётся совместимым с привычными инструментами: `ssh`, `scp`, `rsync`, `git` и приложениями, которые опираются на SSH/libssh.

## Что делает

Главная задача `assh` — превратить разрастающийся SSH config из ручного файла в управляемую модель. Вместо длинных блоков `Host`, вложенных `ProxyCommand` и копипасты пользователь описывает правила в `~/.ssh/assh.yml`.

Ключевые возможности:

- алиасы для коротких имён хостов;
- regex / wildcard matching для групп хостов;
- gateway chains и fallback-маршруты;
- includes для разбиения конфигурации по файлам;
- templates и inheritance для повторного использования SSH-опций;
- environment variable expansion;
- dynamic hostname через `ResolveCommand`;
- rate limiting;
- JSON output и Graphviz-граф хостов;
- hooks на события подключения и записи config.

По классу инструмента ASSH ближе к [MCPorter]({{ '/wiki/tools/mcporter' | relative_url }}): оба не являются агентами, а дают операторский CLI-слой вокруг сложной интеграции. MCPorter делает это для MCP-серверов, ASSH — для SSH-конфигурации, gateway routes и control sockets.

## Gateway chains

Самая заметная функция — упрощение SSH-доступа через промежуточные машины. Вместо ручного вложенного `ProxyCommand` можно использовать короткую форму:

```bash
ssh hosta/hostb
ssh hosta/hostb/hostc
```

Это означает: подключиться к `hosta` через `hostb`, либо через цепочку `hostc → hostb → hosta`. В YAML можно задать несколько gateways, включая `direct` как первый вариант и fallback через bastion/gateway, если прямой доступ невозможен.

Для инфраструктуры это полезно там, где доступ зависит от сети: офис/VPN/внешняя сеть, jump hosts, bastion hosts, временные firewall-ограничения. Вместо нескольких разных команд пользователь получает один стабильный host alias.

## YAML-модель конфигурации

Базовая структура `~/.ssh/assh.yml` состоит из:

- `hosts` — именованные хосты и паттерны;
- `templates` — reusable блоки настроек, к которым нельзя подключаться напрямую;
- `defaults` — общие SSH-опции;
- `includes` — дополнительные YAML-файлы;
- `ASSHBinaryPath` — явный путь к бинарнику при необходимости.

ASSH затем строит итоговый `~/.ssh/config`. README прямо предупреждает: так как инструмент управляет этим файлом, перед внедрением нужно держать backup. Это не безобидная read-only утилита; она меняет слой, от которого зависят Git, rsync, deploy-скрипты и интерактивные SSH-сессии.

## Hooks и события

ASSH поддерживает hooks на события:

- `BeforeConnect`;
- `OnConnect`;
- `OnConnectError`;
- `OnDisconnect`;
- `BeforeConfigWrite`;
- `AfterConfigWrite`.

Драйверы hooks:

- `exec` — выполнить shell-команду через Go templates;
- `write` — вывести строку в stdout/stderr;
- `notify` — desktop notification, где платформа поддерживается.

Это позволяет добавлять журналирование, уведомления, backup перед rewrite, постобработку сгенерированного config и статистику соединений. Для длинных операционных цепочек такой SSH-слой может быть step capability внутри [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) или похожего workflow engine: orchestration хранит состояние процесса, ASSH стабилизирует удалённый доступ.

## Команды

В README и коде видны основные команды:

```bash
assh config build      # сгенерировать ~/.ssh/config
assh config list       # показать хосты и опции
assh config graphviz   # вывести Graphviz-граф хостов
assh config search KEY # искать по host config
assh info              # системная информация и статистика
assh sockets list      # активные control sockets
assh sockets flush     # закрыть control sockets
assh sockets master    # создать master control socket
assh ping HOST         # TCP/SSH ping до хоста
```

Graphviz особенно полезен при gateway-heavy конфигурациях: вместо чтения длинного YAML можно увидеть карту маршрутов и зависимостей между хостами.

## Где уместен

ASSH полезен, когда:

- много SSH-хостов и aliases;
- есть bastion/jump hosts;
- нужны fallback routes между direct и gateway-доступом;
- SSH config должен собираться из нескольких файлов;
- одни и те же опции повторяются между группами хостов;
- нужно визуализировать SSH topology;
- нужны hooks на connect/disconnect/config rewrite.

С [OculiX]({{ '/wiki/tools/oculix' | relative_url }}) связь практическая: OculiX описывает visual automation через удалённые/VNC-сессии и SSH tunneling, а ASSH решает нижний слой SSH-маршрутов, aliases и gateway-конфигурации. С [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) связь по CLI-first подходу: оба превращают сложную capability в повторяемые команды, которые можно безопаснее передать человеку, скрипту или агенту.

## Ограничения и осторожность

Главный риск — ASSH управляет `~/.ssh/config`. Ошибка в YAML, hooks или rewrite-логике может сломать привычный доступ к серверам. Перед внедрением нужно:

- сохранить backup текущего SSH config;
- начинать с малого набора хостов;
- проверять `assh config build` и `assh config list` до активного использования;
- аккуратно обращаться с hooks, особенно `exec`;
- не хранить secrets в YAML, если их можно вынести в SSH agent, keychain или отдельный секретный слой.

Также важно не путать ASSH с secret manager или полноценным inventory/CMDB. Он решает SSH config и routing, но не заменяет управление правами, аудит ключей и lifecycle серверов.

## Практический вывод

`assh` полезен как operator layer для SSH. Его ценность появляется там, где обычный `~/.ssh/config` стал слишком ручным: gateway chains, aliases, inheritance, includes и hooks превращают SSH-доступ в описываемую и проверяемую конфигурацию.

Если хостов мало, он может быть лишним. Если доступ к серверам идёт через bastion, VPN, fallback-маршруты и разные команды, ASSH снижает хаос и делает SSH-поведение более воспроизводимым.

## Источники

- https://github.com/moul/assh
- https://pkg.go.dev/moul.io/assh/v2
