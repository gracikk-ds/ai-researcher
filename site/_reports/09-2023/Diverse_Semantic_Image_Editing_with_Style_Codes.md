---
title: Diverse_Semantic_Image_Editing_with_Style_Codes
layout: default
date: 2023-09-25
---
![Fig. 1: Our method can remove objects from a scene (highlighted with red boxes), generate panoramas and inpaint a semantic class with different styles, and add objects to a scene again in different styles.]({{ '/images/09-2023/Diverse_Semantic_Image_Editing_with_Style_Codes/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing semantic image editing methods struggle to generate diverse outputs, especially when adding new objects whose style cannot be inferred from the context of an erased image. Furthermore, they often fail to seamlessly blend generated content with existing pixels because they lack a robust mechanism to handle partially erased objects, leading to visual inconsistencies and artifacts.

## 2. Key Ideas and Methodology
The paper introduces a framework for diverse and consistent semantic editing built on a novel style encoding pipeline.
- **Core Idea:** The model uses a dual-encoding strategy. For partially erased objects, style is extracted from the visible parts. For completely erased objects, style is learned from the original, unerased image during training. This allows substituting styles from reference images during inference to generate diverse results.
- **Methodology:** A key component is a **mask-aware style encoding module**. This module calculates style features by averaging only over the valid (unmasked) pixels of an object. It also learns a normalization based on the "valid ratio" (the proportion of visible pixels), allowing it to adaptively handle objects with varying degrees of occlusion and ensure consistent style extraction. The architecture employs a multi-scale generator to progressively refine the image quality.

## 3. Datasets Used / Presented
The model was trained and evaluated on three standard datasets for semantic editing tasks:
- **Cityscapes:** ~3,000 training images of urban scenes with semantic and instance labels.
- **ADE20k-Room:** A subset of ADE20k with ~2,200 training images of indoor scenes (bedrooms, hotels, etc.).
- **ADE20k-Landscape:** A subset of ADE20k with ~1,700 training images of landscape scenes.

## 4. Main Results
- The proposed method achieved state-of-the-art image quality, consistently obtaining the best (lowest) Fréchet Inception Distance (FID) scores across all datasets and evaluation tasks (free-form inpainting, outpainting, object addition) compared to baselines like SPMPGAN and SIEDOB.
- While achieving superior visual quality, the model maintained comparable performance on semantic consistency metrics (mIoU, Accuracy), demonstrating that it adheres to the input semantic map effectively.
- In a user study against SPMPGAN, the proposed method was preferred 65% of the time for its superior color consistency and instance generation.

## 5. Ablation Studies
- **Removing Style Encoding:** Disabling the style module entirely worsened FID scores and removed the model's ability to generate diverse outputs, making it deterministic.
- **Removing Valid Ratio Normalization:** Disabling the proposed mask-aware normalization based on the valid pixel ratio significantly degraded performance (FID worsened from 24.19 to 25.95 on ADE20k-Landscape), confirming its importance for handling partial erasures.
- **Removing Multi-scale Generator:** Using only a single-scale generator instead of the multi-scale architecture led to a substantial drop in output quality (FID worsened from 24.19 to 27.03).
- **Varying Style Dimension:** A style vector dimension of 128 was found to be optimal, outperforming both smaller (64) and larger (256) dimensions.

## 6. Paper Figures
![Fig. 2: The overall pipeline for the diverse semantic image editing. During training, we both encode the erased and original images. The original image is encoded because if a semantic or instance ID is completely erased, then its style is extracted from the original image for the training. The encoded styles, instance maps, and binary mask are fed into the style encoding module which is explained in more detail in Sec. 3.1 . The outputs of the style encoding are used in the normalization layers of the generator. The normalization layers additionally take semantic maps, edge maps, and binary masks as inputs. As for the generator, we use a multi-scale generator that refines the predictions at each stage as explained in more depth in Sec. 3.2 .]({{ '/images/09-2023/Diverse_Semantic_Image_Editing_with_Style_Codes/figure_2.jpg' | relative_url }})
![Fig. 3: Comparisons of methods on ADE20k dataset for free-form and outpainting masks. Our method achieves better results in terms of color consistency between the generated and existing pixels and sharpness in the generated parts.]({{ '/images/09-2023/Diverse_Semantic_Image_Editing_with_Style_Codes/figure_3.jpg' | relative_url }})
![Fig. 4: Comparisons of methods on Cityscapes datasets for free-form, outpainting, and extension masks. Our method achieves better results in terms of color consistency between the generated and existing pixels and sharpness in the generated parts.]({{ '/images/09-2023/Diverse_Semantic_Image_Editing_with_Style_Codes/figure_4.jpg' | relative_url }})
![Fig. 5: Comparisons of methods on ADE20k-Room dataset for adding objects setting. Our method can add objects with diverse styles which improves realism.]({{ '/images/09-2023/Diverse_Semantic_Image_Editing_with_Style_Codes/figure_5.jpg' | relative_url }})
![Fig. 6: Comparisons of methods on Cityscapes dataset for adding objects setting. Our method can add objects with diverse styles which improves realism.]({{ '/images/09-2023/Diverse_Semantic_Image_Editing_with_Style_Codes/figure_6.jpg' | relative_url }})
![Fig. 7: Adding diverse objects with our method. The chair is erased from the image and is inpainted with different style codes that are extracted from corresponding semantic classes of the style images.]({{ '/images/09-2023/Diverse_Semantic_Image_Editing_with_Style_Codes/figure_7.jpg' | relative_url }})
