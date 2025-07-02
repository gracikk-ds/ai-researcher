---
title: OmniGen2:_Exploration_to_Advanced_Multimodal_Generation
layout: default
date: 2025-06-23
---
## OmniGen2: Exploration to Advanced Multimodal Generation
**Authors:**
- Chenyuan Wu
- Zheng Liu

**ArXiv URL:** http://arxiv.org/abs/2506.18871v2

**Citation Count:** None

**Published Date:** 2025-06-23

![Figure 1]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of existing unified generative models, which often struggle with task diversity, precise image editing, and maintaining subject consistency in in-context generation. While specialized models excel at specific tasks, they lack versatility. The paper aims to bridge this gap by creating OmniGen2, a powerful, open-source, and unified model that can proficiently handle a wide range of tasks—including text-to-image, image editing, and subject-driven generation—within a single framework. A key motivation is also to tackle the scarcity of high-quality data for advanced editing and in-context tasks by developing new data construction pipelines.

## 2. Key Ideas and Methodology
The core idea of OmniGen2 is to **decouple the architectural pathways for multimodal understanding and image generation**. Unlike models with shared parameters, OmniGen2 employs two distinct components:
1.  A frozen, pre-trained Multimodal Large Language Model (MLLM) (Qwen2.5-VL-3B) processes textual and visual conditions, preserving its strong, native understanding capabilities.
2.  A separate Diffusion Transformer, with randomly initialized parameters, is dedicated solely to image synthesis. It is conditioned on both high-level hidden states from the MLLM and low-level visual features from a VAE encoder.

This decoupled design avoids the performance degradation seen when adapting MLLMs for image generation. For handling multiple input images in editing and in-context tasks, the paper introduces **Omni-RoPE**, a novel 3D rotary position embedding that distinguishes between different source images while maintaining local spatial coordinate consistency to facilitate precise edits.

## 3. Datasets Used / Presented
-   **Training Data:** The model was trained on a combination of existing and newly created datasets. This includes ~140 million open-source images for text-to-image generation (e.g., Recap-DataComp, LAION), public editing datasets (e.g., UltraEdit), and understanding data (LLaVA-OneVision).
-   **Presented Data Pipelines:** To overcome the limitations of existing data, the authors developed comprehensive pipelines to generate high-quality training data from videos for:
    -   **In-Context Generation & Editing:** Creating subject-driven training pairs by tracking subjects across video frames and manipulating backgrounds.
    -   **General Image Editing:** Generating accurate editing instructions for image pairs created via inpainting techniques.
-   **Presented Benchmark:**
    -   **OmniContext:** A new, comprehensive benchmark designed to evaluate subject-driven (in-context) generation. It includes eight subtasks across Character, Object, and Scene categories and uses GPT-4.1 to score models on Prompt Following (PF) and Subject Consistency (SC).

## 4. Main Results
OmniGen2 achieves a strong balance of performance across all evaluated tasks, establishing itself as a top-tier open-source unified model.
-   **In-Context Generation:** On the newly introduced **OmniContext** benchmark, OmniGen2 achieves an overall score of **7.18**, setting a strong baseline and outperforming other open-source models like BAGEL (5.73).
-   **Text-to-Image Generation:** It achieves competitive scores of **0.86 on GenEval** and **83.57 on DPG-Bench**, rivaling much larger models while using significantly fewer trainable parameters (4B) and less training data.
-   **Image Editing:** The model sets a new state-of-the-art score of **3.44 on ImgEdit-Bench** among open-source models and demonstrates superior instruction following on other editing benchmarks.

The authors conclude that OmniGen2 is a highly capable and efficient unified generative model, with its performance particularly excelling in complex in-context generation tasks.

## 5. Ablation Studies
While a formal ablation section is not present, the "Design Principle" section details experiments that motivated the final architecture:
1.  **LLM Backbone Impact:** Replacing the original LLM with a more powerful one (Qwen) in a coupled architecture surprisingly *degraded* image generation quality.
2.  **Parameter Initialization:** An experiment using a Mixture-of-Experts (MoE) architecture showed that initializing the image branch with parameters from the text branch led to *inferior performance* compared to random initialization.

These findings validated the decision to decouple the diffusion model from the MLLM and train its parameters from scratch, which became a cornerstone of the OmniGen2 design.

## 6. Paper Figures
![Figure 2: Architecture of OmniGen2. OmniGen2 employs separate transformer architectures for autoregressive and diffusion. Two distinct image encoders are utilized: ViT encodes images for input into the text transformer, while VAE encodes images for the diffusion transformer.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_2.jpg' | relative_url }})
![Figure 3: An illustration of Omni-RoPE. It decomposes position information into three components: (1) a Sequence and Modality Identifier ( id seq ) that is constant for all tokens within a single image (treating it as a semantic unit) but unique across different images; and (2) and (3) 2D spatial coordinates ( h, w ) that are locally computed from (0,0) for each image entity. This dual mechanism enables the model to unambiguously distinguish different images via their unique id seq , while the shared local spatial coordinates enhance consistency for tasks like image editing.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_3.jpg' | relative_url }})
![Figure 4: Multimodal Reflection for image generation.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_4.jpg' | relative_url }})
![Figure 5: In-Context Generation Dataset Construction Pipeline. The final input images are outlined with a red border and the target image is marked by a blue boundary.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_5.jpg' | relative_url }})
![Figure 6: In-Context Editing Dataset Construction Pipeline. The final input and target images are outlined by red and blue consistent with Figure 5.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_6.jpg' | relative_url }})
![Figure 7: Create image edit pairs from videos. We first filter out frames belonging to different scenes to ensure contextual consistency, and then remove frames that exhibit significant changes in viewpoint.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_7.jpg' | relative_url }})
![Figure 8: Overview of OmniContext benchmark. Left: Image genres included in OmniContext. Right: Example images for each genre in OmniContext.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_8.jpg' | relative_url }})
![Figure 9: An illustrative example of evaluating the output image in the OmniContext benchmark.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_9.jpg' | relative_url }})
