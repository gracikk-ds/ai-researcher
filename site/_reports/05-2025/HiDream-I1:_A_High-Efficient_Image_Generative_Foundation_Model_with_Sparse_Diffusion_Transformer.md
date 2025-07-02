---
title: HiDream-I1:_A_High-Efficient_Image_Generative_Foundation_Model_with_Sparse_Diffusion_Transformer
layout: default
date: 2025-05-28
---
## HiDream-I1: A High-Efficient Image Generative Foundation Model with Sparse Diffusion Transformer
**Authors:**
- Qi Cai
- Tao Mei

**ArXiv URL:** http://arxiv.org/abs/2505.22705v1

**Citation Count:** 0

**Published Date:** 2025-05-28

![Figure 1 | Generated images by HiDream-I1.]({{ '/images/05-2025/HiDream-I1:_A_High-Efficient_Image_Generative_Foundation_Model_with_Sparse_Diffusion_Transformer/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the critical trade-off in modern image generative foundation models, where advancements in image quality have often come at the cost of increased computational complexity and high inference latency. This makes real-time, cost-effective deployment a significant challenge. The paper aims to bridge this gap by creating a highly efficient yet state-of-the-art generative model.

## 2. Key Ideas and Methodology
The core of the research is **HiDream-I1**, a 17B parameter model built on a novel **sparse Diffusion Transformer (DiT)** architecture. This architecture uses a dynamic **Mixture-of-Experts (MoE)** system to efficiently manage computational load while maintaining high capacity. The model first uses a dual-stream structure to independently process image and text tokens, then transitions to a single-stream for multi-modal interaction. Text understanding is enhanced by a hybrid encoding module using four different text encoders (CLIP-L/G, T5-XXL, Llama 3.1).

To improve inference speed, the full model is distilled into faster variants (HiDream-I1-Dev and -Fast) using a GAN-powered distillation technique, which preserves sharpness and detail. The framework is also extended to an instruction-based image editor (**HiDream-E1**) and a comprehensive conversational agent (**HiDream-A1**).

## 3. Datasets Used / Presented
- **Training Data**: A large-scale dataset was curated from a mix of public web-sourced data and internal copyrighted images. This data underwent a rigorous pre-processing pipeline involving deduplication (removing ~20% of images), multi-faceted filtering (for safety, aesthetics, and technical quality), and automated annotation using the MiniCPM-V 2.6 Vision-Language Model.
- **Editing Data**: The HiDream-E1 editor was fine-tuned on a dataset of 5 million triplets, each containing a source image, an editing instruction, and the corresponding target image.
- **Evaluation Benchmarks**: The models were evaluated on DPG-Bench and GenEval for prompt adherence and compositionality, HPSv2.1 for human preference, and EmuEdit/ReasonEdit for instruction-based editing performance.

## 4. Main Results
HiDream-I1 demonstrated state-of-the-art performance across multiple benchmarks.
- **Prompt Adherence**: It achieved the top overall scores on DPG-Bench (85.89%) and GenEval (0.83), outperforming models like SD3-Medium and DALL-E 3, and showing particular strength in rendering complex relationships and compositions.
- **Human Preference**: On the HPSv2.1 benchmark, HiDream-I1 obtained the highest average score (33.82) and ranked first in all tested styles (Animation, Concept Art, Painting, Photo).
- **Image Editing**: The HiDream-E1 model also secured the leading scores on both the EmuEdit (6.40) and ReasonEdit (7.54) benchmarks, validating its effectiveness in precise, instruction-based editing.

The authors claim that HiDream-I1 and its extensions provide a powerful, efficient, and open-source framework for interactive visual content creation.

## 5. Ablation Studies
Not performed.

## 6. Paper Figures
![Figure 2 | Pipeline of data pre-processing.]({{ '/images/05-2025/HiDream-I1:_A_High-Efficient_Image_Generative_Foundation_Model_with_Sparse_Diffusion_Transformer/figure_2.jpg' | relative_url }})
![Figure 3 | Overall framework of the HiDream-I1 model.]({{ '/images/05-2025/HiDream-I1:_A_High-Efficient_Image_Generative_Foundation_Model_with_Sparse_Diffusion_Transformer/figure_3.jpg' | relative_url }})
