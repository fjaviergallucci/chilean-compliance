"""Parse NCG 524's amendment instructions targeting NCG 502 into records.

NCG 524 is amendment-formatted: numbered operative items using verbs like
Reemplázase / Sustitúyese / Intercálase / Agrégase / Elimínase / Modifícase,
each pointing at a section of NCG 502. Heuristic extraction; the human
validates before applying.

Structure of NCG 524:
  I. MODIFÍQUESE LA NCG 502 …
    A. En la sección I         <- capital-letter top group
      a. En el Título A. …    <- lowercase subsection header (a–z, aa–nn)
        1. Reemplázase …      <- numbered amendment item
        2. Intercálase …
      b. En el Título C.2. …
        1. Elimínase …
    B. En la sección II:
      1. Reemplázase …        <- items directly under capital section
      2. Elimínase …
      a. En el Título A. …
        1. Agrégase …
    E. En la sección V:
      a. Reemplázase …        <- replacement of whole section (not in SUBSEC_RE, handled as direct)
      G. En las secciones VI…  <- further sub-groups within the replacement text
        1. Reemplázase …
  II. VIGENCIA               <- end of operative text

Extraction technique: multi-line curly-quoted replacement blocks (U+201C…U+201D spanning
newlines) are stripped before item matching to avoid false positives from numbered lists
inside new legal text.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pdfplumber

# All amendment verb forms encountered in NCG 524 (including typographic variants)
_VERB_PAT = (
    r"Reempl[áa]z[ao](?:se|nse)"
    r"|Elim[íi]n[ao](?:se|nse)|Elim[íi]n[ae]se"
    r"|Agr[eé]g[au](?:e|se)|Agr[eé]g[ao]nse"
    r"|Int[eé]rc[áa]lase|Interc[áa]l[ao]nse"
    r"|Modif[íi]c[ao](?:se|nse)"
    r"|Sustitúyese|Sustitúyanse"
    r"|Incorp[oó]r[ao](?:se|nse)"
    r"|Der[oó]g[ao]se"
)
VERB_RE = re.compile(r"\b(" + _VERB_PAT + r")\b", re.IGNORECASE)

# Numbered amendment item at line start (digits + period or parenthesis + space)
# Anchored to amendment verbs OR location phrases ("En el …", "En la …", etc.)
INSTR_RE = re.compile(
    r"^\s{0,4}(\d+)[.)]\s+("
    + _VERB_PAT
    + r"|En el |En la |En los |En las "
    r")",
    re.MULTILINE | re.IGNORECASE,
)

# Capital-letter top group: "A. En la sección I", …, "E. En la sección V"
CAP_SECTION_RE = re.compile(
    r"^([A-G])\.\s+En (?:la|las|el|los) secci[oó]n",
    re.MULTILINE,
)

# Lowercase subsection header within a capital group.
# Codes go from "a." through "nn." (1–2 letter pairs).
# Anchored to "En el/los Título" or "Agrégase al final" to avoid roman-numeral false positives.
SUBSEC_RE = re.compile(
    r"^\s*([a-z]{1,2})\.\s+"
    r"(?:En (?:el|los)\s+T[íi]tulo|Agr[eé]g[au](?:e|se)\s+al\s+final)",
    re.MULTILINE,
)

# End of operative text
END_RE = re.compile(r"^II\.\s+VIGENCIA", re.MULTILINE)

# Multi-line curly-quoted replacement blocks — strip these to avoid false positives
_OPEN_Q = "“"
_CLOSE_Q = "”"
_MULTILINE_QUOTE_RE = re.compile(
    _OPEN_Q + r"[^" + _CLOSE_Q + r"]*\n[^" + _CLOSE_Q + r"]*" + _CLOSE_Q,
    re.DOTALL,
)


def _read(path: Path) -> str:
    with pdfplumber.open(path) as pdf:
        return "\n".join(p.extract_text() or "" for p in pdf.pages)


def _extract_items(
    chunk: str, subsection_label: str, section_label: str
) -> list[dict]:
    """Extract numbered amendment items from a chunk of text.

    Multi-line replacement blocks (curly-quoted) are stripped first to prevent
    numbered lists inside new legal text from being captured as amendment items.
    Item text begins at the verb/instruction phrase (group 2 of INSTR_RE).
    """
    stripped = _MULTILINE_QUOTE_RE.sub("[…]", chunk)
    instr_matches = list(INSTR_RE.finditer(stripped))
    items = []
    for ii, im in enumerate(instr_matches):
        # Item text starts at group(2) — the verb or location phrase
        text_start = im.start(2)
        item_end = (
            instr_matches[ii + 1].start()
            if ii + 1 < len(instr_matches)
            else len(stripped)
        )
        item_text = stripped[text_start:item_end].strip()
        verb_m = VERB_RE.search(item_text)
        items.append(
            {
                "item": im.group(1),
                "subsection": subsection_label,
                "section": section_label,
                "verb": verb_m.group(1) if verb_m else "",
                "text": item_text,
            }
        )
    return items


def parse(pdf_path: Path) -> list[dict]:
    """Parse NCG 524 and return a list of amendment item dicts."""
    text = _read(pdf_path)

    # Bound to operative text (before "II. VIGENCIA")
    end_match = END_RE.search(text)
    body = text[: end_match.start()] if end_match else text

    cap_sections = list(CAP_SECTION_RE.finditer(body))
    subsec_matches = list(SUBSEC_RE.finditer(body))

    all_items: list[dict] = []

    for ci, cs in enumerate(cap_sections):
        cap_end = (
            cap_sections[ci + 1].start() if ci + 1 < len(cap_sections) else len(body)
        )
        cap_label = body[cs.start() : cs.start() + 80].split("\n")[0].strip()
        cap_chunk_start = cs.end()
        cap_chunk = body[cap_chunk_start:cap_end]

        # Subsection headers within this capital section
        subsecs_in_cap = [
            sm
            for sm in subsec_matches
            if cap_chunk_start <= sm.start() < cap_chunk_start + len(cap_chunk)
        ]

        # Direct items: those before the first subsection letter header in this section
        if subsecs_in_cap:
            direct_chunk = cap_chunk[
                : subsecs_in_cap[0].start() - cap_chunk_start
            ]
        else:
            direct_chunk = cap_chunk

        direct_items = _extract_items(
            direct_chunk, cap_label + " (direct)", cap_label
        )
        all_items.extend(direct_items)

        # Items under each lowercase subsection
        for si, sm in enumerate(subsecs_in_cap):
            sub_end_abs = (
                subsecs_in_cap[si + 1].start()
                if si + 1 < len(subsecs_in_cap)
                else cap_chunk_start + len(cap_chunk)
            )
            sub_label = body[sm.start() : sm.start() + 120].split("\n")[0].strip()
            sub_chunk = body[sm.end() : sub_end_abs]
            sub_items = _extract_items(sub_chunk, sub_label, cap_label)
            all_items.extend(sub_items)

    return all_items


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: parse_524_amendments.py <pdf>", file=sys.stderr)
        sys.exit(2)
    json.dump(parse(Path(sys.argv[1])), sys.stdout, ensure_ascii=False, indent=2)
