---
title: Diffusion_Model_Compression_for_Image-to-Image_Translation
layout: default
date: 2024-01-31
---
## Diffusion Model Compression for Image-to-Image Translation
**Authors:**
- Geonung Kim
- Sunghyun Cho

**ArXiv URL:** http://arxiv.org/abs/2401.17547v2

**Citation Count:** 1

**Published Date:** 2024-01-31

![Fig. 1: Motivations of our approach. (a) Even after removing the network layers beneath a certain depth, IP2P [6], a downstream I2I model, still produces a plausible result. (b) By focusing on earlier time steps, a feasible output can be obtained using only five denoising steps.]({{ '/images/01-2024/Diffusion_Model_Compression_for_Image-to-Image_Translation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Large-scale text-to-image (T2I) diffusion models have enabled high-quality results in various downstream image-to-image (I2I) translation tasks. However, their practical use is limited by their massive model size and the high computational latency of the iterative denoising process. The authors identify a gap in existing compression techniques, which are typically task-agnostic and fail to exploit the unique characteristics of I2I tasks. Specifically, in I2I translation, the input image already provides rich structural information, suggesting that the full generative capacity of the large model may be redundant. This paper addresses the need for a compression method tailored specifically for diffusion-based I2I models to reduce both model footprint and latency.

## 2. Key Ideas and Methodology
The paper introduces a novel compression method comprising two simple yet effective components: depth-skip pruning and time-step optimization.

-   **Core Hypothesis:** The authors hypothesize that for I2I tasks, (1) the deeper, coarser layers of the denoising U-Net are less critical since the image structure is already provided by the input condition, and (2) the importance of denoising time steps is biased, with different tasks being more sensitive to either early or late stages of the diffusion process.
-   **Depth-Skip Pruning:** This method reduces the model size by systematically pruning network blocks beyond a certain depth in the U-Net architecture. An efficient "depth-search" algorithm identifies the optimal pruning depth that maintains output quality above a predefined threshold. The pruned model is then fine-tuned to recover performance. This approach assumes the denoising network is based on a U-Net architecture.
-   **Time-step Optimization:** This method reduces latency by finding an optimal, non-uniform sequence of denoising steps. Instead of an exhaustive search, the authors parameterize the time-step schedule using a gamma curve, allowing them to find a biased sequence (favoring early or late steps) by efficiently optimizing a single parameter. This significantly reduces the search time compared to prior work.

The two components are independent and can be applied sequentially to achieve combined reductions in model size and latency.

## 3. Datasets Used / Presented
The method's effectiveness is validated on three representative I2I models and tasks. The datasets were used for fine-tuning the pruned models and for quantitative evaluation:
-   **InstructPix2Pix (IP2P) for Image Editing:** Evaluation was performed following the original paper's protocol.
-   **StableSR for Image Restoration:** Evaluation was performed on the **DIV2K** validation dataset.
-   **ControlNet for Conditional Generation:** The model was fine-tuned on the **COCO** dataset and evaluated on its validation set. For the depth-search process, 100 images were randomly sampled from the training set of each respective task.

## 4. Main Results
The proposed method achieves significant compression and speedup while maintaining satisfactory visual quality.
-   For **InstructPix2Pix**, the model size was reduced by **39.2%** and latency by **81.4%** (from 50 to 10 steps).
-   For **StableSR**, the model size was reduced by **56.4%** and latency by **68.7%** (from 50 to 20 steps).
-   For **ControlNet**, the model size was reduced by **39.2%** and latency by **31.1%** (from 20 to 15 steps).

The authors claim their approach effectively reduces both model size and latency while preserving the generative power required for each task, significantly outperforming previous task-agnostic pruning and time-scheduling methods.

## 5. Ablation Studies
The paper includes several ablation studies to validate its design choices:
-   **Effect of Fine-tuning:** Comparing depth-skip pruning with and without fine-tuning showed that the fine-tuning step is crucial. For StableSR, fine-tuning a pruned model (D8) significantly improved FID, PSNR, and LPIPS scores, allowing it to match the original model's performance with less than half the parameters.
-   **Single- vs. Multi-depth Search:** The proposed simple "single-depth search" was compared to a more complex "multi-depth search" (using different pruning depths for different time steps). The results showed that the single-depth approach finds near-optimal solutions with considerably less search overhead, justifying the simpler strategy.
-   **Time-step Optimization vs. Baselines:** The proposed time-step optimization was compared to prior methods like AutoDiffusion and Xue et al. The proposed method consistently achieved higher quality results (e.g., higher PSNR on all tasks) and was dramatically faster than AutoDiffusion (e.g., requiring minutes of search time vs. tens of hours).
-   **Independence of Components:** An experiment showed that the optimal time-step parameters were nearly identical for both the original and the depth-pruned models. This confirms that depth-skip pruning and time-step optimization are independent and can be performed in any order.

## 6. Paper Figures
![Fig. 2: (a) Depth-skip pruning eliminates all layers deeper than a certain depth level, effectively reducing the model size. (b) Given a fixed number of time steps, our timestep optimization finds differently biased time step sequences for different I2I tasks.]({{ '/images/01-2024/Diffusion_Model_Compression_for_Image-to-Image_Translation/figure_2.jpg' | relative_url }})
![Fig. 3: Qualitative examples of our depth-skip pruning and time-step optimization on IP2P [6], StableSR [71], and ControlNet [80].]({{ '/images/01-2024/Diffusion_Model_Compression_for_Image-to-Image_Translation/figure_3.jpg' | relative_url }})
