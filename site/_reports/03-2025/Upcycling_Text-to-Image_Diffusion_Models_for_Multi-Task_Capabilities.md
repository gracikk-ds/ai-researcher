---
title: Upcycling_Text-to-Image_Diffusion_Models_for_Multi-Task_Capabilities
layout: default
date: 2025-03-14
---
## Upcycling Text-to-Image Diffusion Models for Multi-Task Capabilities
**Authors:**
- Ruchika Chavhan, h-index: 5, papers: 18, citations: 82
- Sourav Bhattacharya, h-index: 3, papers: 14, citations: 25

**ArXiv URL:** http://arxiv.org/abs/2503.11905v1

**Citation Count:** None

**Published Date:** 2025-03-14

![Figure 1. A chatbot showcasing a potential use case of Multi-Task Upcycling. Our approach efficiently upcycles pre-trained text-to-image models, enabling them to perform multiple image generation tasks using a single backbone.]({{ '/images/03-2025/Upcycling_Text-to-Image_Diffusion_Models_for_Multi-Task_Capabilities/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of adapting large, pre-trained text-to-image (T2I) diffusion models to support multiple downstream tasks (e.g., image editing, super-resolution, inpainting). Current methods for creating such multi-task models either require resource-intensive retraining of the entire model or significantly increase the parameter count and computational load by adding new components. This makes them inefficient and unsuitable for deployment on resource-constrained platforms like edge devices. The paper aims to bridge this gap by introducing an efficient method to "upcycle" a single-task T2I model into a versatile, multi-task model without inflating its size or computational cost.

## 2. Key Ideas and Methodology
The core of the paper is **Multi-Task Upcycling (MTU)**, a method inspired by two key insights: (1) an empirical finding that the Feed-Forward Network (FFN) layers of a diffusion model undergo the most significant changes when fine-tuned for a new task, and (2) the concept of Mixture-of-Experts (MoE) from Large Language Model literature.

The methodology involves the following steps:
1.  The FFN layers in a pre-trained T2I model (like Stable Diffusion) are replaced with a set of smaller FFNs, called "experts." The size and number of these experts are chosen to keep the total parameter count similar to the original model.
2.  A lightweight "router" network is introduced. For any given task, the router takes a learnable task-specific embedding as input and dynamically computes weights to combine the outputs of the experts.
3.  Task-specific input layers and layer normalization modules are added to handle varying input data (e.g., image conditioning) and stabilize training across different task distributions.
4.  During training, only the newly added components (experts, router, and task-specific layers) are updated, while the vast majority of the original model's parameters remain frozen. This makes the upcycling process highly parameter-efficient.

## 3. Datasets Used / Presented
The method was trained and evaluated on a combination of datasets, each corresponding to a specific task:
*   **Text-to-Image (T2I):** The COCO Captions dataset was used to maintain the model's original text-to-image generation capabilities.
*   **Image Editing (IE):** The InstructPix2pix dataset, which contains input images, editing instructions, and corresponding target images.
*   **Super-Resolution (SR):** The Real-ESRGAN dataset, consisting of high-resolution images from which lower-resolution counterparts were generated for training.
*   **Image Inpainting (IP):** A dataset based on GQA, providing images with text prompts for object removal.

## 4. Main Results
The primary result is that the MTU framework successfully creates a single model that performs on par with, and in some cases surpasses, specialized single-task models, all while maintaining the same computational footprint (TFLOPs) as the original base model.
*   For the SDv1.5 base model, MTU outperforms the single-task baseline in Image Editing (I-T Directional Similarity of 17.2 vs. 15.4) and Super-Resolution (LPIPS of 24.8 vs. 38.0).
*   For the larger SDXL model, MTU achieves a state-of-the-art FID score of 3.9 on T2I generation, slightly better than the original SDXL's 4.1, while simultaneously handling three other tasks.
The authors claim that MTU is the first framework to seamlessly blend multi-task learning with on-device compatibility for diffusion models.

## 5. Ablation Studies
The authors conducted several ablation studies to validate their design choices:
*   **Number of Experts:** The performance was tested with a varying number of experts (1, 2, 4, 8, 16). For the SDv1.5 model, using 4 experts yielded the best results, while performance degraded with more (and therefore smaller) experts. For the larger SDXL model, a single expert (i.e., fine-tuning the FFN block with task-specific normalization) was optimal, suggesting that splitting the FFN is not always necessary for larger models.
*   **Comparison with PEFT Methods:** MTU was compared against standard parameter-efficient fine-tuning methods like LoRA and IA3 applied to the FFN layers. MTU consistently and significantly outperformed both across all tasks, demonstrating its superior ability to support multi-task learning. For example, on SDXL, MTU scored 20.1 on image editing, while IA3 scored only 8.4.
*   **Router Weight Analysis:** An analysis of the router's expert assignments showed that it learns to specialize experts for different tasks. For instance, one expert was primarily used for Super-Resolution, while others were shared between T2I and Image Editing, validating the effectiveness of the dynamic routing mechanism.

## 6. Paper Figures
![Figure 2. We analyze the deviation between fine-tuned weights θ τ f and pre-trained initialization θ p across different layers in the LDM (i.e., Φ τ = || θ τ f − θ p || ) and rank them accordingly. We present the average rank of these deviations across all tasks. The x-axis represents layer depth, while the y-axis indicates the component type. FFN layers show the highest deviation, suggesting they specialize in adapting to downstream tasks.]({{ '/images/03-2025/Upcycling_Text-to-Image_Diffusion_Models_for_Multi-Task_Capabilities/figure_2.jpg' | relative_url }})
![Figure 3. (a) Overview: We introduce Multi-task Upcycling (MTU), a method for transforming a pre-trained text-to-image model to support multiple tasks. (b) In MTU, we replace the FFN layer in the pre-trained model with a set of smaller experts, which are dynamically combined using a router mechanism.]({{ '/images/03-2025/Upcycling_Text-to-Image_Diffusion_Models_for_Multi-Task_Capabilities/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative comparison of MTU based on SDv1.5 (left) and SDXL (right) with corresponding single-task baselines for Image Editing (IE) ( Brooks et al. , 2023 ), Super Resolution (SR) ( Rombach et al. , 2022 ), and Inpainting (IP). ( Yildirim et al. , 2023 )]({{ '/images/03-2025/Upcycling_Text-to-Image_Diffusion_Models_for_Multi-Task_Capabilities/figure_4.jpg' | relative_url }})
![Figure 5. Analysis for expert selection by the router. We show the expert weight distribution assigned by the router for SDv1.5 with four experts (N = 4).]({{ '/images/03-2025/Upcycling_Text-to-Image_Diffusion_Models_for_Multi-Task_Capabilities/figure_5.jpg' | relative_url }})
