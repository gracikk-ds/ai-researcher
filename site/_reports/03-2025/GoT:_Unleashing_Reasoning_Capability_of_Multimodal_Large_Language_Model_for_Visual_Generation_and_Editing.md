---
title: GoT:_Unleashing_Reasoning_Capability_of_Multimodal_Large_Language_Model_for_Visual_Generation_and_Editing
layout: default
date: 2025-03-13
---
![Figure 1. Generation Chain-of-Thought (GoT) with Semantic-Spatial Reasoning. Our approach transforms input prompts into explicit reasoning chains with coordinates (middle), which guides vivid image generation and precise editing (right). This reasoning-based generation paradigm unifies spatial understanding across visual tasks: semantically-grounded visual generation (top), controllable interactive generation (middle), and localized image editing (bottom).]({{ '/images/03-2025/GoT:_Unleashing_Reasoning_Capability_of_Multimodal_Large_Language_Model_for_Visual_Generation_and_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current image generation and editing models process textual prompts directly, often failing to comprehend complex scenes that require precise spatial arrangements or specific object relationships. This lack of explicit reasoning leads to errors in composition. While Multimodal Large Language Models (MLLMs) possess advanced reasoning skills, these capabilities have not been effectively integrated into visual synthesis pipelines. The authors address this gap by proposing a method to embed a reasoning process directly into the generation and editing workflow.

## 2. Key Ideas and Methodology
The core idea is the **Generation Chain-of-Thought (GoT)**, a novel paradigm where the model first generates an explicit reasoning chain before producing an image. This GoT is a structured textual plan that includes both semantic descriptions of objects and their explicit spatial coordinates (e.g., bounding boxes).

The methodology consists of a unified end-to-end framework that leverages an MLLM (Qwen2.5-VL) as a reasoning engine and a diffusion model for image synthesis. The MLLM processes the user's input (a text prompt or an editing instruction) to generate the GoT. This reasoning chain then guides the diffusion process via a novel **Semantic-Spatial Guidance Module (SSGM)**. The SSGM conditions the image generation on three signals:
1.  **Semantic Guidance (`Gt`)**: Embeddings from the MLLM representing the content.
2.  **Spatial Guidance (`Gs`)**: Features derived from the coordinates in the GoT.
3.  **Reference Image Guidance (`Gr`)**: For editing tasks, features from the source image.

This design unifies text-to-image generation, interactive generation, and image editing into a single, reasoning-guided system.

## 3. Datasets Used / Presented
The authors constructed the first large-scale datasets with detailed GoT annotations to train their model.
*   **GoT Generation Dataset**: Contains 8.4 million samples. It was created by processing images from existing datasets (LAION-Aesthetics, JourneyDB, FLUX.1) through an automated pipeline using Qwen2-VL and Qwen2.5 to generate rich semantic-spatial descriptions (the GoT).
*   **GoT Editing Dataset**: Contains 920,000 samples. It was built upon the OmniEdit and SEED-Edit-Multiturn datasets, with GoT annotations generated to break down editing instructions into structured reasoning steps.

## 4. Main Results
The GoT framework demonstrated state-of-the-art performance on both generation and editing tasks.
*   **Text-to-Image Generation**: On the GenEval benchmark, the model achieved the highest overall score of 0.64, outperforming strong baselines like SD3 (0.62) and JanusFlow (0.63). It particularly excelled in tasks requiring accurate counting (0.67) and color rendering (0.85).
*   **Image Editing**: The model achieved top scores on multiple benchmarks, including Emu-Edit (0.864 CLIP-I) and ImagenHub (0.533 GPT-4o Eval). It showed superior ability to handle complex edits requiring precise spatial and semantic understanding.
*   **Author Takeaway**: By integrating an explicit reasoning step, the GoT framework significantly enhances the compositional accuracy, controllability, and alignment of visual generation models with human intent.

## 5. Ablation Studies
The authors conducted an ablation study to validate the contributions of each component of their framework.
*   **Baseline**: A model without GoT reasoning or the SSGM performed poorly (GenEval score: 0.38).
*   **Adding GoT Reasoning**: Introducing the GoT reasoning chains provided a slight improvement in semantic guidance (GenEval score: 0.40).
*   **Adding SSGM**: Incorporating the Semantic-Spatial Guidance Module significantly improved performance, especially for editing tasks that rely on spatial control (ImagenHub score increased from 0.181 to 0.370).
*   **Full Framework**: The complete model, including GoT, SSGM, and extensive pretraining, achieved the highest scores (GenEval: 0.64, ImagenHub: 0.533), demonstrating that all components and the pretraining phase are critical for achieving state-of-the-art results.

## 6. Paper Figures
![Figure 2. GoT Dataset Construction Process. Left: Text-to-image GoT annotation pipeline that labels detailed GoT with semantic content and spatial coordinates. Right: Editing GoT annotation pipeline that processes source image, target image, and instruction to generate entity-aware reasoning GoT with precise spatial grounding. Both pipelines leverage Qwen2-VL [ 46 ] and Qwen2.5 [ 51 ] models for various stages of the annotation process.]({{ '/images/03-2025/GoT:_Unleashing_Reasoning_Capability_of_Multimodal_Large_Language_Model_for_Visual_Generation_and_Editing/figure_2.jpg' | relative_url }})
![Figure 3. GoT Framework with Semantic-Spatial Guidance. Left: Our dual-task framework handling both text-to-image generation (T2I) and image editing. Right: The SSGM Diffusion Module, which combines spatial layouts guidance G s , reference image guidance G r , and semantic guidance G t to generate the final image with precise content and spatial control.]({{ '/images/03-2025/GoT:_Unleashing_Reasoning_Capability_of_Multimodal_Large_Language_Model_for_Visual_Generation_and_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Text-to-Image samples generated by our model. The GoT framework can plan object placement based on the input caption and generate highly aligned and aesthetic images accordingly.]({{ '/images/03-2025/GoT:_Unleashing_Reasoning_Capability_of_Multimodal_Large_Language_Model_for_Visual_Generation_and_Editing/figure_4.jpg' | relative_url }})
![Figure 5. Samples on interactive generation with GoT framework. By modifying GoT content (description and bounding box position), user can customize their text-to-image process with: 1. Object replacement 2. Object position adjustment 3. Object attribute modification.]({{ '/images/03-2025/GoT:_Unleashing_Reasoning_Capability_of_Multimodal_Large_Language_Model_for_Visual_Generation_and_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Qualitative results of image editing. Our GoT framework demonstrates superior performance in settings that require semantic-spatial reasoning. Red bounding boxes indicate the coordinates predicted by MLLM within the GoT framework.]({{ '/images/03-2025/GoT:_Unleashing_Reasoning_Capability_of_Multimodal_Large_Language_Model_for_Visual_Generation_and_Editing/figure_6.jpg' | relative_url }})
