---
title: filesql
type: technology
created: 2026-09-20
last_updated: 2026-09-20
domain: infra
related: ["PocketBase", "PostgreSQL + VectorChord", "Teable"]
sources: ["github-nao1215-filesql-2026-09-20"]
tags: [go, sqlite, sql, database, tools, open-source]
---

# filesql

`filesql` — Go-библиотека, которая превращает набор data files в временную in-memory SQLite database и отдаёт обычный `*sql.DB`. Она подходит для ad-hoc анализа, file-to-file joins и embedding data files в Go-приложение без отдельного сервера и ручного ETL.

Важно не перепутать границу: «без импорта» означает отсутствие отдельного пользовательского шага. При открытии файлы всё равно загружаются в SQLite в памяти; это не query engine, выполняющий predicate pushdown напрямую по CSV или произвольному Parquet lake.

## Форматы и интерфейс

Поддержаны CSV, TSV, LTSV, JSON, JSONL, Parquet, XLSX, ACH и Fedwire, включая распространённые сжатия. Имя файла становится именем таблицы, поэтому можно открыть несколько источников и выполнить `JOIN` между ними. Источником может быть path, directory, `io.Reader` или `embed.FS`.

```go
ctx := context.Background()
db, err := filesql.Open(ctx, "users.csv", "orders.jsonl", "returns.parquet")
if err != nil { log.Fatal(err) }
defer db.Close()

rows, err := db.QueryContext(ctx, `
  SELECT u.name, COUNT(*)
  FROM users u JOIN orders o ON u.id = json_extract(o.data, '$.user_id')
  GROUP BY u.name`)
```

SQL dialect по умолчанию — SQLite: CTE, window functions, aggregation, `json_extract()` и joins работают через SQLite. Опциональные PostgreSQL/MySQL/GoogleSQL modes — лишь перевод поддерживаемого подмножества в SQLite; несовместимые конструкции библиотека должна отвергнуть, а не эмулировать произвольно.

## Память, типы и безопасность данных

CSV/TSV/JSONL/JSON arrays/Parquet поступают chunk-ами, но в конце становятся таблицами in-memory SQLite. LTSV, full JSON documents, XLSX, ACH и Fedwire читаются целиком. Особенно опасен XLSX: ZIP-размер плохо предсказывает память после распаковки и обработки ячеек. Для untrusted uploads нужны size limits, cancellation context и process-level memory limit.

Типы CSV/TSV/LTSV/XLSX inferred по всем значениям column. Библиотека специально оставляет column TEXT при leading zeros, integer beyond `int64`, unsafe float or padded codes, чтобы не портить данные. Но числовое formatting не сохраняется: `2.50` превратится в REAL `2.5`. Исходный файл остаётся источником правды для display/spelling.

Изменения по умолчанию живут только в памяти. `DumpDatabase`, `EnableAutoSave` и `EnableAutoSaveOnCommit` превращают library в writer — это уже явная side effect, который нельзя включать рядом с исходными или неподтверждёнными путями без backup/atomic-write policy.

## Где уместен

- разовый SQL-анализ набора файлов в Go service/CLI;
- controlled import pipeline, где files сначала нормализует `prep`, затем SQLite SQL объединяет их;
- тесты и local tools без database server;
- небольшие и средние datasets, для которых memory budget известен.

Это не замена [PocketBase]({{ '/wiki/infra/pocketbase' | relative_url }}): PocketBase — persistent backend с API/auth/realtime, filesql — библиотека для временного query layer. Это также не замена [PostgreSQL + VectorChord]({{ '/wiki/infra/postgresql-vectorchord-hybrid-search' | relative_url }}): там persistent SQL/retrieval architecture, здесь file ingestion в memory для SQL-задачи. С [Teable]({{ '/wiki/tools/teable' | relative_url }}) возможна связка: Teable — UI/операционная база, filesql — code-level ad-hoc обработка экспортов.

## Проверка

Для ingest просмотрен upstream SHA [`034d8e8`](https://github.com/nao1215/filesql/commit/034d8e8d60adfe3fddcaa96ddc862c0ec524c62f). Локально выполнен заявленный `make test`: `go test -cover ./...` завершился успешно для root, dialect, internal packages и `prep`. Это подтверждает unit/integration suite проекта в данном окружении, но не устанавливает пригодность для произвольного объёма или враждебных файлов.

## Вывод

filesql — хороший file-to-SQL adapter, когда SQL нужен сейчас, а данные уже лежат в файлах. Его ценность — знакомый Go `database/sql` contract и много форматов. Его ограничение ровно то же: это in-memory conversion layer, поэтому перед production use нужно явно задать max input size, memory budget, timeout и rule для любого write-back.

## Источники

- [Upstream repository](https://github.com/nao1215/filesql/tree/034d8e8d60adfe3fddcaa96ddc862c0ec524c62f)
- [README](https://github.com/nao1215/filesql/blob/034d8e8d60adfe3fddcaa96ddc862c0ec524c62f/README.md)
- [Package documentation](https://pkg.go.dev/github.com/nao1215/filesql)
