---
title: PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions
layout: default
date: 2024-09-23
---
![Figure 1: Task Overview of the Omni Pixel-to-Pixel Instruction-tuning Dataset for PixWizard.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the gap in creating a truly versatile visual assistant. Current approaches are either diffusion-based models limited to a narrow set of tasks (e.g., image editing) or in-context learning models that cannot effectively follow open-language instructions. This paper aims to develop a single, unified framework, **PixWizard**, that can perform a comprehensive range of image generation, manipulation, and translation tasks guided by free-form natural language, overcoming the limitations of prior work.

## 2. Key Ideas and Methodology
The core idea is to unify a diverse set of vision tasks into a single image-to-image translation framework. The methodology is built on three pillars:
- **Architecture**: The model uses a flow-based Diffusion Transformer (DiT) as its foundation, initialized from a powerful pre-trained text-to-image model (Lumina-Next-T2I). It is enhanced with both **structural-aware guidance** (using a VAE to preserve image details) and **semantic-aware guidance** (using CLIP embeddings for contextual understanding). A **Task-Aware Dynamic Sampler** is introduced to efficiently select relevant image tokens, reducing computational cost.
- **Data**: The authors curate a large-scale **Omni Pixel-to-Pixel Instruction-Tuning Dataset** to train the model across a wide spectrum of tasks.
- **Training**: A **two-stage training and data-balancing strategy** is employed. The first stage prioritizes tasks with smaller datasets to ensure balanced initial learning. The second stage fine-tunes the model on the entire combined dataset, leading to robust and generalized performance.

## 3. Datasets Used / Presented
The paper presents the **Omni Pixel-to-Pixel Instruction-Tuning Dataset**, a new collection of 30 million image-instruction-image triplets. It is constructed by unifying numerous public and in-house datasets across seven primary domains:
- **Image Generation**: Text-to-image, controllable generation (from Canny, depth, pose, etc.), inpainting, and outpainting.
- **Image Editing**: Object removal, addition, style transfer, etc.
- **Image Restoration**: Denoising, deraining, deblurring, super-resolution, etc.
- **Image Grounding**: Referring segmentation and box detection.
- **Dense Image Prediction**: Depth/normal estimation, semantic segmentation, etc.

For evaluation, the model is tested on standard benchmarks like COCO, gRefCOCO, NYUv2, ADE20K, SIDD, Rain100L, MagicBrush, and Emu Edit.

## 4. Main Results
PixWizard demonstrates strong and versatile performance, often outperforming other general-purpose visual models and remaining competitive with task-specific methods.
- **General Tasks**: In image grounding, it outperforms InstructDiffusion by 4.8 cIoU on RefCOCO. In image restoration, it achieves higher PSNR on deraining (31.43) than generalists like Painter (29.87).
- **Image Generation**: It achieves state-of-the-art results in outpainting (FID of 7.54) and is highly competitive in inpainting (FID of 9.27) and controllable generation.
- **Image Editing**: It achieves performance comparable to the state-of-the-art Emu Edit model and surpasses other baselines like InstructPix2Pix and MagicBrush.

The authors claim that PixWizard is a powerful and interactive visual assistant with strong overall multi-task performance and generalization capabilities to unseen instructions.

## 5. Ablation Studies
The paper reports several ablation studies to validate its design choices:
- **Guidance Mechanisms**: Training with only structural guidance led to poor performance on flexible tasks like editing. Training with only semantic guidance struggled with tasks requiring detail preservation. Combining both was crucial for achieving a balanced, robust performance across all tasks.
- **Dynamic Semantic Token Sampling (DSTS)**: Removing the DSTS module resulted in a minor performance drop but increased computational load and inference time. This confirms its role in improving efficiency without significantly compromising accuracy.
- **Two-Stage Training Strategy**: Training without the two-stage strategy led to a noticeable performance degradation on tasks with smaller datasets (e.g., -1.07 PSNR in deraining, -1.54 cIoU in grounding). This highlights the strategy's importance for balancing learning across diverse task data volumes.

## 6. Paper Figures
![Figure 2: Overall framework of PixWizard.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_2.jpg' | relative_url }})
![Figure 3: The schematic illustrations of PixWizard Block and Task-Aware Dynamic Sampler.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_3.jpg' | relative_url }})
![Figure 4: Qualitative Evaluation of Instruction-based Image Restoration.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative Results of Instruction-based Image Grounding.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_5.jpg' | relative_url }})
![Figure 6: Visualizations of dense image prediction examples.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_6.jpg' | relative_url }})
![Figure 7: Qualitative examples comparing PixWizard with other editing approaches.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_7.jpg' | relative_url }})
![Figure 8: Visualization examples under different conditions.]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_8.jpg' | relative_url }})
![Figure 9: Visualization results of Inpainting , Outpainting and Text-to-Image Generation .]({{ '/images/09-2024/PixWizard:_Versatile_Image-to-Image_Visual_Assistant_with_Open-Language_Instructions/figure_9.jpg' | relative_url }})
