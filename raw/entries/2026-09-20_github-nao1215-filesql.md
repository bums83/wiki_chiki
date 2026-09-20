---
id: github-nao1215-filesql-2026-09-20
date: 2026-09-20
source_type: url
source_url: https://github.com/nao1215/filesql
title: filesql — Go SQL driver for data files
domain: infra
tags: [go, sqlite, sql, database, tools, open-source]
reviewed_revision: 034d8e8d60adfe3fddcaa96ddc862c0ec524c62f
---

# filesql — исходный материал

`filesql` — Go library, которая загружает CSV, TSV, LTSV, JSON/JSONL, Parquet, XLSX, ACH и Fedwire в in-memory SQLite database и возвращает `*sql.DB`. SQL исполняется SQLite, а не прямо над файловыми блоками: импорт не нужен пользователю, но данные materialize в памяти.

- Просмотрен upstream SHA `034d8e8d60adfe3fddcaa96ddc862c0ec524c62f`; license MIT.
- README требует Go 1.25.13+ либо 1.26.6+; это связано с исправлениями `encoding/xml`/`encoding/asn1`, а XLSX использует `encoding/xml`.
- Supports streaming/chunk loading for CSV, TSV, JSONL, JSON arrays and Parquet; LTSV, full JSON documents, XLSX, ACH and Fedwire load in full. Итоговая база остаётся in-memory SQLite.
- Column types for delimited and XLSX formats inferred from all values; lexical representation may intentionally change (`2.50` → numeric `2.5`), so source remains truth when spelling matters.
- XLSX memory can greatly exceed compressed file size because workbook is unpacked and processed wholly. Do not accept unbounded workbooks in constrained process.
- Can read paths, directories, `io.Reader`, `embed.FS`; optional save/dump and SQL-dialect translation exist. MySQL/PostgreSQL/GoogleSQL are translated subsets, not real engines.
- Проверка: `make test` passed on local clone: `go test -cover ./...`, including root, dialect, internal packages and `prep`.

Sources:
- https://github.com/nao1215/filesql/tree/034d8e8d60adfe3fddcaa96ddc862c0ec524c62f
- https://pkg.go.dev/github.com/nao1215/filesql
