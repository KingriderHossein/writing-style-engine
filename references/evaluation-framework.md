# Evaluation Framework

Framework version: 0.1.0

## Principle

Evaluate multiple dimensions separately. Use hard gates before soft ranking.

## Gate A — Meaning Preservation

Pass only if no critical semantic change is detected in protected facts, numbers, entities, polarity, modality, causality, scope, exceptions, time relations, or claim strength.

Suggested evidence bundle:

- deterministic protected-item check;
- proposition/slot comparison;
- bidirectional entailment or cross-encoder semantic metric when validated for the language;
- human review for high-stakes or borderline cases.

Do not use BLEU/ROUGE as the primary meaning gate.

## Gate B — Domain compliance

If domain constraints exist, any prohibited claim, required-term violation, unsupported certainty increase, or policy/legal-force change fails the candidate.

## Soft rubric after gates

Score 0–5 independently:

- Style adherence
- Tone perception fit
- Voice consistency
- Genre fit
- Naturalness
- Readability/comprehensibility
- Information organization
- Engagement

Subtract a separate 0–3 penalty for clickbait/overstatement/manipulative urgency. Do not combine the penalty into Meaning Preservation.

## Human evaluation

Blind candidate identity where possible. Randomize presentation order. For pairwise comparisons, reverse order in a balanced design to limit position bias. Do not let the same LLM generation order determine judging order.

## LLM-as-judge

Use as an auxiliary evaluator only. Require rubric-based dimension-by-dimension scoring. Use order reversal or multiple permutations for pairwise/listwise comparisons. Prefer an ensemble or human sample for promotion decisions.

## Promotion gates

These are explicit project governance thresholds.

### Experimental → Candidate

Require all:

- feature definition and extraction/annotation method documented;
- provenance from at least 2 independent credible sources or one strong empirical source plus professional rule evidence;
- preliminary corpus evidence on at least 40 relevant documents total, with no obvious Topic/Length confound;
- profile is practically distinguishable from existing profiles on at least 2 feature families;
- no critical meaning-preservation failure in a 20-item generation pilot.

### Candidate → Validated

Require all:

- primary corpus `n >= 100`, preferably 160 for the initial media study;
- matched or deconfounded design with held-out evaluation;
- feature direction replicates on held-out data for at least 70% of pre-specified differentiating features;
- cluster/profile stability bootstrap adjusted Rand index or equivalent median `>= 0.70`, when clustering is used;
- human perception study with at least 3 raters per item or a justified equivalent;
- Krippendorff alpha `>= 0.67` for subjective profile labels and `>= 0.80` desired;
- Persian validation: median naturalness `>= 4/5`, readability `>= 4/5`, intended Tone recognition `>= 70%`, and no critical meaning change in at least 95% of test items;
- any remaining critical meaning failures are analyzed and blocked by a guardrail before promotion;
- performance demonstrated across at least 2 topic families and 2 genres.

### Validated → Core

Require all:

- independent replication on a new corpus or time window;
- successful Persian revalidation after profile/instruction revisions;
- evaluation in a second vertical independent of journalism;
- no systematic conflict with domain-constraint handoffs in at least 2 specialist domains;
- meaning hard-gate critical failure rate `<= 1%` on the promotion test set, with human adjudication;
- intended profile perception `>= 80%` or statistically clear separation from nearest profile;
- no adjacent profile can be merged without meaningful loss of control;
- provenance, scripts, corpus manifest, version, and known limitations are reproducible.

A profile can be demoted when replication fails.

## Confidence

- Low: theoretical or guide-derived only, or conflicting evidence.
- Medium: corpus or perception evidence exists but lacks independent replication/Persian confirmation.
- High: replicated and meets Validated/Core gates.
