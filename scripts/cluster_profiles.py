#!/usr/bin/env python3
"""Writing Style Engine - exploratory profile clustering baseline, version 0.1.0.

Use ONLY after topic, genre, source and length confounds have been matched or
residualized. This script proposes clusters; it does not validate a taxonomy.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VERSION = "0.1.0"
DEFAULT_EXCLUDE = {
    "word_count", "sentence_count", "paragraph_count", "headline_char_count",
    "url_count", "feature_version", "language", "id", "cluster",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("features_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--k-min", type=int, default=2)
    parser.add_argument("--k-max", type=int, default=6)
    parser.add_argument("--include-length-features", action="store_true")
    parser.add_argument("--allow-mixed-languages", action="store_true", help="unsafe exploratory override; prefer one language per clustering run")
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args()
    try:
        import numpy as np
        import pandas as pd
        from sklearn.cluster import AgglomerativeClustering
        from sklearn.impute import SimpleImputer
        from sklearn.metrics import silhouette_score
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
    except ImportError as exc:
        print("ERROR requires pandas, numpy, scikit-learn", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2

    frame = pd.read_csv(args.features_csv)
    if "language" in frame.columns:
        languages = sorted({str(value).strip().lower() for value in frame["language"].dropna() if str(value).strip()})
        if len(languages) > 1 and not args.allow_mixed_languages:
            print("ERROR mixed-language clustering is disabled by default: " + ", ".join(languages), file=sys.stderr)
            print("Run each language separately. Cross-language feature effects require independent validation.", file=sys.stderr)
            return 2
    if len(frame) < 6:
        print("ERROR clustering baseline requires at least 6 rows", file=sys.stderr)
        return 2
    numeric = frame.select_dtypes(include=[np.number]).columns.tolist()
    exclude = set(DEFAULT_EXCLUDE)
    if args.include_length_features:
        exclude -= {"word_count", "sentence_count", "paragraph_count", "headline_char_count"}
    features = [name for name in numeric if name not in exclude]
    if len(features) < 2:
        print("ERROR fewer than two numeric style features after exclusions", file=sys.stderr)
        return 2

    matrix = frame[features]
    prep = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
    x = prep.fit_transform(matrix)
    max_k = min(args.k_max, len(frame) - 1)
    scores: dict[int, float] = {}
    labels_by_k: dict[int, list[int]] = {}
    for k in range(args.k_min, max_k + 1):
        model = AgglomerativeClustering(n_clusters=k, linkage="ward")
        labels = model.fit_predict(x)
        if len(set(labels)) < 2:
            continue
        score = float(silhouette_score(x, labels))
        scores[k] = score
        labels_by_k[k] = labels.tolist()
    if not scores:
        print("ERROR could not fit a valid cluster solution", file=sys.stderr)
        return 2
    best_k = max(scores, key=scores.get)
    frame["cluster"] = labels_by_k[best_k]
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output_csv, index=False)

    summaries = {}
    for cluster_id, group in frame.groupby("cluster"):
        summaries[str(int(cluster_id))] = {
            "n": int(len(group)),
            "feature_means": {name: round(float(group[name].mean()), 4) for name in features},
        }
    report = {
        "version": VERSION,
        "n": int(len(frame)),
        "features": features,
        "silhouette_by_k": {str(k): round(v, 6) for k, v in scores.items()},
        "selected_k": int(best_k),
        "selected_silhouette": round(scores[best_k], 6),
        "cluster_summaries": summaries,
        "warning": "Exploratory baseline only. Validate confound control, bootstrap stability, human interpretability, Persian perception, and held-out replication before naming or promoting profiles.",
    }
    report_path = args.report or args.output_csv.with_suffix(".cluster-report.json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"selected k={best_k} silhouette={scores[best_k]:.4f}; wrote {args.output_csv} and {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
