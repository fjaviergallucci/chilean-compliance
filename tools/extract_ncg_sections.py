"""Extract sections from a Chilean CMF Norma de Carácter General (NCG) PDF.

NCGs are hierarchical (Roman I/II -> letter A/B -> numbered A.1 -> A.2.1),
unlike the article-based laws. We use the document's own ÍNDICE (table of
contents) as the authoritative section spine, then slice the body text.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import TypedDict

import pdfplumber

TOC_LINE_RE = re.compile(
    r"^\s*(?P<number>[IVXLC]+|[A-Z](?:\.\d+)*|\d+(?:\.\d+)*)\.??\s+"
    r"(?P<title>.+?)\s*\.{2,}\s*(?P<page>\d+)\s*$"
)
INDICE_RE = re.compile(r"^\s*[ÍI]NDICE\s*$", re.MULTILINE | re.IGNORECASE)


class TocEntry(TypedDict):
    number: str
    title: str
    page: int


class SectionBlock(TypedDict):
    number: str
    title: str
    spanish_text: str


def _read_pages(pdf_path: Path) -> list[str]:
    with pdfplumber.open(pdf_path) as pdf:
        return [p.extract_text() or "" for p in pdf.pages]


def parse_toc(pdf_path: Path) -> list[TocEntry]:
    full = "\n".join(_read_pages(pdf_path))
    start = INDICE_RE.search(full)
    region = full[start.end():] if start else full
    entries: list[TocEntry] = []
    for line in region.splitlines():
        m = TOC_LINE_RE.match(line)
        if not m:
            # Skip non-matching lines (wrapped long titles, blank lines, page
            # numbers, body headings); body headings never carry dots+page so
            # they will not match TOC_LINE_RE — no early break needed.
            continue
        entries.append(
            TocEntry(
                number=m.group("number").strip().rstrip("."),
                title=m.group("title").strip(),
                page=int(m.group("page")),
            )
        )
    return entries


def _heading_regex(number: str, title: str) -> re.Pattern:
    num = re.escape(number)
    words = [re.escape(w) for w in title.split()[:3]]
    title_pat = r"\s+".join(words)
    return re.compile(rf"^\s*{num}\.?\s+{title_pat}", re.IGNORECASE | re.MULTILINE)


def _find_body_start(full: str, toc_region_start: int) -> int:
    """Walk line-by-line from toc_region_start to find the first non-ToC line.

    Needed because re.finditer with $ in MULTILINE mode does not reliably
    locate ToC line boundaries in the full concatenated PDF string on Python 3.14+.
    """
    pos = toc_region_start
    toc_lines_end = toc_region_start
    found_toc = False
    while pos < len(full):
        nl = full.find("\n", pos)
        if nl == -1:
            nl = len(full)
        line = full[pos:nl]
        if TOC_LINE_RE.match(line):
            toc_lines_end = nl + 1
            found_toc = True
        elif found_toc and line.strip():
            break
        pos = nl + 1
    return toc_lines_end


def extract_sections(pdf_path: Path) -> list[SectionBlock]:
    toc = parse_toc(pdf_path)
    full = "\n".join(_read_pages(pdf_path))
    indice = INDICE_RE.search(full)
    toc_region_start = indice.end() if indice else 0
    body_start = _find_body_start(full, toc_region_start)
    positions: list[tuple[int, TocEntry]] = []
    search_from = body_start
    for entry in toc:
        pat = _heading_regex(entry["number"], entry["title"])
        m = pat.search(full, search_from)
        if m:
            positions.append((m.start(), entry))
            search_from = m.end()
    positions.sort(key=lambda x: x[0])
    blocks: list[SectionBlock] = []
    for i, (pos, entry) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(full)
        blocks.append(
            SectionBlock(
                number=entry["number"],
                title=entry["title"],
                spanish_text=full[pos:end].strip(),
            )
        )
    return blocks


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        print("usage: extract_ncg_sections.py <pdf>", file=sys.stderr)
        sys.exit(2)
    out = {
        "toc": parse_toc(Path(sys.argv[1])),
        "sections": [
            {"number": s["number"], "title": s["title"]}
            for s in extract_sections(Path(sys.argv[1]))
        ],
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
