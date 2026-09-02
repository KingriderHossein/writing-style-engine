---
name: writing-style-engine
description: Analyze, recommend, apply, compare, and evaluate writing Voice, Tone, Style, and Genre as separate but interacting layers. Use when ChatGPT must choose an evidence-grounded writing profile, rewrite or generate text in a controlled manner, compare style options, measure observable style features, enforce meaning preservation, or accept domain constraints from another skill. Always produce user-facing output in Persian. Do not treat publication names, author names, or vague adjectives as style profiles; use measurable feature vectors, rhetorical behaviors, provenance, validation status, and explicit evaluation gates.
---

# Writing Style Engine

Protocol version: 0.2.0

Always produce user-facing output in Persian. Keep source titles, identifiers, metric names, and technical terms in their original language when useful.

## Task router

Use the narrowest execution path that satisfies the request. Do not run recommendation, generation, and scoring stages mechanically for every task.

### ANALYZE
Use when the user wants to understand the Voice, Tone, Style, Genre, features, or rhetorical behavior of existing text.

- Analyze only the requested layers and observable features.
- Do not rewrite or generate alternatives unless requested.
- Report evidence and validation limits for any profile attribution.

### RECOMMEND
Use when the user asks which Voice/Tone/Style/Genre profile is appropriate, gives an ambiguous target, or wants trade-offs before writing.

- Propose at least 3 materially different compatible options when enough context exists.
- Explain the main trade-off of each option.
- Select one recommended option only after checking purpose, audience, channel, Genre, and domain constraints.

### DIRECT APPLY
Use when the user asks to rewrite or generate text and already supplies a usable tone, style, genre, profile, or clear communication constraint.

- Apply the closest compatible profile or feature set directly.
- Do not force 3 profile proposals or multiple variants.
- Return the finished text as the primary output.
- Surface evaluation details only when requested or when a material conflict must be explained.

### COMPARE
Use when the user asks to compare profiles, drafts, tones, styles, or genres.

- Compare the requested alternatives on separate dimensions.
- Keep meaning/domain hard gates separate from soft preferences.
- Do not collapse trade-offs into one universal score.

### EVALUATE
Use when the user asks to score, diagnose, or validate text against a profile or constraints.

- Evaluate the supplied text without rewriting it unless the user also asks for correction.
- Show hard-gate failures separately from soft quality scores.

### MANUAL PROFILE
If the user explicitly selects a profile or feature target, treat it as a direct constraint. Warn only when it conflicts with Genre, domain constraints, meaning preservation, or known validation limits.

## Core model

Keep these layers separate:

- **Voice:** stable identity-level communication invariants across contexts.
- **Tone:** context-sensitive interpersonal and emotional stance.
- **Style:** observable linguistic and rhetorical realization.
- **Genre:** communicative form with structural expectations and moves.

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

Treat `domain_constraints` and `preservation_requirements` as higher priority than style or engagement preferences. Read `references/domain-constraints-contract.md` for handoffs from science, legal, medical, financial, policy, or other specialist workflows.

Interpret `mode: automatic` according to the task router: use RECOMMEND when the profile is not yet chosen; use DIRECT APPLY when the writing target is already clear. Do not make `automatic` synonymous with always generating three options.

## Workflow

1. Parse the communication task, purpose, audience, channel, and any domain constraints.
2. Route to ANALYZE, RECOMMEND, DIRECT APPLY, COMPARE, EVALUATE, or MANUAL PROFILE.
3. Identify the intended Genre separately from Voice, Tone, and Style.
4. For rewrite/transformation tasks, extract protected propositions, numbers, entities, dates, causal relations, modality, negation, scope, and claim strength before changing style.
5. Load only the feature/profile references needed for the routed task.
6. If alternatives are requested or RECOMMEND requires them, make them materially different in rhetorical organization, information order, stance, density, sentence/paragraph behavior, or other relevant features. Do not create fake diversity through synonym replacement.
7. Apply the Meaning Preservation hard gate to rewrite/transformation candidates.
8. Apply Domain Constraint Compliance as a hard gate when constraints were supplied.
9. Use `references/evaluation-framework.md` for explicit EVALUATE, COMPARE, or RECOMMEND scoring/ranking and when a material quality conflict must be resolved.
10. Report validation status and uncertainty whenever a profile claim depends on empirical support. Never promote an unvalidated profile by rhetoric.

## Recommendation output

For RECOMMEND tasks, default to this compact Persian structure:

1. **تحلیل زمینه** — purpose, audience, channel, Genre, constraints.
2. **گزینه‌های مناسب** — at least 3 materially different profiles with fit rationale and main trade-off.
3. **انتخاب پیشنهادی** — one profile and why it best fits the current context.
4. **خروجی** — only when generation/rewrite is part of the user's request.
5. **ارزیابی** — only when comparison/ranking is useful or requested.
6. **وضعیت شواهد** — Experimental/Candidate/Validated/Core and confidence when a profile claim is made.

Use profile cards from `references/profile-cards.md` only within their stated validation status.

## Direct Apply output

For DIRECT APPLY or MANUAL PROFILE tasks:

- return the requested finished text as the main output;
- preserve domain and meaning constraints;
- do not expose internal profile-search or scoring work by default;
- do not generate variants unless requested;
- add a brief warning only when the requested style would violate a hard constraint or depends on unsupported validation claims.

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

When explicit evaluation is needed, evaluate dimensions separately. Do not hide trade-offs behind one aggregate score.

Relevant dimensions include:

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

Do not print this full rubric for simple DIRECT APPLY tasks unless the user asks for evaluation.

## Corpus-backed profile rules

Before promoting a profile, follow `references/corpus-protocol.md`, `references/annotation-protocol.md`, and `references/persian-validation.md`.

Do not call a profile **Core** unless it satisfies the promotion gates in `references/evaluation-framework.md`.

Do not claim the engine is empirically domain-independent until it passes a second vertical independent of journalism.

## Publication and author handling

Use publications, organizations, and authors only as evidence sources or corpus strata. Convert observed patterns into independent features and rhetorical behaviors. Do not create profiles named after a publication or living writer.

## Tool use

When corpus files are available locally:

- build/validate a sampling manifest with `scripts/build_corpus_manifest.py`;
- extract deterministic features with `scripts/extract_style_features.py`;
- cluster only after matching/residualizing confounds; use `scripts/cluster_profiles.py` as a baseline, not as proof of taxonomy;
- run deterministic preservation checks with `scripts/check_meaning_gate.py`.

Read `references/tooling.md` before interpreting automated features.

## Reference navigation

Load only what the routed task needs:

- Concept boundaries and architecture: `references/concept-model.md`
- Feature definitions: `references/style-feature-schema.md`
- Card schema: `references/tone-card-schema.md`
- Current profile hypotheses: `references/profile-cards.md`
- Domain handoff contract: `references/domain-constraints-contract.md`
- Corpus and matching: `references/corpus-protocol.md`
- Manual annotation: `references/annotation-protocol.md`
- Evaluation and promotion gates: `references/evaluation-framework.md`
- Persian validation: `references/persian-validation.md`
- Evidence register and include/reject decisions: `references/source-register.md`
- Tools and limitations: `references/tooling.md`
- Current validation state: `references/validation-status.md`
