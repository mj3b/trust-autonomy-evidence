#!/usr/bin/env python3
"""Render a GitHub-readable manuscript from Pandoc citation keys and BibTeX."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper" / "manuscript.md"
BIBLIOGRAPHY = ROOT / "paper" / "references.bib"
OUTPUT = ROOT / "paper" / "manuscript-reader.md"

CITATION_GROUP = re.compile(r"\[(@[A-Za-z0-9_:.+-]+(?:\s*;\s*@[A-Za-z0-9_:.+-]+)*)\]")
SOURCE_NOTE = re.compile(
    r"<!-- SOURCE-CITATION-NOTE-START -->.*?<!-- SOURCE-CITATION-NOTE-END -->\n*",
    flags=re.DOTALL,
)
FIELD = re.compile(
    r"(?ms)^\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}\s*,?"
)


def split_entries(text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    position = 0
    while True:
        start = text.find("@", position)
        if start < 0:
            break
        header = re.match(r"@\w+\{([^,]+),", text[start:])
        if header is None:
            position = start + 1
            continue
        key = header.group(1).strip()
        body_start = start + header.end()
        depth = 1
        index = body_start
        while index < len(text) and depth:
            if text[index] == "{":
                depth += 1
            elif text[index] == "}":
                depth -= 1
            index += 1
        if depth:
            raise ValueError(f"unclosed BibTeX entry: {key}")
        entries[key] = text[body_start : index - 1]
        position = index
    return entries


def clean_latex(value: str) -> str:
    replacements = {
        r"\&": "&",
        r'A\"imeur': "Aimeur",
        r'{\"o}': "o",
        r'{"o}': "o",
        "--": "-",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    return value.replace("{", "").replace("}", "").strip()


def parse_bibliography(text: str) -> dict[str, dict[str, str]]:
    parsed: dict[str, dict[str, str]] = {}
    for key, body in split_entries(text).items():
        parsed[key] = {
            name.lower(): clean_latex(value)
            for name, value in FIELD.findall(body)
        }
    return parsed


def family_names(author_field: str) -> list[str]:
    names = []
    for author in author_field.split(" and "):
        author = author.strip()
        if not author or author.lower() == "others":
            continue
        family = author.split(",", 1)[0].strip() if "," in author else author.split()[-1]
        names.append(clean_latex(family))
    return names


def short_author(author_field: str) -> str:
    names = family_names(author_field)
    if not names:
        return "Unknown author"
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} & {names[1]}"
    return f"{names[0]} et al."


def full_author(author_field: str) -> str:
    authors = [clean_latex(item.strip()) for item in author_field.split(" and ") if item.strip()]
    displayed = []
    for author in authors:
        if author.lower() == "others":
            displayed.append("et al.")
        elif "," in author:
            family, given = [item.strip() for item in author.split(",", 1)]
            displayed.append(f"{given} {family}")
        else:
            displayed.append(author)
    if len(displayed) <= 1:
        return "".join(displayed)
    if len(displayed) == 2:
        return f"{displayed[0]} and {displayed[1]}"
    return ", ".join(displayed[:-1]) + f", and {displayed[-1]}"


def citation_link(key: str, entry: dict[str, str]) -> str:
    label = f"{short_author(entry.get('author', ''))}, {entry.get('year', 'n.d.')}"
    target = entry.get("url") or (f"https://doi.org/{entry['doi']}" if entry.get("doi") else "")
    return f"[{label}]({target})" if target else label


def replace_citations(source: str, entries: dict[str, dict[str, str]]) -> tuple[str, set[str]]:
    used: set[str] = set()

    def replacement(match: re.Match[str]) -> str:
        keys = [item.strip().removeprefix("@") for item in match.group(1).split(";")]
        missing = [key for key in keys if key not in entries]
        if missing:
            raise ValueError(f"unresolved citation key(s): {', '.join(missing)}")
        used.update(keys)
        return "(" + "; ".join(citation_link(key, entries[key]) for key in keys) + ")"

    return CITATION_GROUP.sub(replacement, source), used


def reference_line(key: str, entry: dict[str, str]) -> str:
    authors = full_author(entry.get("author", "")) or "Unknown author"
    year = entry.get("year", "n.d.")
    title = entry.get("title", "Untitled")
    container = entry.get("journal") or entry.get("booktitle") or entry.get("publisher") or ""
    volume = entry.get("volume", "")
    number = entry.get("number", "")
    pages = entry.get("pages", "")
    target = entry.get("url") or (f"https://doi.org/{entry['doi']}" if entry.get("doi") else "")
    linked_title = f"[{title}]({target})" if target else title
    details = []
    if container:
        details.append(f"*{container}*")
    if volume:
        details.append(f"{volume}({number})" if number else volume)
    if pages:
        details.append(pages)
    suffix = ", ".join(details)
    return f"- {authors}. ({year}). {linked_title}." + (f" {suffix}." if suffix else "")


def render() -> str:
    source = SOURCE.read_text(encoding="utf-8")
    source = SOURCE_NOTE.sub("", source)
    entries = parse_bibliography(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    rendered, used = replace_citations(source, entries)
    notice = (
        "> **Reader edition.** This file converts the manuscript's Pandoc citation keys into "
        "clickable author-year citations. The [auditable source](manuscript.md) preserves the "
        "citation keys, and [references.bib](references.bib) preserves the checked metadata.\n\n"
    )
    heading_end = rendered.find("\n\n", rendered.find("\n\n") + 2)
    if heading_end < 0:
        raise ValueError("manuscript heading block was not found")
    rendered = rendered[: heading_end + 2] + notice + rendered[heading_end + 2 :]
    ordered = sorted(used, key=lambda key: (family_names(entries[key].get("author", ""))[:1], entries[key].get("year", ""), key))
    references = "\n\n## References\n\n" + "\n".join(reference_line(key, entries[key]) for key in ordered) + "\n"
    result = rendered.rstrip() + references
    if CITATION_GROUP.search(result) or re.search(r"\[@", result):
        raise ValueError("reader manuscript still contains an unresolved Pandoc citation")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify that the reader edition is current")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected:
            print("reader manuscript: FAIL (missing or stale)")
            return 1
        print("reader manuscript: PASS")
        return 0
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
