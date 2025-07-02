---
title: FOCUS:_Unified_Vision-Language_Modeling_for_Interactive_Editing_Driven_by_Referential_Segmentation
layout: default
date: 2025-06-20
---
## FOCUS: Unified Vision-Language Modeling for Interactive Editing Driven by Referential Segmentation
**Authors:**
- Fan Yang
- Jinqiao Wang

**ArXiv URL:** http://arxiv.org/abs/2506.16806v1

**Citation Count:** 0

**Published Date:** 2025-06-20

![Figure 1: FOCUS enables fine-grained segmentation and editing for both images and videos through multimodal user instructions. It supports various region specification formats including clicks , scribbles , boxes , and masks , and for videos, annotations on any single frame suffice to guide fullclip editing. FOCUS can perform detailed region segmentation (e.g., identifying individual people), and supports diverse editing operations such as removal, replacement , and scene transformation across spatial and temporal domains.]({{ '/images/06-2025/FOCUS:_Unified_Vision-Language_Modeling_for_Interactive_Editing_Driven_by_Referential_Segmentation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current Large Vision-Language Models (LVLMs) typically handle visual perception (e.g., segmentation) and generative tasks (e.g., image editing) as separate processes, often relying on multiple, disjointed models. This separation creates a gap between understanding *what* to edit in an image and *how* to edit it, limiting their ability to perform precise, object-level manipulations based on natural language instructions. The authors address this practical problem by developing a single, unified framework that deeply integrates segmentation-aware perception with controllable generation.

## 2. Key Ideas and Methodology
The paper introduces FOCUS (Unified Vision-Language Modeling for Interactive Editing Driven by Referential Segmentation), an end-to-end LVLM designed to unify perception and generation.

-   **Core Principle**: The central hypothesis is that by jointly optimizing for segmentation and generation, the model can achieve superior fine-grained, region-controllable editing. The key mechanism is to use predicted segmentation masks as direct spatial prompts to guide the generation process.
-   **High-level Approach**: The model architecture integrates several key components:
    1.  A **dual-branch visual encoder** that processes images at two resolutions: a vanilla encoder (QwenViT-style) captures global semantics from low-resolution inputs, while a hierarchical encoder (ConvNeXt-L) extracts fine-grained, multi-scale details from high-resolution inputs.
    2.  A **generative visual tokenizer** (MoVQGAN-based) that discretizes visual information into semantic and pixel-level tokens to enhance generation quality.
    3.  A **Large Language Model** (Qwen2.5-3B) that acts as the central reasoning unit, processing text instructions and visual features to produce outputs for segmentation and generation.
    4.  A **segmentation predictor** and a **diffusion decoder** (initialized from SDXL). Based on a user's prompt, the model first predicts a segmentation mask for the target region. This mask is then fed directly into the cross-attention layers of the diffusion decoder to guide the image synthesis, ensuring the edit is localized and precise.
-   **Training Strategy**: A progressive four-stage training pipeline is employed to manage the complexity of joint optimization. The stages incrementally build capabilities: (1) pretraining the visual tokenizer and diffusion decoder, (2) warming up visual-language adapters, (3) multimodal pretraining with segmentation-aware alignment, and (4) instruction tuning for region-controlled editing tasks.

## 3. Datasets Used / Presented
FOCUS is trained using a diverse and large-scale collection of datasets structured across its progressive training stages.
-   **Stage 1 (Visual Pretraining)**: 45M image-text pairs from **COYO**, **EMOVA**, and **LAION-2B** were used to train the dual-branch visual tokenizer and the diffusion decoder on fundamental image modeling.
-   **Stage 2 & 3 (Multimodal Pretraining)**: A composite dataset was used for aligning modalities and learning structural signals. This included general image-text data (**LLaVA-150K**, **COYO**), editing data (**UltraEdit**, **AnyEdit**), segmentation data (**RefCOCO-series**, **DAVIS-2017**, **Paco-LVIS**), and dialogue/QA data (**OpenOrca**, **Magpie**).
-   **Stage 4 (Instruction Tuning)**: The model was fine-tuned on a curated set of high-quality instruction-following datasets for specific tasks, including editing (**OmniEdit**, **InstructPix2Pix**), reasoning segmentation (**ReasonSeg**, **ReVOS**), and interactive segmentation (**COCO-Interactive**).

## 4. Main Results
FOCUS demonstrates strong performance across multimodal understanding, referring segmentation, and controllable generation, often outperforming or matching larger, state-of-the-art models.
-   **Multimodal Understanding**: On the MMBench benchmark, FOCUS (3B parameters) achieves a score of 81.5, outperforming the comparable ILLUME+ (3B) model (80.8) and performing competitively with the larger Janus-Pro-7B model.
-   **Referring Segmentation**: The model achieves state-of-the-art results on standard benchmarks. On the RefCOCO testA set, it scores a mean Intersection-over-Union (mIoU) of 86.3, surpassing specialized methods.
-   **Controllable Generation and Editing**: In image editing, FOCUS achieves a high CLIP-T score of 0.275 on the Emu Edit benchmark, indicating strong alignment between the edited image and the text instruction. For image generation, it obtains a competitive FID score of 6.05 on the MJHQ-30K benchmark.
-   The authors claim these results validate the effectiveness of their unified architecture, which bridges segmentation-aware perception with fine-grained visual synthesis in a single, end-to-end framework.

## 5. Ablation Studies
The authors conducted an ablation study to validate their choice of using explicit masks for guiding the diffusion decoder.
-   **Experiment**: They compared two methods for conditioning the diffusion model: (1) their proposed approach using predicted, explicit segmentation masks as a direct spatial prompt, and (2) an alternative using learned mask token embeddings generated by the LLM.
-   **Finding**: The experiment revealed that providing direct spatial control through explicit masks resulted in significantly better localization and more faithful region editing compared to using abstract token embeddings. This finding confirms the importance of the tight integration between the segmentation and generation modules for achieving precise control.

## 6. Paper Figures
![Figure 2: Comparison of controllable image editing paradigms. (a) Modular methods rely on separately trained components. (b) Task-routing LLMs orchestrate existing tools without joint modeling. (c) Unified models combine perception and generation but lack fine-grained control. (d) Our FOCUS jointly models segmentation and generation for precise, region-level editing.]({{ '/images/06-2025/FOCUS:_Unified_Vision-Language_Modeling_for_Interactive_Editing_Driven_by_Referential_Segmentation/figure_2.jpg' | relative_url }})
![Figure 3: Overview of the FOCUS framework and training pipeline. The left part shows the unified architecture, which integrates a vanilla encoder, a hierarchical encoder, a pixel encoder, a large language model, a segmentation predictor, and a diffusion decoder for fine-grained perception and controllable image generation.]({{ '/images/06-2025/FOCUS:_Unified_Vision-Language_Modeling_for_Interactive_Editing_Driven_by_Referential_Segmentation/figure_3.jpg' | relative_url }})
