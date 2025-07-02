---
title: IMAGHarmony:_Controllable_Image_Editing_with_Consistent_Object_Quantity_and_Layout
layout: default
date: 2025-06-02
---
## IMAGHarmony: Controllable Image Editing with Consistent Object Quantity and Layout
**Authors:**
- Fei Shen
- Jinhui Tang, h-index: 3, papers: 5, citations: 65

**ArXiv URL:** http://arxiv.org/abs/2506.01949v1

**Citation Count:** None

**Published Date:** 2025-06-02

![(b) Multi-Object Editing Figure 1: Editing results on (a) few-object and (b) multi-object scenes. Existing methods struggle to preserve the count, layout, and semantics in multi-object cases, while ours ensures consistent and faithful edits.]({{ '/images/06-2025/IMAGHarmony:_Controllable_Image_Editing_with_Consistent_Object_Quantity_and_Layout/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a significant limitation in modern diffusion-based image editing: the lack of precise control in multi-object scenarios. While current models excel at editing images with one or two objects, they often fail when tasked with modifying scenes containing multiple objects. Specifically, they struggle to preserve the correct object quantity and spatial layout as specified in the editing instructions. This failure stems from the weak counting ability of diffusion models and their difficulty in distinguishing multiple entities within an image. To tackle this, the paper introduces a new task, **Quantity-and-Layout consistent image editing (QL-Edit)**, which aims to enable fine-grained control over object counts and arrangements in complex scenes.

## 2. Key Ideas and Methodology
The core of the paper is **IMAGHarmony**, a framework designed to enforce object quantity and layout consistency. Its methodology is built on two key components:

1.  **Harmony-Aware Attention (HA):** This module explicitly models object counts and spatial layouts by integrating multimodal information. It fuses auxiliary textual features (encoding count) and visual features (encoding layout) from the source image. These fused "harmony features" are then injected into the denoising UNet of a frozen Stable Diffusion XL (SDXL) model, guiding it to generate structurally consistent results.
2.  **Preference-Guided Noise Selection (PNS):** To counteract the high sensitivity of diffusion models to initial noise, this inference-time strategy improves generation stability. It first generates several low-step candidate images from different noise seeds. A frozen vision-language model (VLM) then evaluates these candidates for semantic alignment with the prompt. The noise seed that produced the best-aligned candidate is selected to initialize the full, high-quality denoising process.

This dual approach allows IMAGHarmony to maintain structural integrity and semantic accuracy without needing to retrain the entire diffusion model.

## 3. Datasets Used / Presented
The authors introduce **HarmonyBench**, a new comprehensive benchmark dataset created specifically for the QL-Edit task.
*   **Content:** The dataset contains 200 image-caption pairs with object counts ranging from 1 to 20. To ensure diversity, it includes 10 different layout examples for each count level.
*   **Source:** Images are sourced from real-world datasets like COCO and OpenImages, as well as synthesized using SDXL to provide rich visual diversity.
*   **Usage:** Each image is paired with 10 different editing prompts covering category changes, scene modifications, and style transfers, resulting in a total of 2,000 test instructions for systematic evaluation of a model's ability to control quantity and layout.

## 4. Main Results
IMAGHarmony consistently outperforms a wide range of state-of-the-art methods across all QL-Edit tasks.
*   **Quantitative:** In the "Class Editing" task, IMAGHarmony achieved an Object Count Accuracy (OCA) of 80.7% and an Average Precision (AP) for layout of 75.7%. This represents a significant improvement over the best-performing mask-free method, MagicBrush (70.3% OCA, 69.2% AP), and the best mask-based method, IC-Edit (73.2% OCA, 74.6% AP). Similar performance gains were observed in scene and style editing tasks.
*   **Qualitative & User Study:** Visual results show that IMAGHarmony successfully preserves object counts and layouts in complex edits (e.g., changing "Seven Dogs" to "Seven Bears"), where other methods produce incorrect counts or distorted arrangements. A user study confirmed these findings, with participants ranking IMAGHarmony highest for both semantic correctness and overall quality.

The author-claimed impact is that IMAGHarmony provides a robust and effective solution for controllable multi-object editing, a challenging frontier for generative AI.

## 5. Ablation Studies
The authors conducted several ablation studies to validate the contribution of each component of IMAGHarmony.

1.  **Module Effectiveness:**
    *   Removing both the **HA module** and **PNS strategy** resulted in the worst performance, with low object count accuracy (OCA) and poor layout preservation (AP).
    *   Using the **HA module** alone (without PNS) significantly improved OCA and AP, demonstrating its effectiveness in modeling structure. However, the results were less stable, leading to a lower image quality score (IR).
    *   Using the **PNS strategy** alone (without HA) improved OCA and IR over the baseline but failed to capture complex layouts, confirming that intelligent seed selection helps but is insufficient without explicit structural guidance.
    *   The full model with both **HA and PNS** achieved the best performance across all metrics, proving the two components are complementary and essential.

2.  **Injection Location:** Injecting the harmony features into the 4th downsampling block ("Down4") of the UNet yielded the highest accuracy, suggesting this layer offers the optimal balance between semantic and spatial information for structural control.

3.  **Hyperparameter Impact:** The best results were achieved when the influence of both the HA module and the attention mechanism were set to their maximum values (scaling factors α=1.0, β=1.0), indicating their full contributions are beneficial.

## 6. Paper Figures
![Figure 2: Overview of the IMAGHarmony framework. Given a reference image and a text instruction, we first sample multiple candidate noise seeds and evaluate their semantic alignment using a vision-language model (VLM). The topk candidates are retained for inference. The harmony-aware attention (HA) module fuses auxiliary textual and visual features to jointly model object count and spatial layout. An image prompt (IP) attention layer injects these layout-aware features into the UNet backbone without modifying its frozen weights. During inference, the preference-guided noise selection (PNS) strategy selects the best candidate seed to guide the full denoising process, leading to edited images that are consistent in both quantity and layout.]({{ '/images/06-2025/IMAGHarmony:_Controllable_Image_Editing_with_Consistent_Object_Quantity_and_Layout/figure_2.jpg' | relative_url }})
![Figure 3: Examples from HarmonyBench. Each sample includes a source image and a validated count-object caption, verified by YOLO-World [ 4 ] and human review.]({{ '/images/06-2025/IMAGHarmony:_Controllable_Image_Editing_with_Consistent_Object_Quantity_and_Layout/figure_3.jpg' | relative_url }})
![Figure 4: Qualitative comparisons with several state-of-the-art models on the HarmonyBench dataset. cations. Notably, SEED-X [ 11 ] additionally shows inconsistencies in object count. (3) In style editing (last two rows), IMAGHarmony transfers the target style ( e.g., “Cyberpunk” ) without altering object semantics or disrupting spatial arrangement. In contrast, existing methods frequently over-stylize or distort structure. For example, Show-o [ 61 ] mistakenly changes the object category during editing. In summary, IMAGHarmony effectively disentangles content from instructions, delivering semantically faithful and structurally consistent edits, even under complex multi-object.]({{ '/images/06-2025/IMAGHarmony:_Controllable_Image_Editing_with_Consistent_Object_Quantity_and_Layout/figure_4.jpg' | relative_url }})
![Figure 6: Attention map comparison. (a) w/o HA. (b) w/ HA. HA module better captures object count and layout.]({{ '/images/06-2025/IMAGHarmony:_Controllable_Image_Editing_with_Consistent_Object_Quantity_and_Layout/figure_6.jpg' | relative_url }})
![“ Six Cats ” Figure 8: Effect of attention weights on editing quality. Setting both α and β to 1.0 produces the best results.]({{ '/images/06-2025/IMAGHarmony:_Controllable_Image_Editing_with_Consistent_Object_Quantity_and_Layout/figure_8.jpg' | relative_url }})
