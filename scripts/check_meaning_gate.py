#!/usr/bin/env python3
"""Writing Style Engine - deterministic meaning-preservation gate, version 0.1.0.

Checks protected literals and high-risk surface facts. It is intentionally
conservative and is NOT a substitute for semantic entailment or human review.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

VERSION = "0.1.0"
URL_RE = re.compile(r"https?://[^\s)\]}>,]+", re.I)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.I)
NUMBER_RE = re.compile(r"(?<!\w)[+-]?\d+(?:[.,]\d+)?(?:\s*%)?(?!\w)")
DATE_ISO_RE = re.compile(r"\b(?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2}\b")
CAP_ID_RE = re.compile(r"\b[A-Z][A-Z0-9_-]{2,}\b")
EN_NEG = re.compile(r"\b(?:no|not|never|without|cannot|can't|didn't|doesn't|isn't|aren't|wasn't|weren't)\b", re.I)
FA_NEG = re.compile("(?:\\u0646\\u0647|\\u0647\\u0631\\u06af\\u0632|\\u0628\\u062f\\u0648\\u0646|\\u0646\\u0645\\u06cc\\u200c|\\u0646\\u0628\\u0648\\u062f|\\u0646\\u06cc\\u0633\\u062a|\\u0646\\u0634\\u062f)")


def extract_high_risk(text: str) -> dict[str, Counter[str]]:
    return {
        "urls": Counter(URL_RE.findall(text)),
        "emails": Counter(EMAIL_RE.findall(text)),
        "dois": Counter(item.rstrip(".,;") for item in DOI_RE.findall(text)),
        "numbers": Counter(item.replace(" ", "") for item in NUMBER_RE.findall(text)),
        "iso_dates": Counter(DATE_ISO_RE.findall(text)),
        "capitalized_ids": Counter(CAP_ID_RE.findall(text)),
    }


def counter_diff(a: Counter[str], b: Counter[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for key in sorted(set(a) | set(b)):
        delta = b.get(key, 0) - a.get(key, 0)
        if delta:
            result[key] = delta
    return result


def normalize_literal(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--protected", type=Path, default=None, help="UTF-8 file; one exact protected phrase per line")
    parser.add_argument("--json-output", type=Path, default=None)
    parser.add_argument("--allow-new-numbers", action="store_true")
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    candidate = args.candidate.read_text(encoding="utf-8")
    source_facts = extract_high_risk(source)
    candidate_facts = extract_high_risk(candidate)
    diffs = {key: counter_diff(source_facts[key], candidate_facts[key]) for key in source_facts}
    failures: list[str] = []
    warnings: list[str] = []

    for category, diff in diffs.items():
        if not diff:
            continue
        removed = [item for item, delta in diff.items() if delta < 0]
        added = [item for item, delta in diff.items() if delta > 0]
        if removed:
            failures.append(f"removed {category}: {removed}")
        if added:
            if category == "numbers" and args.allow_new_numbers:
                warnings.append(f"added numbers allowed by flag: {added}")
            else:
                failures.append(f"added {category}: {added}")

    protected_missing = []
    if args.protected:
        protected = [line.strip() for line in args.protected.read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
        candidate_norm = normalize_literal(candidate)
        for phrase in protected:
            if normalize_literal(phrase) not in candidate_norm:
                protected_missing.append(phrase)
        if protected_missing:
            failures.append(f"missing protected phrases: {protected_missing}")

    source_neg = len(EN_NEG.findall(source)) + len(FA_NEG.findall(source))
    candidate_neg = len(EN_NEG.findall(candidate)) + len(FA_NEG.findall(candidate))
    if source_neg != candidate_neg:
        warnings.append(f"negation-marker count changed: source={source_neg} candidate={candidate_neg}; human/semantic review required")

    result = {
        "version": VERSION,
        "pass": not failures,
        "failures": failures,
        "warnings": warnings,
        "surface_fact_differences": diffs,
        "protected_missing": protected_missing,
        "limitations": [
            "Does not prove paraphrase equivalence or factual entailment.",
            "Does not reliably detect changed causal direction, modality, scope, actor roles, or Persian negation morphology.",
            "Use semantic metrics and human/domain review for critical content.",
        ],
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_output:
        args.json_output.write_text(payload, encoding="utf-8")
    print(payload)
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
