#!/usr/bin/env python3
"""Rename 'Task N: ...' Heading 1/2 paragraphs to 'Lab N: ...' so the
docx_to_markdown.py splitter treats them as separate lab pages.

Usage:
    python scripts/rename_task_headings.py path/to/guide.docx
Writes a new file alongside the input named "<name>-labs<ext>".
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from docx import Document

TASK_RE = re.compile(r"^\s*Task\s+(\d+)\s*:\s*(.*)$", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_docx", help="Path to the source .docx file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input_docx)
    output_path = input_path.with_name(f"{input_path.stem}-labs{input_path.suffix}")

    doc = Document(str(input_path))
    renamed = 0
    for paragraph in doc.paragraphs:
        style_name = paragraph.style.name if paragraph.style else ""
        if style_name not in ("Heading 1", "Heading 2"):
            continue
        match = TASK_RE.match(paragraph.text)
        if not match:
            continue
        new_text = f"Lab {match.group(1)}: {match.group(2)}"
        # Replace text while preserving the first run's formatting; clear extra runs.
        if paragraph.runs:
            paragraph.runs[0].text = new_text
            for extra_run in paragraph.runs[1:]:
                extra_run.text = ""
        else:
            paragraph.text = new_text
        renamed += 1

    doc.save(str(output_path))
    print(f"Renamed {renamed} heading(s). Saved: {output_path}")


if __name__ == "__main__":
    main()
