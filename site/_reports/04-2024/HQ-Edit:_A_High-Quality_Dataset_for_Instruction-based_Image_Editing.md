---
title: HQ-Edit:_A_High-Quality_Dataset_for_Instruction-based_Image_Editing
layout: default
date: 2024-04-15
---
## HQ-Edit: A High-Quality Dataset for Instruction-based Image Editing
**Authors:**
- Mude Hui, h-index: 4, papers: 6, citations: 134
- Cihang Xie, h-index: 10, papers: 26, citations: 439

**ArXiv URL:** http://arxiv.org/abs/2404.09990v1

**Citation Count:** 73

**Published Date:** 2024-04-15

![Fig. 1: (a) (d): example images and edit instructions from HQ-Edit. (e): we compare the dataset quality between our HQ-Edit and existing ones. Note that “Alignment” and “Coherence” are our newly developed metrics (introduced in Sec. 3.4 ) for measuring image/text qualities.]({{ '/images/04-2024/HQ-Edit:_A_High-Quality_Dataset_for_Instruction-based_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of existing datasets for instruction-based image editing. They argue that current datasets, such as the one powering InstructPix2Pix, suffer from low-resolution images, poor alignment between the textual edit instruction and the actual visual change, and a lack of diversity in editing operations. These shortcomings hinder the development of high-fidelity and versatile image editing models that can accurately follow user commands.

## 2. Key Ideas and Methodology
The paper introduces HQ-Edit, a large-scale, high-quality dataset synthesized using advanced foundation models. The core methodology is a three-stage automated pipeline:
1.  **Expansion:** A small seed set of edit examples (input/output descriptions and an edit instruction) is expanded to ~100,000 diverse instances using GPT-4.
2.  **Generation:** GPT-4 refines these text triplets into detailed prompts for DALL-E 3. A key technique is generating a single "diptych" image containing the input and output images side-by-side, which enhances consistency between the two.
3.  **Post-processing:** This crucial stage involves decomposing the diptychs, warping the image pairs for precise pixel-level alignment, and filtering out distorted results. Furthermore, GPT-4V is used to rewrite the edit instructions to better match the visual changes and to generate inverse-edit instructions, effectively doubling the dataset size.

The authors also propose two novel GPT-4V-based metrics, **Alignment** (semantic consistency with the prompt) and **Coherence** (aesthetic quality of the edited image), for quantitative evaluation.

## 3. Datasets Used / Presented
*   **HQ-Edit (Presented):** A new synthetically generated dataset containing approximately 200,000 instruction-based image edit pairs. It is characterized by high-resolution images (approx. 900x900 pixels) and detailed, high-quality edit instructions.
*   **Comparison Datasets (Used):** The quality of HQ-Edit is benchmarked against existing public datasets, including InstructPix2Pix, HIVE, and MagicBrush, by sampling 500 data points from each.

## 4. Main Results
*   **Dataset Quality:** HQ-Edit significantly outperforms existing datasets on the authors' proposed metrics. It achieves an Alignment score of 92.80 and a Coherence score of 91.87, far surpassing datasets like InstructPix2Pix (68.29 Alignment, 83.35 Coherence) and MagicBrush (80.61 Alignment, 65.42 Coherence).
*   **Model Performance:** An InstructPix2Pix model fine-tuned on HQ-Edit achieves state-of-the-art performance, improving the Alignment score from 34.71 (base model) to 47.01 and Coherence from 80.52 to 86.16.
*   **Metric Validation:** The proposed Alignment metric shows a strong positive correlation (0.3592) with human evaluation, whereas the commonly used CLIP Directional Similarity shows a negative correlation (-0.1446), validating the new metric's effectiveness.

## 5. Ablation Studies
The authors performed an ablation study on the components of their post-processing pipeline by training an InstructPix2Pix model on datasets with different steps enabled.
*   **RAW Data:** Training on raw, simply decomposed DALL-E 3 images (without post-processing) improved image `Coherence` but severely degraded `Alignment` with the instruction (score dropped from 34.71 to 16.83).
*   **Instruction Rewriting:** Adding GPT-4V instruction rewriting provided the most significant boost to `Alignment`, increasing the score from 16.83 to 28.62.
*   **Inverse, Warp, and Filter:** Each subsequent step—adding inverse instructions, warping images for alignment, and filtering distorted pairs—provided further cumulative improvements, leading to the final model's top `Alignment` score of 47.01. This demonstrates that each component of the post-processing pipeline is crucial for creating a high-quality training dataset.

## 6. Paper Figures
![Fig. 2: Our method consists of three steps: (1)Expansion: Massively generating image descriptions and edit instructions based on seed samples using GPT-4. (2)Generation: Generating diptychs using GPT-4V and DALL-E according to image descriptions and instructions. (3)Post-Processing: Post-process diptychs and edit instructions with GPT-4V and other various methods to produce image pairs and further enhance the quality of the dataset in different aspects.]({{ '/images/04-2024/HQ-Edit:_A_High-Quality_Dataset_for_Instruction-based_Image_Editing/figure_2.jpg' | relative_url }})
![Fig. 3: The effect of decomposing and warping in image post-processing. Filtering is not demonstrated in this figure. Without warping, there is a part of the desk edge in the output image on the right. This issue is addressed after warping.]({{ '/images/04-2024/HQ-Edit:_A_High-Quality_Dataset_for_Instruction-based_Image_Editing/figure_3.jpg' | relative_url }})
![Fig. 4: The effect of rewriting and inversion in edit post-processing. After postprocessing, the edit instruction is of greater complexity and aligns better with the input/output image pair.]({{ '/images/04-2024/HQ-Edit:_A_High-Quality_Dataset_for_Instruction-based_Image_Editing/figure_4.jpg' | relative_url }})
![Coherence : 80 Fig. 7: Examples of different Coherence. As the Coherence score increases, the image quality improves significantly.]({{ '/images/04-2024/HQ-Edit:_A_High-Quality_Dataset_for_Instruction-based_Image_Editing/figure_7.jpg' | relative_url }})
