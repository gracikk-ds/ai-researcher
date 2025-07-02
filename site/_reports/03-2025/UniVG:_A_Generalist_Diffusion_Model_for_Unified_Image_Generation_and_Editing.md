---
title: UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing
layout: default
date: 2025-03-16
---
## UniVG: A Generalist Diffusion Model for Unified Image Generation and Editing
**Authors:**
- Tsu-Jui Fu, h-index: 2, papers: 4, citations: 12
- Yinfei Yang, h-index: 15, papers: 27, citations: 1155

**ArXiv URL:** http://arxiv.org/abs/2503.12652v2

**Citation Count:** 2

**Published Date:** 2025-03-16

![Figure 1. We introduce UniVG, a single generalist model that can support diverse image generation tasks, including text-to-image, inpainting, identity-preserving generation, layout-guided generation, instruction-based editing, depth estimation, and referring segmentation.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing diffusion models are highly specialized, requiring separate architectures, training pipelines, and parameters for different tasks like text-to-image generation, image editing, or inpainting. This proliferation of models is inefficient, computationally expensive, and difficult to manage. The authors address this gap by developing a single, generalist diffusion model capable of handling a diverse range of image generation and editing tasks within a unified framework, simplifying development and deployment.

## 2. Key Ideas and Methodology
The paper introduces UniVG, a generalist model built on a Multi-modal Diffusion Transformer (MM-DiT) and flow matching. Its core architectural principle is a minimalist and efficient input-handling strategy.

- **Unified Input Representation:** All visual guidance inputs (the latent representations of an input image, a guidance mask, and noise) are concatenated along the *channel dimension* rather than the sequence dimension. This maintains a fixed, short sequence length for the transformer, significantly improving training and inference efficiency, especially for editing tasks.
- **Progressive Multi-Stage Training:** The authors propose a crucial three-stage training recipe to balance performance across tasks and prevent "catastrophic forgetting."
    - **Stage I (Foundation):** The model is trained from scratch exclusively on text-to-image (T2I) generation.
    - **Stage II (Multi-task):** The model is then trained on a mixed dataset including T2I, in/outpainting, instruction-based editing, layout-guided generation, and auxiliary tasks like depth estimation.
    - **Stage III (Finetuning):** Finally, the model is fine-tuned on a mix of all previous tasks plus identity (ID)-preserving generation data. This final stage is essential for adding ID-customization without degrading other capabilities.

## 3. Datasets Used / Presented
UniVG is trained on a large-scale, curated collection of datasets spanning multiple tasks:
- **Text-to-Image:** Internal 2B text-image pairs, JourneyDB-4M, and DALLE3-1M.
- **Instruction-based Editing:** IPr2Pr-1M, UltraEdit-4M, SeedEdit-3M, and others.
- **In/Outpainting:** Internal scene images, OSV-5M, and Places365-1M.
- **Auxiliary Tasks:** COCO, KITTI, and Hypersim for depth/pose estimation; RefCOCO and PhraseCut for referring segmentation.
- **Layout-guided Generation:** Flickr-148K and SBU-840K.
- **ID-preserving Generation:** An internal dataset of 603K images with human faces.

## 4. Main Results
UniVG demonstrates strong performance across all tasks, often outperforming or being competitive with specialized models.
- **Text-to-Image:** Achieves a GenEval score of 0.70, matching the unified model OmniGen and competitive with the specialized SD3 model (0.71).
- **Instruction-based Editing:** Significantly outperforms baselines on the MagicBrush benchmark with a CLIP-T score of 29.5, indicating superior ability to follow editing instructions.
- **ID-preserving Generation:** Outperforms other unified models on the Unsplash-50 benchmark with an ID similarity score of 0.329.
- **Inference Efficiency:** UniVG is much more efficient for editing than prior generalist models like OmniGen (10.4s vs. 36.8s per image), thanks to its channel-wise input concatenation.

## 5. Ablation Studies
The paper presents comprehensive ablation studies to validate its design choices.
- **Task Synergy:** Adding instruction-editing and other tasks (Stage II) to the T2I foundation model (Stage I) did not degrade T2I performance. Furthermore, including auxiliary tasks (depth estimation, etc.) was shown to actively improve instruction-editing performance (MagicBrush CLIP-T score increased from 28.3 to 29.8).
- **Multi-Stage Training:** The necessity of the three-stage training recipe was confirmed. When ID-preserving generation was included from the start instead of in a separate final stage, the model suffered from catastrophic forgetting, causing ID similarity scores to drop significantly (from 0.328 to 0.245).

## 6. Paper Figures
![Figure 2. An overview of our UniVG. UniVG contains a text encoder to extract prompt embeddings from the input text and an MM-DiT to perform cross-modal fusion for latent diffusion, where all visual guidance (latent noise, input image, and input mask) are concatenated along the channel dimension as a fix-length sequence for high efficiency. Additionally, an external condition can be injected through embedding replacement to have further control. Hence, a generalist UniVG can support diverse tasks, such as text-to-image, in/outpainting, instructionbased editing, layout-guided generation, and ID-preserving generation. We also consider auxiliary tasks, including depth estimation, pose estimation, and referring segmentation, to enhance its visual scene perception.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_2.jpg' | relative_url }})
![Figure 3. Qualitative examples of text-to-image generation. Note that we simplify the prompt for better presentation.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative comparisons of instruction-based editing.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_4.jpg' | relative_url }})
![Figure 5. Resuling of model scaling with B (416M), L (1.8B), and XL (3.7B); CLIP-T for EmuEdit and ID for Unsplash-50.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Qualitative examples of layout-guided generation, where the colors of blocks are aligned with the objects in the prompt.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_6.jpg' | relative_url }})
![Figure 7. Qualitative examples of background in/outpainting and text-guided in/outpainting.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_7.jpg' | relative_url }})
![Figure 8. Qualitative examples of auxiliary tasks, including depth estimation, pose estimation, and referring segmentation.]({{ '/images/03-2025/UniVG:_A_Generalist_Diffusion_Model_for_Unified_Image_Generation_and_Editing/figure_8.jpg' | relative_url }})
