---
id: habr-postgresql-vectorchord-hybrid-search-part-2
date: 2026-04-21
source_type: article
source_url: https://habr.com/ru/articles/1024818/
title: PostgreSQL + VectorChord = Гибридный поиск. Часть 2. Безоблачная
domain: infra
tags: [postgresql, vectorchord, hybrid-search, rag, embeddings, reranker, llama-cpp, jina]
---

# PostgreSQL + VectorChord = Гибридный поиск. Часть 2. Безоблачная

Источник: https://habr.com/ru/articles/1024818/

Ключевые тезисы:
- Во второй части автор заменяет временные `spacy`-компоненты из первой статьи на локальные модели для retrieval-контура.
- Для embeddings используется `jina-embeddings-v4-text-retrieval` в формате GGUF через `llama.cpp` server.
- Для reranking используется локальный `jina-reranker-v3` через `transformers` и `torch`.
- Для chunking используется `chonkie` с `SemanticChunker` и overlap refinement.
- Архитектура сохраняет offline-подход и не требует облачных API.
- В статье описаны классы `LocalJinaEmbedding`, `LocalJinaReranker` и `LocalChonkie`, а также изменения в `SearchService` для neural reranking.

Связанный источник первой части:
- https://habr.com/ru/articles/1024810/
