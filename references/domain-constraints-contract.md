# Domain Constraints Contract

Schema version: 0.1.0

Other skills may pass constraints to this engine. Treat this contract as authoritative over stylistic optimization.

```yaml
domain_constraints:
  domain: string
  required_facts: [string]
  protected_terms: [string]
  protected_numbers: [string]
  protected_entities: [string]
  prohibited_claims: [string]
  claim_strength_rules: [string]
  uncertainty_rules: [string]
  attribution_rules: [string]
  legal_or_policy_force_rules: [string]
  citation_rules: [string]
  quotation_rules: [string]
  safety_constraints: [string]
  allowed_simplifications: [string]
  prohibited_rhetorical_moves: [string]
  required_rhetorical_moves: [string]
  audience_assumptions: [string]
```

## Priority

1. Safety/system requirements
2. Domain constraints
3. Meaning/preservation requirements
4. Genre requirements
5. Voice invariants
6. Tone/Style preferences
7. Engagement preferences

## Science handoff example

A science-journalism skill can pass:

- exact study design and sample facts;
- preprint/peer-review status;
- prohibited causal wording;
- effect-size wording limits;
- uncertainty and limitation statements;
- terms that may be simplified only with definitions.

The Writing Style Engine may change presentation, but not these semantic constraints.

## Legal handoff example

A legal skill can pass:

- jurisdiction and date scope;
- mandatory legal terms;
- distinction between obligation, permission, recommendation, and possibility;
- prohibited legal conclusions;
- citation and quotation requirements.

Do not soften or intensify legal force to fit tone.
