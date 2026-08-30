#!/usr/bin/env python3
"""Writing Style Engine - deterministic style feature extractor, version 0.1.0.

This is a reproducible baseline for observable surface features. It intentionally
DOES NOT claim to measure metaphor, rhetorical moves, jargon, syntactic depth,
semantic preservation, or tone perception without additional validated tools or
human annotation.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable

VERSION = "0.1.0"
WORD_RE = re.compile(r"[A-Za-z]+(?:['-][A-Za-z]+)*|[\u0600-\u06FF]+(?:\u200c[\u0600-\u06FF]+)*|\d+(?:[.,]\d+)?", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?\u061f])\s+|\n+(?=\S)")
URL_RE = re.compile(r"https?://\S+", re.I)
QUOTE_RE = re.compile(r"[\"'\u00ab\u00bb\u201c\u201d\u2018\u2019]")
EN_PRONOUNS = {"i","me","my","mine","we","us","our","ours","you","your","yours","he","him","his","she","her","hers","they","them","their","theirs","it","its"}
FA_PRONOUNS = {"\u0645\u0646","\u0645\u0627","\u062a\u0648","\u0634\u0645\u0627","\u0627\u0648","\u0627\u06cc\u0634\u0627\u0646","\u0622\u0646\u0647\u0627","\u0622\u0646\u200c\u0647\u0627","\u0622\u0646","\u0627\u06cc\u0646"}
EN_HEDGES = {"may","might","could","can","perhaps","possibly","probably","likely","unlikely","suggest","suggests","suggested","appear","appears","seem","seems","approximately","about","around","generally","often","sometimes","typically"}
FA_HEDGES = {"\u0645\u0645\u06a9\u0646","\u0634\u0627\u06cc\u062f","\u0627\u062d\u062a\u0645\u0627\u0644\u0627","\u0627\u062d\u062a\u0645\u0627\u0644\u0627\u064b","\u0627\u062d\u062a\u0645\u0627\u0644","\u062a\u0642\u0631\u06cc\u0628\u0627","\u062a\u0642\u0631\u06cc\u0628\u0627\u064b","\u0638\u0627\u0647\u0631\u0627","\u0638\u0627\u0647\u0631\u0627\u064b","\u0628\u0647\u200c\u0646\u0638\u0631","\u0628\u0647","\u0646\u0638\u0631","\u0645\u06cc\u200c\u0631\u0633\u062f","\u0639\u0645\u0648\u0645\u0627","\u0639\u0645\u0648\u0645\u0627\u064b"}
EN_TRANSITIONS = {"however","therefore","moreover","furthermore","meanwhile","instead","thus","nevertheless","consequently","similarly","finally","first","second"}
FA_TRANSITIONS = {"\u0627\u0645\u0627","\u0628\u0646\u0627\u0628\u0631\u0627\u06cc\u0646","\u062f\u0631\u0646\u062a\u06cc\u062c\u0647","\u0647\u0645\u0686\u0646\u06cc\u0646","\u062f\u0631\u0645\u0642\u0627\u0628\u0644","\u0628\u0627\u0627\u06cc\u0646\u200c\u062d\u0627\u0644","\u0627\u0632\u0633\u0648\u06cc\u200c\u062f\u06cc\u06af\u0631","\u0646\u062e\u0633\u062a","\u062f\u0648\u0645","\u062f\u0631\u0646\u0647\u0627\u06cc\u062a"}


def words(text: str) -> list[str]:
    return [m.group(0) for m in WORD_RE.finditer(text)]


def sentences(text: str) -> list[str]:
    cleaned = re.sub(URL_RE, " URL ", text.strip())
    if not cleaned:
        return []
    chunks = [part.strip() for part in SENTENCE_RE.split(cleaned) if part.strip()]
    return chunks or [cleaned]


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n+", text.strip()) if p.strip()]


def percentile(values: list[int], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return float(ordered[lo])
    return ordered[lo] * (hi - pos) + ordered[hi] * (pos - lo)


def mattr(tokens: list[str], window: int = 50) -> float:
    normalized = [token.casefold() for token in tokens if not token.isdigit()]
    if not normalized:
        return 0.0
    if len(normalized) <= window:
        return len(set(normalized)) / len(normalized)
    scores = []
    for start in range(0, len(normalized) - window + 1):
        sample = normalized[start:start + window]
        scores.append(len(set(sample)) / window)
    return statistics.fmean(scores)


def rate(count: float, denominator: float, scale: float = 100.0) -> float:
    return 0.0 if denominator <= 0 else count / denominator * scale


def exact_ngram_hits(tokens: list[str], lexicon: set[str]) -> int:
    folded = [token.casefold() for token in tokens]
    unigrams = Counter(folded)
    total = sum(unigrams.get(item, 0) for item in lexicon if " " not in item)
    phrase_items = [item for item in lexicon if " " in item]
    if phrase_items:
        joined = " ".join(folded)
        total += sum(len(re.findall(r"(?<!\w)" + re.escape(item) + r"(?!\w)", joined)) for item in phrase_items)
    return total


def extract(record: dict[str, str]) -> dict[str, object]:
    text = record.get("text", "") or ""
    title = record.get("title", "") or ""
    language = (record.get("language", "") or "unknown").lower()
    toks = words(text)
    sents = sentences(text)
    paras = paragraphs(text)
    sent_lengths = [len(words(item)) for item in sents]
    para_lengths = [len(words(item)) for item in paras]
    lower_tokens = [token.casefold() for token in toks]
    pronouns = EN_PRONOUNS | FA_PRONOUNS
    hedges = EN_HEDGES | FA_HEDGES
    transitions = EN_TRANSITIONS | FA_TRANSITIONS
    punctuation_counts = {char: text.count(char) for char in ["?", "\u061f", "!", ":", ";", "\u061b", "-", "\u2014", "(", ")"]}
    title_tokens = words(title)
    return {
        "id": record.get("id", ""),
        "language": language,
        "word_count": len(toks),
        "sentence_count": len(sents),
        "paragraph_count": len(paras),
        "mean_sentence_words": round(statistics.fmean(sent_lengths), 4) if sent_lengths else 0.0,
        "p90_sentence_words": round(percentile(sent_lengths, 0.90), 4),
        "mean_paragraph_words": round(statistics.fmean(para_lengths), 4) if para_lengths else 0.0,
        "type_token_ratio": round(len(set(lower_tokens)) / len(lower_tokens), 4) if lower_tokens else 0.0,
        "mattr_50": round(mattr(toks, 50), 4),
        "avg_token_chars": round(statistics.fmean([len(token) for token in toks]), 4) if toks else 0.0,
        "question_per_100_sentences": round(rate(punctuation_counts["?"] + punctuation_counts["\u061f"], len(sents)), 4),
        "exclamation_per_100_sentences": round(rate(punctuation_counts["!"], len(sents)), 4),
        "colon_per_100_sentences": round(rate(punctuation_counts[":"], len(sents)), 4),
        "semicolon_per_100_sentences": round(rate(punctuation_counts[";"] + punctuation_counts["\u061b"], len(sents)), 4),
        "dash_per_100_sentences": round(rate(punctuation_counts["-"] + punctuation_counts["\u2014"], len(sents)), 4),
        "parenthesis_pairs_per_100_sentences": round(rate(min(punctuation_counts["("], punctuation_counts[")"]), len(sents)), 4),
        "quote_marks_per_100_words": round(rate(len(QUOTE_RE.findall(text)), len(toks)), 4),
        "pronoun_hits_per_100_words": round(rate(exact_ngram_hits(toks, pronouns), len(toks)), 4),
        "hedge_modal_hits_per_100_words": round(rate(exact_ngram_hits(toks, hedges), len(toks)), 4),
        "transition_hits_per_100_words": round(rate(exact_ngram_hits(toks, transitions), len(toks)), 4),
        "headline_word_count": len(title_tokens),
        "headline_char_count": len(title.strip()),
        "headline_is_question": int(bool(re.search(r"[?\u061f]\s*$", title))),
        "headline_has_colon": int(":" in title),
        "headline_has_number": int(bool(re.search(r"\d", title))),
        "url_count": len(URL_RE.findall(text)),
        "feature_version": VERSION,
        "measurement_warning": "surface baseline only; Persian pronoun counts are incomplete because Persian permits pro-drop; validate lexicons and perceptual effects in Persian",
    }


def read_records(path: Path) -> Iterable[dict[str, str]]:
    if path.suffix.lower() in {".jsonl", ".ndjson"}:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"invalid JSON at line {line_number}: {exc}") from exc
                yield {str(k): "" if v is None else str(v) for k, v in data.items()}
        return
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            yield {str(k): "" if v is None else str(v) for k, v in row.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args()
    records = list(read_records(args.input))
    required = {"id", "text"}
    if records and not required.issubset(records[0]):
        print("ERROR input must contain id and text fields; title and language are optional", file=sys.stderr)
        return 2
    features = [extract(item) for item in records]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() in {".jsonl", ".ndjson"}:
        with args.output.open("w", encoding="utf-8") as handle:
            for row in features:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    else:
        fields = list(features[0].keys()) if features else []
        with args.output.open("w", encoding="utf-8", newline="") as handle:
            if fields:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(features)
    print(f"extracted {len(features)} records with feature schema {VERSION} -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
