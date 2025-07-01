---
title: Accelerating_Text-to-Image_Editing_via_Cache-Enabled_Sparse_Diffusion_Inference
layout: default
date: 2023-05-27
---
![Figure 1: In real-world scenarios, users may desire the ability to provide masks and selectively modify only the regions within the mask that they consider unsatisfactory. As shown in the provided example, The user specifies different masks and edits prompt from ”Mountaineering Wallpapers” to ”Mountaineering Wallpapers under fireworks” .]({{ '/images/05-2023/Accelerating_Text-to-Image_Editing_via_Cache-Enabled_Sparse_Diffusion_Inference/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the inefficiency of interactive text-to-image editing using diffusion models. In a typical user workflow, an initial image is generated, and the user then makes minor modifications to the text prompt to refine specific parts of the image. Current methods typically regenerate the entire image from scratch for each edit, which is computationally expensive and slow, as the unchanged regions are needlessly recomputed. The paper aims to solve this practical problem by accelerating the editing process while preserving the quality of the unchanged image regions.

## 2. Key Ideas and Methodology
The core principle of the paper is to exploit the spatial redundancy between consecutive image generations during an editing session. The proposed framework, Fast Image Semantically Edit (FISEdit), accelerates inference by only re-computing the image regions affected by the textual modification.

The methodology consists of three main components:
1.  **Fine-Grained Mask Generation:** FISEdit automatically identifies the affected image regions without requiring a user-drawn mask. It runs a few initial denoising steps for both the original and modified prompts, compares the resulting latent feature maps, and generates a difference mask that isolates the regions with significant changes. This process is stabilized by reusing parts of the cross-attention map corresponding to the unchanged text.
2.  **Sparse Diffusion Inference:** Using the generated mask, FISEdit employs a sparse inference engine for the remaining denoising steps. It selectively computes feature maps only for the masked (affected) regions while reusing cached data for the unmasked regions. This is achieved through:
    *   **Adaptive Pixel-wise Sparse Convolution (APSC):** An optimized tiled sparse convolution that adapts the block size based on the mask's distribution to maximize efficiency.
    *   **Approximate Normalization & Attention:** For layers that operate globally (like Group Normalization and Attention), the framework reuses cached statistics (mean, variance) and applies sparse computation, assuming minor edits do not drastically alter the overall feature distribution.
3.  **Cache-Based Editing Pipeline:** To support sparse inference, FISEdit caches activations and parameters from the previous generation. It uses a distributed storage system and asynchronous data movement to manage the large memory footprint and hide data transfer latency, making the caching process efficient.

## 3. Datasets Used / Presented
The authors use the **LAION-Aesthetics** dataset for evaluation. This dataset contains 454,445 examples, each consisting of an image-text pair. Following the preprocessing method from InstructPix2Pix, the dataset was used to create pairs of original and edited prompts to quantitatively and qualitatively evaluate the performance of FISEdit against other text-based image editing models.

## 4. Main Results
FISEdit demonstrates significant improvements in efficiency while generating high-quality, semantically consistent images.
*   **Efficiency:** Compared to the standard Stable Diffusion pipeline, FISEdit achieves a speedup of up to **4.4× on an NVIDIA TITAN RTX GPU** and **3.4× on an NVIDIA A100 GPU**. The performance gain is most pronounced when the edit size is small (e.g., 5% of the image area).
*   **Image Quality:** Quantitative metrics (Image-Image Similarity, Directional CLIP Similarity, FID) show that FISEdit achieves a competitive trade-off between preserving the original image content and accurately reflecting the semantic changes from the edited text.

The authors claim that FISEdit provides a practical and efficient solution for interactive text-to-image editing, making the user experience faster and more responsive.

## 5. Ablation Studies
The authors conducted an ablation study on a TITAN RTX GPU to validate the effectiveness of each optimization component for a 768x768 image. The results show a cumulative performance gain:
*   **Baseline (Vanilla Stable Diffusion):** 1.83 iterations/second (it/s), representing a 1.0× speed ratio.
*   **+ CUDA Kernel Improvements (e.g., Flash Attention):** Performance increased to 2.73 it/s (1.5× speedup).
*   **+ Tiled Sparse Convolution (without APSC):** Performance increased to 3.17 it/s (1.7× speedup).
*   **+ Adaptive Pixel-wise Sparse Convolution (APSC):** Performance increased to 3.61 it/s (2.0× speedup).
*   **+ Approximate Attention (Full FISEdit Model):** The final model achieved **8.13 it/s**, resulting in a **4.4× total speedup**.

Each component progressively contributes to the overall acceleration, with the sparse computation in convolution and attention layers providing the most substantial gains.

## 6. Paper Figures
![Figure 2: Overview structure of FISEdit. When a query arrives, our system first executes k denoise steps, and then generates a difference mask according to the output latents of k steps. In the remaining denoise steps, the pre-computed results (activations and parameters) of each layers in U-Net will be reused according to the mask and the feature maps will be computed sparsely. Compared to existing frameworks which leverage the batched inputs, we collect and cache the results of previous generation to avoid redundant computation, and use the mask to control as well as accelerate the new T2I generation process at U-Net level.]({{ '/images/05-2023/Accelerating_Text-to-Image_Editing_via_Cache-Enabled_Sparse_Diffusion_Inference/figure_2.jpg' | relative_url }})
![Figure 3: Variation of latent difference with iteration steps.]({{ '/images/05-2023/Accelerating_Text-to-Image_Editing_via_Cache-Enabled_Sparse_Diffusion_Inference/figure_3.jpg' | relative_url }})
![Figure 4: Overall improvement of the attention module.]({{ '/images/05-2023/Accelerating_Text-to-Image_Editing_via_Cache-Enabled_Sparse_Diffusion_Inference/figure_4.jpg' | relative_url }})
![Figure 6: Qualitative results of the (768, 768) images generated by baselines and our method.]({{ '/images/05-2023/Accelerating_Text-to-Image_Editing_via_Cache-Enabled_Sparse_Diffusion_Inference/figure_6.jpg' | relative_url }})
