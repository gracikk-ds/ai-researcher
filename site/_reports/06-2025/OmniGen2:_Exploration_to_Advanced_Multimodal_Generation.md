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
The authors address the limitations of existing unified multimodal models, which often struggle to achieve high performance across diverse generation tasks simultaneously. Specifically, they note that models using shared parameters for both text and image generation often see a degradation in image quality. Furthermore, these models can lack the consistency required for complex tasks like precise image editing and subject-driven (in-context) generation. This is compounded by a scarcity of high-quality, diverse datasets and comprehensive benchmarks for these advanced capabilities, creating a performance gap between open-source and commercial systems.

## 2. Key Ideas and Methodology
The core idea of OmniGen2 is to decouple the architectural pathways for text and image generation to optimize for both modalities. The methodology includes:
- **Decoupled Architecture:** OmniGen2 uses a frozen, pre-trained Multimodal Large Language Model (MLLM) based on Qwen2.5-VL to process multimodal inputs and generate text. The hidden states from this MLLM then serve as conditional input for a completely separate diffusion transformer, which handles image synthesis. This separation preserves the MLLM's strong understanding capabilities.
- **Dual Image Encoders:** The model uses a ViT encoder for the MLLM (for high-level understanding) and a VAE encoder whose features are fed directly into the diffusion model (for capturing fine-grained visual details for generation).
- **Omni-RoPE:** A novel 3D rotary position embedding is introduced to handle multiple input images. It decomposes position into a sequence/modality identifier and 2D spatial coordinates, enabling the model to distinguish between different source images while maintaining spatial consistency for tasks like editing.
- **Reflection Mechanism:** The model can be fine-tuned on a dataset of generated images and corresponding textual critiques, enabling it to iteratively reflect on and correct its own outputs.

## 3. Datasets Used / Presented
OmniGen2 is trained on a combination of existing and newly created datasets:
- **Existing Data:** Training incorporates ~140M open-source images (from LAION, ShareGPT4V, etc.) and 10M proprietary images for text-to-image generation, alongside public editing datasets (e.g., UltraEdit, OmniEdit).
- **New Datasets (Constructed):** The authors developed a comprehensive data construction pipeline using video sources to create high-quality datasets for:
    - **In-Context Generation:** Extracting subjects from video frames to create training pairs with consistent identity but varied poses and scenes.
    - **Image Editing:** Creating precise instruction-based editing pairs from subtle changes between video frames.
- **New Benchmark (Presented):** The paper introduces the **OmniContext Benchmark**, a new evaluation suite for subject-driven (in-context) generation. It includes three categories (Character, Object, Scene) and eight subtasks, using GPT-4.1 to evaluate both Prompt Following (PF) and Subject Consistency (SC).

## 4. Main Results
OmniGen2 demonstrates strong, balanced performance across a range of tasks, particularly excelling in consistency and control.
- **In-Context Generation:** On the new OmniContext benchmark, OmniGen2 achieves a state-of-the-art overall score of 7.18 among open-source models, significantly outperforming prior work like BAGEL (5.73) and the original OmniGen (4.34).
- **Text-to-Image Generation:** The model is highly competitive with specialized models. On GenEval, it scores 0.86, approaching the SOTA BAGEL (0.88) with significantly fewer parameters. On DPG-Bench, its score of 83.57 rivals leading models like SD3-medium (84.08).
- **Image Editing:** On the GEdit-Bench, OmniGen2 achieves a top-tier Semantic Consistency score of 7.16. On Emu-Edit, it obtains the highest CLIP-Out score (0.309), indicating it is most effective at applying the requested edits.
The authors conclude that OmniGen2 is a versatile and efficient open-source model that achieves competitive performance by decoupling its core components.

## 5. Ablation Studies
The authors report two key preliminary experiments that motivated their final design:
1.  **Stronger LLM Impact:** When replacing the base LLM in their previous model (OmniGen) with a more powerful one, they observed a surprising *decline* in image generation quality. This suggested that parameters optimized for text are not well-suited for image modeling.
2.  **Parameter Initialization:** An experiment with a Mixture-of-Experts (MoE) architecture revealed that initializing the image-pathway parameters from the text branch led to *inferior* performance compared to random initialization.

Both findings support the core design principle of OmniGen2: to fully decouple the diffusion process from the text-centric MLLM and train its parameters from scratch.

## 6. Paper Figures
![Figure 2: Architecture of OmniGen2. OmniGen2 employs separate transformer architectures for autoregressive and diffusion. Two distinct image encoders are utilized: ViT encodes images for input into the text transformer, while VAE encodes images for the diffusion transformer.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_2.jpg' | relative_url }})
![Figure 3: An illustration of Omni-RoPE. It decomposes position information into three components: (1) a Sequence and Modality Identifier ( id seq ) that is constant for all tokens within a single image (treating it as a semantic unit) but unique across different images; and (2) and (3) 2D spatial coordinates ( h, w ) that are locally computed from (0,0) for each image entity. This dual mechanism enables the model to unambiguously distinguish different images via their unique id seq , while the shared local spatial coordinates enhance consistency for tasks like image editing.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_3.jpg' | relative_url }})
![Figure 4: Multimodal Reflection for image generation.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_4.jpg' | relative_url }})
![Figure 5: In-Context Generation Dataset Construction Pipeline. The final input images are outlined with a red border and the target image is marked by a blue boundary.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_5.jpg' | relative_url }})
![Figure 6: In-Context Editing Dataset Construction Pipeline. The final input and target images are outlined by red and blue consistent with Figure 5.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_6.jpg' | relative_url }})
![Figure 7: Create image edit pairs from videos. We first filter out frames belonging to different scenes to ensure contextual consistency, and then remove frames that exhibit significant changes in viewpoint.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_7.jpg' | relative_url }})
![Figure 8: Overview of OmniContext benchmark. Left: Image genres included in OmniContext. Right: Example images for each genre in OmniContext.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_8.jpg' | relative_url }})
![Figure 9: An illustrative example of evaluating the output image in the OmniContext benchmark.]({{ '/images/06-2025/OmniGen2:_Exploration_to_Advanced_Multimodal_Generation/figure_9.jpg' | relative_url }})
