---
title: Interactive_Image_Manipulation_with_Complex_Text_Instructions
layout: default
date: 2022-11-25
---
## Interactive Image Manipulation with Complex Text Instructions
**Authors:**
- Ryugo Morita, h-index: 2, papers: 10, citations: 10
- Jinjia Zhou, h-index: 15, papers: 114, citations: 787

**ArXiv URL:** http://arxiv.org/abs/2211.15352v1

**Citation Count:** 3

**Published Date:** 2022-11-25

![Figure 1. Given an image and text instruction that reveals desired modifications to the image, our method first tries to understand the image and localize where should be modified, then makes appropriate manipulations. In addition, our network design also allows users to adjust the affected area and add/redo image manipulations for undesired results. As an advantage, this work provides effective image manipulations with high controllability, such as changing an object’s attributes (e.g., colors and texture), enlarging, dwindling, removing objects, and replacing the background.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address key limitations in existing text-guided image manipulation methods. These methods often (1) randomly alter text-irrelevant content, degrading image quality; (2) lack the ability to perform complex operations beyond simple attribute changes (e.g., color); and (3) fail to handle tasks like object resizing, removal, or background replacement. The core problem identified is the difficulty of accurately localizing the specific image content that the text instruction refers to.

## 2. Key Ideas and Methodology
The paper proposes a novel, interactive framework that divides image manipulation into three distinct phases to ensure precision and control.
- **Core Idea:** The central principle is to explicitly separate the input image into "text-relevant" and "text-irrelevant" content. This allows the model to modify only the relevant region while perfectly preserving the rest of the image.
- **Methodology:**
    1.  **Pre-processing:** A segmentation network (using Deeplabv3 and YOLOv4) first identifies the target object described in the text, generating a segmentation mask. The text-relevant region is then upscaled using a super-resolution network (BSRGAN) to enable finer-grained manipulation.
    2.  **Manipulation:** A modified GAN architecture, based on ManiGAN, edits the upscaled text-relevant content according to the text instruction. This module is capable of handling complex commands like "enlarge" or "remove".
    3.  **Combination:** The edited text-relevant content is fused back with the original, untouched text-irrelevant content. An inpainting network is used to smooth seams and fill any holes created during the process.
- **Interactivity:** A key feature is a user interface that allows for manual correction of the initial segmentation mask, enabling users to refine the target area for more accurate results.

## 3. Datasets Used / Presented
The method was trained and evaluated on two standard datasets:
-   **Caltech-UCSD Birds-200-2011 (CUB):** A dataset of 11,788 bird images across 200 categories. The authors used 8,855 images for training and 2,933 for testing.
-   **Microsoft Common Objects in Context (MS COCO):** A large-scale dataset with 123,287 images of everyday scenes. 82,783 images were used for training and 40,504 for testing.

## 4. Main Results
The proposed model demonstrates superior performance both quantitatively and qualitatively against state-of-the-art methods like ManiGAN.
-   **Quantitative:** On the CUB dataset, the model achieved a higher Inception Score (IS) of 6.79 and a lower Frechet Inception Distance (FID) of 7.15. On the COCO dataset, it also achieved a top IS of 21.67 and FID of 25.60, indicating higher quality and more realistic generated images.
-   **Author-claimed impact:** The proposed method enables interactive, flexible, and accurate image manipulation that can handle complex instructions in real-time, outperforming existing models by precisely editing target objects while preserving background details.

## 5. Ablation Studies
The authors performed several component analyses to validate their design choices:
-   **Super-resolution Network:** Removing the super-resolution module resulted in a loss of fine details like texture and color in the manipulated object. Including it improved the IS from 6.30 to 6.79 and reduced the FID from 9.56 to 7.15 on the CUB dataset, confirming its role in preserving detail.
-   **Inpainting Network:** The inpainting network was shown to be crucial for seamlessly combining the edited object with the background. Without it, visible artifacts and color differences appeared at the boundaries.
-   **Interactive Segmentation Editing:** The user interface proved effective in cases where the automatic segmentation was imperfect. By allowing users to manually correct the mask, the final manipulation was significantly more accurate and aligned with the user's intent.

## 6. Paper Figures
![Figure 10. The results of modifying the n times segmentation using the interface.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_10.jpg' | relative_url }})
![Figure 2. The overview of our proposed model. It allows users to edit the segmentation map automatically.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_2.jpg' | relative_url }})
![Figure 3. The detailed content of TRDCM and Combination network is shown above.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_3.jpg' | relative_url }})
![Figure 4. The qualitative comparison of the proposed ours(auto seg.) and related works on the CUB dataset. Existing methods lack details (e.g., eyes, patterns, etc.), and fail to preserve the text-irrelevant content. In contrast, by adopting semantic map information and the super-resolution method, this method successfully keeps text-irrelevant content and generates better text-relevant content.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_4.jpg' | relative_url }})
![Figure 5. The qualitative comparison of the proposed ours (auto seg.) and related works on the COCO dataset. We can see that ManiGAN manipulates all regions of the image. In contrast, our model is capable of editing images only for a specific object so that it can generate better results.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_5.jpg' | relative_url }})
![Figure 6. The qualitative comparison of ours w/o super-resolution, w super-resolution, and ManiGAN.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_6.jpg' | relative_url }})
![Figure 7. The result of changing the size and the background.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_7.jpg' | relative_url }})
![Figure 8. Comparison of the results before and after inpainting.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_8.jpg' | relative_url }})
![Figure 9. The qualitative result of before and after modifying the segmentation map.]({{ '/images/11-2022/Interactive_Image_Manipulation_with_Complex_Text_Instructions/figure_9.jpg' | relative_url }})
