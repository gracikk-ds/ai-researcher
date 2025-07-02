---
title: DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing
layout: default
date: 2024-03-21
---
## DesignEdit: Multi-Layered Latent Decomposition and Fusion for Unified & Accurate Image Editing
**Authors:**
- Yueru Jia, h-index: 2, papers: 4, citations: 26
- Shanghang Zhang, h-index: 4, papers: 6, citations: 32

**ArXiv URL:** http://arxiv.org/abs/2403.14487v1

**Citation Count:** None

**Published Date:** 2024-03-21

![Figure 1. Examples of visual design image editing. Our approach facilitates a range of image editing operations with a training-free and unified framework to achieve accurate spatial-aware editing of the design image. Our approach is able to manipulate different objects simultaneously, as well as implement various operations at the same time. All results are produced using one diffusion denoising process.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of achieving precise, spatial-aware image editing using large-scale text-to-image models. While these models excel at generation, they often struggle with tasks requiring accurate spatial control, such as object counting, placement, and resizing. Existing editing methods are often task-specific, require computationally expensive optimization (backpropagation), and find it difficult to manipulate multiple objects with different instructions simultaneously. This paper introduces a unified, training-free framework to overcome these limitations, drawing inspiration from the layer-based editing paradigm common in design software.

## 2. Key Ideas and Methodology
The core idea is to reframe complex spatial editing as a two-stage process: **Multi-Layered Latent Decomposition** and **Multi-Layered Latent Fusion**.

*   **Decomposition:** The source image's latent representation is segmented into multiple object layers and one background layer. User instructions (e.g., "remove pig," "shrink house") are parsed by GPT-4V to guide this process. To create a clean background, the method introduces a **Key-Masking Self-Attention** scheme. This novel, training-free technique modifies the self-attention mechanism of a pretrained diffusion model (SDXL) to inpaint the areas where objects are removed. By masking the `key` features corresponding to the object, the model is forced to reconstruct the missing region using context from the surrounding, unmasked areas.
*   **Fusion:** The manipulated object latents (e.g., resized, moved) are then sequentially "pasted" onto the inpainted background canvas latent according to the desired layout. A few final denoising steps are applied to harmonize the layers, ensuring seamless blending at the boundaries. An artifact suppression scheme is also used to improve the quality of background inpainting.

## 3. Datasets Used / Presented
*   **MagicBrush Benchmark:** Used to quantitatively evaluate the object removal (inpainting) capability. The experiments were run on 51 examples from the dataset that contained mask-guided removal instructions.
*   **Author-Collected User Study Data:** For comparing against Self-Guidance and DiffEditor, the authors selected 10 examples featuring complex edits (movement and resizing). They collected 1460 votes from 73 users on image quality and edit accuracy. A separate user study for inpainting collected 452 votes from 113 users.
*   The paper also demonstrates qualitative results on a diverse set of design images, posters, and photorealistic images to showcase the framework's versatility.

## 4. Main Results
The proposed method, DesignEdit, demonstrates superior performance and flexibility as a unified editing framework.

*   **User Studies:** In a head-to-head comparison with the state-of-the-art method DiffEditor, DesignEdit was preferred by users for image quality 60.41% of the time and for edit accuracy 69.63% of the time.
*   **Inpainting Quality:** On the MagicBrush benchmark, the method achieves object removal quality comparable to specialized, fine-tuned inpainting models like SDXL-Inpainting, despite being training-free. In a user study, the method's inpainting results were preferred 51% of the time against four other models.
*   The authors claim their approach is a unified framework that successfully supports over six different types of accurate image editing tasks (e.g., removal, movement, swapping, repetition) in a single, forward-only process.

## 5. Ablation Studies
*   **Effect Range of Key-Masking:** The authors tested the duration (number of denoising steps) for applying the key-masking. Applying it for the first 40 of 50 steps (`K=40`) yielded the best results, effectively removing the object while seamlessly blending the inpainted region with the background.
*   **Mask Positioning in Self-Attention:** The study compared applying the mask to the `query`, `key`, or `value` tensors in the self-attention block. Masking the `key` was found to be optimal for clean removal. Masking the `query` led to blurring, while masking the `value` distorted the image.
*   **Layer-wise Size Adjustment:** Resizing an object at the image level before encoding it into a latent was compared to resizing the latent directly. Image-level resizing preserved significantly more detail and avoided the blurriness and information loss associated with latent-level resizing.
*   **Canvas Initialization for Pan/Zoom:** For out-of-frame editing, initializing the new canvas area by pasting the original image (providing context) was compared to using a blank (black or white) canvas. The original image initialization produced coherent, detailed inpainting, whereas blank canvases resulted in disjointed and discordant content.

## 6. Paper Figures
![Figure 10. Qualitative comparison on the M AGIC B RUSH dataset. We chose the mask-provided instruction-guided removal tasks to evaluate the inpainting ability of our method. The third column shows the removal results provided by DALL · E2 serving as ground truth. We compare the results of LaMa, ControlNet-Inpainting, SDXL-inpainting, Uni-paint with ours.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_10.jpg' | relative_url }})
![Figure 2. Comparison between our method against Self-Guidance and DiffEditor. We report the win-rate comparison across image quality and edit accuracy in (a). For each comparison, we select 10 examples with multiple operations like movement and resizing. Users were asked to vote from two aspects, image quality and edit accuracy. The “Draw” option represents equal effect. We collect answers from 73 users, with a total of 1460 votes for each metric.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3. Illustrating the overall framework of our approach: During the multi-layered decomposition stage, given a user’s editing instruction and the source image, we first utilize GPT-4V to perform instruction planning, generating a set of detailed layer-wise editing instructions. Then, we segment the source image into multiple image layers, including the background layer that requires additional inpainting, implemented by a novel key-masking self-attention scheme, and the other object layers of the object to manipulate. For the multi-layered fusion stage, We follow the layers’ orders and layer-wise instructions sequentially to paste them onto the canvas in latent space. We further apply multiple denoising steps to harmonize the fused multi-layered latent representations. Additionally, we perform artifact suppression to improve the background inpainting quality.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Key-Masking Self-Attention Mechanism at time step t. The figure shows the diagram for the removal latent Z S t at timestep t . The surroundings of pixel features are kept by the source latent Z S t . M remove and M refine are utilized on key features to reduce attention within the mask.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5. Illustrating the Key-Masking Self-Attention Mechanism. (a) shows that regions inside the mask query only from the regions outside the mask, which are copied from the source latent to complete the information. (b) presents the output heatmaps changing over time from the source and removal latent. The maps come from the first self-attention block at a resolution of 64 × 64 .]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Qualitative illustrations of the usage of M refine in artifact suppression refinement. (a) and (b) show text removal within board elements, while (c) shows the removal of regions near styled text.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7. Illustration of the mask usage in camera panning and zooming out tasks. The figure presents two cases of image adjustment and the formation of their related masks.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_7.jpg' | relative_url }})
![Figure 8. Illustrating the Integrated Decomposition-Fusion Technique in occlusion-aware object editing at timestep t . To relocate the dog and ball and inpaint the occluded dog leg, we conduct Key-Masking Self-Attention twice on the background latent Z L 0 t and the canvas latent Z L 0 t respectively. ˆ M occlude represents the moved M occlude with the occluded Layer-1 Z L 1 t . The target latent is the new canvas removal latent ˆ Z C t .]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_8.jpg' | relative_url }})
![Figure 9. Comparison with other mask-guided inpainting models. (a) shows qualitative the comparison of large object removal ability, with our method not causing obvious blurriness or filling the removed area with unrelated elements. (b) shows the user study results of 452 votes from 113 users, with our method achieving a 51% preference percentage.]({{ '/images/03-2024/DesignEdit:_Multi-Layered_Latent_Decomposition_and_Fusion_for_Unified_&_Accurate_Image_Editing/figure_9.jpg' | relative_url }})
