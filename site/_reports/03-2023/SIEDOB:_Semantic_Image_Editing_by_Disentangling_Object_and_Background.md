---
title: SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background
layout: default
date: 2023-03-23
---
## SIEDOB: Semantic Image Editing by Disentangling Object and Background
**Authors:**
- Wuyang Luo, h-index: 5, papers: 8, citations: 82
- Weishan Zhang, h-index: 8, papers: 18, citations: 164

**ArXiv URL:** http://arxiv.org/abs/2303.13062v1

**Citation Count:** None

**Published Date:** 2023-03-23

![Figure 1. Existing methods struggle to deal with the compound of backgrounds and several overlapping objects in a complex scene. They generate distorted objects and texturally inconsistent backgrounds . The proposed method can cope well with this input.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key limitation in existing semantic image editing methods. Current approaches typically use a single, monolithic model to generate both foreground objects and backgrounds. This is problematic because objects and backgrounds have fundamentally different characteristics; objects are class-specific and have defined shapes, while backgrounds are often large, amorphous, and require strict texture consistency with surrounding unedited areas. Consequently, monolithic models struggle with complex scenes, often producing distorted objects and backgrounds with inconsistent textures. The paper aims to solve this by proposing a new paradigm that handles objects and backgrounds separately.

## 2. Key Ideas and Methodology
The core idea of the paper is to disentangle the generation of objects and backgrounds by using a heterogeneous network architecture, named **SIEDOB (Semantic Image Editing by Disentangling Object and Background)**. This approach mimics how a human expert would edit a complex photo.

The methodology consists of three main stages:
1.  **Disassembly:** The input image is first decomposed into a background region and multiple instance-level object regions based on a user-provided segmentation map.
2.  **Separate Generation:**
    *   **Background:** A specialized background generator synthesizes the missing background regions. It uses a novel **Semantic-Aware Self-Propagation Module (SASPM)** to explicitly transfer features from known regions to edited regions of the same semantic class, ensuring texture consistency. A **Boundary-Anchored Patch Discriminator (DBAP)** further enforces local texture quality along the editing boundary.
    *   **Objects:** A two-pronged object generator handles foreground elements. A lightweight network inpaints partially visible objects, while a **Style-Diversity Object Generator**, guided by a class-aware style bank, synthesizes new, diverse, and high-quality objects from only a mask.
3.  **Fusion:** Finally, a simple fusion network integrates the newly generated background and objects, harmonizing them with each other and the existing image context to eliminate artifacts and create a coherent final image.

## 3. Datasets Used / Presented
The authors conduct experiments on two standard, complex-scene datasets:
*   **Cityscapes:** A dataset of urban street scenes from German cities. It is used to evaluate the model's performance on complex outdoor environments with many overlapping objects (e.g., cars, pedestrians).
*   **ADE20K-Room:** A subset of the ADE20K dataset, containing images of indoor scenes (e.g., bedrooms, living rooms). It is used to test the model on cluttered indoor environments with various objects (e.g., beds, chairs, lamps).

Both datasets were used for training and testing the model at a 256×256 resolution.

## 4. Main Results
SIEDOB demonstrates superior performance over state-of-the-art methods across various metrics and mask types (free-form, extension, outpainting).
*   **Quantitative:** On the Cityscapes dataset with free-form masks, SIEDOB achieved a Fréchet Inception Distance (FID) of 11.07 and a Learned Perceptual Image Patch Similarity (LPIPS) of 0.077, outperforming the next-best baseline, SPMPGAN (FID 11.90, LPIPS 0.084). Similar improvements were observed on the ADE20K-Room dataset.
*   **Object Addition & Diversity:** In object addition tasks, SIEDOB produced more realistic objects and achieved higher diversity. On Cityscapes, it obtained a diversity score of 0.0055, higher than competing methods like ASSET (0.0052).
*   **Author-claimed impact:** The authors conclude that their disentangled generation strategy significantly improves the model's ability to synthesize realistic and diverse objects while maintaining texture-consistent backgrounds, especially in complex, crowded scenes.

## 5. Ablation Studies
The paper includes comprehensive ablation studies to validate the contribution of each key component of the SIEDOB framework.
*   **Background Generation Modules:** Removing the **SASPM** resulted in noticeable texture inconsistencies, and removing the **DBAP** degraded the quality at the editing boundaries. Quantitatively, removing SASPM worsened the FID on Cityscapes from 12.15 to 14.11.
*   **Object Generation:** Removing the **Style Cycle-Consistency Loss (Lscc)** caused the generated object's style to mismatch the target style. Replacing the learned **style bank** with random noise led to lower-quality and less diverse object generation.
*   **Separate Generation:** A version of the model without the separate object/background pipeline ("w/o Separation") produced visually inferior results, particularly for objects in complicated surroundings. The full model improved the FID from 6.78 to 6.29 in the object addition task on Cityscapes.
*   **Fusion Network:** Removing the fusion network or its skip connection resulted in abrupt, disharmonious boundaries between the generated elements and the rest of the image, degrading both qualitative and quantitative performance.

## 6. Paper Figures
![Figure 10. Out-of-distribution editing. Our method can add cars in the middle of the road or on the sidewalk, which do not exist in the training dataset.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_10.jpg' | relative_url }})
![Figure 2. Overview of the proposed method. To reduce the complexity of modeling the entire edited region, we use a heterogeneous model to synthesize foreground objects and backgrounds separately, which contains three components: (1) Background generation, (2) object generation, (3) fusion network.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_2.jpg' | relative_url }})
![Figure 3. (a) A background category, such as sky, may span known and edited regions. We want to transfer the features from the known region to the generated region in a semantic-aware fashion. (b) The principle of SASPM . We extract the feature code for each background category from the known region and then propagate it to the entire region. (c) The architecture of our background generator.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_3.jpg' | relative_url }})
![Figure 4. Boundary-Anchored Patch Discriminator D BAP takes in four real image patches or fake image patches of random size. All patches are centered on the boundary of the edited region enclosed by the red line.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_4.jpg' | relative_url }})
![Figure 5. (a) How to extract style maps? During training, we extract their style codes from ground truth images or randomly sampled images and then generate style maps by broadcasting. During inference, we sample a class-specific style code directly from the style bank. (b) The structure of Semantic-Style Normalization Module (SSNM) . (c) We build a Style-Diversity Object Generator equipped with SSNM .]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_5.jpg' | relative_url }})
![Figure 6. Structure of Fusion Network. The red line indicates the skip connection.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_6.jpg' | relative_url }})
![Figure 7. Visual comparisons with state-of-the-art methods. Our method is effective in generating texture-consistent backgrounds and photo-realistic objects.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_7.jpg' | relative_url }})
![Figure 8. Visual results of addition objects.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_8.jpg' | relative_url }})
![Figure 9. Multi-modal generation results.]({{ '/images/03-2023/SIEDOB:_Semantic_Image_Editing_by_Disentangling_Object_and_Background/figure_9.jpg' | relative_url }})
