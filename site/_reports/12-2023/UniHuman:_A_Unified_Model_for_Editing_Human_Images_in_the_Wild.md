---
title: UniHuman:_A_Unified_Model_for_Editing_Human_Images_in_the_Wild
layout: default
date: 2023-12-22
---
## UniHuman: A Unified Model for Editing Human Images in the Wild
**Authors:**
- Nannan Li
- Zhe Lin

**ArXiv URL:** http://arxiv.org/abs/2312.14985v2

**Citation Count:** None

**Published Date:** 2023-12-22

![Figure 1. The results of UniHuman on diverse real-world images. UniHuman learns informative representations by leveraging multiple data sources and connections between related tasks, achieving high-quality results across various human image editing objectives.]({{ '/images/12-2023/UniHuman:_A_Unified_Model_for_Editing_Human_Images_in_the_Wild/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
    - Prior work in human image editing typically addresses tasks like reposing (changing pose), virtual try-on (changing clothes), and text-based manipulation in isolation. This approach overlooks the potential for mutual reinforcement from learning these related tasks jointly. Furthermore, existing models often struggle to generalize to diverse, "in-the-wild" images with varied backgrounds, poses, and clothing styles, as they are trained on limited, in-studio datasets.

## 2. Key Ideas and Methodology
    - **Core Principle:** The paper introduces UniHuman, a single, unified model that jointly handles reposing, virtual try-on, and text manipulation. The central hypothesis is that learning these tasks together allows the model to leverage shared information and synergies, boosting performance and generalization for all tasks.
    - **High-level Approach:** UniHuman is built upon a Stable Diffusion (SD) backbone. Its key components are:
        1.  A **Part Encoder** that extracts texture and style features from segmented human parts (e.g., face, hair, clothing) using DINOv2 and CLIP embeddings.
        2.  A lightweight, training-free **Pose-Warping Module** that explicitly maps visible textures from a source image or garment to a target pose. It flexibly uses either dense (UV maps) or sparse (keypoints) pose information, making it robust to different scenarios and unseen patterns.
        3.  A **Conditioning Encoder** that feeds the target pose, warped texture, and background information into the SD UNet to guide the image generation process.
    - **Theoretical Foundation:** The model unifies the tasks within a single denoising pipeline, where different inputs (target pose, target garment, text prompt) activate different conditional paths, while sharing the core generative architecture.

## 3. Datasets Used / Presented
    - **LH-400K (New):** A large-scale training dataset curated by the authors, containing 409,270 high-quality, single-human image-text pairs from LAION-400M. It features diverse ages, backgrounds, and clothing styles to improve in-the-wild generalization.
    - **WPose (New):** An out-of-domain test set for reposing, comprising 2,304 image pairs of people in challenging and diverse poses (e.g., dancing, squatting).
    - **WVTON (New):** An out-of-domain test set for virtual try-on, with 440 pairs featuring garments with diverse patterns and textures.
    - **Existing Datasets:** The model was also trained and evaluated on standard in-domain benchmarks, including DeepFashion, DressCode, and VITON-HD.

## 4. Main Results
    - **Quantitative Insights:** UniHuman significantly outperforms specialized, state-of-the-art models on both in-domain and out-of-domain tests.
        - For **reposing** on the out-of-domain WPose dataset (512x512), UniHuman achieved a Fréchet Inception Distance (FID) of 27.7, a substantial improvement over the next-best model, DisCo (58.3).
        - For **virtual try-on** on the out-of-domain WVTON dataset (512x512), UniHuman achieved an FID of 127.9, compared to 147.4 for the next-best model, LaDI-VTON.
    - **Author-claimed Impact:** User studies corroborate the quantitative results, with UniHuman being preferred by users in an average of 77% of cases across all tasks. The work demonstrates that a unified approach, combined with diverse data, is highly effective for robust human image editing in real-world scenarios.

## 5. Ablation Studies
    - **Pose-Warped Texture:** Removing the pose-warping module and its corresponding attention loss (`w.o. I_tex`) caused a marked drop in performance across all metrics. This highlights the critical role of providing explicit, pose-aligned texture guidance for high-fidelity generation.
    - **LH-400K Dataset:** Training the model without the new LH-400K dataset (`w.o. 400K`) resulted in significantly worse performance on out-of-domain test sets (e.g., FID on WPose increased from 27.6 to 47.7). This confirms that the diverse, large-scale data is essential for generalization.
    - **Joint vs. Single-Task Training:** Training separate models for each task (`rp only`, `vt only`) led to inferior performance compared to the unified multi-task model. This demonstrates that the tasks mutually benefit from being learned jointly, as the model can transfer knowledge (e.g., from reposing data to the try-on task).

## 6. Paper Figures
![Figure 2. An overview of our model. (a) Our inference pipeline. Starting from a noise latent code, our model edits the source person given the source image, the target pose, the visual prompt (optional), and the text prompt (optional). Blue arrow is the reposing flow, which is also the base flow for all tasks. Pink dashed arrow indicates the optional virtual try-on flow that takes a clothing image as its input. In try-on task, the clothing image should replace the source image as the input to the pose-warping module. Brown dashed arrow is the optional text manipulation flow, which accepts a text description as its prompt. (b) The introduced pose-warping module. It maps the original RGB pixels of the source texture to the target pose based on pose correspondences. Best view in color.]({{ '/images/12-2023/UniHuman:_A_Unified_Model_for_Editing_Human_Images_in_the_Wild/figure_2.jpg' | relative_url }})
![Figure 3. Representative examples from different datasets. Our LH-400K includes people of diverse ages and backgrounds.]({{ '/images/12-2023/UniHuman:_A_Unified_Model_for_Editing_Human_Images_in_the_Wild/figure_3.jpg' | relative_url }})
![(b) Out-of-domain examples on WPose. Figure 4. Visualized results of reposing (256x256). Our model transfers the texture patterns better, particularly in out-of-domain samples. More results can be found in Supp.]({{ '/images/12-2023/UniHuman:_A_Unified_Model_for_Editing_Human_Images_in_the_Wild/figure_4.jpg' | relative_url }})
![Figure 5. Virtual try-on results (512 x 512). Our UniHuman better recovers the intricate details in the target garment, particularly in out-of-domain samples. More results can be found in Supp.]({{ '/images/12-2023/UniHuman:_A_Unified_Model_for_Editing_Human_Images_in_the_Wild/figure_5.jpg' | relative_url }})
![Figure 6. Results of text manipulation. Our model manipulates the clothing to match the specified concept.]({{ '/images/12-2023/UniHuman:_A_Unified_Model_for_Editing_Human_Images_in_the_Wild/figure_6.jpg' | relative_url }})
