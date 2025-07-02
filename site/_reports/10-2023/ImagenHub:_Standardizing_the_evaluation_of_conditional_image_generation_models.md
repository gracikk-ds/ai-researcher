---
title: ImagenHub:_Standardizing_the_evaluation_of_conditional_image_generation_models
layout: default
date: 2023-10-02
---
## ImagenHub: Standardizing the evaluation of conditional image generation models
**Authors:**
- Max Ku
- Wenhu Chen, h-index: 13, papers: 18, citations: 2004

**ArXiv URL:** http://arxiv.org/abs/2310.01596v4

**Citation Count:** 48

**Published Date:** 2023-10-02

![Figure 1: The overview of ImagenHub framework, which consists of the newly curated ImagenHub dataset, ImagenHub library, and ImagenHub evaluation platform and standard.]({{ '/images/10-2023/ImagenHub:_Standardizing_the_evaluation_of_conditional_image_generation_models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the significant inconsistencies in the evaluation of conditional image generation models. Different research papers use their own private datasets, varied inference procedures (e.g., prompt engineering, hyperparameter tuning), and non-standardized evaluation metrics. This lack of a unified benchmark makes it nearly impossible to perform fair comparisons between models, track the true progress of the field, and reproduce published results.

## 2. Key Ideas and Methodology
The paper introduces **ImagenHub**, a comprehensive framework to standardize the evaluation of conditional image generation models.

- **Core Principle:** To create a centralized, fair, and reproducible evaluation standard for a wide range of conditional image generation tasks.
- **High-level Approach:** The framework is built on three pillars:
    1.  **ImagenHub Dataset:** A newly curated, high-quality dataset covering seven prominent tasks (e.g., text-to-image, subject-driven editing, control-guided generation).
    2.  **ImagenHub Inference Library:** A unified codebase that standardizes the inference process for various models, fixing hyperparameters and prompt formats to ensure fair comparisons.
    3.  **ImagenHub Evaluator:** A standardized human evaluation protocol based on two metrics: **Semantic Consistency (SC)**, which measures alignment with input conditions, and **Perceptual Quality (PQ)**, which assesses image realism and artifacts. Both are rated on a three-point scale (0, 0.5, 1), and an overall score is calculated as the geometric mean of SC and PQ.

## 3. Datasets Used / Presented
The paper presents the **ImagenHub Dataset**, which is a collection of evaluation sets curated from existing public datasets (like DrawBench, MagicBrush, SuTI) and new instances created by the authors. It is organized into seven subsets, one for each of the following core tasks, with each subset containing 100-200 evaluation instances:
1.  Text-guided Image Generation
2.  Mask-guided Image Editing
3.  Text-guided Image Editing
4.  Subject-driven Image Generation
5.  Subject-driven Image Editing
6.  Multi-concept Image Composition
7.  Control-guided Image Generation

## 4. Main Results
After evaluating approximately 30 models, the authors reported three key findings:
- The performance of existing models is generally poor across most tasks, with 74% of models achieving an overall score below 0.5. Text-guided Image Generation (e.g., DALL-E 3, Overall: 0.76) and Subject-driven Image Generation (e.g., SuTI, Overall: 0.58) are notable exceptions.
- The evaluation rankings from ImagenHub are largely consistent with the claims in the original papers, with 83% of published rankings holding true.
- Existing automatic metrics (e.g., CLIP score, LPIPS) show very low correlation (Spearman's < 0.2) with human preference, indicating their inadequacy for holistic evaluation.

## 5. Ablation Studies
- **Overall Score Computation:** The authors compared their geometric mean score (O = √SC × PQ) against a weighted sum approach. The weighted sum was found to be misleading, as a model could achieve a high score by simply outputting a high-quality but semantically incorrect image. The geometric mean better penalizes models that fail on either consistency or quality, providing a more balanced assessment.
- **Human Evaluation Metric Range:** The authors tested different rating scales for SC and PQ. An initial four-point scale [0, 0.5, 1, 2] resulted in low inter-rater agreement. A binary scale [0, 1] was too polarized. The final three-point scale [0, 0.5, 1] with clear guidelines provided the best trade-off between granularity and rater reliability.

## 6. Paper Figures
![Figure 3: The visualization of all the conditional image generation tasks. Here we consider tasks with 1-3 conditions, where ∅ means empty. The special token [V] and [M] are special identifiers.]({{ '/images/10-2023/ImagenHub:_Standardizing_the_evaluation_of_conditional_image_generation_models/figure_3.jpg' | relative_url }})
![Figure 4: Model performance and standard deviation in each task.]({{ '/images/10-2023/ImagenHub:_Standardizing_the_evaluation_of_conditional_image_generation_models/figure_4.jpg' | relative_url }})
