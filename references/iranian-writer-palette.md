# Iranian Writer Palette

Module version: 0.1.0
Status: Experimental

This module adds Persian writer-oriented composition presets without creating a fifth conceptual layer. A Writer Palette is a **preset composer** over observable Style features and Persian-specific prose controls. Voice, Tone, Style, and Genre remain separate.

## Purpose

Use this module when the user asks for an Iranian/Persian writer palette, Persian prose architecture, a writer-like rhetorical shape, or a named Iranian writer as a stylistic reference.

The module must produce independent prose. It must not reproduce distinctive phrases, signature passages, or close textual imitation.

## Composition model

Use this order:

`Domain constraints -> Meaning preservation -> Genre -> Voice -> Tone -> Style profile -> Writer Palette -> Final text`

Writer Palette may adjust only compatible Style features. It must not weaken scientific/legal/medical/financial uncertainty, factual boundaries, or Genre requirements.

A Writer Palette is not itself a Voice or Tone. For example, `IW-02` can be used with a cautious scientific Tone or a warmer educational Tone.

## Named-writer handling

When the user gives a writer name:

1. Treat the writer as an evidence/corpus reference, not as a profile name.
2. If user-provided excerpts or a lawful corpus are available, ANALYZE observable features first.
3. Convert observations into a feature vector and rhetorical-move description.
4. Apply that feature vector to new prose while keeping wording independent.
5. For a living writer, do not perform direct imitation. Use a non-identifying feature target such as sentence rhythm, narrator presence, metaphor density, argument structure, or lexical register.
6. If evidence is absent or thin, mark the derived target `Experimental` with low confidence. Do not invent a writer profile from reputation alone.

## Persian prose controls

Use only the controls that matter for the current task:

- `sentence_rhythm`: short/long alternation, periodicity, and cadence variation.
- `syntactic_complexity`: clause depth and coordination/subordination behavior.
- `lexical_register_fa`: colloquial, neutral-standard, formal, literary, or academic Persian.
- `lexical_origin_mix_fa`: descriptive balance of common Persian-origin and Arabic-origin vocabulary when measurable; never treat either side as inherently better.
- `narrator_presence`: absent, low, moderate, or foregrounded narrator.
- `metaphor_density`: frequency and prominence of figurative language.
- `rhetorical_question_use`: genuine/rhetorical question frequency and function.
- `paragraph_architecture`: typical sequence of problem, scene, explanation, contrast, evidence, limitation, conclusion, or open question.
- `argument_density`: explicit claim-evidence-warrant/contrast/limitation moves.
- `emotional_distance`: detached, observational, involved, or intimate stance.
- `epistemic_caution`: strength of hedging, uncertainty marking, and claim boundaries.
- `information_compression`: how much propositional content is packed into each sentence/paragraph.

Load `references/style-feature-schema.md` for measurement rules and confounds.

## Experimental Writer Architecture presets

These are composition presets, not validated Style Profiles. Do not promote them into `profile-cards.md` without corpus replication and Persian perception validation.

| ID | Name | Core rhetorical architecture | Typical feature tendency |
|---|---|---|---|
| IW-01 | روشن و گزارشی | fact -> function -> evidence -> limitation | short-medium sentences; low metaphor; low narrator presence; high clarity |
| IW-02 | جستاری و اندیشمند | problem/question -> exploration -> evidence -> reflective implication | medium-long sentences; high argument/explanation; moderate metaphor/question use |
| IW-03 | مینیمال و برنده | key fact -> compression -> contrast -> strong close | short sentences; very high compression; low ornament; selective emphasis |
| IW-04 | روایی و مشاهده‌گر | scene/problem -> concrete observation -> explanation -> open implication | high narrative density; moderate narrator presence; controlled metaphor |
| IW-05 | ادبی-علمی | concrete image -> scientific explanation -> evidence boundary -> restrained image/close | richer lexicon; medium metaphor; scientific caution preserved |
| IW-06 | استدلالی و دانشگاهی | definition/claim -> evidence -> limitation -> implication | high argument density; high epistemic caution; low metaphor; low narrator presence |
| IW-07 | گفت‌وگویی و معلم‌گونه | example -> question -> explanation -> check/limitation | high explanatory density; moderate question use; low-medium compression |
| IW-08 | مشاهده‌گر و کنایه‌پرداز | ordinary observation -> contrast/incongruity -> interpretation -> understated close | moderate compression; indirect contrast; narrator presence medium; requires compatible Tone if humor is desired |

## Default vectors

Rate each dimension 0-4. These values are starting targets only.

| ID | Rhythm | Lexical richness | Narrative | Explanation | Metaphor | Questions | Argument | Caution | Compression | Narrator |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| IW-01 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | 3 | 3 | 0 |
| IW-02 | 3 | 3 | 2 | 4 | 2 | 2 | 4 | 3 | 2 | 1 |
| IW-03 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 4 | 0 |
| IW-04 | 3 | 3 | 4 | 3 | 2 | 1 | 2 | 3 | 2 | 2 |
| IW-05 | 3 | 4 | 2 | 3 | 3 | 1 | 2 | 3 | 2 | 1 |
| IW-06 | 3 | 3 | 0 | 4 | 0 | 0 | 4 | 4 | 3 | 0 |
| IW-07 | 2 | 2 | 1 | 4 | 1 | 3 | 2 | 3 | 2 | 1 |
| IW-08 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 |

## Direct Apply behavior

If the user selects an `IW-*` preset, apply it directly unless it conflicts with a hard constraint. Do not first generate three alternatives.

If the user says only "مثل یک نویسنده ایرانی" without a concrete writer or preset, route to RECOMMEND and offer at least three materially different IW presets.

If the user gives a named writer plus a concrete text, preserve the text's protected facts before applying any derived feature vector.

## Evaluation

When evaluation is requested, score separately:

- Meaning Preservation — hard gate
- Domain Constraint Compliance — hard gate
- Writer Palette adherence
- Style Profile adherence
- Tone fit
- Genre fit
- Persian naturalness/readability
- Claim-strength consistency
- Overwriting/ornament penalty when figurative or rhetorical features exceed the selected target

## Validation status

All `IW-*` presets are **Experimental**. They are engineering presets derived from the current feature schema, not empirically discovered clusters of Iranian writers. They require a dedicated Persian corpus, confound-controlled analysis, and native-rater perception testing before promotion.
