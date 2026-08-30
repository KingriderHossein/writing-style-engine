## Important include/reject decisions

### Include in `references/`

- Conceptual distinctions: Biber/Conrad plus professional voice/tone systems.
- Measurement seeds: stylometry, TST evaluation, human-evaluation reviews.
- Editorial constraints: Reuters, GOV.UK, GitHub Docs, Microsoft, Mailchimp, Poynter, KSJ/WFSJ/Open Notebook.
- Engagement guardrails: Upworthy as attention evidence and Webis Clickbait as a counterweight.
- Preservation evidence: MIS, AlignScore, QAFactEval, plus deterministic protected-item checks.
- Persian tooling: UD Persian/Stanza-compatible analysis as feature infrastructure, not as proof of tone perception.

### Reject from v0.1 runtime

- Fine-tuning or dedicated style-transfer models as a requirement.
- Publication-name or living-author imitation profiles.
- One-click "AI humanizer" repositories and prompt collections without reproducible evaluation.
- CTR/virality as a global objective.
- A single classifier score as proof of tone/style quality.
- BLEU/ROUGE as a meaning-preservation gate.
- LLM-as-judge without order controls, independent rubrics, and human calibration.
- English numeric thresholds copied directly into Persian.
- Uncontrolled corpus clustering before Topic/Genre/Length deconfounding.

## Corpus publication sources

The initial media corpus uses these outlets as sampling strata, not as named styles:

- Nature — https://www.nature.com/
- Quanta Magazine — https://www.quantamagazine.org/
- Scientific American — https://www.scientificamerican.com/
- Science News — https://www.sciencenews.org/
- STAT — https://www.statnews.com/
- Undark — https://undark.org/
- Reuters — https://www.reuters.com/
- Guardian Science — https://www.theguardian.com/science

Do not bundle copyrighted full article text. Store URLs, metadata, rights notes, local lawful text pointers, derived features, and annotation IDs.
