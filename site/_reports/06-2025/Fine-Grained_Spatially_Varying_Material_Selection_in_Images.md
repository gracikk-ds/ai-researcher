---
title: Fine-Grained_Spatially_Varying_Material_Selection_in_Images
layout: default
date: 2025-06-10
---
## Fine-Grained Spatially Varying Material Selection in Images
**Authors:**
- Julia Guerrero-Viu, h-index: 4, papers: 10, citations: 77
- Valentin Deschaintre, h-index: 3, papers: 7, citations: 77

**ArXiv URL:** http://arxiv.org/abs/2506.09023v2

**Citation Count:** None

**Published Date:** 2025-06-10

![Fig. 1. Our proposed method allows fine-grained material selection in images on two different levels of granularity, significantly outperforming previous work (Materialistic [Sharma et al . 2023]) in selection accuracy and consistency. We show here results on challenging examples due to specular reflections (top left) and fine patterns outside the training data (top right, bottom left). Selection masks are shown as green image overlays. The bottom right row shows material editing results using our predicted two-level selection masks, with the masks shown as insets.]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address key limitations in existing material selection methods for images. Previous state-of-the-art approaches, which leverage Vision Transformers (ViTs), often suffer from low precision, especially around object boundaries and fine structures. This is due to the coarse resolution of ViT feature maps. Furthermore, existing methods and datasets define materials at a single level (e.g., a patterned wallpaper as one material), which prevents users from selecting individual components of a texture (e.g., only the flowers on the wallpaper). The paper aims to solve these problems by developing a more precise and flexible material selection tool.

## 2. Key Ideas and Methodology
The core of the work is a new model architecture and training strategy that builds upon prior work ("Materialistic") to enable more precise, two-level material selection. The key ideas are:
-   **Multi-Resolution Feature Aggregation:** To overcome the low-resolution limitations of ViTs, the model processes the input image at multiple scales. It extracts features from a downscaled version of the entire image (for global context) and from higher-resolution image tiles (for fine details). These features are then aggregated, preserving high-frequency information and leading to sharper, more accurate selections.
-   **Two-Level Selection:** The model is designed with two output heads to predict material similarity at both a "texture" level (e.g., an entire chessboard) and a "subtexture" level (e.g., only the black squares on the board). This provides users with finer control over the selection granularity.
-   **Improved Training Strategy:** During training, the model samples multiple query pixels from different materials within each image. This multi-query approach improves training stability and makes the final model more robust and consistent in its selections. The model uses features from the DINOv2 encoder, which proved more discriminative than alternatives.

## 3. Datasets Used / Presented
-   **DUMAS (Dual-level Material Selection) Dataset:** The authors created and presented a new, large-scale synthetic dataset comprising over 800,000 rendered images of indoor and outdoor scenes. Its key feature is the inclusion of dense, per-pixel annotations for both texture and subtexture levels, which is necessary to train their two-level model.
-   **MATERIALISTIC TEST Dataset:** An existing real-world test set of 50 images with texture-level annotations, used for quantitative evaluation and comparison with prior work.
-   **TWO-LEVEL TEST Dataset:** A new, manually annotated real-world test set of 20 challenging images, created by the authors to evaluate performance at both texture and subtexture levels.

## 4. Main Results
The proposed method significantly outperforms previous state-of-the-art models in quantitative evaluations.
-   On the `MATERIALISTIC TEST` dataset (texture level), the authors' model achieved a mean Intersection over Union (IoU) of 0.896, compared to 0.858 for the "Materialistic" model.
-   On the new, more challenging `TWO-LEVEL TEST` dataset, the model achieved an IoU of 0.750 for texture selection and 0.673 for subtexture selection, demonstrating its superior accuracy and unique two-level capability.
The authors claim their method produces more precise and robust selections, especially for fine structures and in challenging lighting conditions, while offering an unprecedented level of control with its dual-level output.

