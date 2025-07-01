---
title: ICE-Bench:_A_Unified_and_Comprehensive_Benchmark_for_Image_Creating_and_Editing
layout: default
date: 2025-03-18
---
![Figure 1. Overview of our ICE-Bench , including evaluation tasks, data, and metrics.]({{ '/images/03-2025/ICE-Bench:_A_Unified_and_Comprehensive_Benchmark_for_Image_Creating_and_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the significant challenge of evaluating modern image generation models. Existing benchmarks are often too narrow, focusing on specific tasks like text-to-image creation (e.g., MS-COCO) or a limited set of editing functions. These frameworks lack comprehensive evaluation dimensions, often relying on a few metrics that may not align with human perception. Furthermore, they frequently suffer from data bias, using either exclusively real or exclusively synthetic images, which limits the ability to assess model performance on diverse data. This creates a gap for a unified, comprehensive, and unbiased benchmark to rigorously evaluate the wide-ranging capabilities of today's versatile image generation models.

## 2. Key Ideas and Methodology
The paper introduces **ICE-Bench**, a unified and comprehensive benchmark designed for the holistic evaluation of image creation and editing models. Its methodology is built on three core principles:

*   **Coarse-to-Fine Tasks:** The benchmark systematically deconstructs image generation into a hierarchy of **31 fine-grained tasks**. These are categorized into four high-level groups based on the presence of source/reference images: No-ref Creating, Ref Creating, No-ref Editing, and Ref Editing. This structure covers a broad spectrum of generation requirements, from simple text-to-image to complex, controllable editing.
*   **Multi-dimensional Metrics:** Evaluation is performed across **6 dimensions**: Aesthetic Quality, Imaging Quality, Prompt Following, Source Consistency, Reference Consistency, and Controllability. These are quantified by **11 specialized metrics**. A key innovation is the **VLLM-QA** metric, which uses a Vision Large Language Model to assess whether an editing instruction was successfully executed, providing a more robust measure of prompt following.
*   **Hybrid Data:** To ensure diversity and mitigate bias, the benchmark is built on a hybrid dataset containing both real-world and synthetically generated images.

## 3. Datasets Used / Presented
The paper presents a new benchmark dataset named **ICE-Bench**.

*   **Name:** ICE-Bench
*   **Size:** It consists of **6,538 task instances**.
*   **Domain:** The dataset covers general-purpose image creation and editing.
*   **Usage:** It is designed as a comprehensive evaluation suite. The data construction pipeline leverages large pre-trained models and human annotation to create diverse and high-quality evaluation cases, each containing inputs (text, source/reference images, masks) and a target caption.

## 4. Main Results
The authors evaluated 10 state-of-the-art image generation models (including OmniGen, ACE, FLUX, and IP-Adapter) using ICE-Bench. The main findings are:

*   **Limited Generality:** Most existing models are task-specific and show limited general-purpose capabilities. Even models designed to be versatile, like ACE and OmniGen, perform poorly on certain tasks such as Style Transfer and Face Swap.
*   **Performance Trade-offs:** A clear trade-off exists between different evaluation dimensions. For instance, models that excel in reference consistency (replicating a style or subject) often struggle with prompt adherence (following the textual instruction), and vice-versa.
*   **Impact of Scale and Data:** The results demonstrate a strong correlation between model scale, training data quality, and final imaging quality. Larger models trained on high-resolution data (e.g., OmniGen) consistently produce higher-quality images than smaller models (e.g., ACE).

The authors claim that ICE-Bench effectively highlights these strengths and weaknesses, providing a robust framework for discriminative and comprehensive model evaluation.

## 5. Ablation Studies  *(If none are reported, write “Not performed”)*
Not performed. The paper's focus is on introducing a new benchmark and using it to conduct a comparative analysis of existing models, rather than proposing a new model and ablating its components.

## 6. Paper Figures
![Figure 2. The overall pipeline of dataset construction.]({{ '/images/03-2025/ICE-Bench:_A_Unified_and_Comprehensive_Benchmark_for_Image_Creating_and_Editing/figure_2.jpg' | relative_url }})
![Figure 3. Data distribution of each task in ICE-Bench .]({{ '/images/03-2025/ICE-Bench:_A_Unified_and_Comprehensive_Benchmark_for_Image_Creating_and_Editing/figure_3.jpg' | relative_url }})
![Figure 5. Examples of generation results on 3 tasks.]({{ '/images/03-2025/ICE-Bench:_A_Unified_and_Comprehensive_Benchmark_for_Image_Creating_and_Editing/figure_5.jpg' | relative_url }})
