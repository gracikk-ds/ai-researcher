---
title: LayerDiff:_Exploring_Text-guided_Multi-layered_Composable_Image_Synthesis_via_Layer-Collaborative_Diffusion_Model
layout: default
date: 2024-03-18
---
## LayerDiff: Exploring Text-guided Multi-layered Composable Image Synthesis via Layer-Collaborative Diffusion Model
**Authors:**
- Runhui Huang
- Hang Xu

**ArXiv URL:** http://arxiv.org/abs/2403.11929v1

**Citation Count:** None

**Published Date:** 2024-03-18

![Fig. 1: An examples of the multi-layered composable image. The multi-layered composable image includes a background layer, a set of foreground layers and the corresponding layer masks. The layer images, layer masks and the layer prompts with the same color are belonging to the same layer. The text-guided multi-layered composable image synthesis is aimed to generate the layer images and layer masks simultaneously under the guidance of global prompt to control the holistic content, and the layer prompts to control the per layer’s content. It’s able to composite a whole image by assembling these layers according to the masks.]({{ '/images/03-2024/LayerDiff:_Exploring_Text-guided_Multi-layered_Composable_Image_Synthesis_via_Layer-Collaborative_Diffusion_Model/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Standard text-to-image diffusion models generate high-quality but monolithic (single-layer) images. This approach limits their utility in real-world applications like professional graphic design and digital art, where images are typically created and manipulated as a composition of multiple, independent layers to afford greater flexibility and control. The authors address this gap by proposing a method for text-guided, multi-layered, composable image synthesis, allowing for the generation and manipulation of individual objects and the background as distinct layers.

## 2. Key Ideas and Methodology
The core of the paper is **LayerDiff**, a novel layer-collaborative diffusion model designed to generate a background layer, a set of foreground layers, and their corresponding masks simultaneously. The model is guided by both a global text prompt describing the entire scene and layer-specific prompts for each element.

The key methodological contributions are:
*   **Layer-Collaborative Attention Block**: This new block is integrated into the UNet architecture. It consists of an **inter-layer attention module** to capture dependencies and ensure coherence across layers, and a **text-guided intra-layer attention module** to inject layer-specific text prompts, thereby controlling the content of each individual layer.
*   **Layer-Specific Prompt Enhancer**: This module enriches the layer-specific prompts by integrating contextual information from the global prompt, leading to more accurate and detailed layer generation.
*   **Self-Mask Guidance (SMG) Sampling**: A novel sampling strategy that leverages the model's predicted layer masks during the denoising process to guide the generation, improving the quality and definition of content within each layer.
*   **Data Construction Pipeline**: The authors designed a pipeline that uses existing models for captioning (InstructBLIP), segmentation (DetCLIP+SAM), and inpainting (Stable Diffusion) to automatically create a large-scale dataset for training multi-layer generative models.

## 3. Datasets Used / Presented
The authors introduce a new dataset named **MLCID (Multi-Layered Composable Image Dataset)**.
*   **Size**: Approximately 2 million multi-layered image-text pairs, sourced from LAION-400M and a private dataset.
*   **Composition**: The dataset is long-tailed, containing 1.7M two-layer, 0.3M three-layer, and 0.08M four-layer images. Each data point includes a global prompt, layer-specific prompts, and the corresponding layer images and masks.
*   **Usage**: It was used to train and evaluate the LayerDiff model. A distinct test set of 27k samples was created using the same pipeline.

## 4. Main Results
*   LayerDiff demonstrates the ability to generate high-quality, multi-layered images. For two-layer synthesis, its performance is comparable to the monolithic image generation of Stable Diffusion v1.5 (FID of 25.9 for LayerDiff+SMG vs. 27.0 for SDv1.5).
*   The model enables a range of controllable applications without requiring fine-tuning, such as layer-specific image editing (inpainting) and style transfer, by manipulating the prompts and noise of individual layers.
*   The authors note that performance on three- and four-layer images is weaker, which they attribute to the limited amount of training data for these more complex compositions in the current MLCID dataset.

## 5. Ablation Studies
The authors conducted several ablation studies to validate the contributions of their proposed components:
*   **Layer-Specific Guidance**: Removing the intra-layer attention and layer-specific prompts caused a catastrophic drop in performance (FID for two-layer images increased from ~54 to ~358), proving that layer-specific guidance is essential for coherent multi-layer generation.
*   **Layer-Specific Prompt Enhancer**: Adding the enhancer module consistently improved FID scores, demonstrating its effectiveness in refining the textual guidance for each layer.
*   **Self-Mask Guidance (SMG)**: The proposed SMG sampling method was shown to be superior to both standard classifier-free guidance (CFG) and Self-Attention Guidance (SAG). SMG improved the overall FID from 112.8 (CFG) to 88.9 on a 1k-sample test set, confirming its ability to enhance generation quality.

## 6. Paper Figures
![Fig. 2: Overall architecture of the proposed LayerDiff. LayerDiff performs the multilayered composable image synthesis by generating the layer images and layer masks simultaneously under the guidance of both the global prompt and layer prompts. The layer-specific prompt enhancer ensures the layer text conditions to guide the content generation in each layer. In the layer collaborative diffusion model, the layercollaborative attention block learns the cross-layer relationship and injects the text guidance signal into the model.]({{ '/images/03-2024/LayerDiff:_Exploring_Text-guided_Multi-layered_Composable_Image_Synthesis_via_Layer-Collaborative_Diffusion_Model/figure_2.jpg' | relative_url }})
![Fig. 4: Pipeline of the Multi-Layered Composable Image Construction. We use the InstructBLIP [5] for image captioning. These prompts guide open-set segmentation via DetCLIP+SAM to produce image layers and masks and the background image is refined by using the Stable Diffusion inpainting model [26].]({{ '/images/03-2024/LayerDiff:_Exploring_Text-guided_Multi-layered_Composable_Image_Synthesis_via_Layer-Collaborative_Diffusion_Model/figure_4.jpg' | relative_url }})
