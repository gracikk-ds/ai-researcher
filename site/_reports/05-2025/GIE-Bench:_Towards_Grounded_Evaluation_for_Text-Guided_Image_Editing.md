---
title: GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing
layout: default
date: 2025-05-16
---
## GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing
**Authors:**
- Yusu Qian, h-index: 5, papers: 8, citations: 160
- Zhe Gan, h-index: 11, papers: 19, citations: 789

**ArXiv URL:** http://arxiv.org/abs/2505.11493v1

**Citation Count:** 1

**Published Date:** 2025-05-16

![Figure 1: Overview of the proposed GIE-Bench pipeline for grounded and fine-grained evaluation of text-guided image editing models. GIE-Bench consists of two components: ( i ) functional correctness evaluation; and ( ii ) content preservation evaluation.]({{ '/images/05-2025/GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing evaluation methods for text-guided image editing, such as those relying on global image-text similarity metrics like CLIP, lack precision. They cannot effectively distinguish whether a model has correctly performed a specific edit instruction versus how well it has preserved the parts of the image that were not meant to be changed. This gap makes it difficult to perform a fine-grained, grounded, and scalable comparison of different editing models.

## 2. Key Ideas and Methodology
The paper introduces **GIE-Bench**, a benchmark designed for a more grounded evaluation along two critical axes:

*   **Functional Correctness**: This measures if the model successfully executed the edit instruction. The methodology uses a VQA-style protocol where a multiple-choice question is automatically generated for each edit. The question is designed so that it can only be answered correctly by inspecting the edited image, making it a robust test of instruction-following. An LLM (GPT-4o) is used to answer the questions automatically.

*   **Content Preservation**: This evaluates the model's ability to leave irrelevant image regions unchanged. The core idea is to use an "object-aware" mask to isolate the region targeted by the edit instruction. This mask is generated using a combination of GPT-4 (to identify the object from text), GroundingDINO (for object detection), and SAM (for segmentation). The mask is then inverted, and preservation metrics (e.g., MSE, PSNR, CLIP) are computed only on the non-edited background regions.

## 3. Datasets Used / Presented
The paper presents the **GIE-Bench** dataset, which was created for this study.
*   **Name**: GIE-Bench (Grounded Image Editing Evaluation Benchmark)
*   **Size**: It consists of 1,080 high-quality, human-filtered image-instruction pairs based on 856 unique source images.
*   **Domain**: The dataset is diverse, with images spanning 20 categories (e.g., architecture, animals, food, people) and instructions covering 9 distinct edit types (e.g., color change, object removal, layout modification).
*   **Usage**: It is used to conduct a large-scale comparative study of state-of-the-art image editing models, including GPT-Image-1, OmniGen, MGIE, and others.

## 4. Main Results
*   **Functional Correctness**: GPT-Image-1 demonstrated superior instruction-following ability, achieving the highest overall correctness score of 85.0%. In contrast, the next best model, OmniGen, scored 60.7%.
*   **Content Preservation**: Models like OneDiffusion and MagicBrush excelled at preserving unedited content, achieving the highest scores on pixel-based metrics. GPT-Image-1, despite its high correctness, performed poorly on preservation, indicating a tendency to make unnecessary changes to the background.
*   **Human Correlation**: The proposed automated metrics showed a strong correlation with human judgments. For content preservation, the Spearman correlation between human rankings and the masked CLIP score was 0.952.
*   **Author-claimed impact**: GIE-Bench provides a scalable and reproducible framework that reveals a key trade-off in current models between instruction-following accuracy and content preservation, enabling more accurate and fine-grained evaluation.

## 5. Ablation Studies
*   **Robustness of LLM-based Judge**: To validate the functional correctness evaluation, the authors used Gemini-2-Flash as a secondary judge alongside GPT-4o. The results were highly consistent across both LLMs, with model rankings remaining nearly identical. For instance, GPT-Image-1 scored 85.0% with GPT-4o and 82.7% with Gemini-2-Flash. This confirmed that the automated VQA protocol is robust and reliable.
*   **Masked vs. Unmasked Preservation**: The paper compares preservation scores calculated over the entire image (unmasked) versus only the background (masked). The results show that unmasked metrics can be misleading. For example, GPT-Image-1 scores relatively well on unmasked CLIP but has the lowest masked PSNR, which accurately captures its tendency to alter non-targeted regions. This highlights the necessity of using object-aware masks for precise preservation evaluation.

## 6. Paper Figures
![Figure 2: Example image editing instructions and edited results by GPT-Image-1 [1], OmniGen [5], and MGIE [4].]({{ '/images/05-2025/GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Distribution of object mask size ratios.]({{ '/images/05-2025/GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Left: Functional correctness per edit type. Right: Model preservation rankings based on masked MSE (inverted), PSNR, and CLIP scores. We empirically observe that model ranking evaluated by masked CLIP differs from model ranking evaluated by CLIP.]({{ '/images/05-2025/GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Examples showing three failure modes: functional failure, preservation failure, and combined failure, paired with correct editing.]({{ '/images/05-2025/GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Examples of GPT-Image-1’s failure modes.]({{ '/images/05-2025/GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7: Left: Correlation between human and GPT-4o evaluated functional correctness scores. Right: Correlation between human-evaluated preservation and inverted calibrated MSE rank.]({{ '/images/05-2025/GIE-Bench:_Towards_Grounded_Evaluation_for_Text-Guided_Image_Editing/figure_7.jpg' | relative_url }})
