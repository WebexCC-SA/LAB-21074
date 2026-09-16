#!/usr/bin/env python3
"""Repair double-indentation introduced by re-running fix_list_continuity.py.

Re-running that script a second time added an extra 4-space indent on top of
blocks that were already correctly indented, turning working images into
broken code blocks. This script finds "filler" chunks (everything that is not
a top-level numbered list item or heading) inside list sections, measures
their minimum indentation, and shifts the whole chunk so the minimum becomes
exactly 4 spaces -- preserving any deeper relative nesting (e.g. admonition
bodies) while undoing the accidental double-indent.

Usage:
    python scripts/fix_double_indent.py docs/lab-*.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^#{1,6}\s")
LIST_ITEM_RE = re.compile(r"^\d+\.\s")


def fix_text(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    n = len(lines)

    # Identify boundary line indices: headings and top-level list items.
    boundaries = [
        i for i, ln in enumerate(lines) if HEADING_RE.match(ln) or LIST_ITEM_RE.match(ln)
    ]

    fixed_chunks = 0
    i = 0
    while i < n:
        if HEADING_RE.match(lines[i]) or LIST_ITEM_RE.match(lines[i]):
            i += 1
            continue
        # Determine whether we're inside an active list section: the nearest
        # preceding boundary (if any) must be a list item, not a heading, and
        # must exist.
        prev_boundary = None
        for b in boundaries:
            if b < i:
                prev_boundary = b
            else:
                break
        in_list_context = prev_boundary is not None and LIST_ITEM_RE.match(lines[prev_boundary])

        # Collect the filler chunk: consecutive lines until next boundary or EOF.
        start = i
        while i < n and not (HEADING_RE.match(lines[i]) or LIST_ITEM_RE.match(lines[i])):
            i += 1
        chunk = lines[start:i]

        if in_list_context:
            non_blank = [ln for ln in chunk if ln.strip() != ""]
            if non_blank:
                min_indent = min(len(ln) - len(ln.lstrip(" ")) for ln in non_blank)
                delta = min_indent - 4
                if delta > 0:
                    new_chunk = []
                    for ln in chunk:
                        if ln.strip() == "":
                            new_chunk.append(ln)
                        else:
                            new_chunk.append(ln[delta:])
                    lines[start:i] = new_chunk
                    fixed_chunks += 1

    return "\n".join(lines) + "\n", fixed_chunks


def main() -> None:
    paths = [Path(p) for p in sys.argv[1:]]
    total = 0
    for path in paths:
        text = path.read_text()
        new_text, n = fix_text(text)
        if n:
            path.write_text(new_text)
            print(f"{path}: repaired {n} chunk(s)")
            total += n
    print(f"Total chunks repaired: {total}")


if __name__ == "__main__":
    main()
