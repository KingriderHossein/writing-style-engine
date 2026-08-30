# Validation Status

Version: 0.1.0

## What has been validated in this package

- Skill structure and metadata: package validator.
- `build_corpus_manifest.py`: creates exactly 160 planned rows, 20 per outlet.
- `extract_style_features.py`: smoke-tested on English and Persian Unicode text.
- `cluster_profiles.py`: smoke-tested on synthetic English data and rejects mixed-language input by default.
- `check_meaning_gate.py`: smoke-tested with a passing rewrite and an intentional failure that changed `240` to `420` and removed a protected uncertainty phrase.

These are **software smoke tests**, not empirical validation of any Style Profile.

## What has not yet been validated

- The full 160-document media corpus has not been lawfully collected and analyzed in this package.
- Manual rhetorical/narrative annotation has not been completed.
- Inter-annotator reliability has not been estimated on the target corpus.
- Persian perception testing with native raters has not been completed.
- A second independent vertical has not been completed.
- No profile is therefore Validated or Core.

## Current profile status

All initial profiles in `profile-cards.md` are **Experimental** hypotheses.

## Interpretation rule

Do not describe the engine as empirically domain-independent. It is architecturally domain-neutral and supports domain constraints, but empirical domain independence requires the promotion evidence defined in `evaluation-framework.md`.
