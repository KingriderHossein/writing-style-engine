# Writing Style Engine

A reusable ChatGPT Skill for evidence-grounded analysis, recommendation, generation, rewriting, comparison, and evaluation of **Voice**, **Tone**, **Style**, and **Genre** as separate but interacting layers.

The Skill always produces user-facing output in Persian. Research sources may be in other languages, but Persian style effects must be validated separately rather than inferred from English.

## Current version

`v0.1.0`

All initial Style/Tone profiles are **Experimental**. No profile is currently Validated or Core.

## Design principles

- Keep Voice, Tone, Style, and Genre separate.
- Represent style with observable features and rhetorical behavior, not vague adjective lists.
- Treat Meaning Preservation and Domain Constraints as hard gates.
- Treat Engagement as a soft criterion, not the main objective.
- Do not create publication-name or living-author imitation profiles.
- Do not copy English thresholds directly into Persian.
- Require corpus evidence and human perception testing before profile promotion.

## Modes

### Automatic Mode

Analyze context, propose at least three materially different compatible profiles, explain trade-offs, choose the best option, generate variants when requested, and evaluate them.

### Manual Mode

Apply a user-selected profile while preserving domain constraints and critical meaning.

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

`Experimental → Candidate → Validated → Core`

Promotion requires explicit corpus, held-out replication, human perception, Persian validation, meaning-preservation checks, and eventually a second independent vertical outside journalism.

See `references/evaluation-framework.md` for exact gates.

## Corpus plan

The initial media study is designed for 160 texts across Nature, Quanta Magazine, Scientific American, Science News, STAT, Undark, Reuters, and Guardian Science. Sampling is stratified to reduce Topic, Genre, and Length confounding.

The repository does **not** bundle copyrighted full article text.

## Scripts

- `build_corpus_manifest.py` — generate and validate the planned 160-item corpus manifest.
- `extract_style_features.py` — deterministic baseline feature extraction.
- `cluster_profiles.py` — exploratory clustering after confound control.
- `check_meaning_gate.py` — deterministic checks for protected facts, identifiers, numbers, and phrases.

## Important limitation

The software structure and helper scripts have smoke tests, but the full 160-document corpus study, Persian perception study, inter-annotator reliability study, and independent second-vertical validation have not yet been completed. Therefore the current taxonomy must not be described as empirically validated.
