## 15. News Summarisation

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Grusky et al. (2018), *NEWSROOM*. https://aclanthology.org/N18-1065/ | 1.3M article-summary pairs from 38 publications; diverse extractive/abstractive behavior | Include as genre/summarization research dataset, not as style-transfer ground truth |
| A2 | Narayan et al. (2018), *XSum*. https://github.com/EdinburghNLP/XSum | Extreme news summarization dataset, code and human evaluation | Include for concise-news evaluation; watch hallucination/factuality risk |

## 16. Engagement Research

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Matias & Munger et al., Upworthy Research Archive. https://upworthy.natematias.com/ | 32,487 documented headline A/B experiments; archive also documents a 2024 randomization warning affecting 22% of tests in a specific 2013-2014 window | Include as soft engagement evidence only; exclude/flag the documented randomization-risk window for confirmatory analysis and record headline/image package confounds |
| A2 | Berger & Milkman (2012), *What Makes Online Content Viral?* Journal of Marketing Research. DOI 10.1509/jmr.10.0353 | Observational + experimental evidence about arousal/emotion and sharing | Include as engagement-mechanism evidence, not universal style advice |
| B1 | Contemporary story-structure engagement experiments | Useful for structure/flow hypotheses | Require direct methods check before adding any numeric rule to profiles |

## 17. Clickbait Detection

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Potthast et al. (2018), *Crowdsourcing a Large Corpus of Clickbait on Twitter*. https://aclanthology.org/C18-1127/ | 38,517 posts, publisher/topic sampling controls, 5 annotators, graded clickbait | Include as clickbait-risk benchmark |
| A2 | Webis Clickbait Challenge 2017 resources. https://webis.de/events/clickbait-challenge/ | Benchmark and labels | Include for future classifier testing |
| B1 | Curiosity-gap linguistic analyses | Mechanism hypotheses such as superlatives/information gaps | Keep as annotation hypotheses; do not automatically ban curiosity |

## 18. Semantic Preservation

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Babakov et al. (2022), *A large-scale computational study of content preservation measures...*. https://aclanthology.org/2022.acl-srw.23/ | 57 measures on 19 annotated datasets; introduces Mutual Implication Score | Include as primary TST-preservation reference |
| A2 | Zha et al. (2023), *AlignScore*. https://aclanthology.org/2023.acl-long.634/ | Unified factual alignment trained on millions of examples; multi-dataset evaluation | Include as optional supporting metric |
| A3 | Fabbri et al. (2022), *QAFactEval*. https://aclanthology.org/2022.naacl-main.187/ | QA-based factual consistency benchmark | Include as optional factuality support |
| B1 | BERTScore. https://github.com/Tiiiger/bert_score | Widely used semantic overlap metric and implementation | Supporting metric only; never hard gate alone |

## 19. AI-generated Content Evaluation

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Liu et al. (2023), *G-Eval*. https://aclanthology.org/2023.emnlp-main.153/ | LLM-based rubric evaluation correlated with human judgement; documents evaluator bias | Include as auxiliary evaluator pattern |
| A2 | *Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge* (2025). https://aclanthology.org/2025.ijcnlp-long.18/ | Large systematic position-bias analysis | Include; require order reversal/randomization |
| B1 | MAUVE and distributional generation metrics | Useful for corpus-level distribution comparison | Future research; not directly interpretable as a tone/style quality score |

## 20. Multilingual Style Transfer

| Rank | Source | Evidence | Decision |
|---|---|---|---|
| A1 | Briakou et al. (2021), *XFORMAL*. https://aclanthology.org/2021.naacl-main.256/ | Formality benchmark in Brazilian Portuguese, French and Italian; demonstrates multilingual difficulty | Include as warning against English-only generalization |
| A2 | Mukherjee et al. (2025) | English/Hindi/Bengali evaluation meta-study | Include for language-specific metric validation |
| A3 | Universal Dependencies Persian. https://universaldependencies.org/fa/index.html | Persian treebanks and UD syntax; reproducible parser-compatible features | Include as Persian tooling foundation, not tone ground truth |
| B1 | Arabic/Urdu authorship-style-transfer shared tasks and AraGenEval | Useful Arabic-script comparative evidence | Future reference; script similarity does not imply Persian perceptual validity |

# Ranked GitHub projects for this Skill

Popularity is never used as a validity proxy. Stars below were checked in August 2026 through GitHub metadata where available.

Exact citation counts are dynamic and provider-dependent. Record the linked peer-reviewed publication and methodological contribution, but do not let a citation count override benchmark quality, dataset relevance, maintenance, or reproducibility.

| Rank | Repository | Stars | Method relevance | Maintenance signal | v0.1 decision |
|---|---|---:|---|---|---|
| 1 | `s-nlp/mutual_implication_score` | 12 | Directly targets meaning preservation in TST; benchmark code/datasets | Last push 2022 | **Reference/optional metric**. High methodological relevance despite low popularity. |
| 2 | `yuh-zha/AlignScore` | 168 | Factual alignment metric; strong multi-dataset evaluation | Last push 2024 | **Reference/optional metric**. Do not use alone. |
| 3 | `salesforce/QAFactEval` | 58 | QA-based factual consistency; directly useful to preservation checks | Pushed June 2026 | **Reference/optional metric**. |
| 4 | `llnl/LUAR` | 49 | Authorship/style representation and cross-domain generalization evidence | Last push 2024 | **Reference/future embedding route**. Particularly important for domain-transfer cautions. |
| 5 | `ykshi/text-style-transfer-benchmark` | 55 | Direct TST benchmark orientation | Last push 2021 | **Reference only**. Relevant but old/stagnant. |
| 6 | `Tiiiger/bert_score` | 1918 | Semantic similarity; mature/widely used | Last push 2024 | **Supporting metric only**. Popularity does not make it a hard gate. |
| 7 | `zacharyhorvitz/TinyStyler` | 32 | Few-shot authorship style transfer with embeddings and human evaluation | Last push 2024 | **Future model-based path**; reject from v0.1 runtime due model/fine-tuning dependency. |
| 8 | `uber-research/PPLM` | 1152 | Classic plug-and-play controllable generation | Last push 2024 | **Research only** for v0.1; GPT-2-era and inference-heavy. |
| 9 | `yangkevin2/naacl-2021-fudge-controlled-generation` | 102 | Attribute control via future discriminator | Last push 2022 | **Research only**; model/logit/predictor dependency. |
| 10 | `alisawuffles/DExperts` | 119 | Expert/anti-expert decoding | Last push 2023 | **Research only**; model integration and license metadata caution. |
