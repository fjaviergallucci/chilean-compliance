"""Sample-based Spanish-text fidelity check against the source PDF.

For each sampled article, normalize whitespace and compare the Spanish
block in the corpus to the extracted PDF text. Report articles whose
similarity falls below the threshold.

NCG mode (--mode ncg): instead of per-article matching, verify that each
corpus section's Original Spanish block is present in the PDF full text
via substring containment or longest-match coverage.
"""
from __future__ import annotations

import argparse
import random
import re
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import pdfplumber

from tools.extract_articles import extract_articles

ANCHOR_BLOCK_RE = re.compile(
    r"##\s+(?:Article\s+)?"
    r"(\d+(?:\s+bis|\s+ter|\s+qu[áa]ter|\s+quinquies|\s+sexies|\s+septies|\s+octies|\s+nonies)?"
    r"|[IVXLC]+(?:\.[A-Z0-9]+)*)"
    r"\b.*?### Original Spanish\s*\n>\s*\"(.+?)\"",
    re.DOTALL | re.IGNORECASE,
)

# Minimum normalized length for a block to be considered non-trivial.
_TRIVIAL_THRESHOLD = 40


def _normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def _normalize_ncg(s: str) -> str:
    """Like _normalize but also strips Unicode combining marks (accents).

    NCG PDFs often extract accented characters as replacement characters
    (U+FFFD or similar), so normalizing both corpus and PDF text to their
    accent-free equivalents enables reliable substring matching.

    NCG 524 uses a narrow two-column justified layout whose pdfplumber
    extraction yields hard-hyphenated line breaks: a word is split across
    lines with a trailing hyphen (regular U+002D or soft-hyphen U+00AD)
    followed by a newline or other whitespace, then the remainder in
    lowercase.  De-hyphenate these splits BEFORE whitespace collapse so
    that clean corpus text ("instrumento") matches the PDF fragment
    ("instru-\\nsable").  Only join when the character resuming after the
    hyphen+whitespace is lowercase — line-break continuations always are,
    while genuine "- Word" list/dash patterns start with a capital.
    """
    # De-hyphenate line-break splits: letter + hyphen + whitespace + lowercase letter
    s = re.sub(r"([A-Za-zÁÉÍÓÚáéíóúÑñ])[­\-]\s+([a-záéíóúñ])", r"\1\2", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def _extract_pdf_full_text(pdf_path: Path) -> str:
    """Extract all text from a PDF using pdfplumber."""
    parts: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                parts.append(text)
    return "\n".join(parts)


def _parse_ncg_corpus_blocks(corpus_dir: Path) -> list[tuple[str, str]]:
    """Parse all corpus .md files and extract (identifier, spanish_text) pairs.

    Splits each file at ``^## `` section boundaries, then within each section
    locates the ``### Original Spanish`` subsection and extracts blockquote lines.
    """
    results: list[tuple[str, str]] = []
    for md in sorted(corpus_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        lines = text.splitlines()

        # Split into section blocks at lines starting with "## "
        section_starts: list[int] = []
        for i, line in enumerate(lines):
            if line.startswith("## "):
                section_starts.append(i)

        for idx, start in enumerate(section_starts):
            end = section_starts[idx + 1] if idx + 1 < len(section_starts) else len(lines)
            section_lines = lines[start:end]

            # Identifier: token after "## " (e.g. "I.A")
            header = section_lines[0][3:].strip()  # strip "## "
            identifier = header.split()[0].rstrip("—").rstrip()

            # Find "### Original Spanish" within this section
            orig_start: int | None = None
            for j, line in enumerate(section_lines):
                if line.strip() == "### Original Spanish":
                    orig_start = j + 1
                    break
            if orig_start is None:
                continue

            # Collect blockquote lines until next ### subsection, "> **…**" marker,
            # or end.  Stop on any line starting with "> **" (covers both
            # "> **Source:**" and "> **TN:**" annotation lines that may follow
            # the closing quote of the Spanish block).
            bq_parts: list[str] = []
            for line in section_lines[orig_start:]:
                if line.startswith("###"):
                    break
                if line.startswith("> **"):
                    break
                if line.startswith("> ") or line == ">":
                    content = line[2:] if line.startswith("> ") else ""
                    # Strip surrounding double-quotes (first/last line may have them)
                    content = content.strip('"')
                    bq_parts.append(content)

            spanish_text = " ".join(bq_parts).strip().strip('"')
            if spanish_text:
                results.append((identifier, spanish_text))

    return results


def _chunk_coverage(block_norm: str, pdf_norm: str, chunk_size: int = 100, step: int = 80) -> float:
    """Estimate what fraction of *block_norm* appears in *pdf_norm*.

    Slides a fixed-size window over the block; each chunk that is found as a
    literal substring of the PDF text contributes ``chunk_size`` matched chars.
    Because blocks can span PDF page-breaks (which introduce different
    whitespace), an exact full-block substring check often misses even perfectly
    transcribed content.  This sliding-window approach is fast (O(n) Python
    ``in`` checks) and handles multi-page blocks reliably.
    """
    if not block_norm:
        return 1.0
    # Fast path: whole block is a literal substring
    if block_norm in pdf_norm:
        return 1.0
    total = len(block_norm)
    matched = 0
    i = 0
    while i < total:
        chunk = block_norm[i : i + chunk_size]
        if len(chunk) < 20:
            break
        if chunk in pdf_norm:
            matched += len(chunk)
            i += chunk_size  # full advance — no overlap counted
        else:
            i += step  # slide forward by step
    return min(matched / total, 1.0)


def check_ncg(
    pdf_path: Path,
    corpus_dir: Path,
    threshold: float,
    exclude: list[str] | None = None,
) -> list[tuple[str, float]]:
    """Check NCG corpus Spanish blocks against the PDF full text.

    For each section's Original Spanish block, verify it appears in the PDF
    via substring containment or chunked coverage >= threshold.  Both the
    corpus block and the PDF text are accent-stripped (via *_normalize_ncg*)
    so that PDF encoding artifacts (accented chars extracted as replacement
    chars) do not cause false failures.

    *exclude* is an optional list of section identifiers (e.g. ``["I.A"]``)
    that will be silently skipped — useful for intercalación sections whose
    spliced wording cannot reach threshold in any single source PDF.

    Returns a list of (identifier, coverage) for blocks that fail.
    """
    _exclude: set[str] = set(exclude) if exclude else set()
    full_text = _extract_pdf_full_text(pdf_path)
    pdf_norm = _normalize_ncg(full_text)

    blocks = _parse_ncg_corpus_blocks(corpus_dir)
    failures: list[tuple[str, float]] = []

    for identifier, spanish_text in blocks:
        if identifier in _exclude:
            continue

        block_norm = _normalize_ncg(spanish_text)

        # Skip trivial/heading-only blocks (e.g. parent section headings)
        if len(block_norm) < _TRIVIAL_THRESHOLD:
            continue

        coverage = _chunk_coverage(block_norm, pdf_norm)
        if coverage < threshold:
            failures.append((identifier, coverage))

    return failures


def check_ncg_multi(
    pdf_paths,
    corpus_dir,
    threshold: float,
    exclude: list[str] | None = None,
) -> list[tuple[str, float]]:
    """NCG round-trip against multiple source PDFs.

    A corpus section's Spanish block passes if its chunk-coverage is >=
    threshold against ANY of the supplied PDFs.  For consolidated corpora
    whose text comes from a baseline PDF plus amendment PDF(s).

    *exclude* is an optional list of section identifiers (e.g. ``["I.A",
    "I.C.2"]``) that will be silently skipped — useful for NCG 524
    intercalación sections whose spliced mid-sentence wording does not appear
    as a contiguous passage in either source PDF and therefore cannot reach
    threshold even when the corpus text is faithful.

    Returns a list of (section_id, best_coverage) for blocks below threshold.
    """
    _exclude: set[str] = set(exclude) if exclude else set()
    norms = [_normalize_ncg(_extract_pdf_full_text(Path(p))) for p in pdf_paths]
    failures: list[tuple[str, float]] = []
    for ident, spanish_text in _parse_ncg_corpus_blocks(Path(corpus_dir)):
        if ident in _exclude:
            continue
        bn = _normalize_ncg(spanish_text)
        if len(bn) < _TRIVIAL_THRESHOLD:
            continue
        best = max((_chunk_coverage(bn, n) for n in norms), default=0.0)
        if best < threshold:
            failures.append((ident, best))
    return failures


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
    ap.add_argument("--sample", type=int, default=10, help="0 = check all articles (law mode only)")
    ap.add_argument("--threshold", type=float, default=0.85)
    ap.add_argument("--mode", choices=["law", "ncg"], default="law",
                    help="'law' (default): per-article similarity check; 'ncg': full-text containment check")
    ap.add_argument("--also-pdf", action="append", default=[],
                    metavar="PDF",
                    help="(ncg mode) additional source PDF(s); when supplied, a section passes if it "
                         "matches ANY of the given PDFs (the primary pdf plus all --also-pdf paths)")
    ap.add_argument("--exclude", action="append", default=[],
                    metavar="SECTION",
                    help="(ncg mode) section identifier to skip in the round-trip check (may be "
                         "repeated). Use for intercalación sections whose spliced wording cannot "
                         "reach threshold in any single source PDF even when faithful.")
    args = ap.parse_args()

    if args.mode == "ncg":
        if args.also_pdf:
            pdf_paths = [args.pdf] + args.also_pdf
            failures = check_ncg_multi(pdf_paths, Path(args.corpus_dir), args.threshold,
                                       exclude=args.exclude)
            if not failures:
                print("OK: NCG sections match source PDFs within threshold")
                sys.exit(0)
            for identifier, coverage in failures:
                print(f"  {identifier}: coverage {coverage:.2f} < {args.threshold}")
            sys.exit(1)
        else:
            failures = check_ncg(Path(args.pdf), Path(args.corpus_dir), args.threshold,
                                 exclude=args.exclude)
            if not failures:
                print("OK: NCG sections match source PDF within threshold")
                sys.exit(0)
            for identifier, coverage in failures:
                print(f"  {identifier}: coverage {coverage:.2f} < {args.threshold}")
            sys.exit(1)
    else:
        failures = check(Path(args.pdf), Path(args.corpus_dir), args.sample, args.threshold)
        if not failures:
            print("OK: sampled articles match within threshold")
            sys.exit(0)
        for num, ratio in failures:
            print(f"  Article {num}: similarity {ratio:.2f} < {args.threshold}")
        sys.exit(1)
