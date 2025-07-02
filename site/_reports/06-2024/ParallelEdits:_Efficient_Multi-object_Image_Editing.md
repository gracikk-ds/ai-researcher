---
title: ParallelEdits:_Efficient_Multi-object_Image_Editing
layout: default
date: 2024-06-03
---
## ParallelEdits: Efficient Multi-object Image Editing
**Authors:**
- Mingzhen Huang, h-index: 4, papers: 7, citations: 30
- Siwei Lyu, h-index: 1, papers: 3, citations: 4

**ArXiv URL:** http://arxiv.org/abs/2406.00985v4

**Citation Count:** 0

**Published Date:** 2024-06-03

![Figure 1: Multi-aspect text-driven image editing. Multiple edits in images pose a significant challenge in existing models (such as DirectInverison [ 1 ] and InfEdit [ 2 ]), as their performance downgrades with an increasing number of aspects. In contrast, our ParallelEdits can achieve precise multi-aspect image editing in 5 seconds. The symbol ⊗ denotes a swap action, the symbol ⊕ denotes an object addition action, and the symbol ⊖ denotes an object deletion . Arrows ( → ) on the image highlight the aspects edited by our method.]({{ '/images/06-2024/ParallelEdits:_Efficient_Multi-object_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-driven image editing models perform well on single-attribute edits but struggle when tasked with making simultaneous changes to multiple objects or attributes in an image. Applying these methods sequentially is computationally expensive and often leads to degraded image quality, where later edits can undo earlier ones or accumulate artifacts. The authors address this gap by introducing a method for efficient and effective multi-aspect image editing.

## 2. Key Ideas and Methodology
The core idea of the paper is that multiple edits can be processed in parallel during the diffusion process, rather than sequentially. The authors propose **ParallelEdits**, a method built on this principle.

- **High-level Approach:** ParallelEdits employs a multi-branch architecture. Instead of a single editing path, it uses multiple parallel "target branches" in addition to a "source branch".
- **Key Mechanism (Aspect Grouping):** Before editing, the method uses cross-attention maps from a few initial diffusion steps to analyze the requested edits. It categorizes each edit as either **global** (style/background), **local rigid** (color/texture change), or **local non-rigid** (pose change, object addition/deletion). Edits are then grouped and assigned to different parallel branches.
- **Theoretical Foundation:** The method builds upon inversion-free editing techniques using Latent Consistency Models (LCM), which allows it to bypass the costly inversion step and perform editing efficiently. Each branch is calibrated based on the output of the previous one, with specialized cross-branch interactions (e.g., attention map swapping for rigid edits, feature querying for non-rigid edits) to ensure consistency.

## 3. Datasets Used / Presented
The authors introduce **PIE-Bench++**, a new benchmark dataset designed specifically for evaluating multi-aspect image editing. It is an extension of the original PIE-Bench dataset and contains 700 images with detailed source and target prompts. The dataset is curated so that a majority of examples (76%) involve two or more simultaneous edits, covering changes in objects, attributes, and style.

## 4. Main Results
ParallelEdits significantly outperforms existing state-of-the-art methods, especially when compared to their sequential application.

- On the PIE-Bench++ dataset, ParallelEdits achieves the highest scores on the authors' proposed aspect accuracy metrics: **51.05% on AspAcc-CLIP** and **65.19% on AspAcc-LLaVA**. This is a notable improvement over the next-best sequential method (PnP*), which scored 48.20% and 63.80%, respectively.
- The method is highly efficient, completing a multi-aspect edit in approximately **5 seconds**, which is substantially faster than sequential approaches that can take over 100 seconds.
- The authors claim that ParallelEdits is the first effective and efficient solution for the multi-aspect text-driven image editing problem.

## 5. Ablation Studies
The authors conducted several ablation studies to validate their design choices.

- **Branching and Aspect Grouping:** This was the most critical ablation. A simplified model using only a single branch for all edits performed poorly (57.67% LLaVA accuracy). Adding the multi-branch design without aspect grouping improved performance (58.37%). Incorporating aspect grouping to assign edits to specialized branches (rigid, non-rigid, global) further boosted the score (61.22%). The full model with all components achieved the best performance (65.19%), demonstrating that both the multi-branch design and the attention-based aspect grouping are crucial.
- **Preservation:** The method was evaluated on its ability to preserve background and unchanged content. ParallelEdits achieved state-of-the-art preservation scores (e.g., PSNR of 26.13, LPIPS of 95.87), indicating it successfully modifies target aspects without distorting the rest of the image.
- **Number of Aspects:** The performance of ParallelEdits remained robust and superior to baselines as the number of simultaneous edits increased from one to three or more.

## 6. Paper Figures
![Figure 2: Pipeline. Our method, ParallelEdits, takes a source image, source prompt, and target prompt as input and produces an edited image. The target prompt specifies the edits needed in the source image. Attention maps for all edited aspects are first collected. Aspect Grouping (see Section 4.2.1) categorizes each aspect into one of N groups (in the above figure, N = 5 ). Each group is then assigned a branch and the branch-level updates are detailed in Section 4.2.2. Each branch can be viewed either as a rigid editing branch, non-rigid editing branch, or global editing branch. Finally, adjustments to query/key/value at the self-attention and cross-attention layers are made, as illustrated in the figure and described in Section 4.2.3.]({{ '/images/06-2024/ParallelEdits:_Efficient_Multi-object_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Aspects and Aspect Grouping. In a text prompt, there are multiple independent tokens, with only some being editable, known as aspects and are underlined in the above example. These aspects can be added, deleted, or swapped between the source and target prompts. Pairs of source and target aspects are grouped into branches, and the methodology for aspect grouping is explained in Section 4.2.1.]({{ '/images/06-2024/ParallelEdits:_Efficient_Multi-object_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Qualitative results of ParallelEdits. We denote the edits in arrows with edit actions and aspects for each pair of images. The last image pair is a failure case of ParallelEdits.]({{ '/images/06-2024/ParallelEdits:_Efficient_Multi-object_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative results comparison. Current methods fail to edit multiple aspects effectively, even using sequential edits (noted as *). Methods marked with ⋆⋆ taking additional inputs other than source image and plain text.]({{ '/images/06-2024/ParallelEdits:_Efficient_Multi-object_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Comparison across different numbers of editing aspects. We also include the comparison in PIE-Bench dataset. Our proposed method is robust to different numbers of editing aspects.]({{ '/images/06-2024/ParallelEdits:_Efficient_Multi-object_Image_Editing/figure_6.jpg' | relative_url }})
