#!/usr/bin/env python3
"""Diff normalized plain text between the current formatted docs/ files and a
fresh docx_to_markdown.py conversion, to surface real content changes while
ignoring our manual HTML/formatting additions (width attrs, .bordered class,
admonition wrappers, list-continuity indentation, etc.)
"""
import difflib
import re
from pathlib import Path

CURRENT_DIR = Path("docs")
FRESH_DIR = Path("/tmp/lab_fresh_convert")

FILES = [
    "lab-1-accessing-your-lab-5-minutes.md",
    "lab-2-ai-receptionist-configuration-20-minutes.md",
    "lab-3-configure-webex-calling-tts-announcement-5-minutes.md",
    "lab-4-configure-webex-calling-customer-assist-20-minutes.md",
    "lab-5-testing-and-call-flow-validation-30-minutes.md",
    "lab-appendix.md",
    "lab-learning-objectives.md",
    "lab-overview.md",
]

TAG_RE = re.compile(r"<[^>]+>")
IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)(\{[^}]*\})?")
ATTR_RE = re.compile(r"\{[^}]*\}")
WS_RE = re.compile(r"[ \t]+")
LIST_MARKER_RE = re.compile(r"^(\d+\.|\*|\+|-)\s+")
BOLD_RE = re.compile(r"\*\*")
LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
QUOTE_RE = re.compile(r"[\u201c\u201d\u2018\u2019]")


def normalize(text: str) -> list[str]:
    text = IMG_RE.sub("", text)
    text = TAG_RE.sub(" ", text)
    text = ATTR_RE.sub("", text)
    lines = []
    for line in text.splitlines():
        line = line.strip()
        line = LIST_MARKER_RE.sub("", line)
        line = LINK_RE.sub(r"\1", line)
        line = BOLD_RE.sub("", line)
        line = QUOTE_RE.sub('"', line)
        line = WS_RE.sub(" ", line)
        if line and line not in ("|", "---", "| --- |", "| --- | --- |"):
            lines.append(line)
    return lines


for fname in FILES:
    cur_path = CURRENT_DIR / fname
    fresh_path = FRESH_DIR / fname
    if not cur_path.exists() or not fresh_path.exists():
        print(f"=== {fname}: MISSING on one side ===")
        continue
    cur_lines = normalize(cur_path.read_text())
    fresh_lines = normalize(fresh_path.read_text())
    sm = difflib.SequenceMatcher(None, cur_lines, fresh_lines, autojunk=False)
    opcodes = [op for op in sm.get_opcodes() if op[0] != "equal"]
    if not opcodes:
        continue
    print(f"\n=== {fname} ===")
    for tag, i1, i2, j1, j2 in opcodes:
        print(f"--- {tag} ---")
        if tag in ("delete", "replace"):
            for l in cur_lines[i1:i2]:
                print(f"  CUR: {l}")
        if tag in ("insert", "replace"):
            for l in fresh_lines[j1:j2]:
                print(f"  NEW: {l}")
