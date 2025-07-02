---
title: InstGenIE:_Generative_Image_Editing_Made_Efficient_with_Mask-aware_Caching_and_Scheduling
layout: default
date: 2025-05-27
---
## InstGenIE: Generative Image Editing Made Efficient with Mask-aware Caching and Scheduling
**Authors:**
- Xiaoxiao Jiang, h-index: 1, papers: 3, citations: 4
- Wei Wang

**ArXiv URL:** http://arxiv.org/abs/2505.20600v1

**Citation Count:** 0

**Published Date:** 2025-05-27

![Figure 1. A virtual try-on example of image editing using a SDXL model on H800. InstGenIE achieves a model inference speedup of 1 . 7 × and ensures image quality. The Rightmost image : Naively disregarding unmasked regions in image editing will distort the output image.]({{ '/images/05-2025/InstGenIE:_Generative_Image_Editing_Made_Efficient_with_Mask-aware_Caching_and_Scheduling/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The paper addresses the inefficiency of serving generative image editing requests using diffusion models in production AI cloud services. Existing systems typically treat image editing as a full image regeneration task, which is computationally expensive and leads to high latency and low throughput. This approach fails to exploit the inherent sparsity introduced by masks, which are commonly used to specify the exact regions of an image to be modified while leaving the rest untouched. The authors aim to bridge this gap by designing a system that leverages this mask-guided sparsity to make image editing inference more efficient.

## 2. Key Ideas and Methodology
The core principle of INSTGENIE is that computations for the unmasked (unchanged) regions of an image are redundant and can be skipped by caching and reusing intermediate activations from previous inference runs on the same image template.

The methodology is built on three key designs:
1.  **Mask-Aware Caching with a Bubble-Free Pipeline:** INSTGENIE caches the activations of unmasked tokens to avoid re-computation. To mitigate the high overhead of loading these large caches from host memory to GPU memory, it employs a dynamic programming algorithm. This algorithm selectively decides for each model layer whether to perform a full computation or use the cache, creating an optimized pipeline that overlaps cache loading with computation to minimize stalls and overall latency.
2.  **Disaggregated Continuous Batching:** Adapting the concept from LLM serving, INSTGENIE allows new requests to join a running batch at any denoising step, significantly reducing queueing delays compared to static batching. To prevent performance degradation, it disaggregates CPU-intensive pre/post-processing tasks from the GPU-intensive denoising loop by running them in separate processes.
3.  **Mask-Aware Load Balancing:** Since mask sizes vary widely between requests, a simple request-count-based scheduler leads to load imbalance. INSTGENIE uses a greedy scheduling policy guided by offline-trained regression models. These models accurately estimate the combined computational and cache-loading latency for a batch of requests based on their mask ratios, enabling effective load distribution across worker GPUs.

## 3. Datasets Used / Presented
The authors characterized workloads and evaluated their system using the following:
*   **Private Production Trace:** A 14-day trace collected from a large-scale production face-swap service, containing 34 million images generated across 20,000 GPUs. It was used to analyze mask ratio distributions and template reuse patterns.
*   **Public Image Generation Trace:** A public trace from prior work [37] used to corroborate findings, showing that 70% of requests are for image editing and confirming that mask ratios are typically small but highly variable.
*   **Image Quality Benchmarks:** The system's output quality was evaluated on standard benchmarks, including **InstructPix2Pix** (for SD2.1), **VITON-HD** (for SDXL), and **PIE-Bench** (for Flux).

## 4. Main Results
INSTGENIE demonstrates significant performance improvements over state-of-the-art baselines like Diffusers, FISEdit, and TeaCache.
*   **Throughput and Latency:** It achieves up to **3x higher throughput** and reduces the average end-to-end request latency by up to **14.7x**.
*   **Tail Latency:** The P95 tail latency is reduced by up to 88% compared to baselines.
*   **Image Quality:** These gains are achieved without compromising image quality. INSTGENIE's outputs are visually and quantitatively (via SSIM, FID, and CLIP scores) comparable or superior to those from baselines, achieving an SSIM score of up to 0.99 against standard, non-accelerated outputs.

## 5. Ablation Studies
*   **Continuous Batching:** INSTGENIE’s disaggregated continuous batching design was compared against static batching and a naive (strawman) continuous batching approach. The proposed design reduced P95 tail latency by 35% and 40% respectively, by eliminating queueing delays and CPU-GPU interference.
*   **Load Balancing:** The mask-aware scheduler was evaluated against simpler schedulers that balance load by request count or masked token count. Under high traffic, INSTGENIE's scheduler reduced tail latency by up to 35% by more accurately modeling the true cost of each request.
*   **Mask-Aware Editing:** The direct impact of the caching mechanism was measured, showing that inference latency scales linearly with the mask ratio. At a 20% mask ratio, the system accelerated inference by 1.3x to 2.2x, depending on the diffusion model.

## 6. Paper Figures
![Figure 2. A simplified illustration of diffusion model inference. A darker cells/cuboid means it is masked.]({{ '/images/05-2025/InstGenIE:_Generative_Image_Editing_Made_Efficient_with_Mask-aware_Caching_and_Scheduling/figure_2.jpg' | relative_url }})
![Figure 6. Token activations and attention scores in a SDXL model. Left : Cosine similarity of activations. Right : Zoomedin visualizaiton of attention scores. Tokens with ID 200-236 are masked and with ID 237-300 are unmasked.]({{ '/images/05-2025/InstGenIE:_Generative_Image_Editing_Made_Efficient_with_Mask-aware_Caching_and_Scheduling/figure_6.jpg' | relative_url }})
![Figure 8. An overall architecture of InstGenIE.]({{ '/images/05-2025/InstGenIE:_Generative_Image_Editing_Made_Efficient_with_Mask-aware_Caching_and_Scheduling/figure_8.jpg' | relative_url }})
