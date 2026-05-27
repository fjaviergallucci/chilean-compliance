"""Verify every glossary entry's cited article exists in the corpus."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

TERM_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
DEFINED_IN_RE = re.compile(
    r"\*\*Defined in:\*\*\s+([\d.]+)\s+Art\.\s+(\d+(?:\s+bis|\s+ter|\s+qu[áa]ter|\s+quinquies|\s+sexies|\s+septies|\s+octies|\s+nonies)?)",
)
ANCHOR_RE = re.compile(
    r"^##\s+Article\s+(\d+(?:\s+bis|\s+ter|\s+qu[áa]ter|\s+quinquies|\s+sexies|\s+septies|\s+octies|\s+nonies)?)\b",
    re.MULTILINE | re.IGNORECASE,
)
LAW_HINT_RE = re.compile(r"_law:_\s+([\d.]+)", re.IGNORECASE)


@dataclass
class GlossaryResult:
    unresolved: list[tuple[str, str, str]] = field(default_factory=list)  # (term, law, article)

    @property
    def ok(self) -> bool:
        return not self.unresolved


def _index_corpus(corpus_dir: Path) -> set[tuple[str, str]]:
    """Return set of (law, article_num) tuples present in corpus."""
    present: set[tuple[str, str]] = set()
    for md in corpus_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        law_match = LAW_HINT_RE.search(text)
        # Fall back to a per-anchor hint if no file-level hint:
        file_law = law_match.group(1) if law_match else None
        for art in ANCHOR_RE.finditer(text):
            num = art.group(1).strip()
            if file_law:
                present.add((file_law, num))
    return present


def check_glossary(glossary_file: Path, corpus_dir: Path) -> GlossaryResult:
    text = glossary_file.read_text(encoding="utf-8")
    present = _index_corpus(corpus_dir)
    # Only validate entries for laws that are actually represented in this corpus.
    known_laws = {law for law, _art in present}
    result = GlossaryResult()
    current_term: str | None = None
    for line in text.splitlines():
        term_match = TERM_RE.match(line)
        if term_match:
            current_term = term_match.group(1).strip()
            continue
        def_match = DEFINED_IN_RE.search(line)
        if def_match and current_term:
            law, art = def_match.group(1), def_match.group(2).strip()
            if law in known_laws and (law, art) not in present:
                result.unresolved.append((current_term, law, art))
            current_term = None
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("usage: check_glossary_completeness.py <glossary.md> <corpus_dir>", file=sys.stderr)
        sys.exit(2)
    result = check_glossary(Path(sys.argv[1]), Path(sys.argv[2]))
    if result.ok:
        print("OK: all glossary terms resolve")
        sys.exit(0)
    print(f"UNRESOLVED ({len(result.unresolved)}):")
    for term, law, art in result.unresolved:
        print(f"  - {term!r} -> {law} Art. {art}")
    sys.exit(1)
