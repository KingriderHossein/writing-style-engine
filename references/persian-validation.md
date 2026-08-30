# Persian Validation Protocol

Protocol version: 0.1.0

## Core rule

Do not map English feature thresholds or perceptual effects directly to Persian. Re-test both linguistic realization and reader perception.

## Dataset

For each profile under test, create source texts across at least 3 domains or topics and 2 genres. Generate multiple Persian realizations from the same protected semantic content. Include neutral baselines.

Use Persian-native raters. Keep profile names hidden. Randomize output order.

## Separate outcomes

Rate independently:

1. Naturalness
2. Readability/comprehensibility
3. Meaning preservation
4. Intended Tone perception
5. Style-feature adherence
6. Domain appropriateness

Do not ask one global “quality” question instead of these dimensions.

## Meaning validation

Create a protected proposition sheet before rewriting. Include:

- named entities;
- numbers, dates, units and percentages;
- negation;
- causal vs correlational relation;
- possibility/probability/certainty;
- source attribution;
- exceptions and conditions.

Have raters flag added, removed, weakened, or strengthened propositions.

## Persian-specific processing

- Preserve and normalize Zero Width Non-Joiner intentionally; do not delete it blindly.
- Calibrate tokenization and sentence segmentation for Persian punctuation and mixed Persian/English text.
- Surface pronoun counts under-estimate person reference because Persian permits pro-drop; parser/morphological features should supplement raw pronoun counts.
- Validate passive detection with Persian UD relations such as `aux:pass`/`nsubj:pass`, not English auxiliary heuristics.
- Build Persian hedge/modal and discourse-marker lexicons from a corpus pilot; do not translate an English list word-for-word and call it validated.

Useful infrastructure includes Universal Dependencies Persian treebanks (PerDT and Seraji) and Stanza Persian models. These support parser-based measurement but do not by themselves validate style effects.

## Perception design

Use anchored 0–4 or 1–5 scales and a forced profile-choice task. Add pairwise A/B comparisons when two neighboring profiles are hard to distinguish.

Balance candidate order. If an LLM is used as a preliminary judge, include human adjudication and order-reversal checks.

## Promotion rule

Persian validation is mandatory for Validated/Core status in this skill. English evidence alone can support only Experimental/Candidate status.
