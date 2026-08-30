# Concept Model

Schema version: 0.1.0

## 1. Layer boundaries

### Voice
A relatively stable set of communication invariants that persists across contexts. Examples of invariants: plainspoken vs institutionally formal identity, degree of self-reference, default empathy stance, default evidence orientation, stable terminology preferences. Voice is not a mood.

### Tone
Context-sensitive stance toward the audience and situation. Tone can change inside one Voice. Treat tone as a vector, not a label. Main axes in v0.1.0: formality, seriousness, respect/deference, enthusiasm, emotional intensity, humor, directness, epistemic caution.

### Style
Observable realization in language and rhetoric. Examples: sentence and paragraph length, lexical accessibility, pronoun use, hedging, quotation density, question frequency, metaphor frequency, information order, transition behavior, narrative/explanatory density, headline and lede structure.

### Genre
A communicative form with expected purpose, structure, and rhetorical moves. Examples: straight news report, explainer, feature, tutorial, legal notice, product help, social post. Genre constrains what structural moves are legitimate, but does not determine one Tone or Style.

## 2. Causal view

Context + Purpose + Audience + Channel + Domain Constraints + Genre
→ feasible Tone region
→ compatible Style realizations
while Voice remains comparatively stable.

Do not infer the reverse mechanically. The same observable feature can serve different functions in different genres.

## 3. Taxonomy design principle

Build the taxonomy in two levels:

1. **Dimensions**: continuous or ordinal measurable properties.
2. **Profiles**: useful clusters or target regions in the multidimensional space.

Do not promote a cluster to a named profile unless it is stable, interpretable, useful in generation, distinguishable in perception, and robust after controlling for Topic, Genre, and Length.

## 4. Evidence hierarchy

Prefer, in order:

1. corpus evidence with matched sampling and held-out replication;
2. human perception experiments or controlled evaluation;
3. reproducible benchmark/data/code;
4. explicit professional editorial rules with controlled examples;
5. expert craft guidance;
6. model-generated or prompt-only taxonomies.

A large prompt collection is not evidence of a valid style construct.

## 5. Current empirical status

v0.1.0 is an architecture and research implementation. It does not contain any Core profile. Initial profiles are Experimental until the specified 160-document media corpus and Persian validation are executed.
