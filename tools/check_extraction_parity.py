"""Verify every article in a PDF appears in exactly one corpus markdown file."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from tools.extract_articles import extract_articles

ANCHOR_RE = re.compile(
    r"^##\s+Article\s+(\d+(?:\s+bis|\s+ter|\s+qu[áa]ter|\s+quinquies|\s+sexies|\s+septies|\s+octies|\s+nonies)?)\b",
    re.MULTILINE | re.IGNORECASE,
)


@dataclass
class ParityResult:
    missing: list[str] = field(default_factory=list)
    duplicated: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.missing and not self.duplicated


def check_parity(
    pdf_path: Path,
    corpus_dir: Path,
    exclude_titulos: list[str] | None = None,
) -> ParityResult:
    excluded = set(exclude_titulos or [])
    expected = {
        b["article_num"]
        for b in extract_articles(pdf_path)
        if b["titulo"] not in excluded
    }
    seen: dict[str, int] = {}
    for md in corpus_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for match in ANCHOR_RE.finditer(text):
            num = match.group(1).strip()
            seen[num] = seen.get(num, 0) + 1

    missing = sorted(expected - set(seen), key=lambda x: (len(x), x))
    duplicated = sorted([n for n, c in seen.items() if c > 1], key=lambda x: (len(x), x))
    return ParityResult(missing=missing, duplicated=duplicated)


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(
        description="Verify every article in a PDF appears in exactly one corpus markdown file."
    )
    ap.add_argument("pdf", help="Path to the source PDF")
    ap.add_argument("corpus_dir", help="Path to the corpus directory")
    ap.add_argument(
        "--exclude-titulo",
        action="append",
        default=[],
        dest="exclude_titulos",
        metavar="ROMAN",
        help="Roman numeral of a Título to drop from the expected set (repeatable)",
    )
    args = ap.parse_args()
    result = check_parity(
        Path(args.pdf), Path(args.corpus_dir), exclude_titulos=args.exclude_titulos
    )
    if result.ok:
        print("OK: all articles present, no duplicates")
        raise SystemExit(0)
    if result.missing:
        print(f"MISSING ({len(result.missing)}): {result.missing}")
    if result.duplicated:
        print(f"DUPLICATED ({len(result.duplicated)}): {result.duplicated}")
    raise SystemExit(1)
