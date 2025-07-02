---
title: PhotoDoodle:_Learning_Artistic_Image_Editing_from_Few-Shot_Pairwise_Data
layout: default
date: 2025-02-20
---
## PhotoDoodle: Learning Artistic Image Editing from Few-Shot Pairwise Data
**Authors:**
- Shijie Huang
- Jiaming Liu

**ArXiv URL:** http://arxiv.org/abs/2502.14397v2

**Citation Count:** 7

**Published Date:** 2025-02-20

![Figure 1. PhotoDoodle can mimic the styles and techniques of human artists in creating photo doodles, adding decorative elements to photos while maintaining perfect consistency between the preand post-edit states.]({{ '/images/02-2025/PhotoDoodle:_Learning_Artistic_Image_Editing_from_Few-Shot_Pairwise_Data/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The paper addresses the challenges of "photo doodling," the artistic process of overlaying decorative elements onto photographs. This task is difficult for existing AI models because it requires a unique combination of capabilities: the added elements must be contextually coherent and seamlessly integrated with the background, the original background must be preserved without distortion, and the model must be able to learn a specific artist's unique style from only a few examples (few-shot learning). The authors argue that previous methods, which focus on global style transfer or masked inpainting, are ill-suited for these specific requirements, creating a gap for a precise, context-aware, and customizable artistic editing tool.

## 2. Key Ideas and Methodology
The core of the paper is **PhotoDoodle**, a framework built on a Diffusion Transformer (DiT) that uses a two-stage training strategy to learn artistic editing.

*   **Stage 1: OmniEditor Pre-training:** A general-purpose image editing model, named OmniEditor, is pre-trained on a large-scale dataset. This stage endows the model with robust, general editing and instruction-following capabilities.
*   **Stage 2: EditLoRA Fine-tuning:** The pre-trained OmniEditor is then fine-tuned using a low-rank adaptation (LoRA) technique called EditLoRA. This allows the model to learn a specific artist's unique doodling style from a small set of 30-50 paired examples.

Two key technical innovations support this framework:
1.  **Positional Encoding (PE) Cloning:** To ensure spatial consistency between the input and output, the same positional encoding is applied to both the source image's condition tokens and the noised latent tokens of the image being generated. This acts as a strong spatial hint, preventing misalignment.
2.  **Noise-Free Conditioning:** The source image is used as a clean, noise-free condition throughout the diffusion process. This preserves high-frequency details and textures from the original background, preventing degradation and unwanted alterations.

## 3. Datasets Used / Presented
*   **SeedEdit:** A large-scale dataset of 3.5 million image editing pairs used to pre-train the general-purpose OmniEditor model.
*   **PhotoDoodle Dataset (newly presented):** A curated dataset created for this work, containing over 300 high-quality samples across six distinct artistic styles (e.g., cartoon monster, hand-drawn outline, 3D effects). Each sample consists of a before-and-after image pair and a corresponding text instruction. It is used for fine-tuning and evaluating the EditLoRA module.
*   **HQ-Edit & Pexels Benchmark:** Used for quantitative evaluation of general and customized editing tasks, respectively.

## 4. Main Results
PhotoDoodle demonstrates superior performance over existing baselines in both general and customized image editing.
*   **General Editing:** On the HQ-Edit benchmark, the OmniEditor model achieved a **GPT Score of 51.16** and a **CLIP Score of 0.261**, significantly outperforming methods like Instruct-Pix2Pix (38.20 GPT Score, 0.237 CLIP Score) and MagicBrush.
*   **Customized Editing:** When fine-tuned on the PhotoDoodle dataset, the model achieved a **GPT Score of 63.21** and a **CLIP Score of 0.279**, again surpassing baselines in instruction alignment and edit quality.

The authors claim that PhotoDoodle is the first framework to effectively learn style-specific photo doodling from few-shot examples while maintaining strict background consistency.

## 5. Ablation Studies
The paper validates the contribution of each key component through ablation studies:
*   **Without OmniEditor Pre-training:** Directly fine-tuning with EditLoRA resulted in weaker text-following ability and reduced harmony between the generated doodles and the source photo.
*   **Without Positional Encoding (PE) Cloning:** Removing this mechanism led to decreased consistency in the generated output, causing unwanted changes and misalignments in the background.
*   **Without EditLoRA:** Using only the pre-trained OmniEditor for generation produced results with significantly less stylization, failing to capture the specific artistic style from the few-shot examples.

## 6. Paper Figures
![Figure 2. The overall architecture and training prodigim of photodoodle. The ominiEditor and EditLora all follow the lora training prodigm. We use a high rank lora for pre-training the OmniEditor on a large-scale dataset for general-purpose editing and text-following capabilities, and a low rank lora for fine-tuning EditLoRA on a small set of paired stylized images to capture individual artists’ specific styles and strategies for efficient customization. We encode the source image into a condition token and concatenate it with a noised latent token, controlling the generation outcome through MMAttention.]({{ '/images/02-2025/PhotoDoodle:_Learning_Artistic_Image_Editing_from_Few-Shot_Pairwise_Data/figure_2.jpg' | relative_url }})
![Figure 3. The generated results of PhotoDoodle. PhotoDoodle can mimic the manner and style of artists creating photo doodles, enabling instruction-driven high-quality image editing.]({{ '/images/02-2025/PhotoDoodle:_Learning_Artistic_Image_Editing_from_Few-Shot_Pairwise_Data/figure_3.jpg' | relative_url }})
![Figure 4. Compared to baselines, PhotoDoodle demonstrates superior instruction following, image consistency, and editing effectiveness.]({{ '/images/02-2025/PhotoDoodle:_Learning_Artistic_Image_Editing_from_Few-Shot_Pairwise_Data/figure_4.jpg' | relative_url }})
![Figure 5. Ablation study results.]({{ '/images/02-2025/PhotoDoodle:_Learning_Artistic_Image_Editing_from_Few-Shot_Pairwise_Data/figure_5.jpg' | relative_url }})
![Figure 7. More photo doodling results: one adds lines to a photo of clouds, imagining them as animals; the other converts the photo into a monochrome version and decorates it with color blocks.]({{ '/images/02-2025/PhotoDoodle:_Learning_Artistic_Image_Editing_from_Few-Shot_Pairwise_Data/figure_7.jpg' | relative_url }})
