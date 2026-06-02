"""Verify every NCG section in a _toc.json appears once in the corpus."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

# Anchor: "## I.A.2 — Title" or "## I.A.2 - Title". Capture the section number.
ANCHOR_RE = re.compile(
    r"^##\s+([IVXLC]+(?:\.[A-Z0-9]+)*|\d+(?:\.\d+)*)\s+[—-]",
    re.MULTILINE,
)


@dataclass
class NcgParityResult:
    missing: list[str] = field(default_factory=list)
    duplicated: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.missing and not self.duplicated


def check_ncg_parity(toc_path: Path, corpus_dir: Path,
                     exclude: list[str] | None = None) -> NcgParityResult:
    excluded = set(exclude or [])
    toc = json.loads(Path(toc_path).read_text(encoding="utf-8"))
    expected = {e["number"] for e in toc if e["number"] not in excluded}
    seen: dict[str, int] = {}
    for md in Path(corpus_dir).rglob("*.md"):
        for m in ANCHOR_RE.finditer(md.read_text(encoding="utf-8")):
            num = m.group(1)
            seen[num] = seen.get(num, 0) + 1
    missing = sorted(expected - set(seen))
    duplicated = sorted(n for n, c in seen.items() if c > 1)
    return NcgParityResult(missing=missing, duplicated=duplicated)


if __name__ == "__main__":
    import argparse
    import sys

    ap = argparse.ArgumentParser()
    ap.add_argument("toc_json")
    ap.add_argument("corpus_dir")
    ap.add_argument("--exclude", action="append", default=[],
                    help="Section number to drop from the expected set (repeatable)")
    args = ap.parse_args()
    result = check_ncg_parity(Path(args.toc_json), Path(args.corpus_dir),
                              exclude=args.exclude)
    if result.ok:
        print("OK: all NCG sections present, no duplicates")
        sys.exit(0)
    if result.missing:
        print(f"MISSING ({len(result.missing)}): {result.missing}")
    if result.duplicated:
        print(f"DUPLICATED ({len(result.duplicated)}): {result.duplicated}")
    sys.exit(1)
