---
id: github-vladimir-human-humanizer-ru-2026-07-27
date: 2026-07-27
source_type: url
source_url: https://github.com/Vladimir-Human/humanizer-ru
title: humanizer-ru GitHub repository
domain: llm-agents
tags: [llm, agents, writing, prompt-engineering, eval, workflow]
---

# humanizer-ru GitHub repository

Canonical source: https://github.com/Vladimir-Human/humanizer-ru

Observed repository state on 2026-07-27:

- Repository: `Vladimir-Human/humanizer-ru`.
- Version: `3.7.0` in `SKILL.md`; last reviewed 2026-07-26.
- License: MIT.
- Repository form: Russian-language Agent Skill, mostly Markdown instructions plus standard-library Python validation/eval scripts.
- Git HEAD inspected: `3d58df3564810acfc634310d09fdfa205b9d9647` on branch `main`.
- The repository describes 37 style/AI-writing patterns (25 base + 12 Russian extensions) and 38 regex markers divided into class A and class B.

## What the source provides

`humanizer-ru` is an Agent Skill for inspecting Russian prose for signs of machine-generated writing and, only when explicitly asked, rewriting it without adding facts. It covers prose for publication, posts, articles, letters and documents. It is not intended for source code/configs, legal or normative documents, or literary prose and poetry, because genre conventions in those materials overlap with many style signals.

The skill distinguishes two kinds of evidence:

- class A: hard copy/paste artefacts such as vendor citation markers, hidden separators, tool URLs, placeholder fields and stray reasoning tags;
- class B: contextual indicators such as zero-width characters or generic placeholders. A B marker never establishes AI authorship by itself.

Its stated rule is deliberately conservative: do not label a text as AI-written from one soft style sign. A hard class-A marker, confirmed source fabrication, or a combination of several soft signs from different categories is required before making a stronger claim. Human text should be left alone if the evidence is weak.

## Content and architecture

`SKILL.md` is a compact decision map. Detailed guidance lives in `references/`: content, language, structural/style and communication patterns; chatbot artefacts; source fabrication; quantitative heuristics; false positives; rewrite guidance; model-fingerprint evidence levels; and test fixtures.

The repository also contains:

- `PERSONA.md` — short rules for natural Russian conversational output;
- `scripts/check_markers.py` — marker parity and arbitrary-file scan mode;
- specification, budget, docs, examples, corpus, registry, performance and release validators;
- `eval/run_eval.py` — a fixed neutral corpus with hashes;
- `eval/blind_eval.py` — paired effect evaluation that separately measures marker removal, fabricated facts, false edits, length and blind-judge outcomes;
- `docs/REVIEW.md` — review classes and the evidence required for a new marker or validator.

## Evidence and limitations preserved in the source

The project does not market itself as a detector-bypass tool. It explicitly forbids claims that it can prove authorship from a single soft signal, and it documents false-positive boundaries: literary style, legal boilerplate, academic register, long dashes, quotation autocorrection and rhetorical triples can be legitimate.

The checked baseline eval (`2026-07-26`) reported zero edits on two human controls and no fabricated facts in its recorded pairs, but it did **not** establish a clear readability advantage: the blind model judge preferred the skill in 2 pairs, the no-skill variant in 1, with 3 ties. The source retains this non-flattering result instead of presenting it as proof of superiority.

## Verification run

The complete documented offline validation sequence was run in the temporary clone. It passed:

```text
python3 scripts/check_spec.py SKILL.md --strict --expect-dir humanizer-ru
python3 scripts/check_budget.py SKILL.md --expect-dir humanizer-ru
python3 scripts/check_docs.py
python3 scripts/check_markers.py --parity
python3 scripts/check_examples.py
python3 scripts/check_corpus.py
python3 scripts/check_fixture_sources.py research/fixtures/marker-sources.json
python3 eval/run_eval.py
python3 eval/blind_eval.py --selftest
python3 scripts/check_release.py --root . --build dist/humanizer-ru.zip
python3 scripts/check_release.py --verify dist/humanizer-ru.zip
```

Notable observed results: 38 regex entries documented; 31 Before/After pairs passed the no-new-facts gate; the corpus had zero human hits; `blind_eval` selftest passed 27/27; the deterministic release archive verified with SHA-256 `6e4dcb4d6c0302ef62f7e001e325babe6d7d0a3a95ae1f9fee38118be64a1e2c`.

`check_fixture_sources.py` emitted two non-fatal warnings about intentionally repeated source URLs while still closing its 14/14 evidence gate. The repo itself reports evidence records for 14 of 38 markers and labels the remaining 24 as legacy; this is a limitation, not a claim of full source coverage.

## Source snapshot

A working-tree copy of the inspected repository is saved at:

`raw/sources/github/Vladimir-Human/humanizer-ru/`

Snapshot metadata is saved at:

`raw/sources/github/Vladimir-Human/humanizer-ru.source-metadata.json`

The snapshot excludes nested Git metadata, virtualenvs, dependency directories, bytecode/test caches and generated `dist`/`build` output. It preserves the reviewed instructions, references, validators, eval corpus and research material.

## Wiki integration notes

Nearest Wiki Chiki neighbors:

- [[Prompt Master]] — prepares instructions before model execution; humanizer-ru reviews resulting Russian prose afterward.
- [[Agents.md]] — both package scoped instructions with progressive disclosure, validation and safety boundaries.
- [[Academic Research Skills]] — both use integrity gates, but ARS validates research/citations while humanizer-ru focuses on prose and chatbot artefacts.
- [[OpenAI Privacy Filter]] — both inspect text conservatively; one looks for PII, the other for writing artefacts.
