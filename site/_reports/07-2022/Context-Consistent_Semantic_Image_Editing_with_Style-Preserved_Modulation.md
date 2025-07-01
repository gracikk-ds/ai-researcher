---
title: Context-Consistent_Semantic_Image_Editing_with_Style-Preserved_Modulation
layout: default
date: 2022-07-13
---
![Fig. 1: Applications of the proposed method. Our image editing system is flexible in responding to a wide variety of editing requirements.]({{ '/images/07-2022/Context-Consistent_Semantic_Image_Editing_with_Style-Preserved_Modulation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the problem of style inconsistency in semantic image editing. Existing methods, particularly those based on the SPADE block (like SESAME), often produce edited regions that do not stylistically match the surrounding, unedited parts of the image. This results in visible seams and unrealistic outputs. The core issue identified is that these methods generate content based only on an external semantic layout, ignoring the unique, image-specific style (e.g., color, texture) present in the known pixels of the image.

## 2. Key Ideas and Methodology
The paper introduces two main contributions to solve this problem:

*   **Style-Preserved Modulation (SPM):** The core of the method is a novel modulation block that operates in two stages.
    1.  **Fusion Stage:** SPM generates modulation parameters from two distinct sources: the user-provided semantic map (for structure) and the *un-normalized* feature maps of the image itself (for style). Using un-normalized features is a key design choice, as normalization layers tend to "wash out" style information. These two sets of parameters are fused to create context-aware modulation signals.
    2.  **Modulation Stage:** These fused signals are then used to modulate the network's feature maps, simultaneously injecting the desired semantic structure while preserving the original image's contextual style.

*   **Progressive Architecture (SPMPGAN):** The SPM blocks are integrated into a progressive, coarse-to-fine generative adversarial network. This architecture generates the edited content across multiple scales, starting with a low-resolution global structure and progressively adding finer details. This allows style information from the known regions to propagate more effectively into the generated region.

## 3. Datasets Used / Presented
The model was trained and evaluated on three standard semantic segmentation datasets, adapted for the editing task:
*   **ADE20K-room:** A subset of the ADE20K dataset focusing on indoor scenes (Bedroom, Hotel Room, Living Room), containing 2,246 training and 255 testing images.
*   **ADE20K-landscape:** A subset of ADE20K featuring outdoor landscape scenes, with 1,689 training and 155 testing images.
*   **Cityscapes:** A dataset of urban street scenes, comprising 2,975 training and 500 testing images.
These datasets were used to evaluate performance on various editing tasks, including free-form inpainting, outpainting, and object addition/removal.

## 4. Main Results
*   **Quantitative Performance:** The proposed SPMPGAN significantly outperformed prior state-of-the-art methods like SESAME, SPADE, and HIM across all datasets and tasks. It consistently achieved lower (better) FID and LPIPS scores, indicating higher image fidelity and perceptual quality. For instance, on ADE20K-Room with a free-form mask, SPMPGAN achieved an FID of 18.83, a notable improvement over SESAME's 21.73.
*   **User Study:** In a study involving 21 volunteers, the results from SPMPGAN were overwhelmingly preferred (1479 votes) for better style preservation compared to SESAME (493 votes) and HIM (128 votes).
*   **Author's Takeaway:** The proposed method effectively resolves the style inconsistency problem by explicitly integrating contextual style with the target semantic layout, leading to more realistic and seamlessly edited images.

## 5. Ablation Studies
The authors conducted several ablation studies to validate their design choices:
*   **SPM vs. SPADE:** Replacing all SPM blocks with standard SPADE blocks ("w SPADE") significantly worsened performance (FID on ADE20K-Room increased from 18.83 to 23.27). This confirms that the proposed two-stage modulation is critical for style preservation.
*   **Importance of Bypassing Normalization:** When context-style parameters were derived from *normalized* feature maps instead of the original ones ("w norm"), performance degraded (FID increased to 20.51). This validates the hypothesis that un-normalized features are essential for capturing style.
*   **Effectiveness of Progressive Architecture:** Removing the progressive, multi-scale architecture and using only a single-scale generator ("w/o prog") resulted in lower-quality outputs and style inconsistencies (FID increased to 20.47).
*   **Model Design vs. Parameter Count:** A smaller version of the proposed model (SPMPGAN-S) still significantly outperformed a larger version of the SPADE-based baseline. This demonstrates that the performance gains stem from the superior architectural design of SPM, not merely from an increased number of parameters.

## 6. Paper Figures
![Fig. 3: Overview of the progressive architecture.]({{ '/images/07-2022/Context-Consistent_Semantic_Image_Editing_with_Style-Preserved_Modulation/figure_3.jpg' | relative_url }})
![Fig. 4: Visual comparison with other methods.]({{ '/images/07-2022/Context-Consistent_Semantic_Image_Editing_with_Style-Preserved_Modulation/figure_4.jpg' | relative_url }})
![Fig. 5: Visual results of addition and removal objects.]({{ '/images/07-2022/Context-Consistent_Semantic_Image_Editing_with_Style-Preserved_Modulation/figure_5.jpg' | relative_url }})
