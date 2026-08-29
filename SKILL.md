---
name: writing-style-engine
description: Analyze, recommend, apply, compare, and evaluate writing Voice, Tone, Style, and Genre as separate but interacting layers. Use when ChatGPT must choose an evidence-grounded writing profile, rewrite or generate text in a controlled manner, compare style options, measure observable style features, enforce meaning preservation, or accept domain constraints from another skill. Always produce user-facing output in Persian. Do not treat publication names, author names, or vague adjectives as style profiles; use measurable feature vectors, rhetorical behaviors, provenance, validation status, and explicit evaluation gates.
---

# Writing Style Engine

Always produce user-facing output in Persian. Keep source titles, identifiers, metric names, and technical terms in their original language when useful.

## Core model

Keep these layers separate:

- **Voice**: stable identity-level communication invariants across contexts.
- **Tone**: context-sensitive interpersonal and emotional stance.
- **Style**: observable linguistic and rhetorical realization.
- **Genre**: communicative form with structural expectations and moves.

Never collapse the four layers into one adjective label. Never infer that a feature validated in English has the same perceptual effect in Persian without Persian validation.

Read `references/concept-model.md` when layer boundaries are unclear.

## Input contract

Accept free-form requests or a structured handoff. When present, preserve these fields:

- `task`: analyze | recommend | rewrite | generate | compare | evaluate
- `mode`: automatic | manual
- `content`
- `purpose`
- `audience`
- `channel`
- `genre`
- `voice_constraints`
- `tone_target`
- `style_profile`
- `domain_constraints`
- `preservation_requirements`
- `variant_count`

Treat `domain_constraints` and `preservation_requirements` as higher priority than style or engagement preferences. Read `references/domain-constraints-contract.md` for handoffs from science, legal, medical, financial, policy, or other specialist skills.

## Workflow

1. Parse the communication task and any domain constraints.
2. Identify the intended Genre separately from Voice, Tone, and Style.
3. If rewriting, extract protected propositions, numbers, entities, dates, causal relations, modality, negation, and claim strength before changing style.
4. Load relevant feature definitions from `references/style-feature-schema.md`.
5. Select mode:
   - **Automatic Mode**: propose at least 3 materially different compatible profiles, explain trade-offs, then select one.
   - **Manual Mode**: apply the requested profile. Warn only when it conflicts with Genre, domain constraints, preservation requirements, or validation limits.
6. If generating alternatives, produce structurally different versions. Change rhetorical organization, sentence/paragraph behavior, information order, stance, and density when appropriate. Do not create fake diversity by synonym replacement.
7. Apply the Meaning Preservation hard gate before ranking outputs.
8. Evaluate surviving outputs using `references/evaluation-framework.md`.
9. Report validation status and uncertainty. Never promote an unvalidated profile by rhetoric.

## Automatic Mode output

Default to this structure in Persian:

1. **تحلیل زمینه** — purpose, audience, channel, Genre, constraints.
2. **گزینه‌های مناسب** — at least 3 profiles, each with fit rationale and main trade-off.
3. **انتخاب پیشنهادی** — one profile and why it dominates for this context.
4. **خروجی‌ها** — multiple materially distinct versions when generation is requested.
5. **ارزیابی** — hard-gate result plus rubric scores and ranking.
6. **وضعیت شواهد** — Experimental/Candidate/Validated/Core and confidence.

Use profile cards from `references/profile-cards.md` only as hypotheses until their stated validation status permits stronger claims.

## Manual Mode output

Apply the selected profile directly. Preserve domain constraints. If a requested setting is undefined, infer the minimum required value from the profile rather than inventing a new profile.

## Meaning Preservation hard gate

For rewrite or transformation tasks, fail a candidate if it changes any critical meaning, including:

- protected facts, entities, numbers, dates, units, URLs, identifiers, citations, or quotations;
- polarity or negation;
- causal direction;
- actor/action/object relations when material;
- uncertainty, confidence, probability, legal force, or scientific claim strength;
- scope, conditions, exceptions, or temporal relations.

A failed candidate cannot recover through Style, Engagement, Readability, or Naturalness scores.

Use `scripts/check_meaning_gate.py` for deterministic protected-token checks when local text files are available. Treat semantic metrics as supporting evidence, not sole authority.

## Evaluation rules

Evaluate dimensions separately. Do not hide trade-offs behind a single score.

Required dimensions:

- Meaning Preservation — hard gate
- Domain Constraint Compliance — hard gate when supplied
- Style Profile Adherence
- Tone Perception Fit
- Voice Consistency
- Genre Fit
- Naturalness
- Readability/Comprehensibility
- Factual/claim-strength consistency when applicable
- Engagement — soft criterion only
- Clickbait/overstatement risk — penalty

Do not use CTR, virality, classifier confidence, LLM-as-judge, BLEU, ROUGE, or any single metric as a universal quality score.

## Corpus-backed profile rules

Before promoting a profile, follow `references/corpus-protocol.md`, `references/annotation-protocol.md`, and `references/persian-validation.md`.

Do not call a profile **Core** unless it satisfies the promotion gates in `references/evaluation-framework.md`.

Do not claim the engine is empirically domain-independent until it passes a second vertical independent of journalism.

## Publication and author handling

Use publications, organizations, and authors only as evidence sources or corpus strata. Convert observed patterns into independent features and rhetorical behaviors. Do not create profiles named “Nature style”, “Reuters style”, “Quanta style”, or a living writer's style.

## Tool use

When corpus files are available locally:

- Build/validate a sampling manifest with `scripts/build_corpus_manifest.py`.
- Extract deterministic features with `scripts/extract_style_features.py`.
- Cluster only after matching/residualizing confounds; use `scripts/cluster_profiles.py` as a baseline, not as proof of taxonomy.
- Run deterministic preservation checks with `scripts/check_meaning_gate.py`.

Read `references/tooling.md` before interpreting automated features.

## Reference navigation

- Concept boundaries and architecture: `references/concept-model.md`
- Feature definitions: `references/style-feature-schema.md`
- Card schema: `references/tone-card-schema.md`
- Initial non-Core profiles: `references/profile-cards.md`
- Domain handoff contract: `references/domain-constraints-contract.md`
- Corpus and matching: `references/corpus-protocol.md`
- Manual annotation: `references/annotation-protocol.md`
- Evaluation and promotion gates: `references/evaluation-framework.md`
- Persian validation: `references/persian-validation.md`
- Evidence register and include/reject decisions: `references/source-register.md`
- Tools and limitations: `references/tooling.md`
- Current validation state: `references/validation-status.md`