## 5. Ablation Studies
The authors performed several ablation studies to validate their design choices:
-   **Multi-Resolution Processing:** Removing the multi-resolution feature aggregation module caused a noticeable drop in performance, particularly in selecting thin structures like a basketball net. On a challenging subset, texture-level IoU dropped from 0.763 to 0.585.
-   **Multi-Query Sampling:** Removing the multi-query sampling strategy during training also degraded performance and confidence, especially in cases of albedo entanglement (similar colors on different materials). On the challenging subset, texture-level IoU dropped from 0.763 to 0.685.
-   **Image Encoder:** Replacing the DINOv2 encoder with either DINO or Hiera resulted in less accurate selections. For example, using DINO instead of DINOv2 lowered the texture-level IoU on the `TWO-LEVEL TEST` from 0.750 to 0.698.
-   **Joint Two-Level Training:** Training a single model for both levels simultaneously was shown to be more effective than training two separate, specialized models. The jointly trained model outperformed the single-level variant, with texture-level IoU on the `TWO-LEVEL TEST` increasing from 0.680 to 0.750.

## 6. Paper Figures
![Fig. 10. Limitations. Our method struggles with clicks on out-of-focus regions (top) and long-horizon imagery with changing frequencies (middle). Textures without individual components (bottom) stretches our definition of subtexture.]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_10.jpg' | relative_url }})
![Fig. 2. Model architecture. Our model extracts ViT features at different resolutions, for the full image and for each separate tile, leading to a multi-resolution feature encoding. The subsequent spatial processing layers upscale the features before the cross-similarity computes the attention with respect to the clicked image pixel and patch. We exploit the information encoded at different depths by repeating this process across four ViT levels, before fusing the output with a residual CNN and feeding it to our two-level selection head, producing selections at both subtexture and texture level. The ViT is frozen, the red blocks are trained. FC is short for fully-connected network.]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_2.jpg' | relative_url }})
![Fig. 3. Fine-grained material selection. Our multi-resolution aggregation allows to recover thin structures, overcoming a limitation acknowledged in previous work [Sharma et al. 2023].]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_3.jpg' | relative_url }})
![Fig. 4. DuMaS training dataset creation. Starting from twelve base noise patterns from Substance Designer, we vary their parameters to create 1,571 binary masks which we use to randomly combine 3,026 stationary reflectance maps to generate 10,881 materials (see text for more details). We assign these material maps to objects of our 132 scenes under different combinations, and render videos by varying camera viewpoints, resulting in 816,415 individual images. For each image, our dataset includes dense annotations at both subtexture and texture level; annotation IDs are mapped to gray levels for visualization.]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_4.jpg' | relative_url }})
![Fig. 5. Qualitative results . We show results of our method (two-level selection) for images in our real-world test datasets. For each example and level, we show the predicted, binarized selection masks as green image overlays and the similarity score before thresholding in false color (blue low, red high). Our method works well at both subtexture and texture levels even for cluttered scenes and patterns very different from the ones in the training set (third row, wallpaper), and with challenging examples where objects in the scene share the same color (bottom row). In non-spatially varying materials (bottom row) our model’s predictions for both levels are consistently the same.]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_5.jpg' | relative_url }})
![Fig. 6. Qualitative comparison. Texture-level selection results for Materialistic, SAM2 fine-tuned on our DuMaS dataset, and our method. The white squares highlight areas where the methods struggle. Materialistic fails to select relevant areas, especially in the presence of small or thin structures (first and last rows), or to produce sharp, clear selections (second and third rows). SAM2 has improved sharpness, but produces many false positives in areas of similar appearance.]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_6.jpg' | relative_url }})
![Fig. 7. Robustness. Robustness evaluation of our method with respect to the clicked pixel (left subset), the image crop with increasing zoom levels (middle subset), and illumination changes (right subset). The images are challenging due to similar albedo (left), strong shading variations on the cushions (middle) and specular highlights on the toaster (right).]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_7.jpg' | relative_url }})
![Fig. 8. Ablations. We ablate parts of our method (multi-resolution and multi-sampling, respectively) on two challenging examples containing thin structures (net and zebra stripes) and albedo entanglement (net has a similar albedo to the white parts of the basketball, in front of a patterned background).]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_8.jpg' | relative_url }})
![Fig. 9. Editing. We use our method’s selection masks at subtexture level to perform fine-granular edits of the image’s materials in Photoshop.]({{ '/images/06-2025/Fine-Grained_Spatially_Varying_Material_Selection_in_Images/figure_9.jpg' | relative_url }})
