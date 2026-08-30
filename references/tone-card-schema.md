# Tone / Style Profile Card Schema

Schema version: 0.1.0

```yaml
profile_id: string
name_fa: string
status: Experimental | Candidate | Validated | Core
confidence: low | medium | high
definition: string
communicative_goal: [string]
audience_fit:
  good: [string]
  poor: [string]
context_fit:
  good: [string]
  poor: [string]
compatible_genres: [string]
incompatible_genres: [string]
voice_compatibility: [string]
observable_features:
  sentence_structure: {}
  paragraph_structure: {}
  lexical_behavior: {}
  rhetorical_moves: []
dimensions_0_to_4:
  formality: null
  seriousness: null
  respect: null
  enthusiasm: null
  emotional_intensity: null
  humor: null
  directness: null
  narrative_density: null
  explanatory_density: null
  metaphor_use: null
  question_use: null
  jargon_density: null
  epistemic_caution: null
  engagement_pressure: null
headline_behavior:
  preferred: []
  avoid: []
opening_lede_behavior:
  preferred: []
  avoid: []
positive_examples: []
negative_examples: []
anti_patterns: []
provenance:
  sources: []
  corpus_ids: []
corpus_evidence:
  n: 0
  matched_design: false
  replicated: false
persian_validation:
  status: not_started | pilot | passed | failed
  n_raters: 0
  notes: string
evaluation_method: []
known_limitations: []
```

## Rules

- Do not omit provenance or validation status.
- Do not name a profile after a publication, brand, living author, or single adjective.
- Keep profile count small. Prefer a continuous dimension adjustment when two candidates differ only weakly.
- If users ask for a non-existent profile, compose a temporary target vector and mark it `Experimental`, not Core.
