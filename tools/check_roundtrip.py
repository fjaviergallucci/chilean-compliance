"""Sample-based Spanish-text fidelity check against the source PDF.

For each sampled article, normalize whitespace and compare the Spanish
block in the corpus to the extracted PDF text. Report articles whose
similarity falls below the threshold.
"""
from __future__ import annotations

import argparse
import random
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

from tools.extract_articles import extract_articles

ANCHOR_BLOCK_RE = re.compile(
    r"##\s+(?:Article\s+)?"
    r"(\d+(?:\s+bis|\s+ter|\s+qu[áa]ter|\s+quinquies|\s+sexies|\s+septies|\s+octies|\s+nonies)?"
    r"|[IVXLC]+(?:\.[A-Z0-9]+)*)"
    r"\b.*?### Original Spanish\s*\n>\s*\"(.+?)\"",
    re.DOTALL | re.IGNORECASE,
)


def _normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def check(pdf_path: Path, corpus_dir: Path, sample: int, threshold: float) -> list[tuple[str, float]]:
    pdf_blocks = {b["article_num"]: b["spanish_text"] for b in extract_articles(pdf_path)}
    corpus_blocks: dict[str, str] = {}
    for md in corpus_dir.rglob("*.md"):
        for m in ANCHOR_BLOCK_RE.finditer(md.read_text(encoding="utf-8")):
            corpus_blocks[m.group(1).strip()] = m.group(2)

    common = sorted(set(pdf_blocks) & set(corpus_blocks), key=lambda x: (len(x), x))
    if sample and sample < len(common):
        common = random.sample(common, sample)

    failures: list[tuple[str, float]] = []
    for num in common:
        ratio = SequenceMatcher(None, _normalize(pdf_blocks[num]), _normalize(corpus_blocks[num])).ratio()
        if ratio < threshold:
            failures.append((num, ratio))
    return failures


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("corpus_dir")
    ap.add_argument("--sample", type=int, default=10, help="0 = check all articles")
    ap.add_argument("--threshold", type=float, default=0.85)
    args = ap.parse_args()
    failures = check(Path(args.pdf), Path(args.corpus_dir), args.sample, args.threshold)
    if not failures:
        print("OK: sampled articles match within threshold")
        sys.exit(0)
    for num, ratio in failures:
        print(f"  Article {num}: similarity {ratio:.2f} < {args.threshold}")
    sys.exit(1)
