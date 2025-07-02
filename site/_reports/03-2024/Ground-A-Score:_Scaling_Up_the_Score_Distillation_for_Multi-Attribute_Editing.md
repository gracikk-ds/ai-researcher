---
title: Ground-A-Score:_Scaling_Up_the_Score_Distillation_for_Multi-Attribute_Editing
layout: default
date: 2024-03-20
---
## Ground-A-Score: Scaling Up the Score Distillation for Multi-Attribute Editing
**Authors:**
- Hangeol Chang, h-index: 1, papers: 2, citations: 3
- Jong Chul Ye, h-index: 8, papers: 16, citations: 264

**ArXiv URL:** http://arxiv.org/abs/2403.13551v1

**Citation Count:** 3

**Published Date:** 2024-03-20

![Fig. 1: Multi-attribute image editing results by Ground-A-Score.]({{ '/images/03-2024/Ground-A-Score:_Scaling_Up_the_Score_Distillation_for_Multi-Attribute_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key limitation in text-to-image diffusion models used for image editing: their tendency to fail when given long, complex text prompts that require multiple simultaneous attribute changes. Existing score distillation-based methods often overlook some parts of the prompt or introduce unintended artifacts, as the underlying text-to-image model struggles to process all the information in a complex request. This creates a bottleneck for performing intricate, multi-faceted image edits.

## 2. Key Ideas and Methodology
The paper introduces **Ground-A-Score**, a model-agnostic editing method that scales up score distillation to handle complex prompts using a "divide-and-conquer" strategy.

-   **Core Principle:** Instead of using a single complex prompt, the method breaks it down into multiple simple subtasks. For example, "A dog on grass becomes a tiger on snow" is split into "dog → tiger" and "grass → snow".
-   **High-level Approach:**
    1.  **Automated Task Decomposition:** A multimodal Large Language Model (mLLM) parses the user's request and the source image to generate source/target text prompts and a list of individual subtasks.
    2.  **Grounding:** A zero-shot object detection model (GroundingDINO) identifies the spatial location (mask) of each object to be edited in the source image.
    3.  **Grounded Gradient Aggregation:** A separate score distillation gradient is calculated for each subtask. These gradients are confined to their corresponding object masks and then aggregated. An additional "full-prompt guidance" term, using the original complete prompts, is added to maintain coherence between the edited regions.
    4.  **Null-Text Penalty:** To prevent objects from being inadvertently erased (a common failure mode), a penalty coefficient is introduced. It reduces the gradient's influence if the model is not confident about an edit, which is detected when the prediction for the target text is too similar to the prediction for a null-text.

## 3. Datasets Used / Presented
-   **Visual Genome:** For quantitative evaluation, 300 images were randomly sampled from the Visual Genome dataset. For these images, editing tasks (source and target prompts) were synthetically generated using an mLLM to create a benchmark for multi-attribute editing.
-   **Qualitative Examples:** Various images are used throughout the paper for qualitative comparisons and ablation studies.

## 4. Main Results
Ground-A-Score demonstrates superior performance in multi-attribute editing compared to baseline methods like DDS, CDS, InstructPix2Pix, and GLIGEN.

-   **Quantitative Metrics:** The method achieved the best (lowest) LPIPS score of **0.3668**, indicating higher perceptual quality and better preservation of unedited regions. While its standard CLIP score was comparable to others, its **masked CLIP score** (measuring alignment only within edited regions) was the highest at **25.07**, confirming superior fidelity to the specific edit instructions.
-   **User Study:** In a survey with 25 participants, Ground-A-Score was rated highest across all criteria: **Fidelity** (4.65/5), **Preservation** (4.65/5), and overall **Quality** (4.38/5).
-   **Author Takeaway:** The proposed method successfully adheres to intricate details of complex prompts, producing high-quality edits that respect the original image's attributes by effectively grounding and combining editing guidance.

## 5. Ablation Studies
The authors conducted several ablation studies to validate each component of their proposed pipeline.

-   **Without Subtasks:** Relying only on the full-prompt guidance (i.e., no subtask decomposition) resulted in the model failing to execute some of the requested edits.
-   **Without Masks & Full-Prompt Guidance:** Removing both the gradient masking and the full-prompt guidance term caused significant disruption, leading to a blurred background and a complete failure to perform the intended changes.
-   **Without Full-Prompt Guidance:** Removing only the coherence term resulted in blurred and distorted boundaries between simultaneously edited objects.
-   **Without Null-Text Penalty:** Removing this regularization caused the target object to disappear from the image instead of being correctly modified, demonstrating its importance in preventing object erasure.

## 6. Paper Figures
![Fig. 2: The overview of the proposed pipeline for image editing with complex user requests. (a) We leverage the prior knowledge from the multimodal LLM and the zero-shot grounding model to break down the user request into multiple image editing subtasks for a single entity. (b) A pre-trained text-to-image diffusion model is used for each subtask to obtain a corresponding gradient for the source image. These gradients are masked and aggregated to get a total gradient that is efficient and stable.]({{ '/images/03-2024/Ground-A-Score:_Scaling_Up_the_Score_Distillation_for_Multi-Attribute_Editing/figure_2.jpg' | relative_url }})
![Fig. 3: The difference between the predicted noise on the target image, with the given condition and null text, in two image editing scenarios. The source image and the output from DDS are also provided. The red boxes indicate the region corresponding to the object meant to be edited.]({{ '/images/03-2024/Ground-A-Score:_Scaling_Up_the_Score_Distillation_for_Multi-Attribute_Editing/figure_3.jpg' | relative_url }})
![Fig. 4: The benchmark result of Ground-A-Score with other baseline models using the same editing prompts.]({{ '/images/03-2024/Ground-A-Score:_Scaling_Up_the_Score_Distillation_for_Multi-Attribute_Editing/figure_4.jpg' | relative_url }})
