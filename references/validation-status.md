# Validation Status

Version: 0.2.0

## What has been validated in this package

- Skill structure and metadata: package validator.
- `build_corpus_manifest.py`: creates exactly 160 planned rows, 20 per outlet.
- `extract_style_features.py`: smoke-tested on English and Persian Unicode text.
- `cluster_profiles.py`: smoke-tested on synthetic English data and rejects mixed-language input by default.
- `check_meaning_gate.py`: smoke-tested with a passing rewrite and an intentional failure that changed `240` to `420` and removed a protected uncertainty phrase.

These are **software smoke tests**, not empirical validation of any Style Profile or Writer Palette preset.

## What has not yet been validated

- The full 160-document media corpus has not been lawfully collected and analyzed in this package.
- Manual rhetorical/narrative annotation has not been completed.
- Inter-annotator reliability has not been estimated on the target corpus.
- Persian perception testing with native raters has not been completed.
- A second independent vertical has not been completed.
- A dedicated Iranian/Persian writer corpus has not been collected and analyzed with Topic, Genre, Length, historical period, translation status, and editorial-intervention controls.
- The new Persian prose controls in `style-feature-schema.md` have not yet received reliability estimates.
- No `IW-*` Writer Palette preset has been empirically recovered as a stable corpus cluster or validated by native-rater perception testing.
- No profile or Writer Palette preset is therefore Validated or Core.

## Current profile status

All initial profiles in `profile-cards.md` are **Experimental** hypotheses.

All `IW-*` presets in `iranian-writer-palette.md` are **Experimental composition presets**. They are engineering starting points, not claims about actual Iranian writers as a population.

## Named-writer interpretation rule

A named writer may be used as a corpus/evidence source. Do not convert reputation or a small anecdotal sample directly into a validated profile. Writer-derived targets must remain feature-based and must report confidence according to evidence quality.

For living writers, the engine uses non-identifying feature targets rather than direct imitation.

## Interpretation rule

Do not describe the engine as empirically domain-independent. It is architecturally domain-neutral and supports domain constraints, but empirical domain independence requires the promotion evidence defined in `evaluation-framework.md`.

Do not describe the Iranian Writer Palette as empirically validated until the dedicated Persian corpus and perception-validation path is complete.
