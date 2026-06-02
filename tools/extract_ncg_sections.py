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
# Matches structurally valid Roman numeral strings (non-empty).
# NOTE: this is necessary but not sufficient — C, D, L are valid Roman
# characters but are also letter subsection labels in NCG documents.
# Sequential validation (_roman_to_int + strict increment) is used to
# disambiguate them at parse time.
_ROMAN_RE = re.compile(
    r"^M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})$"
)
_ROMAN_VALS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def _roman_to_int(s: str) -> int:
    result = 0
    prev = 0
    for ch in reversed(s):
        v = _ROMAN_VALS.get(ch, 0)
        result += v if v >= prev else -v
        prev = v
    return result


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


def _parse_toc_from_text(full: str) -> list[dict]:
    """Return ToC entries as dicts with keys: number (full path), title, page,
    and _local (the raw token from the índice, used internally for heading
    matching in body text).

    Full-path rule:
    - Pure Roman tokens (I, II, ...) → full path == token; update current Roman.
    - All other tokens (letter, letter-rooted dotted, numeric dotted) →
      full path == "<current_roman>.<token>".
    """
    start = INDICE_RE.search(full)
    region = full[start.end():] if start else full
    entries: list[dict] = []
    current_roman: str | None = None
    current_roman_int: int = 0
    for line in region.splitlines():
        m = TOC_LINE_RE.match(line)
        if not m:
            # Skip non-matching lines (wrapped long titles, blank lines, page
            # numbers, body headings); body headings never carry dots+page so
            # they will not match TOC_LINE_RE — no early break needed.
            continue
        # M-2: TOC_LINE_RE's \.?? is outside the number group so the
        # capture never contains a trailing dot — .strip() suffices.
        local = m.group("number").strip()
        # A token is a top-level Roman section only if:
        # 1. It matches the Roman numeral character pattern (non-empty), AND
        # 2. Its integer value is exactly one more than the previous Roman
        #    section (strict sequence). This disambiguates letter subsection
        #    labels like 'C', 'D', 'L' which are also valid Roman characters
        #    but would jump discontinuously in value (e.g. C=100 after I=1).
        is_roman_section = False
        if _ROMAN_RE.match(local) and local:
            val = _roman_to_int(local)
            if val == current_roman_int + 1:
                is_roman_section = True
        if is_roman_section:
            # Top-level Roman section: full path == the token itself.
            current_roman = local
            current_roman_int = _roman_to_int(local)
            full_number = local
        else:
            # Sub-section: prefix with current Roman section if available.
            full_number = f"{current_roman}.{local}" if current_roman else local
        entries.append(
            {
                "number": full_number,
                "title": m.group("title").strip(),
                "page": int(m.group("page")),
                "_local": local,
            }
        )
    return entries


def parse_toc(pdf_path: Path) -> list[TocEntry]:
    full = "\n".join(_read_pages(pdf_path))
    raw = _parse_toc_from_text(full)
    return [TocEntry(number=e["number"], title=e["title"], page=e["page"]) for e in raw]


def _heading_regex(local_token: str, title: str) -> re.Pattern:
    """Build a body-heading pattern using the LOCAL token (not the full path).

    Body headings use the local token (e.g. "A. Sub A"), not the full
    hierarchical path (e.g. "I.A. Sub A"), so we match on `local_token`.
    """
    num = re.escape(local_token)
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


def _extract_sections_from_text(full: str) -> list[SectionBlock]:
    toc = _parse_toc_from_text(full)
    indice = INDICE_RE.search(full)
    toc_region_start = indice.end() if indice else 0
    body_start = _find_body_start(full, toc_region_start)
    positions: list[tuple[int, dict]] = []
    search_from = body_start
    for entry in toc:
        # Use the LOCAL token for body-heading matching (body says "A. Sub A",
        # not "I.A. Sub A"), but the full path is stored in entry["number"].
        local_token = entry.get("_local", entry["number"])
        pat = _heading_regex(local_token, entry["title"])
        m = pat.search(full, search_from)
        if m:
            positions.append((m.start(), entry))
            search_from = m.end()
    # M-1: Defensive sort — guards against ToC entries whose body heading is
    # located out of document order; normally a no-op since search_from
    # advances linearly through the text.
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


def extract_sections(pdf_path: Path) -> list[SectionBlock]:
    full = "\n".join(_read_pages(pdf_path))
    return _extract_sections_from_text(full)


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        print("usage: extract_ncg_sections.py <pdf>", file=sys.stderr)
        sys.exit(2)
    # Read the PDF once; derive both toc and sections from the same text.
    _full = "\n".join(_read_pages(Path(sys.argv[1])))
    out = {
        "toc": _parse_toc_from_text(_full),
        "sections": [
            {"number": s["number"], "title": s["title"]}
            for s in _extract_sections_from_text(_full)
        ],
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
