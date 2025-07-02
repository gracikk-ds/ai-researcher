---
title: InsightEdit:_Towards_Better_Instruction_Following_for_Image_Editing
layout: default
date: 2024-11-26
---
## InsightEdit: Towards Better Instruction Following for Image Editing
**Authors:**
- Yingjing Xu, h-index: 1, papers: 4, citations: 4
- Qiang Liu

**ArXiv URL:** http://arxiv.org/abs/2411.17323v1

**Citation Count:** 1

**Published Date:** 2024-11-26

![Figure 1. We propose InsightEdit , an end-to-end instruction-based image editing model, trained on high-quality data and designed to fully harness the capabilities of Multimodal Large Language Models (MLLM), achieving high-quality edits with strong instruction-following and background consistency.]({{ '/images/11-2024/InsightEdit:_Towards_Better_Instruction_Following_for_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address two primary limitations in existing instruction-based image editing models. First, current datasets suffer from low resolution, poor background consistency after edits, and overly simplistic, template-based instructions, which hinders model training for complex tasks. Second, existing models primarily rely on textual conditions and underutilize the rich visual information from the source image, leading to inferior performance in following complex instructions and maintaining background integrity.

## 2. Key Ideas and Methodology
The paper introduces two main contributions to solve these problems: a new dataset and a novel model architecture.

-   **Core Idea:** The central hypothesis is that guiding the diffusion process with both high-level textual instructions and rich visual features, as reasoned by a Multimodal Large Language Model (MLLM), will lead to more precise and context-aware image edits.
-   **Methodology:**
    1.  **Automated Data Pipeline:** An automated pipeline is proposed to create a high-quality dataset. It uses an MLLM to extract object details from high-resolution images, GroundedSAM for masking, a mask-based editing model to generate high-fidelity edits (removal, addition, replacement), and another MLLM to generate diverse and complex instructions.
    2.  **InsightEdit Model:** The proposed model, `InsightEdit`, features a two-stream bridging mechanism.
        -   **Comprehension Module:** An MLLM (LLaVA) processes the source image and text instruction to generate special `[MM]` tokens that encapsulate multimodal understanding.
        -   **Bridging Module:** This module has two branches to condition the diffusion model: a **Textual Branch** extracts instructional concepts from the `[MM]` tokens, while an **Image Branch** with a novel **Image Alignment Adapter (IAA)** aligns the `[MM]` tokens with the target image features, providing direct visual supervision for the edit.
        -   **Generation Module:** A diffusion U-Net uses a decoupled cross-attention mechanism to integrate both the textual and image conditions to generate the final image.

## 3. Datasets Used / Presented
-   **AdvancedEdit Dataset (Proposed):** A large-scale dataset of 2,536,674 editing pairs created using the authors' automated pipeline. The source images are high-resolution (1024x1024) photographs from Pexels. It is divided into:
    -   `SimpleEdit`: Pairs with simple instructions.
    -   `AdvancedEdit`: Pairs with complex, reasoning-based instructions.
-   **AdvancedEdit-Eval (Proposed):** A curated evaluation set of 300 image pairs with intricate editing scenarios to test model capabilities.
-   **Reason-Edit:** An existing benchmark used for evaluation, designed to assess editing abilities across various reasoning scenarios (e.g., spatial, color, size).

## 4. Main Results
-   On the proposed **AdvancedEdit-Eval** benchmark, `InsightEdit` trained with the `AdvancedEdit` dataset achieved state-of-the-art performance, outperforming methods like SmartEdit-7B with a VIEScore of **0.831** vs. 0.682 and a CLIPScore of **21.002** vs. 20.114, indicating superior instruction following and human preference.
-   On the **Reason-Edit** benchmark, `InsightEdit` also set a new state-of-the-art, achieving a VIEScore of **0.934** in "Understanding" scenarios and **0.947** in "Reasoning" scenarios, demonstrating its advanced comprehension and execution capabilities.
-   The authors claim that their method excels in complex instruction following and maintaining high background consistency, which is supported by both quantitative metrics (PSNR, SSIM, LPIPS) and qualitative examples.

## 5. Ablation Studies
-   **Effectiveness of the Image Alignment Adapter (IAA):** An ablation was performed by removing the IAA module. This resulted in a drop in performance across all metrics (e.g., PSNR dropped from 22.871 to 22.348). Qualitatively, the model without IAA struggled with background consistency (e.g., erroneously changing a house into wildflowers) and produced less natural edits.
-   **Impact of Instruction Complexity:** The model was trained on different data subsets.
    -   Training with the `SimpleEdit` dataset provided a performance boost over the baseline.
    -   Further training with the `AdvancedEdit` dataset (containing complex instructions) led to substantial improvements, especially in instruction following metrics like CLIPScore and VIEScore. Qualitatively, the model trained on `AdvancedEdit` could execute more nuanced and detailed instructions accurately (e.g., replacing a bird with a specific monarch butterfly).

## 6. Paper Figures
![Figure 2. The overall data construction pipeline. (1) Captioning & Object Extraction: Utilizing VLM to generate a global caption from the source image, and further get an object JSON list contains both simple caption and detailed caption. (2) Mask Generation: Utilizing GroundedSAM to obtain the corresponding mask of each object. (3) Editing Pair Construction: Utilizing mask-based image editing model to construct target image and templated instruction. (4) Instruction Recaptioning: Utilizing VLM to rewrite instruction to gain diverse instructions. (5) Quality Evaluation: Filtering the datasets using VIEScore.]({{ '/images/11-2024/InsightEdit:_Towards_Better_Instruction_Following_for_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3. The overall architecture of InsightEdit. It mainly consists of three parts: (1) Comprehension Module: A comprehension module that leverages MLLM to perceive and comprehend the image editing task; (2) Bridging Module: A bridging module that better interacts and extracts both the textual and image features; (3) Generation Module: A generation module that receives editing guidance via diffusion model to generate the target image.]({{ '/images/11-2024/InsightEdit:_Towards_Better_Instruction_Following_for_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative comparison on AdvancedEdit. InsightEdit shows superior instruction following and background consistency capability.]({{ '/images/11-2024/InsightEdit:_Towards_Better_Instruction_Following_for_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5. Demonstration of the effectiveness of the IAA module.]({{ '/images/11-2024/InsightEdit:_Towards_Better_Instruction_Following_for_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Demonstration of the effectiveness of AdvancedEdit.]({{ '/images/11-2024/InsightEdit:_Towards_Better_Instruction_Following_for_Image_Editing/figure_6.jpg' | relative_url }})
