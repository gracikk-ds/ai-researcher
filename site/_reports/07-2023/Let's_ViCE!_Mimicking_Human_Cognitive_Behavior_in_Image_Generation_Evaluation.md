---
title: Let's_ViCE!_Mimicking_Human_Cognitive_Behavior_in_Image_Generation_Evaluation
layout: default
date: 2023-07-18
---
## Let's ViCE! Mimicking Human Cognitive Behavior in Image Generation Evaluation
**Authors:**
- Federico Betti, h-index: 1, papers: 3, citations: 7
- Nicu Sebe

**ArXiv URL:** http://arxiv.org/abs/2307.09416v2

**Citation Count:** 7

**Published Date:** 2023-07-18

![Figure 1. Different types of Image Generation tasks. Top : in a multimodal Image Targeted Editing setup, given an input image paired with a textual instruction, the generative system is called to modify the former according to the latter. Bottom : in a cross-modal image generation setup, the generative system is called to produce an image based on the textual description provide as the sole input.]({{ '/images/07-2023/Let's_ViCE!_Mimicking_Human_Cognitive_Behavior_in_Image_Generation_Evaluation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The primary challenge addressed by the authors is the absence of a reliable and methodical automated framework for evaluating the output of image generation models. While models can produce high-quality images from text prompts, current evaluation metrics either focus on image fidelity (like FID) without considering prompt alignment, or on simple text-image similarity (like CLIPScore) which can be biased. The gold standard remains subjective and expensive human evaluation. This paper aims to bridge this gap by developing an automated method that mimics the cognitive process humans use to assess the consistency between a textual request and a generated image.

## 2. Key Ideas and Methodology
The core idea introduced is **Visual Concept Evaluation (ViCE)**, a process designed to replicate human-like reasoning for image assessment. The methodology is a unified pipeline that leverages the strengths of both Large Language Models (LLMs) and Visual Question Answering (VQA) models.

The high-level approach is as follows:
1.  **Concept Generation:** Given a text prompt, a Reasoning Model (GPT-3.5-turbo) first outlines the key "visual concepts" that are expected to be present in the generated image.
2.  **Question Formulation:** The Reasoning Model then generates a series of specific questions based on these concepts to verify their presence, attributes, and relationships within the image.
3.  **Visual Verification:** A VQA model (BLIP-2) analyzes the generated image to provide answers to these questions.
4.  **Iterative Refinement:** The system can enter a refinement cycle, where the Reasoning Model asks follow-up questions based on the initial answers to gain a deeper understanding of the image.
5.  **Scoring:** Finally, the Reasoning Model evaluates the complete set of questions and answers to produce a final score that quantifies the image's adherence to the original prompt.

## 3. Datasets Used / Presented
The study did not present a new dataset. For the experimental evaluation, the authors generated a set of **1000 images** using the **Stable Diffusion 2** model. The text prompts used for generation were sampled from a diverse collection of existing datasets, including **DALL-EVAL** and **COCO**, to ensure the evaluation was not limited to a single domain. These 1000 generated image-prompt pairs were then scored by human evaluators on a 0-10 scale for prompt consistency, providing a ground-truth benchmark for comparing automated metrics.

## 4. Main Results
*   ViCE demonstrated the strongest linear relationship with human judgments among the tested metrics, achieving the highest **Pearson correlation of 0.332**. This outperformed other methods like LLMScore (0.293), BLIP-ITC (0.269), and CLIPScore (0.195).
*   While LLMScore achieved a slightly higher non-parametric (Spearman) correlation, visual analysis using Bland-Altman plots showed that LLMScore tends to overestimate image quality compared to human scores. In contrast, ViCE's scores showed a more balanced distribution, indicating closer alignment with human evaluations.
*   The authors claim that ViCE provides a more reliable and trustworthy automated evaluation method by moving beyond simple similarity measurement to a more nuanced, cognitive assessment process that mirrors human reasoning.

## 5. Ablation Studies
The authors performed ablation studies to assess the importance of different components of the ViCE pipeline.

*   **No Refinement (`ViCE_blind`):** A version of the model was tested using only the initial "blind" questions, without the iterative refinement step. This resulted in a performance drop, with the Pearson correlation decreasing from 0.332 to 0.275. This highlights the value of the refinement cycle in achieving a more accurate assessment.
*   **Reduced Questions (`ViCE_5`):** A simplified version was tested using only 5 initial questions and no refinement. The performance degraded further, with the Pearson correlation falling to 0.252. This demonstrates that a sufficient number of detailed questions is critical for the model to effectively reason about the image content and its alignment with the prompt.

## 6. Paper Figures
![Figure 2. Visual Concept Evaluation Pipeline]({{ '/images/07-2023/Let's_ViCE!_Mimicking_Human_Cognitive_Behavior_in_Image_Generation_Evaluation/figure_2.jpg' | relative_url }})
![Figure 3. Bland-Altman plots for different automated metrics.]({{ '/images/07-2023/Let's_ViCE!_Mimicking_Human_Cognitive_Behavior_in_Image_Generation_Evaluation/figure_3.jpg' | relative_url }})
![Figure 4. ViCE applied to the ITE task, whereby an LLM generates context-specific queries to assess the quality of the edit. The variation in the generated responses offers insights about the effectiveness of the edit operations.]({{ '/images/07-2023/Let's_ViCE!_Mimicking_Human_Cognitive_Behavior_in_Image_Generation_Evaluation/figure_4.jpg' | relative_url }})
