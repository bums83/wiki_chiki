---
title: PocketBase
type: technology
created: 2026-05-01
last_updated: 2026-06-18
domain: infra
related: ["Directus", "Teable", "PowerInfer", "RTK", "Вайб-кодинг"]
tags: ["backend", "go", "sqlite", "realtime", "open-source", "prototyping"]
sources: ["github-pocketbase-pocketbase-2026-05-01"]
---

# PocketBase

`PocketBase` — open-source бэкенд на Go, который помещает всё в один исполняемый файл (~15 МБ): SQLite с realtime-подписками, авторизация, файловый storage, админ-панель и REST-ish API.

Предназначен для быстрых прототипов и проектов, где основная боль — фронтенд, а не настройка инфраструктуры. Ещё не достиг v1.0.0, но уже стабильно используется в проде.

## Что внутри

| Компонент | Описание |
|---|---|
| **Embedded SQLite** | Полноценная БД с realtime-подписками (`subscribe` из коробки) |
| **Users & Auth** | Встроенная система авторизации, refresh tokens, OAuth |
| **Files storage** | Загрузка/раздача файлов с disk storage |
| **Admin UI** | Готовая админ-панель на `/ _/` — сразу из коробки |
| **REST API** | Автогенерируемый API для всех коллекций |
| **JS VM plugin** | Встроенная JavaScript VM для кастомной логики |
| **Go plugin system** | Нативные Go-плагины для расширения |

## Установка и запуск

Один бинарник, никаких зависимостей:

```bash
# Скачать с GitHub Releases
curl -L https://github.com/pocketbase/pocketbase/releases/latest/download/pocketbase_linux_amd64.zip -o pb.zip
unzip pb.zip

# Запуск
./pocketbase serve

# Админ-панель доступна на http://127.0.0.1:8090/_/
```

Или из исходников — чистый Go без CGO (статический бинарник):

```bash
git clone https://github.com/pocketbase/pocketbase
cd pocketbase/examples/base
CGO_ENABLED=0 go build
./base serve
```

## Архитектура

PocketBase поставляется как обычная Go-библиотека. Можно встроить в свой проект:

```go
package main

import (
    "log"
    "github.com/pocketbase/pocketbase"
    "github.com/pocketbase/pocketbase/core"
)

func main() {
    app := pocketbase.New()

    app.OnServe().BindFunc(func(se *core.ServeEvent) error {
        se.Router.GET("/hello", func(re *core.RequestEvent) error {
            return re.String(200, "Hello world!")
        })
        return se.Next()
    })

    if err := app.Start(); err != nil {
        log.Fatal(err)
    }
}
```

Поддерживаемые платформы: linux (amd64, arm64, arm, 386, ppc64le, riscv64, s390x, loong64), darwin (amd64, arm64), windows (amd64, arm64, 386), freebsd.

## SDK и интеграции

Официальные клиенты:

| SDK | Платформы |
|---|---|
| [JavaScript](https://github.com/pocketbase/js-sdk) | Browser, Node.js, React Native |
| [Dart](https://github.com/pocketbase/dart-sdk) | Web, Mobile, Desktop, CLI |

Можно также использовать как обычный REST API без SDK.

## Realtime

SQLite с pub/sub — подписка на изменения из фронтенда:

```javascript
// JS SDK пример
const pb = new PocketBase('http://127.0.0.1:8090')

// Подписка на изменения коллекции "messages"
pb.collection('messages').subscribe('*', function (e) {
    console.log(e.action) // "create", "update", "delete"
    console.log(e.record) // changed record
})
```

## Расширение через JavaScript

Кастомная логика на встроенном JS (MuJS):

```javascript
// pb_hooks/example.js
onRecordCreateRequest((e) => {
    // Ваша логика
    console.log("New record:", e.record)
}, 'messages')
```

Или кастомные actions, валидация, webhooks — всё на JS внутри бинарника.

## Когда подходит

**Да:**
- Быстрые прототипы и MVP
- Инди-проекты, SaaS-микросервисы
- Fullstack-проекты, где основная работа на фронтенде
- Замена Firebase для тех, кто хочет self-hosting
- Локальные инструменты с простым бэкендом

**Нет:**
- Высокая нагрузка (SQLite — не для этого)
- Сложная бизнес-логика (лучше Go-микросервисы)
- PostgreSQL-специфичные фичи (jsonb, partitioning и т.д.)
- Мультитенантность без танцев с коллекциями

## В контексте Wiki Chiki

В связке с локальными AI-инструментами из Wiki Chiki:

- [PowerInfer]({{ '/wiki/infra/powerinfer' | relative_url }}) — локальный inference для AI-фич внутри PocketBase-плагинов
- [RTK]({{ '/wiki/infra/rtk' | relative_url }}) — оптимизация контекста при работе с PocketBase API из AI-coding инструментов
- [Directus]({{ '/wiki/tools/directus' | relative_url }}) — альтернатива с более богатым REST/GraphQL, но без realtime из коробки
- [Teable]({{ '/wiki/tools/teable' | relative_url }}) — более тяжёлый no-code Postgres/Airtable-like слой, когда нужна командная таблица с views и self-hosted database stack
- [Вайб-кодинг]({{ '/wiki/llm-agents/vibe-coding' | relative_url }}) — PocketBase удобен для быстрого прототипирования AI-фич: собрал схему, описал API-контракт, отдал агенту

## Ресурсы

- Репозиторий: https://github.com/pocketbase/pocketbase
- Документация: https://pocketbase.io/docs
- Roadmap: https://github.com/orgs/pocketbase/projects/2
- JS SDK: https://github.com/pocketbase/js-sdk
- Dart SDK: https://github.com/pocketbase/dart-sdk