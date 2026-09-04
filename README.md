# Writing Style Engine

A reusable ChatGPT Skill for evidence-grounded analysis, recommendation, generation, rewriting, comparison, and evaluation of **Voice**, **Tone**, **Style**, and **Genre** as separate but interacting layers.

The Skill always produces user-facing output in Persian. Research sources may be in other languages, but Persian style effects must be validated separately rather than inferred from English.

## Current version

`v0.3.0`

All current Style/Tone profiles and Iranian Writer Palette presets remain **Experimental** unless `references/validation-status.md` explicitly records a later promotion. Version 0.3.0 adds a Persian writer-oriented preset system; it does not claim empirical validation of Iranian author styles.

## Main change in v0.3.0

The engine now includes **Iranian Writer Palette**, a preset composer for Persian prose architecture.

It does not create a fifth conceptual layer and it does not turn writer names into imitation profiles. Instead, it composes observable controls such as:

- sentence rhythm and syntactic complexity;
- Persian lexical register and descriptive Persian/Arabic lexical-origin mix;
- narrator presence and emotional distance;
- metaphor and rhetorical-question use;
- paragraph architecture and argument density;
- epistemic caution and information compression.

Eight Experimental Writer Architecture presets are available as `IW-01` to `IW-08`, including روشن و گزارشی، جستاری و اندیشمند، مینیمال و برنده، روایی و مشاهده‌گر، ادبی-علمی، استدلالی و دانشگاهی، گفت‌وگویی و معلم‌گونه، and مشاهده‌گر و کنایه‌پرداز.

Named writers are treated as corpus/evidence references. The engine converts observed traits into independent feature vectors. For living writers, it does not perform direct imitation.

## Task router

The Skill uses a task router instead of forcing the same large workflow for every request:

- **ANALYZE** — inspect existing writing without rewriting it.
- **RECOMMEND** — propose at least three materially different compatible profiles or Writer Palette presets and explain trade-offs.
- **DIRECT APPLY** — when the requested style/tone/genre/Writer Palette is already clear, apply it directly without first generating three options or exposing a scoring report.
- **COMPARE** — compare requested alternatives dimension by dimension.
- **EVALUATE** — score or diagnose supplied text without silently rewriting it.
- **MANUAL PROFILE** — apply an explicitly selected profile, Writer Palette preset, or feature set directly.

This keeps meaning preservation and domain constraints as hard gates while reducing unnecessary output and context use for simple rewrites.

## Design principles

- Keep Voice, Tone, Style, and Genre separate.
- Treat Writer Palette as a Style preset composer, not a fifth layer.
- Represent style with observable features and rhetorical behavior, not vague adjective lists.
- Treat Meaning Preservation and Domain Constraints as hard gates.
- Treat Engagement as a soft criterion, not the main objective.
- Do not create publication-name or living-author imitation profiles.
- Do not reproduce distinctive phrases or signature passages from named writers.
- Do not copy English thresholds directly into Persian.
- Treat Persian/Arabic lexical-origin mix descriptively, never as a purity or quality score.
- Require corpus evidence and human perception testing before profile or Writer Palette promotion.
- Use the narrowest workflow that satisfies the current writing task.

## Repository structure

```text
writing-style-engine/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── annotation-protocol.md
│   ├── concept-model.md
│   ├── corpus-protocol.md
│   ├── domain-constraints-contract.md
│   ├── evaluation-framework.md
│   ├── iranian-writer-palette.md
│   ├── persian-validation.md
│   ├── profile-cards.md
│   ├── source-register.md
│   ├── source-register-01-research-foundations.md
│   ├── source-register-02-editorial-and-summarisation.md
│   ├── source-register-03-evaluation-and-multilingual.md
│   ├── source-register-04-decisions-and-corpus.md
│   ├── style-feature-schema.md
│   ├── tone-card-schema.md
│   ├── tooling.md
│   └── validation-status.md
└── scripts/
    ├── build_corpus_manifest.py
    ├── check_meaning_gate.py
    ├── cluster_profiles.py
    ├── extract_style_features.py
    └── requirements.txt
```

## Validation path

Profiles move through:

`Experimental -> Candidate -> Validated -> Core`

Writer Palette presets use the same evidence discipline but require a dedicated Persian corpus and native-rater validation before promotion.

Promotion requires explicit corpus evidence, held-out replication, human perception testing, Persian validation, meaning-preservation checks, and eventually a second independent vertical outside journalism.

See `references/evaluation-framework.md` for exact gates.

## Corpus plan

The initial media study is designed for 160 texts across multiple English-language science/editorial sources. Sampling is stratified to reduce Topic, Genre, and Length confounding. The repository does **not** bundle copyrighted full article text.

The Iranian Writer Palette requires a separate Persian corpus plan that also controls historical period, translation status, editorial intervention, Topic, Genre, and Length. That study has not yet been completed.

## Scripts

- `build_corpus_manifest.py` — generate and validate the planned corpus manifest.
- `extract_style_features.py` — deterministic baseline feature extraction.
- `cluster_profiles.py` — exploratory clustering after confound control.
- `check_meaning_gate.py` — deterministic checks for protected facts, identifiers, numbers, and phrases.

## Important limitation

The software structure and helper scripts have smoke tests, but the full corpus study, dedicated Iranian/Persian writer corpus study, Persian perception study, inter-annotator reliability study, and independent second-vertical validation have not yet been completed. Therefore the current profile taxonomy and `IW-*` Writer Palette presets must not be described as empirically validated.
