# Lab Guide for WebexOne Lab LAB-21074

Web guide link: https://webexcc-sa.github.io/LAB-21074/


## DOCX to Markdown script

Use `scripts/docx_to_markdown.py` to convert a DOCX lab guide into markdown files.

### What it does

- Reads one `.docx` input file
- Extracts all embedded images into `docs/assets/` (or a custom assets directory)
- Splits each Heading 1/Heading 2 that starts with `Lab` into its own markdown file in `docs/`
- Writes all non-lab content to `docs/non-lab.md`

### Usage

```bash
python scripts/docx_to_markdown.py path/to/guide.docx
```

Optional arguments:

- `--docs-dir` (default: `docs`)
- `--assets-dir` (default: `<docs-dir>/assets`)

## Helper scripts (run after docx_to_markdown.py, in this order if needed)

- `scripts/demote_heading2.py <docx>` — demotes all Heading 2 paragraphs to
  Heading 3 in a copy of the docx, so Steps stay nested inside their parent
  Lab page instead of splitting into their own file. Run this if your
  Steps are Heading 2 and you don't want one file per step.
- `scripts/fix_list_continuity.py docs/lab-*.md` — re-indents images,
  paragraphs, and admonitions that interrupt a numbered list so Markdown
  treats it as one continuous list instead of restarting the numbering at 1.
  **Only run this once per file** — running it twice will double-indent
  already-fixed content and turn images into broken code blocks. If that
  happens, `scripts/fix_double_indent.py` can repair it.
- `scripts/fix_double_indent.py docs/lab-*.md` — repairs the double-indent
  bug described above by re-basing each "filler" block between list items to
  a consistent 4-space indent, preserving deeper nesting (e.g. admonition
  bodies).

## Formatting conventions used in this guide

- **Image sizing:** `docx_to_markdown.py` extracts images at full native
  resolution, which is usually much larger than how Word displays them. Use
  `{ width="NNN" }` (attr_list syntax) after an image to set a display width.
  Prefer sizing *down* from native resolution — sizing up beyond native
  resolution causes visible blur.
- **EMF images:** Word screenshots pasted as Windows Enhanced Metafile (EMF)
  extract as `.bin` files that don't render in browsers. Fix by converting
  with LibreOffice (`brew install --cask libreoffice`, then
  `soffice --headless --convert-to png --outdir DIR file.emf`), then crop out
  the white page margins with Pillow (see repo memory notes / chat history for
  the exact snippet). For extra resolution before enlarging an image, re-run
  the conversion with an explicit `PixelWidth`/`PixelHeight` FilterOption that
  matches the original 8.5x11 aspect ratio.
- **Image borders:** all images use the `.bordered` CSS class
  (`docs/stylesheets/extra.css`) for a light gray outline. Add
  `{ .bordered }` (or combine with width, e.g. `{ .bordered width="753" }`) to
  new images for consistency.
- **Nested tables / lists inside a table cell:** Markdown tables can't nest.
  If a docx table cell contains a sub-list or another table, rewrite it as an
  `!!! note` admonition (for note-style boxes) or raw `<ul>/<ol>` HTML (for
  in-table nested lists). Note: real `<ol>` numbering is CSS-generated and
  is **not** included when a reader copies the text — write literal
  "1." / "2." text inside `<li>` and use `<ul style="list-style:none">` as the
  outer wrapper if copy-paste fidelity matters.
- **Multi-line image alt text:** Word's auto-generated alt text (e.g.
  "A screenshot of a computer\n\nAI-generated content may be incorrect.") has
  a blank line that breaks `![]()` syntax — collapse it to one line.
- **Literal `{{...}}` text** (e.g. screen-pop config values) breaks
  mkdocs-macros' Jinja rendering — escape as `{{ "{{...}}" }}`.

