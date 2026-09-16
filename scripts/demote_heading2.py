#!/usr/bin/env python3
"""Demote Heading 2 paragraphs to Heading 3 so the docx_to_markdown.py splitter
only creates a new page per Heading 1 ("Lab N: ...") and keeps Steps (Heading 2)
merged into their parent Task/Lab page.

Usage:
    python scripts/demote_heading2.py path/to/guide.docx
Writes a new file alongside the input named "<name>-merged<ext>".
"""
from __future__ import annotations

import argparse
from pathlib import Path

from docx import Document


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_docx", help="Path to the source .docx file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input_docx)
    output_path = input_path.with_name(f"{input_path.stem}-merged{input_path.suffix}")

    doc = Document(str(input_path))
    demoted = 0
    for paragraph in doc.paragraphs:
        style_name = paragraph.style.name if paragraph.style else ""
        if style_name == "Heading 2":
            paragraph.style = doc.styles["Heading 3"]
            demoted += 1

    doc.save(str(output_path))
    print(f"Demoted {demoted} Heading 2 paragraph(s) to Heading 3. Saved: {output_path}")


if __name__ == "__main__":
    main()
