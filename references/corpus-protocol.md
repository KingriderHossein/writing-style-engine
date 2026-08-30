# Corpus Protocol

Protocol version: 0.1.0

## Purpose

Validate whether hypothesized style dimensions and profiles correspond to reproducible patterns rather than Topic, Genre, Length, outlet, or one writer.

## Initial media corpus

Target `n = 160` full articles, approximately 20 per outlet:

- Nature
- Quanta Magazine
- Scientific American
- Science News
- STAT
- Undark
- Reuters
- Guardian Science

Do not redistribute copyrighted full text inside the skill. Keep a manifest with URL, metadata, rights note, local-file pointer, and derived features. Analysis should run on lawfully obtained/local text.

## Sampling frame

Use a stratified design. Recommended primary strata:

- Topic family: life/biomed; environment/climate; physics/space; computation/AI
- Genre family: straight-news/reporting; explainer/feature
- Length band: short/medium vs long, defined by corpus quantiles rather than universal word thresholds
- Recency window: fixed period where all outlets have sufficient availability

Aim for 16 pre-specified cells per outlet (4 topics × 2 genre families × 2 length bands) plus 4 reserve/replacement samples. When an exact cell is unavailable, record the deviation rather than silently substituting.

## Matching

Create a matched subset for inferential comparisons:

- match Topic family exactly when possible;
- match Genre family exactly;
- match Length within ±20% or nearest-neighbor on log word count;
- keep publication date reasonably close for fast-changing topics;
- avoid repeated author dominance where possible.

Record match quality.

## Feature extraction

Extract deterministic features first. Parser/model-based features are a second layer. Manual annotation is required for metaphor, rhetorical move function, narrative/explanatory function, and ambiguous rhetorical questions.

For length-sensitive measures use rates or robust measures. Prefer MATTR/MTLD over raw TTR. Report medians/IQRs in addition to means where distributions are skewed.

## Deconfounding

Do not cluster raw article vectors before controlling for confounds.

Recommended sequence:

1. inspect missingness and extraction reliability;
2. standardize within language;
3. residualize continuous features against log length and declared Genre/Topic where appropriate, or cluster on matched cells;
4. remove direct topic-lexical features from style clustering;
5. inspect outlet/author leakage;
6. cluster the deconfounded feature matrix;
7. bootstrap samples and calculate cluster stability;
8. test whether profile differences replicate on held-out articles.

Use UMAP/t-SNE only for visualization. Do not treat a 2D plot as cluster evidence.

## Clustering baseline

Use hierarchical clustering or Gaussian mixture as interpretable baselines. HDBSCAN can be exploratory when profile count is unknown. Select the smallest number of clusters that is stable and practically interpretable.

A cluster becomes a profile only if:

- stability is acceptable across bootstrap resamples;
- at least two observable feature families distinguish it;
- the difference persists across multiple topics;
- human annotators perceive a coherent difference;
- generation instructions can reproduce it without meaning loss.

## Second vertical

Before any claim of empirical domain independence, run an independent vertical. v0.1.0 recommends technical/help content:

- GitHub Docs
- Microsoft Learn / product help
- GOV.UK service guidance where comparable

Use a separate corpus and do not reuse journalism-derived thresholds. Test whether dimensions remain interpretable and whether profiles require domain-specific recalibration.

## Current status

The 160-document study is specified but not bundled or claimed as completed in v0.1.0. Therefore no profile is Core.
