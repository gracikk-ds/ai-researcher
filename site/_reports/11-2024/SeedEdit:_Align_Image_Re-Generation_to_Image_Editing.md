---
title: SeedEdit:_Align_Image_Re-Generation_to_Image_Editing
layout: default
date: 2024-11-11
---
## SeedEdit: Align Image Re-Generation to Image Editing
**Authors:**
- Yichun Shi, h-index: 7, papers: 13, citations: 409
- Weilin Huang, h-index: 4, papers: 7, citations: 67

**ArXiv URL:** http://arxiv.org/abs/2411.06686v1

**Citation Count:** None

**Published Date:** 2024-11-11

![Figure 1: Example images edited by our method with one unified model and instructions only.]({{ '/images/11-2024/SeedEdit:_Align_Image_Re-Generation_to_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key challenge in diffusion-based image editing: the trade-off between flexibility and quality. Existing methods are typically either training-free, which are versatile but often unstable and produce inconsistent results, or data-driven, which are more robust but limited by the scarcity of diverse, high-quality paired editing datasets. The practical problem is the difficulty of creating a model that can perform a wide range of edits reliably while preserving the original image's identity.

## 2. Key Ideas and Methodology
The core idea of SeedEdit is to frame image editing as an alignment problem that seeks an optimal balance between **image reconstruction** (maintaining the original image) and **image re-generation** (creating new content based on a text prompt). The methodology is a progressive alignment framework that converts a standard text-to-image (T2I) model into a strong editor.

- **High-level Approach:** The process begins by using a pre-trained T2I model as a "weak generator" to create a large, diverse set of noisy image-edit pairs. This data is then used to train an image-conditioned diffusion model.
- **Iterative Alignment:** The key to the method is an iterative refinement loop. After an initial training round, the newly improved editor is used to generate a better, higher-quality set of paired data. This new dataset is filtered and used to fine-tune the model again. This cycle is repeated multiple times, progressively aligning the model's behavior towards more precise and stable editing.
- **Model Architecture:** The authors use a "Causal Diffusion Model" with two parameter-shared branches that process the input image and the noisy target image, respectively. A causal self-attention mechanism enables communication between the branches, allowing the model to effectively condition on the input image for better geometric and content consistency.

## 3. Datasets Used / Presented
SeedEdit's performance was evaluated on two public benchmarks. The models were trained on internally generated data, not a public dataset.

- **HQ-Edit:** A benchmark containing 293 DALL-E 3 generated images with editing instructions. This was used as the primary benchmark to evaluate the model's core capability of revising generated images.
- **Emu Edit:** A benchmark of 535 real-world images. This was used as an out-of-domain (OOD) test to assess the model's generalization capabilities.

## 4. Main Results
SeedEdit significantly outperformed previous state-of-the-art methods on both quantitative and qualitative measures.

- **Quantitative Insights:** On the main HQ-Edit benchmark, the SeedEdit (in-house T2I) model achieved a GPT-based evaluation score of **78.54**, far surpassing prior methods like UltraEdit (54.17) and Instruct-Pix2Pix (47.50). It also achieved a high CLIP image similarity score (0.8524), indicating superior preservation of the original image's content compared to other methods.
- **Author-claimed impact:** The authors conclude that their progressive alignment framework produces a model that yields superior results by a large margin, striking a better balance between precise editing and content preservation than existing open-source and commercial systems.

## 5. Ablation Studies
While the paper does not contain a formal ablation study section, it provides an analysis in Figure 3 that validates the core alignment methodology. This analysis compares the final "Aligned Editing Model" against the initial "Pair Data w/ T2I Model" (the weak generator). The results show that for a given prompt alignment score (CLIP Direction Score), the final aligned model achieves substantially higher image similarity. This demonstrates that the iterative alignment process is effective at improving image consistency while maintaining the ability to follow the editing instruction.

## 6. Paper Figures
![(b) Let the subject raise up hands. Figure 5: Example Results of different methods on the HQ-Edit benchmark.]({{ '/images/11-2024/SeedEdit:_Align_Image_Re-Generation_to_Image_Editing/figure_5.jpg' | relative_url }})
![(b) Change the time of the day to night Figure 6: Example results of different methods on the Emu Edit benchmark.]({{ '/images/11-2024/SeedEdit:_Align_Image_Re-Generation_to_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7: Example results from different products for editing based image generation.]({{ '/images/11-2024/SeedEdit:_Align_Image_Re-Generation_to_Image_Editing/figure_7.jpg' | relative_url }})
