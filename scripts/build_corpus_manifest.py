#!/usr/bin/env python3
"""Writing Style Engine - corpus manifest builder, version 0.1.0.

Create a reproducible 160-item sampling manifest without downloading article text.
The manifest reserves matched sampling cells and records provenance/rights metadata.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

VERSION = "0.1.0"
OUTLETS = [
    "Nature",
    "Quanta Magazine",
    "Scientific American",
    "Science News",
    "STAT",
    "Undark",
    "Reuters",
    "Guardian Science",
]
TOPICS = ["biomedicine", "environment", "physical_science", "technology_methods"]
GENRES = ["news_report", "feature_explainer"]
LENGTH_BANDS = ["short_medium", "long"]
BASE_FIELDS = [
    "sample_id",
    "outlet",
    "url",
    "publication_date",
    "topic_family",
    "genre_family",
    "length_band",
    "author",
    "word_count",
    "local_path",
    "rights_note",
    "match_group",
    "status",
    "notes",
]


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for outlet_index, outlet in enumerate(OUTLETS, start=1):
        serial = 1
        for topic in TOPICS:
            for genre in GENRES:
                for length_band in LENGTH_BANDS:
                    rows.append(
                        {
                            "sample_id": f"M{outlet_index:02d}-{serial:02d}",
                            "outlet": outlet,
                            "url": "",
                            "publication_date": "",
                            "topic_family": topic,
                            "genre_family": genre,
                            "length_band": length_band,
                            "author": "",
                            "word_count": "",
                            "local_path": "",
                            "rights_note": "metadata-only until lawful local access is confirmed",
                            "match_group": f"{topic}__{genre}__{length_band}",
                            "status": "planned",
                            "notes": "pre-specified factorial matched cell",
                        }
                    )
                    serial += 1
        for topic_index, topic in enumerate(TOPICS):
            genre = GENRES[(outlet_index + topic_index) % len(GENRES)]
            length_band = LENGTH_BANDS[(outlet_index + topic_index // 2) % len(LENGTH_BANDS)]
            rows.append(
                {
                    "sample_id": f"M{outlet_index:02d}-{serial:02d}",
                    "outlet": outlet,
                    "url": "",
                    "publication_date": "",
                    "topic_family": topic,
                    "genre_family": genre,
                    "length_band": length_band,
                    "author": "",
                    "word_count": "",
                    "local_path": "",
                    "rights_note": "metadata-only until lawful local access is confirmed",
                    "match_group": f"{topic}__{genre}__{length_band}",
                    "status": "planned",
                    "notes": "pre-specified balanced replicate cell",
                }
            )
            serial += 1
    return rows


def write_manifest(path: Path) -> None:
    rows = build_rows()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=BASE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {path}")
    print("planned rows: 160; target completed corpus: 160; 20 samples per outlet")
    print("note: 16 factorial cells plus 4 balanced replicate cells per outlet")


def validate_manifest(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        missing_fields = [field for field in BASE_FIELDS if field not in fields]
        if missing_fields:
            print("ERROR missing fields: " + ", ".join(missing_fields), file=sys.stderr)
            return 2
        rows = list(reader)

    errors: list[str] = []
    warnings: list[str] = []
    ids = [row["sample_id"].strip() for row in rows]
    duplicate_ids = [key for key, count in Counter(ids).items() if key and count > 1]
    if duplicate_ids:
        errors.append("duplicate sample_id: " + ", ".join(duplicate_ids[:10]))

    completed = [row for row in rows if row["status"].strip().lower() in {"included", "complete", "completed"}]
    outlet_counts = Counter(row["outlet"].strip() for row in completed)
    author_counts = Counter(row["author"].strip() for row in completed if row["author"].strip())
    group_counts = Counter(row["match_group"].strip() for row in completed if row["match_group"].strip() and row["match_group"] != "reserve")

    for row in completed:
        if not row["url"].strip():
            warnings.append(f"{row['sample_id']}: completed row has no URL")
        if not row["local_path"].strip():
            warnings.append(f"{row['sample_id']}: completed row has no local_path")
        try:
            count = int(row["word_count"])
            if count <= 0:
                raise ValueError
        except ValueError:
            warnings.append(f"{row['sample_id']}: word_count is missing or invalid")

    if completed and len(completed) < 100:
        warnings.append("completed corpus is below the Candidate->Validated minimum of 100")
    if completed and len(completed) < 160:
        warnings.append("completed corpus is below the preferred initial target of 160")
    if completed:
        dominant_authors = [(name, count) for name, count in author_counts.items() if count / len(completed) > 0.10]
        if dominant_authors:
            warnings.append("repeat-author dominance above 10%: " + ", ".join(f"{name}={count}" for name, count in dominant_authors))
        if len(outlet_counts) < 2:
            warnings.append("only one outlet represented among completed rows")
        underfilled_groups = [group for group, count in group_counts.items() if count < 4]
        if underfilled_groups:
            warnings.append(f"{len(underfilled_groups)} matched groups have fewer than 4 completed samples")

    print(f"rows={len(rows)} completed={len(completed)} outlets_completed={len(outlet_counts)}")
    for outlet in OUTLETS:
        if completed:
            print(f"outlet_count[{outlet}]={outlet_counts.get(outlet, 0)}")
    for item in warnings[:30]:
        print("WARNING " + item)
    if len(warnings) > 30:
        print(f"WARNING ... {len(warnings) - 30} more")
    for item in errors:
        print("ERROR " + item, file=sys.stderr)
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=VERSION)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create", help="create a sampling manifest template")
    create.add_argument("output", type=Path)
    validate = sub.add_parser("validate", help="validate an existing manifest")
    validate.add_argument("manifest", type=Path)
    args = parser.parse_args()
    if args.command == "create":
        write_manifest(args.output)
        return 0
    return validate_manifest(args.manifest)


if __name__ == "__main__":
    raise SystemExit(main())
