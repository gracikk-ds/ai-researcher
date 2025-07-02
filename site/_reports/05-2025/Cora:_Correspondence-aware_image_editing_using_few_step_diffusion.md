---
title: Cora:_Correspondence-aware_image_editing_using_few_step_diffusion
layout: default
date: 2025-05-29
---
## Cora: Correspondence-aware image editing using few step diffusion
**Authors:**
- Amirhossein Almohammadipapers: 1, 
- Ali Mahdavi-Amiri, h-index: 18, papers: 71, citations: 1157

**ArXiv URL:** http://arxiv.org/abs/2505.23907v1

**Citation Count:** 0

**Published Date:** 2025-05-29

![Fig. 1. Cora supports diverse edits, including object insertion, subject and background changes, and non-rigid deformations (e.g., jumping). Our novel correspondence-aware method provides strong control and flexibility for both appearance and structure editing.]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing few-step diffusion-based image editing methods struggle with tasks that require significant structural changes, such as altering an object's pose, shape, or identity. These methods often produce visual artifacts, fail to preserve key attributes of the source image, or misalign textures. This is primarily because standard techniques like noise correction do not account for the spatial misalignment between the source and the structurally edited target image, leading to poor quality results.

## 2. Key Ideas and Methodology
The paper introduces Cora, a framework designed to handle complex structural edits by making the diffusion process aware of the correspondence between the source and target images.

*   **Core Principle**: The central idea is to explicitly align textures and structures during editing by establishing semantic correspondence. This allows the model to accurately transfer textures where appropriate and generate new content where needed.

*   **Methodology**: Cora integrates three key components into a few-step diffusion pipeline (SDXL-Turbo):
    1.  **Correspondence-Aware Latent Correction**: It realigns the noise correction terms from the diffusion inversion process to match the geometry of the edited image. This is achieved using patch-wise correspondence derived from DIFT features, preventing artifacts from misaligned noise.
    2.  **Correspondence-Aware Attention Interpolation**: It blends the self-attention keys and values from both the source and target images using Spherical Linear Interpolation (SLERP). This balances preserving source appearance with generating new content, controlled by a parameter `α`. A content-adaptive mechanism detects "new" regions (e.g., added objects) and generates them purely from the text prompt.
    3.  **Structural Alignment**: To preserve the overall layout and pose, it aligns the self-attention *queries* of the target to the source in the first denoising step using the Hungarian matching algorithm, controlled by a parameter `β`.

## 3. Datasets Used / Presented
The authors did not introduce a new dataset. They demonstrated the effectiveness of their method on a diverse set of real-world images, performing various editing tasks including non-rigid deformations, object insertion/alteration, and appearance changes. These qualitative results are presented throughout the paper.

## 4. Main Results
*   **User Studies**: Cora significantly outperformed competing methods in user studies. When ranked against four other frameworks (including TurboEdit and MasaCtrl), Cora received the highest average preference score (3.29 out of 4), with the next best method scoring 2.24.
*   **Quantitative Metrics**: Cora achieved state-of-the-art text-alignment, scoring highest on CLIP similarity for both the whole image (24.91) and the edited region (22.69). While other methods sometimes scored higher on background preservation metrics (PSNR/LPIPS), Cora remained highly competitive, indicating it strikes a superior balance between edit fidelity and content preservation.
*   **Author-claimed Impact**: Cora enables high-quality, flexible structural image editing with few-step diffusion models, giving users fine-grained control over the trade-off between preserving source content and generating new structures.

## 5. Ablation Studies
The authors performed several ablation studies to validate each component of their framework:
*   **Structural Alignment**: Disabling this component resulted in a noticeable loss of background fidelity and a failure to preserve the source image's overall layout and pose.
*   **Latent Correction**: Removing the correspondence-aware latent correction module led to significant visual artifacts, distortions, and unnatural deformations, especially in edits involving large shape changes.
*   **Attention Mixing Strategy**: A separate user study on attention mixing strategies confirmed that the proposed DIFT-aligned SLERP interpolation produced the most visually appealing results (average rank 3.23), outperforming LERP, concatenation, and other alternatives.
*   **Correspondence in Attention**: Removing the DIFT-based alignment from the attention interpolation step resulted in more artifacts, demonstrating that aligning features before blending is crucial for quality.

## 6. Paper Figures
![Fig. 2. Comparison between TurboEdit [ 10 ] and our correspondence-aware editing approach. Due to misalignment between the source and target images, artifacts are visible in TurboEdit results, such as texture inconsistencies in (a) , silhouette artifacts in the legs and fins in (b, d) , and undesired elements in (c) . Please zoom in for a clearer view of these artifacts.]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_2.jpg' | relative_url }})
![While this approach is somewhat effective, it sometimes causes unwanted artifacts when interpolating between features that are significantly different (see the mirrors in Figure 3:d). To address this limitation, we explore the use of spherical linear interpolation (SLERP) for interpolating between the keys and values, which takes vector directions into account for smoother blending:]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_3.jpg' | relative_url }})
![Fig. 4. Adjusting 𝛼 Provides control over the appearance transition between the source image and the target appearance. When 𝛼 = 0 , the appearance is entirely derived from the source image, and when 𝛼 = 1 , it fully reflects the editing prompt. Intermediate values of 𝛼 allow for a gradual blend, enabling fine-grained control between these two extremes.]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_4.jpg' | relative_url }})
![Fig. 5. Effect of content-adaptive interpolation. Interpolating the keys and values for target image regions without clear correspondence in the source image results in undesirable edits ( b ). Classifying these regions and using only the target keys and values mitigates this issue ( c ).]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_5.jpg' | relative_url }})
![Fig. 6. Structure Alignment. DIFT-aligned queries produce unnatural edits, while our matching algorithm with adjustable blending weights ( 𝛽 ) enables transitions between full structure alignment and new layout generation.]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_6.jpg' | relative_url }})
![Fig. 7. Structural Alignment. In the first denoising step, we extract selfattention queries from both source and target images. We then define two cost matrices: 𝐶 𝑆𝐴 , which promotes structural alignment between source and target, and 𝐶 𝑇𝐶 , which preserves target structure. By linearly combining these matrices, we can control the strength of alignment. The resulting cost matrix is then used in the Hungarian matching algorithm to permute the target queries, aligning them with the source’s structure.]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_7.jpg' | relative_url }})
![Fig. 8. Qualitative results . We demonstrate the ability of our method to perform various types of edits on multiple images.]({{ '/images/05-2025/Cora:_Correspondence-aware_image_editing_using_few_step_diffusion/figure_8.jpg' | relative_url }})
