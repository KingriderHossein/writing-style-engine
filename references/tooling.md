# Tooling and Measurement Limits

Version: 0.1.0

## Bundled scripts

### build_corpus_manifest.py
Creates or validates a metadata manifest. It does not download or redistribute copyrighted article text.

### extract_style_features.py
Extracts deterministic, language-light features from local JSONL/CSV text. It is suitable for baseline measurement, not full stylometry. It intentionally does not pretend to measure metaphor, rhetorical function, active/passive syntax, or semantic preservation without stronger tools.

### cluster_profiles.py
Runs a baseline clustering analysis on numeric features with standardization and bootstrap stability. Use only after Topic/Genre/Length deconfounding described in the corpus protocol.

### check_meaning_gate.py
Checks protected literals and critical numeric/identifier material. It catches only a subset of semantic errors. Pair it with proposition/entailment review.

## Optional external methods for later versions

High priority:

- cross-encoder or NLI-based semantic preservation, including Mutual Implication Score-style bidirectional entailment;
- factual-consistency metrics such as AlignScore or QAFactEval where task/language validation is adequate;
- parser-based syntactic features with Stanza/UD;
- embedding-based style retrieval or authorship representations such as LUAR.

Lower priority for v1 execution:

- PPLM, FUDGE, DExperts decoding-time control;
- fine-tuned style-transfer models;
- publisher/author imitation models.

## Metric cautions

- TTR is strongly length-sensitive; use MATTR/MTLD.
- Passive voice is not reliably detected by string patterns.
- Jargon is domain-relative.
- Metaphor detection is not reliable enough here for unattended promotion decisions.
- LLM judges have position, leniency, length, and self-preference risks.
- A high semantic similarity score can still hide a changed number, negation, modality, or causal relation.
