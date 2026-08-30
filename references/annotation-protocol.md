# Annotation Protocol

Protocol version: 0.1.0

## Unit of annotation

Annotate at two levels:

1. article/document level for perceived Tone and overall structure;
2. span/paragraph level for rhetorical moves, metaphor, narrative/explanatory functions, and headline/lede devices.

## Blinding

When feasible remove outlet branding, author byline, navigation text, and visual identity from annotation copies. Randomize order. Do not tell annotators the hypothesized profile.

## Tone scales

Rate 0–4 using anchored examples for:

- formality
- seriousness
- respect/deference
- enthusiasm
- emotional intensity
- humor
- directness
- epistemic caution
- engagement pressure

Use `0 = absent/very low`, `2 = moderate`, `4 = very high`, with dimension-specific anchors prepared during pilot annotation.

## Rhetorical move labels

Allow multiple labels per paragraph when necessary:

- HOOK/ORIENT
- STATE_MAIN_POINT
- CONTEXTUALIZE
- DEFINE
- EXPLAIN_MECHANISM
- GIVE_EXAMPLE
- COMPARE_CONTRAST
- EVIDENCE/ATTRIBUTION
- QUALIFY/LIMIT
- COUNTERPOINT
- ACTION/NEXT_STEP
- SCENE/EVENT
- CHARACTER
- REFLECT/SIGNIFICANCE
- TRANSITION
- CLOSE/PAYOFF

These labels describe function, not surface form.

## Narrative markers

Annotate scene, chronological event progression, character agency, sensory/concrete detail, dialogue/quotation used as scene, and suspense/information withholding. Do not mark a single anecdote as “narrative style” by itself.

## Explanatory markers

Annotate definition, causal/mechanistic explanation, analogy, worked example, background prerequisite, comparison, uncertainty clarification, and misconception correction.

## Metaphor

Mark only when a lexical or phrasal expression maps one conceptual domain onto another in a way relevant to reader interpretation. Do not count dead idioms or purely technical terms without a pilot rule. Record `literal alternative` and `function` when possible.

## Rhetorical questions

Separate genuine information-seeking questions from rhetorical or reader-engagement questions.

## Reliability

Pilot on at least 20 documents. Use at least 2 annotators; 3 is preferred for subjective labels. Compute Krippendorff's alpha for ordinal/nominal dimensions as appropriate.

- `alpha >= 0.80`: reliable enough for primary validation.
- `0.67 <= alpha < 0.80`: tentative; allow only with adjudication and explicit uncertainty.
- `< 0.67`: revise guidelines and re-annotate before profile promotion.

These are project engineering thresholds, not universal psychometric laws.
