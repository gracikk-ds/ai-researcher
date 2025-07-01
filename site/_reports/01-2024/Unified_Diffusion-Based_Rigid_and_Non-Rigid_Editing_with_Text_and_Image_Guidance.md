---
title: Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance
layout: default
date: 2024-01-04
---
![Fig. 1. Illustration of limitations of prior works on rigid and non-rigid editing tasks.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing diffusion-based image editing methods typically excel at either rigid (e.g., changing an object's color) or non-rigid (e.g., changing an object's pose) editing, but struggle to perform both effectively within a single framework. These methods often produce results that are misaligned with text prompts, especially during substantial modifications, and have limited capabilities for integrating reference images as guidance. The authors address this gap by developing a unified framework that can handle both rigid and non-rigid edits guided by either text or reference images, aiming for better alignment and control.

## 2. Key Ideas and Methodology
The core of the proposed method is a **dual-path injection scheme**. Unlike prior works that use a single generation pipeline, this approach maintains two distinct denoising processes in parallel: one for the source image (providing either appearance or structure) and another for the target guidance (a text prompt or reference image).

Information from these two paths is merged into the final output generation process using a novel **unified self-attention mechanism**. This mechanism computes a structural attention map from the "structure" path and uses it to guide the injection of features from the "appearance" path, ensuring that structural integrity is preserved while appearance is transferred correctly. The mechanism is enhanced with contrast and rearrange operations to prevent artifacts.

To mitigate issues like color shifts and unwanted background changes, the framework incorporates **latent fusion techniques**. It uses Adaptive Instance Normalization (AdaIN) for image-based editing and a blended diffusion strategy for rigid editing to harmonize the latent distributions.

## 3. Datasets Used / Presented
- **PIE-Bench**: A public benchmark used for quantitative and qualitative evaluation of text-based editing. It covers nine different editing scenarios, including rigid, non-rigid, local, and global tasks.
- **Custom Appearance Transfer Dataset**: For evaluating appearance transfer, the authors curated a dataset following the methodology of prior work. It consists of 100 image pairs (20 per domain) across five domains: animal faces, animals, bedrooms, cars, and churches.

## 4. Main Results
The paper demonstrates competitive or superior performance across different editing tasks.

- **Text-Based Editing**: In quantitative comparisons on PIE-Bench (Table I), the method achieves competitive scores against methods like P2P, PnP, and MasaCtrl. While not scoring highest on every individual metric, it provides a versatile balance, effectively handling both rigid and non-rigid scenarios where competitors often fail in one or the other.
- **Appearance Transfer**: The method shows superior performance against state-of-the-art models DiffuseIT and Cross-Image (Table II). It achieves the best average scores for both Structural Preservation (Structure Distance of 7.96 vs. 8.55 and 10.80) and Appearance Preservation (Appearance Distance of 3.01 vs. 4.54 and 4.57).

The authors claim their method is a significant advance in achieving precise and versatile image editing.

## 5. Ablation Studies
The authors performed three main ablation experiments to validate their design choices:

- **Removing the Dual-Path Injection Scheme**: This resulted in poor alignment with the target text prompt and a loss of structural information from the source image, confirming its importance for integrating guidance.
- **Removing Contrast & Rearrange Operations**: Omitting these components from the unified self-attention mechanism led to visual artifacts (e.g., incorrect patterns on a bedsheet) and loss of structural detail (e.g., distorted teacup shape).
- **Removing AdaIN Normalization**: In image-based editing, the absence of AdaIN caused minor but noticeable color distortions in the final output, highlighting its role in harmonizing feature distributions.

## 6. Paper Figures
![Fig. 2. An Overview of Our Approach. Given the input pairs ( I app , T struct ), ( I struct , T app ), and ( I app , I struct ), our method aims to produce the desired editing result I out 1 , I out 2 , I out 2 , which corresponds to achieving text-based non-rigid edits, text-based rigid edits, and image-based edits, respectively. During the denoising step, the source image and target guidance correspond to distinct generation processes, from where information are subsequently injected into the editing process to achieve the desired manipulation.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_2.jpg' | relative_url }})
![Fig. 3. Qualitative Comparisons with Text-Based Editing Methods: P2P [ 7 ], PnP [ 8 ], MasaCtrl [ 9 ]. Our approach successfully accomplishes both rigid and non-rigid editing, demonstrating improved alignment with the target prompt.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_3.jpg' | relative_url }})
![Fig. 4. Qualitative Comparisons to Appearance Transfer Methods. Our method can effectively integrate appearance and structural information from different images.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_4.jpg' | relative_url }})
![Fig. 5. Ablation Study. Each column represents the effect of removing a specific component.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_5.jpg' | relative_url }})
![Fig. 6. Our approach demonstrates strong performance in both rigid and non-rigid editing scenarios, guided by text prompts or reference images.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_6.jpg' | relative_url }})
![Fig. 7. Additional qualitative comparison on text-based non-rigid editing.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_7.jpg' | relative_url }})
![Fig. 8. Additional qualitative comparison on text-based rigid editing.]({{ '/images/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance/figure_8.jpg' | relative_url }})
