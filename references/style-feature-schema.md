# Style Feature Schema

Schema version: 0.2.0

Each feature record should contain:

- `feature_id`
- `label_fa`
- `layer`: voice | tone | style | genre-marker
- `definition`
- `measurement_type`: scalar | rate | categorical | annotation
- `unit`
- `extractor`: deterministic | parser | classifier | human | llm-assisted-human
- `language_calibration`: global | language-specific
- `confounds`
- `reliability`: high | medium | low | unknown
- `validation_source`

## Automatic or semi-automatic features

| feature_id | Measurement | Notes |
|---|---|---|
| sentence_length_mean | words/sentence | Always stratify by language and genre. |
| sentence_length_p90 | words/sentence | Detect tail complexity. |
| sentence_length_variation | coefficient of variation or robust spread | Supporting proxy for sentence rhythm; do not equate variance alone with perceived cadence. |
| paragraph_length_mean | sentences/paragraph and words/paragraph | Medium-sensitive to web formatting. |
| lexical_diversity_mattr | MATTR | Prefer over raw TTR because TTR is length-sensitive. |
| lexical_difficulty | frequency-based or calibrated lexicon score | Must use language-specific frequency resources. |
| syntactic_complexity | dependency depth, clause/dependency markers | Parser-dependent; validate per language. |
| passive_ratio | passive constructions / finite clauses | Parser-dependent; Persian requires UD-aware calibration. |
| question_frequency | questions / 1k tokens | Distinguish genuine vs rhetorical by annotation if important. |
| punctuation_rates | counts / 1k tokens | Track ! ? : ; — parentheses separately. |
| pronoun_rates | first/second/third person / 1k tokens | Morphology can make surface pronouns incomplete in Persian. |
| hedge_modal_rate | hedge/modal tokens / 1k tokens | Use language/domain-specific lexicon and parser when possible. |
| jargon_density | specialist terms / content words | Requires domain glossary or expert annotation. |
| quotation_density | quoted tokens / tokens | Also record quote count and source attribution if available. |
| transition_rate | discourse connectives / paragraph | Lexicon-based baseline; rhetorical relation annotation is stronger. |
| headline_length | words/chars | Never apply English thresholds directly to Persian. |
| headline_structure | clause/question/number/list/quote/entity-led/etc. | Rule + annotation. |
| narrative_markers | event-time-scene-character markers | Mixed automatic/manual. |
| explanatory_markers | definition, cause, comparison, example, mechanism | Mixed automatic/manual. |
| emotional_marker_rate | calibrated affect lexicon/model | Language-specific. |
| metaphor_use | annotated instances / 1k tokens | Human annotation required for stable claims. |

## Persian prose controls

These features support `references/iranian-writer-palette.md`. They are descriptive controls, not value judgments about good or bad Persian.

| feature_id | Measurement | Extractor | Notes |
|---|---|---|---|
| sentence_rhythm_fa | annotated cadence pattern + length variation | deterministic + human | Record short/long alternation, repeated cadence, and periodic sentence behavior. Length statistics are only supporting evidence. |
| lexical_register_fa | colloquial / neutral-standard / formal / literary / academic | human or llm-assisted-human | Calibrate by genre and audience. Do not infer register from one rare word. |
| lexical_origin_mix_fa | distribution of common Persian-origin, Arabic-origin, and other lexical items | curated lexicon + human | Descriptive only. Strongly confounded by domain and genre; never use as a purity/quality score. |
| narrator_presence_fa | 0-4 annotation | human or llm-assisted-human | Consider explicit first person, observer stance, evaluative intrusion, and narrator visibility. |
| rhetorical_question_rate_fa | rhetorical questions / 1k tokens | rule + human | Keep separate from genuine information-seeking questions. |
| paragraph_move_pattern_fa | ordered rhetorical-move labels per paragraph | human or llm-assisted-human | Examples: problem, scene, definition, evidence, contrast, limitation, implication, open question. |
| argument_move_density_fa | claim/evidence/warrant/contrast/limitation moves per paragraph | human or llm-assisted-human | Do not count topical statements as arguments automatically. |
| emotional_distance_fa | 0-4 annotation from detached to intimate/involved | human | Separate emotional distance from emotional intensity. |
| connective_register_fa | discourse-connective types/rate | lexicon + human | Track formal vs conversational transition choices; validate lexicon for Persian. |
| information_compression_fa | propositions per sentence/paragraph, assisted by annotation | parser + human | Use as a relative measure within matched Genre/Topic samples. |

## Tone dimensions

Rate each 0–4 with anchored definitions. Do not infer solely from one lexical feature.

- `formality`
- `seriousness`
- `respect`
- `enthusiasm`
- `emotional_intensity`
- `humor`
- `directness`
- `epistemic_caution`
- `narrative_density`
- `explanatory_density`
- `metaphor_density`
- `questioning_dialogicity`
- `jargon_density_perceived`
- `information_compression`
- `engagement_pressure`

## Confound controls

Always record Topic, Genre, Length, publication/channel, date, and audience. Where possible also record author and section. Do not interpret a topic-heavy lexical feature as Style.

For Persian writer/corpus comparisons, additionally control domain-specific terminology and translation status where possible. `lexical_origin_mix_fa`, register, and sentence rhythm are especially vulnerable to Topic, Genre, editorial intervention, historical period, and translation confounds.

Normalize rates per token/sentence as appropriate. For corpus comparisons, report effect sizes and uncertainty, not only p-values.
