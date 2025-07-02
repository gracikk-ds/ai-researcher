---
title: KRIS-Bench:_Benchmarking_Next-Level_Intelligent_Image_Editing_Models
layout: default
date: 2025-05-22
---
## KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models
**Authors:**
- Yongliang Wu, h-index: 4, papers: 10, citations: 50
- Xu Yang

**ArXiv URL:** http://arxiv.org/abs/2505.16707v1

**Citation Count:** None

**Published Date:** 2025-05-22

![Figure 1: (a) We present KRIS-Bench, a benchmark for instruction-based image editing grounded in a knowledge-based reasoning taxonomy. It covers 3 knowledge dimensions, 7 reasoning dimensions, and 22 editing tasks. Specific examples are shown in Figure 2 . (b) Given an editing pair of (image, instruction) under a specific reasoning dimension ( i.e. , Chemistry in Natural Science), we evaluate the output of image editing models with automated VLM tools over the proposed four complementary metrics, which are aligned with human scoring.]({{ '/images/05-2025/KRIS-Bench:_Benchmarking_Next-Level_Intelligent_Image_Editing_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Recent instruction-based image editing models can produce visually impressive results but often lack the deep reasoning required for knowledge-intensive tasks. For example, a model might place sodium in water without depicting the resulting violent chemical reaction. Existing benchmarks do not systematically evaluate these higher-order reasoning capabilities, creating a gap in understanding and advancing the intelligence of these systems. The authors address this by developing a framework to assess models' ability to perform edits grounded in factual, conceptual, and procedural knowledge.

## 2. Key Ideas and Methodology
The paper introduces **KRIS-Bench (Knowledge-based Reasoning in Image-editing Systems Benchmark)**, a diagnostic tool for evaluating image editing models. The core idea is a new taxonomy for editing tasks inspired by educational theory, categorizing them into three foundational knowledge types:
*   **Factual Knowledge**: Requires direct perception of attributes, spatial relationships, or temporal sequences.
*   **Conceptual Knowledge**: Requires applying abstract principles from domains like social or natural sciences.
*   **Procedural Knowledge**: Requires multi-step, rule-based, or logical reasoning.

Based on this taxonomy, the authors designed 22 tasks across 7 reasoning dimensions. To evaluate models, they propose a comprehensive protocol that includes a novel metric called **Knowledge Plausibility (KP)**. This metric assesses whether an edit is consistent with real-world principles. To facilitate this, each relevant test case is paired with a "knowledge hint" that provides the ground-truth outcome (e.g., "solid sodium will react violently with water"), guiding the evaluation.

## 3. Datasets Used / Presented
The paper presents the **KRIS-Bench** dataset. It consists of **1,267 high-quality annotated editing instances** designed to test a wide range of reasoning skills. The dataset spans **22 distinct tasks** (e.g., Anomaly Correction, Chemistry, Rule-based Reasoning) which are organized under the 7 reasoning dimensions and 3 knowledge types. The images were collected from the internet, generative models, and existing academic datasets, with instructions created by trained annotators and reviewed by experts.

## 4. Main Results
Experiments were conducted on 10 state-of-the-art models, including 3 closed-source (GPT-4o, Gemini 2.0, Doubao) and 7 open-source models.
*   Closed-source models substantially outperform open-source models, with **GPT-4o achieving the highest overall score (80.09/100)**.
*   All models performed weakest on **Procedural Knowledge** tasks, indicating significant challenges with multi-step reasoning and task decomposition.
*   While models achieved high scores in Visual Quality and Visual Consistency, their performance dropped significantly in Instruction Following and especially **Knowledge Plausibility**. This highlights a persistent gap between generating visually plausible images and generating knowledge-consistent ones.

The authors conclude that current models have significant limitations in knowledge-centric reasoning, underscoring the need for benchmarks like KRIS-Bench to drive progress.

## 5. Ablation Studies
The paper reports two key analyses that serve as ablation studies:

1.  **Reasoning Process Integration**: The performance of the BAGEL-Think model (which incorporates an explicit reasoning process) was compared to the baseline BAGEL model. BAGEL-Think showed a marked improvement across all knowledge types, with its overall average score increasing from **39.70 to 47.76**. This demonstrates that integrating a reasoning process is critical for improving performance on knowledge-grounded tasks.
2.  **Evaluation Protocol Validation**: A user study was conducted to validate the automated VLM-based evaluation. The authors compared their prompts incorporating "knowledge hints" against simple baseline prompts. For the Knowledge Plausibility metric, the knowledge-enhanced prompts achieved a much stronger Pearson correlation with human ratings (**r=0.94 vs. 0.66**) and a significantly lower Mean Absolute Error (**MAE=0.23 vs. 1.62**). This confirms that the proposed evaluation protocol with knowledge hints is more reliable and aligned with human judgment.

## 6. Paper Figures
![Figure 2: Representative examples from the 22 knowledge-based reasoning image editing tasks in KRIS-Bench. Each task is designed to evaluate specific knowledge grounded in factual, conceptual, or procedural, covering diverse reasoning dimensions.]({{ '/images/05-2025/KRIS-Bench:_Benchmarking_Next-Level_Intelligent_Image_Editing_Models/figure_2.jpg' | relative_url }})
![Figure 3: Visualization results of (a) Color Change, (b) Position Movement, (c) Humanities, (d) Chemistry, and (e) Abstract Reasoning across different models and metrics. Each example is provided with scores across the four evaluation metrics as well as an overall average score. Note that the knowledge hint is provided solely for evaluation and has been shortened for better illustration.]({{ '/images/05-2025/KRIS-Bench:_Benchmarking_Next-Level_Intelligent_Image_Editing_Models/figure_3.jpg' | relative_url }})
