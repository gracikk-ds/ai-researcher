---
title: PixLens:_A_Novel_Framework_for_Disentangled_Evaluation_in_Diffusion-Based_Image_Editing_with_Object_Detection_+_SAM
layout: default
date: 2024-10-08
---
## PixLens: A Novel Framework for Disentangled Evaluation in Diffusion-Based Image Editing with Object Detection + SAM
**Authors:**
- Stefan Stefanachepapers: 1, 
- Enis Simsar, h-index: 9, papers: 25, citations: 309

**ArXiv URL:** http://arxiv.org/abs/2410.05710v1

**Citation Count:** 0

**Published Date:** 2024-10-08

![Fig. 1: PixLens Edit Evaluation Pipeline: SIZE operation evaluation example.]({{ '/images/10-2024/PixLens:_A_Novel_Framework_for_Disentangled_Evaluation_in_Diffusion-Based_Image_Editing_with_Object_Detection_+_SAM/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the critical problem of evaluating diffusion-based image editing models. Existing evaluation methods are insufficient due to a lack of standardized benchmarks, an over-reliance on potentially unreliable metrics like CLIP scores, or a dependency on costly and subjective human evaluations. Current automated benchmarks often fail to accurately assess complex spatial edits, handle multiple object instances, or measure the preservation of un-edited content, leading to an incomplete understanding of model performance.

## 2. Key Ideas and Methodology
The paper introduces **PixLens**, a novel, automated framework for a fine-grained and disentangled evaluation of text-guided image editing. The core idea is to combine open-vocabulary object detection (GroundingDINO) with segmentation models (SAM) to achieve precise localization and analysis of edited objects.

The methodology consists of three main components:
1.  **Edit Quality Evaluation:** Automatically assesses 9 distinct edit types (e.g., object addition, size change, color change) using a nuanced [0, 1] scoring system and specialized logic ("Multiplicity Handlers") to manage scenarios with multiple objects.
2.  **Preservation Analysis:** Comprehensively evaluates both **subject preservation** (how well the main object's structure, shape, and position are maintained, using SIFT, SSIM, and IoU) and **background preservation** (ensuring un-edited parts of the image remain unchanged).
3.  **Disentanglement Evaluation:** A novel contribution that analyzes the model's latent space to measure how effectively it separates semantic attributes like color, texture, and style, providing insights into the model's internal representations.

## 3. Datasets Used / Presented
-   **EditVAL Dataset:** The primary dataset used to evaluate five state-of-the-art image editing models (InstructPix2Pix, ControlNet, LCM, OpenEdit, VQGAN+CLIP) and to perform a direct comparative analysis between PixLens and the original EditVAL benchmark.
-   **MagicBrush Dataset:** The "dev" split (528 edits) was adapted and used as a sanity check. By evaluating PixLens on MagicBrush's manually created ground-truth images, the authors validated that their framework aligns with expert-curated, high-quality edits.

## 4. Main Results
-   PixLens demonstrates a vastly superior correlation with human judgment compared to prior work. When evaluating InstructPix2Pix, PixLens's automated scores achieved a **Pearson correlation of 0.903** with human-annotated scores, while the competing EditVAL benchmark's automated scores only reached a correlation of **0.146**.
-   The evaluation of state-of-the-art models revealed a common weakness: while most models perform well on object attribute edits (e.g., changing color), they all struggle significantly with spatial manipulation tasks (e.g., moving an object).
-   The authors claim PixLens establishes a new, more reliable standard for evaluating image editing models by providing a task-dependent, multi-faceted assessment that goes beyond simple prompt-image alignment.

## 5. Ablation Studies
While a formal ablation section is not present, the paper's core comparisons serve this function. The most critical analysis is the performance gain of PixLens over EditVAL. This highlights the impact of the proposed methodology, particularly the use of **segmentation masks over bounding boxes** and more robust evaluation logic. This change was responsible for improving the correlation with human scores from 0.146 to 0.903. Furthermore, the framework's separate evaluations for edit quality, subject preservation, and background preservation implicitly justify the necessity of each component, as they are shown to capture distinct and sometimes conflicting aspects of a model's performance.

## 6. Paper Figures
![Fig. 2: Original image (left) and edited images resulting of “changing the color of the boat to black (center) / yellow (right)”, using InstructPix2Pix.]({{ '/images/10-2024/PixLens:_A_Novel_Framework_for_Disentangled_Evaluation_in_Diffusion-Based_Image_Editing_with_Object_Detection_+_SAM/figure_2.jpg' | relative_url }})
![Fig. 3: Good subject preservation example for InstructPix2Pix edit with the prompt Change the color of the dog to red . The subject of this edit is the dog .]({{ '/images/10-2024/PixLens:_A_Novel_Framework_for_Disentangled_Evaluation_in_Diffusion-Based_Image_Editing_with_Object_Detection_+_SAM/figure_3.jpg' | relative_url }})
![Fig. 4: Bad subject preservation example for LCM edit with the prompt Change the color of the backpack to orange . The subject of this edit is the backpack .]({{ '/images/10-2024/PixLens:_A_Novel_Framework_for_Disentangled_Evaluation_in_Diffusion-Based_Image_Editing_with_Object_Detection_+_SAM/figure_4.jpg' | relative_url }})
![Fig. 5: Intra-attribute disentanglement example]({{ '/images/10-2024/PixLens:_A_Novel_Framework_for_Disentangled_Evaluation_in_Diffusion-Based_Image_Editing_with_Object_Detection_+_SAM/figure_5.jpg' | relative_url }})
