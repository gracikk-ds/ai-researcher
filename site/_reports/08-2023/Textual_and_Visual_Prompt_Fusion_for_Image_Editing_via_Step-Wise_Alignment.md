---
title: Textual_and_Visual_Prompt_Fusion_for_Image_Editing_via_Step-Wise_Alignment
layout: default
date: 2023-08-30
---
![Fig. 1: The framework of SWA. The reference image is encoded into features ∆ h . Then, ∆ h are integrated into the latent features h of the editing image. The textual prompt contributes semantic information for the manipulation process.]({{ '/images/08-2023/Textual_and_Visual_Prompt_Fusion_for_Image_Editing_via_Step-Wise_Alignment/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key trade-off in diffusion-based image editing. Existing methods are often either text-guided or image-guided. Text-guided approaches provide strong semantic control but can degrade visual quality or fail when the target edit is complex. Conversely, image-guided methods excel at transferring visual styles and patterns but lack intuitive control over which specific attributes are being edited, leading to semantic ambiguity. The paper aims to bridge this gap by creating a framework that combines the precise semantic control of text prompts with the high-fidelity visual guidance of a reference image.

## 2. Key Ideas and Methodology
The core idea is to fuse both textual and visual prompts into the semantic latent space of a frozen, pre-trained diffusion model. The proposed framework, named **Step-Wise Alignment (SWA)**, integrates these dual guidances to perform controlled image editing.

The methodology involves four key components:
1.  **Text Encoder (CLIP):** Processes source ("a person") and target ("a person with glasses") text prompts.
2.  **Visual Generator (UniDiffuser):** Creates a reference image based on the target text prompt.
3.  **Attribute Encoder:** A small, trainable network that extracts visual features (`Δh`) from the reference image.
4.  **Editing Generator (Frozen DDIM):** The main diffusion model that edits the input image.

The key algorithmic trick is an **asymmetrical update** during the diffusion reverse process. To avoid edits being nullified by "destructive interference," the visual features `Δh` are used to modify only the predicted clean image (`x_0`) component of the step, while the noise direction component remains unchanged. The Attribute Encoder is optimized in a zero-shot manner using a directional CLIP loss (to align the edit with the text prompt) and a reconstruction loss (to preserve the original image structure).

## 3. Datasets Used / Presented
The framework is evaluated on several standard benchmark datasets:
-   **CelebA-HQ:** A high-resolution dataset of celebrity faces. It is used to test both in-domain attribute editing (e.g., "smiling", "old") and out-of-domain editing (e.g., "add glasses", "add makeup").
-   **LSUN-church & LSUN-bedroom:** Large-scale scene datasets. They are used to demonstrate the method's generalization capability for style transfer on non-face images.

## 4. Main Results
SWA is quantitatively compared against prior methods (ILVR, Asyrp, NTI) using Inception Score (ISC), Fréchet Inception Distance (FID), and CLIP Score.
-   **In-domain Editing:** For the "Man" attribute on CelebA-HQ, SWA achieved the best ISC (3.292) and FID (45.31), outperforming NTI (ISC 2.219, FID 52.23).
-   **Out-of-domain Editing:** For adding "glasses", SWA obtained a CLIP score of 30.07, significantly higher than NTI's 26.17, indicating superior alignment with the textual command.

The authors claim that SWA outperforms state-of-the-art methods by generating higher-quality images and providing more realistic and controllable manipulation for both in-domain and out-of-domain attributes.

## 5. Ablation Studies
An ablation study was performed to validate the effectiveness of incorporating a visual reference image.
-   **Experiment:** The authors compared the editing process for the "glasses" attribute with and without the visual features (`Δh`) from the reference image.
-   **Impact:** The qualitative results in Figure 6 show that when the reference image is used (W/ SWA), the pixel modifications are more concentrated and precise on the target attribute's features (the glasses). Without the reference (W/O SWA), the changes are more diffuse and less accurate. This confirms that the visual prompt is crucial for generating high-quality, targeted edits.

## 6. Paper Figures
![Fig. 2: Consistent editing: Once a reference image is provided, our method enables consistent and controllable editing to the reference image. In contrast, NTI fails to generate the corresponding style for the glasses.]({{ '/images/08-2023/Textual_and_Visual_Prompt_Fusion_for_Image_Editing_via_Step-Wise_Alignment/figure_2.jpg' | relative_url }})
![Fig. 3: Editing results for in-domain attributes]({{ '/images/08-2023/Textual_and_Visual_Prompt_Fusion_for_Image_Editing_via_Step-Wise_Alignment/figure_3.jpg' | relative_url }})
![Fig. 4: Editing results for out-of-domain attributes.]({{ '/images/08-2023/Textual_and_Visual_Prompt_Fusion_for_Image_Editing_via_Step-Wise_Alignment/figure_4.jpg' | relative_url }})
![Fig. 5: Editing results of SWA on various datasets.]({{ '/images/08-2023/Textual_and_Visual_Prompt_Fusion_for_Image_Editing_via_Step-Wise_Alignment/figure_5.jpg' | relative_url }})
![Fig. 6: Ablation experiments of reference image: The top half depicts the process without a reference image, while the bottom includes a reference image. Pixels are more concentrated on the attribute’s features.]({{ '/images/08-2023/Textual_and_Visual_Prompt_Fusion_for_Image_Editing_via_Step-Wise_Alignment/figure_6.jpg' | relative_url }})
