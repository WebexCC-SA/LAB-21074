#!/usr/bin/env python3
"""Fix numbered-list interruptions in generated lab markdown files.

Python-Markdown always starts a new <ol> at 1 when a list is interrupted by
a non-indented block (image, paragraph, admonition). This script re-indents
those interrupting blocks by 4 spaces so they become part of the previous
list item's continuation, keeping the numbered list open and sequential.

Usage:
    python scripts/fix_list_continuity.py docs/*.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

LIST_ITEM_RE = re.compile(r"^\d+\.\s")


def parse_blocks(lines: list[str]) -> list[dict]:
    blocks: list[dict] = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if line.strip() == "":
            i += 1
            continue
        if line.startswith("#"):
            blocks.append({"type": "heading", "lines": [line]})
            i += 1
            continue
        if LIST_ITEM_RE.match(line):
            item_lines = [line]
            i += 1
            while i < n and lines[i].strip() != "" and lines[i][0] in " \t":
                item_lines.append(lines[i])
                i += 1
            blocks.append({"type": "list_item", "lines": item_lines})
            continue
        if line.startswith("!!!"):
            adm_lines = [line]
            i += 1
            while i < n and (lines[i].strip() == "" or lines[i][0] in " \t"):
                adm_lines.append(lines[i])
                i += 1
            blocks.append({"type": "admonition", "lines": adm_lines})
            continue
        other_lines = [line]
        i += 1
        while i < n and lines[i].strip() != "":
            other_lines.append(lines[i])
            i += 1
        blocks.append({"type": "other", "lines": other_lines})
    return blocks


def fix_text(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    blocks = parse_blocks(lines)

    for idx, block in enumerate(blocks):
        if block["type"] != "heading":
            continue
        # Determine list-open state for the section following this heading (and initial section).

    fixed_count = 0
    list_open = False
    for idx, block in enumerate(blocks):
        if block["type"] == "heading":
            list_open = False
            continue
        if block["type"] == "list_item":
            list_open = True
            continue
        if block["type"] in ("other", "admonition") and list_open:
            block["lines"] = [
                ("    " + ln if ln.strip() != "" else ln) for ln in block["lines"]
            ]
            fixed_count += 1

    out_lines: list[str] = []
    for block in blocks:
        out_lines.extend(block["lines"])
        out_lines.append("")
    # trim trailing extra blank lines
    while out_lines and out_lines[-1] == "":
        out_lines.pop()
    return "\n".join(out_lines) + "\n", fixed_count


def main() -> None:
    paths = [Path(p) for p in sys.argv[1:]]
    total = 0
    for path in paths:
        text = path.read_text()
        new_text, n = fix_text(text)
        if n:
            path.write_text(new_text)
            print(f"{path}: indented {n} interrupting block(s)")
            total += n
    print(f"Total blocks fixed: {total}")


if __name__ == "__main__":
    main()
