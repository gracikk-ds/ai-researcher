---
title: Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment
layout: default
date: 2025-04-10
---
## Marmot: Multi-Agent Reasoning for Multi-Object Self-Correcting in Improving Image-Text Alignment
**Authors:**
- Jiayang Sun
- Ran He

**ArXiv URL:** http://arxiv.org/abs/2504.20054v2

**Citation Count:** 0

**Published Date:** 2025-04-10

![Figure 1: Existing diffusion-based models often struggle with image-text inconsistencies in object counting, attributes, and spatial relationships during the generation process. Our Marmot can seamlessly integrate with text-to-image models to facilitate object-level self-correction, ensuring precise alignment with user descriptions in object counting, attributes, and spatial relationships.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a critical limitation in diffusion-based text-to-image models: their struggle to accurately generate complex scenes with multiple objects. These models often fail in three key areas: correct object counting, binding attributes (e.g., color, shape) to the right objects, and maintaining correct spatial relationships between objects. While recent self-correction frameworks using Multimodal Large Language Models (MLLMs) as a single agent have been proposed, they are highly dependent on the MLLM's capabilities and often fail to handle all objects and their relationships simultaneously, leading to incomplete or incorrect edits.

## 2. Key Ideas and Methodology
The paper introduces **Marmot**, a novel framework for multi-object self-correction that improves image-text alignment. Its methodology is built on three core ideas:

1.  **Divide-and-Conquer Strategy:** The complex task of self-correction is decomposed into fine-grained, object-level subtasks categorized into three dimensions: counting, attributes, and spatial relationships. This simplifies the problem and allows for focused correction.

2.  **Multi-Agent Self-Correcting System:** For each subtask, Marmot employs a robust **decision-execution-verification** mechanism. This system consists of three specialized agents: a **Decision-Maker** to identify errors, an **Executor** to perform the edits using appropriate models, and a **Verifier** to confirm the correction was successful. This loop-based approach prevents inter-object interference and enhances the reliability of edits by catching failures from either the agent's reasoning or the editing tool.

3.  **Pixel-Domain Stitching Smoother (PDSS):** To efficiently integrate the results from parallel subtask edits, Marmot introduces PDSS. This module first erases the objects to be modified, pastes the new edited objects, and then uses a mask-guided, two-stage latent space optimization with the SDXL-Refiner model. This process seamlessly blends the edited objects into the background, enhancing details and preventing the distortion artifacts common in multi-stage editing pipelines.

## 3. Datasets Used / Presented
-   **T2I-CompBench:** A comprehensive benchmark used for the primary quantitative evaluation of text-to-image generation. It contains complex prompts designed to test a model's compositional reasoning, specifically in attribute binding and spatial/non-spatial relationships.
-   **COCO (Common Objects in Context):** Used for evaluating the framework's performance on layout-to-image generation tasks. The authors created a test set by randomly sampling 100 layouts and assigning color or texture attributes to objects to test attribute modification accuracy.

## 4. Main Results
Marmot significantly enhances the performance of existing text-to-image models. When applied to SDXL on the T2I-CompBench benchmark, it achieved improvements of **11.76% in color**, **6.86% in shape**, and **5.47% in texture** attribute binding. Most notably, it boosted spatial relationship accuracy by **13.12%**. When applied to DALL-E 3, it improved spatial accuracy by **8.08%**. The authors claim that Marmot, using only 8B-parameter open-source models, achieves performance superior to state-of-the-art self-correction frameworks that rely on the much larger, closed-source GPT-4.

## 5. Ablation Studies
-   **Verification Mechanism:** Removing the Verifier and trusting the Decision-Maker's initial command caused a significant drop in performance. For SDXL, attribute binding accuracy for color, shape, and texture decreased by 5.10%, 4.93%, and 5.19%, respectively. This highlights the Verifier's critical role in correcting failures from the editing models.

-   **Two-Stage Visual Reasoning:** Replacing the proposed MLLM+LLM reasoning paradigm with a single MLLM for decision-making reduced performance. Color accuracy dropped by 4.37%, demonstrating that the two-stage approach is more robust and less prone to logical errors.

-   **Parallel vs. Serial Editing:** A qualitative comparison showed that the proposed parallel editing strategy with PDSS effectively preserves background integrity, whereas a serial editing approach (one edit after another) leads to noticeable background distortion.

-   **PDSS Base Model:** Using SDXL-Refiner as the base model for the PDSS module resulted in significantly better detail refinement and realism compared to using the SDXL-Base model, which tended to reconstruct images rather than refine them.

-   **PDSS Hyperparameter K:** The study analyzed the effect of `K`, the number of mask-guided refinement steps. Setting `K=0.75*T` (where T is the total steps) was found to provide the optimal balance between smoothing object edges and preserving background details, as validated by ImageReward scores.

## 6. Paper Figures
![Figure 2: Architecture Comparison Between Single Agent Framework and Marmot. We decompose self-correction into counting, attributes, and spatial dimensions, achieving superior results using only 8B MLLMs and LLMs.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_2.jpg' | relative_url }})
![Figure 3: Overview of Marmot. (a) We first extract descriptions and spatial relationships of scene objects and dynamically adjust the number of objects to achieve counting self-correcting. (b) Subsequently, we perform independent segmentation of each object and utilize a multi-agent self-correcting system to conduct fine-grained editing of each object. (c) Simultaneously, spatially correlated object pairs undergo layout rectification via a parallelized multi-agent self-correcting system. (d) Ultimately, our PDSS seamlessly integrates three-dimensional editing results, while the SDXL-Refiner [26] coupled with composite mask enhances object details and smooth edges.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_3.jpg' | relative_url }})
![Figure 4: The following is a case from a multiagent self-correcting system , demonstrating the collaborative process of attribute self-correction for the “yellow deer”. This case also showcases our two-stage visual reasoning paradigm based on MMCoT [51].]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_4.jpg' | relative_url }})
![Figure 5: Visual Comparisons with Text-to-Image Generation Models. Incorporation with our framework enables more precise modeling of counting, attributes, and spatial relationships within objects, producing images that comprehensively align with user prompts.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_5.jpg' | relative_url }})
![Figure 6: Visual Comparisons with Self-Correcting Framework. Our framework achieves balanced attention to each object in the scene through task decomposition and multi-agent collaborative reasoning, making it the only framework capable of effectively handling the “white deer”.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_6.jpg' | relative_url }})
![Figure 7: Comparison between serial editing and parallel editing with PDSS. Serial editing distorts backgrounds, but our PDSS parallel editing preserves and enhances them.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_7.jpg' | relative_url }})
![Figure 8: Comparison between different base model of PDSS. SDXL-Refiner further refines the details of objects within the image.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_8.jpg' | relative_url }})
![Figure 9: Ablation study on the value of K steps. As the value of K decreases, the edges of objects become increasingly smooth. However, this comes at the cost of deteriorating detail representation.]({{ '/images/04-2025/Marmot:_Multi-Agent_Reasoning_for_Multi-Object_Self-Correcting_in_Improving_Image-Text_Alignment/figure_9.jpg' | relative_url }})
