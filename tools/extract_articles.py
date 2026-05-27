"""Extract article blocks from a Chilean law PDF.

Each block is a dict with keys: titulo, titulo_name, article_num, spanish_text.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import TypedDict

import pdfplumber

TITULO_RE = re.compile(
    # Matches real Titulo headings in three forms:
    #   [opt-quote] TITULO     - plain ASCII (fixture PDFs)
    #   [opt-quote] T\xcdTULO  - U+00CD I-acute, uppercase (21.521-style)
    #   T\xedtulo              - U+00ED i-acute, title-case (19.628-style)
    # The optional curly/straight quote prefix is ONLY allowed before the
    # UPPERCASE forms. The title-case form does NOT accept a quote prefix
    # because the phantom "Titulo XXIX" in 21.521 amendment text uses
    # exactly that combination: a curly-quote + title-case Titulo.
    # NO re.IGNORECASE: lowercase titulo in body text must not match.
    r"^(?:[\u201c\u201d\x22\x27]?(?:TITULO|T[\xcd]TULO)|T[\xed]tulo)\s+(Preliminar|Final|[IVX]+)\s*$",
    re.MULTILINE,
)
# Matches "Disposiciones transitorias" as a virtual section (not a Titulo)
TRANSITORIO_RE = re.compile(
    r"^Disposiciones\s+transitorias\s*$",
    re.MULTILINE | re.IGNORECASE,
)
ARTICLE_RE = re.compile(
    # U+00ED = i-acute (as in Articulo), U+00BA = masculine ordinal (as in 1o.-)
    r"^Art[i\xed]culo\s+(\d+[o\xb0\xba]?(?:\s+bis|\s+ter|\s+qu[áa]ter|\s+quinquies|\s+sexies|\s+septies|\s+octies|\s+nonies)?)\.-\s+",
    re.MULTILINE | re.IGNORECASE,
)


class ArticleBlock(TypedDict):
    titulo: str
    titulo_name: str
    article_num: str
    spanish_text: str


def _read_full_text(pdf_path: Path) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)


def extract_articles(pdf_path: Path) -> list[ArticleBlock]:
    text = _read_full_text(pdf_path)
    titulo_spans = [(m.start(), m.group(1)) for m in TITULO_RE.finditer(text)]
    # Patterns for PDF noise lines to skip when collecting title names
    _FOOTER_RE = re.compile(r"Biblioteca del Congreso Nacional|^Ley\s+\d+\s*$", re.IGNORECASE | re.MULTILINE)
    titulo_names: dict[str, str] = {}
    for start, roman in titulo_spans:
        # Title name = lines immediately after the TITULO heading, up to the first
        # Article line, another Titulo heading, or BCN footer.
        after_lines = text[start:].split("\n")
        name_parts: list[str] = []
        for line in after_lines[1:]:  # skip the TITULO line itself
            stripped = line.strip()
            if not stripped:
                if name_parts:
                    break  # blank line ends the title block
                continue
            if _FOOTER_RE.search(stripped):
                continue  # skip BCN footer lines
            if ARTICLE_RE.match(stripped) or TITULO_RE.match(stripped):
                break  # reached next section
            name_parts.append(stripped)
            # Stop after collecting reasonable title lines (avoid swallowing article text)
            if len(name_parts) >= 3:
                break
        titulo_names[roman] = " ".join(name_parts)

    # Also track "Disposiciones transitorias" as a virtual section.
    transitorio_spans = [(m.start(), "Transitorio") for m in TRANSITORIO_RE.finditer(text)]
    titulo_names["Transitorio"] = "Disposiciones transitorias"
    all_spans = sorted(titulo_spans + transitorio_spans, key=lambda x: x[0])

    def titulo_at(pos: int) -> str:
        current = ""
        for start, roman in all_spans:
            if start <= pos:
                current = roman
        return current

    matches = list(ARTICLE_RE.finditer(text))
    titulo_starts = [start for start, _ in all_spans]
    blocks: list[ArticleBlock] = []
    for i, m in enumerate(matches):
        body_start = m.start()
        next_article_start = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        # Also clip at the earliest Titulo header that appears after this article starts.
        next_titulo_start = next(
            (s for s in titulo_starts if s > body_start), len(text)
        )
        body_end = min(next_article_start, next_titulo_start)
        article_num = m.group(1).strip().rstrip("o\xb0\xba")
        roman = titulo_at(body_start)
        blocks.append(
            ArticleBlock(
                titulo=roman,
                titulo_name=titulo_names.get(roman, ""),
                article_num=article_num,
                spanish_text=text[body_start:body_end].rstrip(),
            )
        )
    return blocks


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        print("usage: extract_articles.py <pdf>", file=sys.stderr)
        sys.exit(2)
    blocks = extract_articles(Path(sys.argv[1]))
    json.dump(blocks, sys.stdout, ensure_ascii=False, indent=2)
