---
title: FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning
layout: default
date: 2024-08-06
---
## FastEdit: Fast Text-Guided Single-Image Editing via Semantic-Aware Diffusion Fine-Tuning
**Authors:**
- Zhi Chen
- Zi Huang

**ArXiv URL:** http://arxiv.org/abs/2408.03355v1

**Citation Count:** None

**Published Date:** 2024-08-06

![Figure 1. FastEdit – Text-Guided Single-Image Editing in 17 seconds. We show the pairs of 512 × 512 input images, and the given target texts with corresponding edited results. Compared with the baseline methods, FastEdit fine-tunes only 0.37% parameters for 50 iterations. Arbitrary target texts are supported for the fine-tuned model, due to its embedding optimization-free nature.]({{ '/images/08-2024/FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Conventional state-of-the-art methods for text-guided single-image editing, such as Imagic, are computationally expensive and slow, often requiring around 7 minutes to edit a single image. This lengthy process, involving extensive optimization of both text embeddings and the generative model itself, poses a significant bottleneck for practical, real-time applications. The authors aim to bridge this gap by developing a method that dramatically accelerates the editing process without sacrificing the quality of the output.

## 2. Key Ideas and Methodology
The paper introduces FastEdit, a method that accelerates single-image editing through three core contributions:

1.  **Image-to-Image Model Variant:** Instead of the conventional text-to-image pipeline, FastEdit uses an image-to-image diffusion model. This allows it to condition directly on image and text features extracted from a pre-trained CLIP model, completely circumventing the time-consuming (approx. 2 minutes) initial step of optimizing text embeddings for the input image.

2.  **Semantic-Aware Diffusion Fine-Tuning:** The authors observe that the required diffusion time step depends on the magnitude of the requested edit. FastEdit calculates the semantic discrepancy (cosine distance between CLIP features) between the input image and target text. This discrepancy is used to select a small, customized range of time steps for fine-tuning, drastically reducing the required iterations from over 1,500 to just 50.

3.  **Parameter-Efficient Fine-Tuning:** To further reduce computational overhead, FastEdit incorporates Low-Rank Adaptation (LoRA) to fine-tune the diffusion model's U-Net. This approach updates only 0.37% of the model's parameters, achieving results comparable to full fine-tuning but with significantly less computational cost.

## 3. Datasets Used / Presented
The authors evaluate their method on two datasets:
*   **TedBench:** A standard benchmark for textual image editing containing 100 pairs of input images and target text prompts that describe complex, non-rigid edits.
*   **Custom Dataset:** A set of 54 image-text pairs collected by the authors from Pexels, featuring a wide range of domains and high-resolution images.

Both datasets were used to perform qualitative and quantitative comparisons against baseline methods.

## 4. Main Results
FastEdit significantly outperforms existing methods in efficiency while maintaining high-quality results.

*   **Speed:** FastEdit reduces the editing time for a single image from **7 minutes** (Imagic) to just **17 seconds**, requiring only **50 fine-tuning iterations** compared to Imagic's 2,500.
*   **Text Alignment:** It achieves a superior CLIP score of **0.269**, indicating better alignment between the edited image and the target text compared to baselines like Imagic (0.248) and SVDiff (0.247).
*   **Human Preference:** In a user study with 120 participants, FastEdit was the preferred method **37.6%** of the time, substantially higher than Imagic (28.9%). This demonstrates its ability to produce more appealing and accurate edits.

The authors claim that FastEdit is the first method to demonstrate such fast text-based editing on real-world images while preserving original image details well.

## 5. Ablation Studies
The paper reports three main ablation experiments to validate the contribution of each component:

1.  **Image-to-Image vs. Text-to-Image Variant:** A comparison showed that the base text-to-image Stable Diffusion model actually produces better raw results than the image-to-image variant. This confirms that FastEdit's performance gains come from its novel methodology (feature-space conditioning and semantic-aware tuning) rather than an inherently superior base model.
2.  **Semantic-Aware Fine-Tuning:** Experiments demonstrated that using a fixed range of time steps (e.g., always high or always low) leads to poor results, such as texture distortion or counterfactual object generation. This validates the necessity of customizing the time step range based on the semantic discrepancy between the image and text.
3.  **Contribution of LoRA:** A "LoRA only" variant (Imagic with LoRA instead of full fine-tuning) was tested. This model failed to faithfully apply the semantic edits described in the text, proving that LoRA alone is insufficient and that FastEdit's other components are critical for its success.

## 6. Paper Figures
![“… da Vinci...” “… a big grin.” “… stars in the sky.” “… wearing glasses.” Figure 2. Different target texts applied to the same images. FastEdit edits the same image differently based on the semantic discrepancy between input image and the target texts.]({{ '/images/08-2024/FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning/figure_2.jpg' | relative_url }})
![Figure 3. Illustration of FastEdit. Given an input image and a target text, we first project them into features using the CLIP model. Then, we calculate the semantic discrepancy between the two to determine the denoising time steps. Further, we fine-tune the lowrank matrixes added to diffusion model for a few iterations. Lastly, we can interpolate the CLIP’s features to generate desired images with the fine-tuned model. • [Text Optimization] The two-minute duration required to optimize text embedding for each image seems unnecessary , as we can project the input image and the target text into the same latent feature space. When applying the fine-tuned model to the same input image but a different target text, the text features and diffusion model can be reused without any adaptation.]({{ '/images/08-2024/FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning/figure_3.jpg' | relative_url }})
![Decoded Noisy Images Figure 4. Fine-tuning on a single denoising time step leads to texture and structure tradeoff. Low time step values tend to preserve the texture details of the object and result in input image structure distortion. In contrast, high time step values tend to preserve the image structure but lose textural details.]({{ '/images/08-2024/FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning/figure_4.jpg' | relative_url }})
![Figure 5. Method comparison. We compare Imagic [ 18 ], SVDiff [ 12 ], LoRA [ 15 ] with our method. FastEdit successfully applies the desired edit and preserves the original details.]({{ '/images/08-2024/FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning/figure_5.jpg' | relative_url }})
![Figure 6. Conditional feature interpolation. Increasing η with the same seed, we see the resulted images are closer to the model’s original understanding towards the target text.]({{ '/images/08-2024/FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning/figure_6.jpg' | relative_url }})
![Figure 7. Effects of semantic-aware diffusion fine-tuning. Different range of time step choices lead to different results on images with various semantic discrepancies.]({{ '/images/08-2024/FastEdit:_Fast_Text-Guided_Single-Image_Editing_via_Semantic-Aware_Diffusion_Fine-Tuning/figure_7.jpg' | relative_url }})
