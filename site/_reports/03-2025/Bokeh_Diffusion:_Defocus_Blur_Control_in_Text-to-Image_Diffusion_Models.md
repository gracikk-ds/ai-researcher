---
title: Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models
layout: default
date: 2025-03-11
---
![Fig. 1. Bokeh Diffusion enables precise, scene-consistent bokeh control in text-to-image diffusion models. Top Left: Images are conditioned on an explicit blur parameter to generate outputs ranging from sharp to strongly defocused. Top Right: Our method maintains consistent scene content across different blur level conditions. Bottom: Continuous adjustment of blur strength produces smooth transitions across the bokeh range.]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current text-to-image models lack precise control over photographic effects like depth-of-field (bokeh). Using text prompts to simulate camera settings is unreliable and often alters the scene's content. This paper introduces a method for direct and scene-consistent bokeh control, addressing the key challenge of scarce real-world training data (images of the same scene with different apertures).

## 2. Key Ideas and Methodology
The paper proposes "Bokeh Diffusion," a framework that conditions a diffusion model on a physical defocus blur parameter.
- **Hybrid Training Pipeline**: To overcome data scarcity, it combines a diverse "in-the-wild" dataset (with EXIF metadata) with synthetically generated "focus-defocus" image pairs. A novel formulation unifies the blur representation across both data sources.
- **Decoupled Conditioning & Grounded Self-Attention**: A lightweight adapter injects the blur condition separately from the text prompt. The core innovation, a grounded self-attention mechanism, uses a "pivot" image to anchor the scene structure while rendering the blur level of a "target" image, effectively disentangling content from blur.

## 3. Datasets Used / Presented
- **In-the-Wild (ITW) Dataset**: A curated set of ~15,000 photos from Flickr, annotated with estimated depth, EXIF data, and captions, providing diverse scenes with authentic lens blur.
- **Synthetic Dataset**: Created by applying synthetic blur to the all-in-focus subset of the ITW data. This generates contrastive pairs of the same scene with varying blur, which is essential for training scene consistency.

## 4. Main Results
- **Quantitative**: Bokeh Diffusion significantly outperformed baselines in both accuracy and consistency. On the FLUX model, it achieved the highest correlation with the target blur level (LVCorr: 0.917) and the best scene consistency (LPIPS: 0.052).
- **User Study**: The method was overwhelmingly preferred by users, with over 91% choosing it for its effective control and consistency. The work enables flexible, lens-like adjustments in generative models while preserving scene integrity.

## 5. Ablation Studies
- **Training Data**: A hybrid of in-the-wild and synthetic data yielded the best results, balancing real-world diversity with the structured supervision needed for consistency.
- **Method Components**: The grounded self-attention mechanism was proven to be the most critical component, dramatically improving scene consistency. The bokeh cross-attention adapter enabled blur control, while an optional color transfer step provided a final polish by harmonizing lighting.

## 6. Paper Figures
![Fig. 2. State-of-the-art text-to-image models [ Labs 2024 ] do not understand textual photographic cues, and unintentionally alter image composition.]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_2.jpg' | relative_url }})
![Fig. 3. Comparison between our generative method and BokehMe [ Peng et al. 2022 ], which depends on external depth estimation.]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_3.jpg' | relative_url }})
![Fig. 4. Data collection and curation pipeline.]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_4.jpg' | relative_url }})
![Fig. 5. In-the-wild image augmentation.]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_5.jpg' | relative_url }})
![Fig. 6. Overview of Bokeh Diffusion’s conditioning and scene-consistency mechanisms. Bokeh Cross-Attention (Sec. 3.3 ), applied at deeper layers of the text-to-image diffusion model, injects a defocus conditioning signal, decoupled from semantic guidance. Grounded Self-Attention (Sec. 3.4 ) ensures fine-grained scene consistency across different defocus levels, where the pivot image’s queries anchor the scene structure, while shared keys allow the model to disentangle defocus blur from scene composition.]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_6.jpg' | relative_url }})
![Fig. 7. Ablation of the proposed modules of Bokeh Diffusion.]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_7.jpg' | relative_url }})
![Fig. 8. Visual comparison with related generative models conditioned on photographic controls CSaT [ Fang et al. 2024 ] and GenPhoto [ Yuan et al. 2024 ].]({{ '/images/03-2025/Bokeh_Diffusion:_Defocus_Blur_Control_in_Text-to-Image_Diffusion_Models/figure_8.jpg' | relative_url }})
