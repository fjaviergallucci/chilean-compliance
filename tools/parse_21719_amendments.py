"""Parse Ley 21.719's amendment list into structured records.

Each record: {
    "amendment_num": "1", "2", ..., "5.uno", "5.dos", ...
    "verb": "Sustituyese" | "Reemplazase" | "Agregase" | "Incorporase" | "Eliminase",
    "target_article": "1°" | "2° lit. a)" | "5° quater" | ...
    "new_text": "<verbatim Spanish of the new wording, if any>",
}
This is a heuristic extraction — the human will validate before applying.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pdfplumber

VERBS = [
    "Sustitúyese", "Sustitúyase", "Sustitúyense",
    "Reemplázase", "Reemplázanse",
    "Agrégase", "Agréguese", "Agréganse",
    # Incorpórase (singular) and Incorpóranse (plural) — both appear in Ley 21.719
    "Incorpórase", "Incorpórense", "Incorpóranse",
    "Elimínase", "Elimínanse",
    "Modifícase", "Modifícanse",
    # Intercálase (singular) and Intercálanse (plural)
    "Intercálase", "Intercálanse",
    "Introdúcense", "Derógase",
]
VERB_RE = re.compile(r"\b(" + "|".join(VERBS) + r")\b", re.IGNORECASE)

# Match top-level numbered items: "1) ", "2) ", ..., "16) "
# Must appear at start of a line (after optional whitespace).
NUMBERED_RE = re.compile(r"^\s*(\d+)\)\s+", re.MULTILINE)

# Match sub-items in Spanish cardinal: "uno) ", "dos) ", etc.
# Must appear at start of a line (after optional whitespace).
SUB_NUMBERED_RE = re.compile(
    r"^\s*(uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez)\)\s+",
    re.MULTILINE | re.IGNORECASE,
)

# BCN-inserted page-break lines to strip (e.g. "Biblioteca del Congreso... página 3 de 56")
BCN_FOOTER_RE = re.compile(
    r"Biblioteca del Congreso Nacional de Chile - www\.leychile\.cl[^\n]*\n?"
    r"(?:Ley \d+\n?)?",
    re.IGNORECASE,
)


def read_pdf(path: Path) -> str:
    with pdfplumber.open(path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)


def _clean(text: str) -> str:
    """Remove BCN footer lines that interrupt the legal text."""
    return BCN_FOOTER_RE.sub("", text)


def parse(pdf_path: Path) -> list[dict]:
    raw_text = read_pdf(pdf_path)
    text = _clean(raw_text)

    # Locate the operative article body:
    # Start: immediately after "Artículo primero.-"
    # End:   at "Artículo segundo.-" (the first one in the law body)
    start = re.search(r"Art[íi]culo primero\.-", text)
    end = re.search(r"Art[íi]culo segundo\.-|DISPOSICIONES TRANSITORIAS", text)
    body = text[start.end() if start else 0 : end.start() if end else len(text)]

    items: list[dict] = []
    top_matches = list(NUMBERED_RE.finditer(body))

    for i, m in enumerate(top_matches):
        num = m.group(1)
        chunk_end = top_matches[i + 1].start() if i + 1 < len(top_matches) else len(body)
        chunk = body[m.end() : chunk_end].strip()

        verb_match = VERB_RE.search(chunk)
        verb = verb_match.group(1) if verb_match else ""

        # Store the parent item (even if it introduces sub-items — useful context)
        items.append({"amendment_num": num, "verb": verb, "text": chunk})

        # Sub-items using Spanish ordinals (uno, dos, tres, …)
        sub_matches = list(SUB_NUMBERED_RE.finditer(chunk))
        for j, sub_m in enumerate(sub_matches):
            sub_label = sub_m.group(1).lower()
            sub_end = sub_matches[j + 1].start() if j + 1 < len(sub_matches) else len(chunk)
            sub_chunk = chunk[sub_m.end() : sub_end].strip()
            sub_verb_m = VERB_RE.search(sub_chunk)
            items.append(
                {
                    "amendment_num": f"{num}.{sub_label}",
                    "verb": sub_verb_m.group(1) if sub_verb_m else "",
                    "text": sub_chunk,
                }
            )

    return items


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: parse_21719_amendments.py <pdf>", file=sys.stderr)
        sys.exit(2)
    json.dump(parse(Path(sys.argv[1])), sys.stdout, ensure_ascii=False, indent=2)
