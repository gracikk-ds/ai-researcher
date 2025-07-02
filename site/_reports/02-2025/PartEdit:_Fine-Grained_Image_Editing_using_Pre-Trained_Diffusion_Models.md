---
title: PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models
layout: default
date: 2025-02-06
---
## PartEdit: Fine-Grained Image Editing using Pre-Trained Diffusion Models
**Authors:**
- Aleksandar Cvejic, h-index: 1, papers: 2, citations: 1
- Peter Wonka, h-index: 7, papers: 42, citations: 309

**ArXiv URL:** http://arxiv.org/abs/2502.04050v2

**Citation Count:** 1

**Published Date:** 2025-02-06

![Fig. 1. Our approach, PartEdit , enables a wide range of fine-grained edits, allowing users to create highly customizable changes. The edits are seamless, precisely localized, and of high visual quality with no leakage into unedited regions.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing pre-trained diffusion models lack a fine-grained understanding of object parts. This gap leads to significant challenges in text-based image editing, where attempts to modify specific parts often result in poorly localized edits, "leakage" into unintended regions, or unwanted entangled changes (e.g., making hair blonde also makes the subject's face younger). The authors address the practical problem of enabling precise, seamless, and high-quality editing of specific object parts, which current methods fail to achieve.

## 2. Key Ideas and Methodology
The core idea is to expand the semantic knowledge of a frozen, pre-trained diffusion model by teaching it to recognize and localize specific object parts through specialized textual tokens.

- **Core Principle**: Instead of retraining the entire model, the authors optimize a new textual token (e.g., `<head>`) for each object part. The optimization goal is to force the cross-attention maps produced by this token to align with the ground-truth segmentation masks of that part.
- **Methodology**:
    1.  **Token Optimization**: Using a small set of images with part masks, a new token is trained via a Binary Cross-Entropy (BCE) loss on its cross-attention maps. The diffusion model's weights remain frozen.
    2.  **Inference Pipeline**: To perform an edit, the model runs three parallel denoising processes: a **source** path for the original image, an **edit** path for the target prompt, and a **localization** path using the optimized part token.
    3.  **Adaptive Feature Blending**: The attention maps from the localization path are aggregated to create a soft, non-binary blending mask. An adaptive thresholding strategy is applied to this mask, which is then used to seamlessly blend the features from the source and edit paths at each denoising step. This ensures the edit is precisely applied only to the intended region.

## 3. Datasets Used / Presented
- **Training Data**: The part tokens are trained using a small number of annotated images (10-20 per part) sourced from existing datasets like **PASCAL-Part** and **PartImageNet**, or from user-provided annotations.
- **Presented Benchmark**: The authors introduce the **PartEdit Benchmark** for evaluation, which includes:
    - **PartEdit-Synth**: A synthetic dataset of 60 images covering 7 object parts (e.g., `<humanoid-head>`, `<car-hood>`) with predefined source prompts and edits.
    - **PartEdit-Real**: A real-world dataset of 13 internet images with manual annotations and corresponding edit prompts.

## 4. Main Results
- **Quantitative Performance**: On the synthetic benchmark, PartEdit significantly outperformed prior methods. For example, it achieved a foreground CLIP score of 91.74 vs. 63.60 for Prompt-to-Prompt, while better preserving the background (PSNR of 31.5 vs. 23.7).
- **User Studies**: The method was overwhelmingly preferred by users, winning 77-89% of the time against other text-based methods and 66-75% of the time against mask-based methods that were provided with ground-truth masks. For real image editing, it was preferred 81% of the time over Ledits++ and 90% over EF-DDPM.
- **Author-claimed Impact**: The paper presents the first text-based editing approach for object parts, enabling high-quality, seamless, and precisely localized edits that were previously not possible, thereby establishing a new direction for fine-grained image manipulation.

## 5. Ablation Studies
- **Number of Training Samples**: The method is highly data-efficient. The localization accuracy (mIoU) was shown to saturate with only 10-20 training images per part token.
- **Blending Timesteps (`te`)**: This hyperparameter provides users with direct control over the edit's locality. A higher `te` value restricts the edit strictly to the part, while a lower value allows the edit to have a broader, more stylistic influence on the image.
- **Adaptive Thresholding Strategy**: The proposed method for creating the blending mask was qualitatively shown to produce much more seamless and artifact-free edits compared to standard binary thresholding (at 0.5) or simple OTSU thresholding.
- **Choice of UNet Layers**: Analysis revealed that optimizing tokens using only the first 8 layers of the UNet decoder is sufficient for robust localization, offering a significant improvement in computational efficiency without sacrificing performance.

## 6. Paper Figures
![Fig. 10. A comparison on synthetic benchmark against Latent Blending [ Avrahami et al . 2023b ] and SDXL Inpainting [ Podell et al . 2024 ] using ground truth masks ( ✓ ) against our predicted masks ( ✗ ). We observe PartEdit outperforming Latent Blending, which fails totally in some of the edits (spiderman, hair, and chair), while others produce unintegrated edits, such as the bear head. More detailed comparisons can be found on the website.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_10.jpg' | relative_url }})
![Fig. 11. Different edits per image on real image editing using our method. We showcase the versatility of our method, as there is no change in the underlying model; we can leverage the full capabilities of the model without any retraining or fine-tuning. More details in Appendix F .]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_11.jpg' | relative_url }})
![Fig. 12. Challenging multiple subjects edits (more in fig. 26 ). Examples of Grounded SAM [ Ren et al . 2024 ] integration for "second dog" or "right" respectively.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_12.jpg' | relative_url }})
![Fig. 2. A visualization for the cross-attention maps of SDXL [ Podell et al . 2024 ] that corresponds to different words of the textual prompt. Object parts such as “head” and “hood” are not well-localized, indicating that the model lacks a sufficient understanding of these parts. DiT-based model analysis in Appendix R .]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_2.jpg' | relative_url }})
![Fig. 3. An overview of our proposed approach for fine-grained part editing. For an object part 𝑝 , we collect a dataset of images I 𝑝 and their corresponding part annotation masks Y 𝑝 . To optimize a textual token to localize this part, we initialize a random textual embedding ˆ 𝐸 that initially generates random cross-attention maps. During optimization, we invert images in I 𝑝 and optimize the part token so that the cross-attention maps at different layers and timesteps match the part masks in Y 𝑝 . After optimizing the token, it can be used during inference to produce a localization mask at each denoising step. These localization masks are used to perform feature bending between the source and the edit image trajectories. Note that we visualize three instances of SDXL [ Podell et al. 2024 ] for illustration, but in practice, this is done with the same model in a batch of three.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_3.jpg' | relative_url }})
![Fig. 4. Impact of timestep choice in the token optimization process. Intermediate timesteps achieve reasonable localization for both big and small parts.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_4.jpg' | relative_url }})
![Fig. 5. Qualitative comparison on synthetic images from the PartEdit benchmark. Our method outperforms both iP2P [ Brooks et al . 2023 ] and P2P [ Hertz et al . 2022 ] on the synthetic setting. Showcasing good localization while integrating seamlessly into the scene, illustrated by the third row with a formal torso edit.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_5.jpg' | relative_url }})
![Fig. 6. Qualitative comparison against EF-DDPM [ Huberman-Spiegelglas et al. 2024 ] and Ledits++ [ Brack et al. 2024 ] on real image editing.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_6.jpg' | relative_url }})
![Fig. 7. Visualization of editing 2 parts at the same time. Note that the attention maps showcase average cross-attention across all time steps.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_7.jpg' | relative_url }})
![Fig. 8. The impact of the number of denoising steps 𝑡 𝑒 to perform feature blending.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_8.jpg' | relative_url }})
![Fig. 9. Comparison of an edit under different mask binarization strategies in our novel layer timestep blending setup.]({{ '/images/02-2025/PartEdit:_Fine-Grained_Image_Editing_using_Pre-Trained_Diffusion_Models/figure_9.jpg' | relative_url }})
