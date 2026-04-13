#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.M)
RELATED_RE = re.compile(r"^related:\s*\[(.*?)\]\s*$", re.M)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
MARKDOWN_MD_LINK_RE = re.compile(r"\((wiki/[^)]+?)\.md\)")
PUBLIC_ABSOLUTE_LINK_RE = re.compile(r"\]\(/(wiki/[^)]+/)\)")
BACKTICKED_LINK_RE = re.compile(r"`(\[[^`]+\]\((?:/wiki/|\{\{.*?relative_url.*?\}\})\))`")


def build_title_map() -> dict[str, str]:
    title_to_url: dict[str, str] = {}
    for path in WIKI_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            continue
        title_match = TITLE_RE.search(match.group(1))
        if not title_match:
            continue
        title = title_match.group(1).strip().strip('"').strip("'")
        rel = path.relative_to(ROOT).as_posix()
        title_to_url[title] = rel[:-3] + "/"
    return title_to_url


def rewrite_body(body: str, title_to_url: dict[str, str], unresolved: set[str]) -> str:
    def replace_wikilink(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = (match.group(2) or target).strip()
        url = title_to_url.get(target)
        if not url:
            unresolved.add(target)
            return match.group(0)
        return f"[{label}]({{{{ '/{url}' | relative_url }}}})"

    body = WIKILINK_RE.sub(replace_wikilink, body)
    body = MARKDOWN_MD_LINK_RE.sub(lambda m: "({{ '/" + m.group(1).rstrip("/") + "/' | relative_url }})", body)
    body = PUBLIC_ABSOLUTE_LINK_RE.sub(lambda m: "]({{ '/" + m.group(1).lstrip("/") + "' | relative_url }})", body)
    body = BACKTICKED_LINK_RE.sub(r"\1", body)
    return body


def normalize_frontmatter(frontmatter: str) -> str:
    def replace_related(match: re.Match[str]) -> str:
        items = []
        for target, _label in WIKILINK_RE.findall(match.group(1)):
            items.append(f'"{target.strip()}"')
        if not items:
            return match.group(0)
        return 'related: [' + ', '.join(items) + ']'

    return RELATED_RE.sub(replace_related, frontmatter)


def process_file(path: Path, title_to_url: dict[str, str], unresolved: set[str]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    frontmatter = ""
    body = text
    match = FRONTMATTER_RE.match(text)
    if match:
        frontmatter = normalize_frontmatter(match.group(0))
        body = text[match.end():]

    body = rewrite_body(body, title_to_url, unresolved)
    updated = frontmatter + body

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    title_to_url = build_title_map()
    unresolved: set[str] = set()

    targets = [*WIKI_DIR.rglob("*.md"), ROOT / "index.md"]
    changed: list[str] = []

    for path in targets:
        if process_file(path, title_to_url, unresolved):
            changed.append(path.relative_to(ROOT).as_posix())

    if changed:
        print("Updated files:")
        for item in changed:
            print(f"- {item}")
    else:
        print("No changes needed.")

    if unresolved:
        print("Unresolved wikilinks:")
        for item in sorted(unresolved):
            print(f"- {item}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
