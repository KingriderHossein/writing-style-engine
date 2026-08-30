## 1. Text Style Transfer

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Jin et al. (2022), *Deep Learning for Text Style Transfer: A Survey*. Computational Linguistics. DOI 10.1162/coli_a_00426. https://aclanthology.org/2022.cl-1.6/ | Survey of 100+ representative TST papers; tasks, datasets, evaluation, methods | Include as field map; do not treat survey taxonomies as validated Persian profiles |
| A2 | Mir et al. (2019), *Evaluating Style Transfer for Text*. https://aclanthology.org/N19-1049/ | Human + automatic evaluation; separates transfer intensity, content preservation, naturalness; released software | Include for multidimensional evaluation design |
| A3 | Krishna et al. (2020), *Reformulating Unsupervised Style Transfer as Paraphrase Generation*. https://aclanthology.org/2020.emnlp-main.55/ | Large style corpus, human evaluation, demonstrates metric gaming/trade-offs | Include as warning against single automatic metrics |

## 2. Controllable Text Generation

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Hu et al. (2017), *Toward Controlled Generation of Text*. https://proceedings.mlr.press/v70/hu17e.html | Explicit attribute control with learned discriminators | Research foundation only; not a v0.1 dependency |
| B1 | Yang & Klein (2021), *FUDGE: Controlled Text Generation with Future Discriminators*. https://www.microsoft.com/en-us/research/publication/fudge-controlled-text-generation-with-future-discriminators/ | Code; attribute predictors; compositional control | Future model-based route; reject from v0.1 execution because it requires model/logit integration |
| B2 | Dathathri et al. (2020), *Plug and Play Language Models*. https://github.com/uber-research/PPLM | Code; plug-and-play steering | Future reference; older GPT-2-era control and heavier inference loop |
| B3 | Liu et al. (2021), *DExperts*. https://github.com/alisawuffles/DExperts | Code; expert/anti-expert controlled decoding | Future reference; requires model experts and generation integration |

## 3. Stylometry

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Stamatatos (2009), *A Survey of Modern Authorship Attribution Methods*. JASIST. DOI 10.1002/asi.21001 | Seminal survey of lexical, character, syntactic and structural stylometry | Include for feature families and leakage warnings |
| A2 | Abbasi & Chen (2008), *Writeprints: A Stylometric Approach to Identity-Level Identification and Similarity Detection in Cyberspace*. ACM TISSEC. DOI 10.1145/1344411.1344413 | Explicit multi-family style feature representation | Include as feature-schema precedent; do not equate authorship identity with communicative tone |

## 4. Authorship Style Transfer

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Rivera-Soto et al. (2021), *Learning Universal Authorship Representations*. https://aclanthology.org/2021.emnlp-main.70/ | Cross-domain authorship representation benchmark | Include as evidence that transfer across domains is non-trivial |
| B1 | Horvitz et al. (2024), *TinyStyler*. https://github.com/zacharyhorvitz/TinyStyler | Code, few-shot authorship embeddings, automatic + human evaluation | Future model-based path; reject from v0.1 execution because it depends on trained/fine-tuned models |

## 5. Style Representation

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Riley et al. (2021), *TextSETTR: Few-Shot Text Style Extraction and Tunable Targeted Restyling*. https://aclanthology.org/2021.acl-long.293/ | Style vectors, targeted restyling, multiple style phenomena | Include as evidence for continuous/multidimensional control rather than adjective labels |
| A2 | Biber & Conrad (2009), *Register, Genre, and Style*. Cambridge University Press | Explicit conceptual distinction among register, genre, style; linguistic feature distributions | Include conceptually; avoid importing English thresholds into Persian |
| A3 | Biber multidimensional register-analysis tradition | Co-occurring linguistic feature dimensions with functional interpretation | Include as methodological model for corpus-derived dimensions |

## 6. Style Evaluation

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Mir et al. (2019) | Multi-axis human/automatic evaluation | Include |
| A2 | Briakou et al. (2021), *A Review of Human Evaluation for Style Transfer*. https://aclanthology.org/2021.gem-1.6/ | Review of 97 TST papers; human protocols often underspecified | Include; require reproducible annotation protocol |
| A3 | Mukherjee et al. (2025), *Evaluating Text Style Transfer Evaluation: Are There Any Reliable Metrics?*. https://aclanthology.org/2025.naacl-srw.41/ | Multilingual meta-evaluation against human judgements | Include; supports metric ensembles and language-specific validation |

## 7. Voice and Tone Systems

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Nielsen Norman Group, *The Four Dimensions of Tone of Voice*. https://www.nngroup.com/articles/tone-of-voice-dimensions/ | Controlled perceptual dimensions: humor, formality, respect, enthusiasm | Include as tone-axis seed, not a complete taxonomy |
| A2 | Nielsen Norman Group, *The Impact of Tone of Voice on Users' Brand Perception*. https://www.nngroup.com/articles/tone-voice-users/ | Controlled near-identical samples and user perception | Include as evidence that tone differences can be experimentally measured |
| A3 | Intuit Content Design, *Voice & tone*. https://contentdesign.intuit.com/ai/voice-tone/ | Voice/tone separation, situational tone, practical AI-content rules | Include as professional workflow evidence |
| A4 | Mailchimp, *Voice and Tone*. https://styleguide.mailchimp.com/voice-and-tone/ | Explicit voice/tone rules and controlled examples | Include as professional rule source |
