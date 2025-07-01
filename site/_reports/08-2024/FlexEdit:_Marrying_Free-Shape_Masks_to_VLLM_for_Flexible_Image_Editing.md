---
title: FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing
layout: default
date: 2024-08-22
---
![Figure 1: Free-shape mask can simplify the user input when dealing with location related instruction, and more flexible for user input. The compared methods are SmartEdit and Largen respectively.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of providing precise and intuitive instructions for image editing. Language-only instructions can be ambiguous, especially for specifying locations, leading to incorrect edits. While masks can specify locations accurately, traditional methods require users to draw precise, complete masks, which is difficult and not user-friendly. This paper tackles the problem of how to make image editing more flexible by enabling models to understand imprecise, "free-shape" masks (like scribbles or simple shapes) drawn by users, combined with natural language commands.

## 2. Key Ideas and Methodology
The core idea of the paper is to create an end-to-end editing model, **FlexEdit**, that can interpret a combination of a source image, a free-shape mask, a subject image (optional), and a text instruction.

-   **Core Principle:** The model leverages a Vision Large Language Model (VLLM) to comprehend the complex, multi-modal user input. The VLLM is trained to understand that a free-shape mask is a positional cue that refers to a larger, complete object or area.
-   **Model Architecture:** The FlexEdit framework consists of three main parts:
    1.  A **VLLM backbone** (LLaVA) processes all inputs (images, mask, text) and generates hidden states that represent the editing intent.
    2.  A **Q-Former** refines these hidden states into embeddings compatible with a diffusion model.
    3.  A novel **Mask Enhanced Adapter (MEA)** module fuses the VLLM's instruction embedding with visual features from the scene and subject images. The MEA uses cross-attention mechanisms to enrich the instruction with fine-grained image details, enhancing the diffusion model's ability to perform the edit accurately.
-   **Training Strategy:** The model is trained not just on editing tasks but also on segmentation tasks where it learns to predict a full object mask from a free-shape mask input. This explicitly teaches the model to infer the user's true intention from an imprecise drawing.

## 3. Datasets Used / Presented
The authors introduce a new benchmark and use several existing datasets for training.

-   **FSMI-Edit (Free-Shape Mask Instruction Edit) Benchmark (Presented):** A new benchmark created by the authors to evaluate editing performance with free-shape masks. It consists of 80 single-image and 125 multiple-image editing scenarios. It includes 8 distinct types of free-shape masks (circle, rectangle, triangle, irregular, each with solid and open-hole variants) to mimic diverse user inputs.
-   **Training Datasets (Used):** The model is trained on a mixture of four data categories:
    1.  **Segmentation Datasets:** Modified versions of COCO and GRefCOCO, used to train the model to understand the relationship between free-shape masks and full object masks.
    2.  **Image Editing Datasets:** Adapted data from MagicBrush, ReasonEdit, and STRAT.
    3.  **Visual Question Answering (VQA) Dataset:** Mimic-it, used to preserve the model's reasoning capabilities.
    4.  **Self-Constructed Dataset:** 390 image pairs with complex instructions and free-shape masks created by the authors.

## 4. Main Results
FlexEdit demonstrates state-of-the-art performance in both single and multiple image editing tasks, especially under the challenging free-shape mask setting.

-   **Multiple Image Editing:** In the free-shape mask setting (Table 1), FlexEdit outperforms baselines like AnyDoor and Largen. For instance, it achieves the highest foreground CLIP-T score (22.48) and DINOv2 score (0.2908), indicating better alignment with text instructions and visual features compared to other models.
-   **Single Image Editing:** FlexEdit surpasses methods like InstructPix2Pix and SmartEdit (Table 2). It achieves the best scores across all metrics: PSNR (22.81), SSIM (0.77), LPIPS (0.073), and CLIP-T (20.71), showing superior image quality and instruction following.
-   **Author-claimed Impact:** The authors conclude that FlexEdit significantly advances intelligent image editing by successfully combining the strengths of VLLMs and diffusion models, providing a user-friendly and highly capable solution that can robustly interpret imprecise user inputs.

## 5. Ablation Studies
The authors performed ablation studies to validate the effectiveness of the key components within their Mask Enhanced Adapter (MEA) module (Tables 3 & 4).

-   **Experiment 1: Role of Cross Attention (CA):** They removed the cross-attention layer that fuses scene image features with the VLLM's output. In multiple image editing, this removal caused a performance drop across all metrics (e.g., foreground CLIP-T decreased from 22.44 to 21.62), demonstrating that direct interaction with the scene image is crucial.
-   **Experiment 2: Role of Decouple Cross Attention (DCA):** They replaced the specialized "decouple" cross-attention (which processes scene and subject features separately) with a general cross-attention mechanism. This also led to a performance degradation, confirming that the decoupled design is more effective for integrating features.
-   **Overall Impact:** The full model with both CA and DCA performed the best in both single and multiple image editing tasks. Removing either component resulted in a noticeable decline in performance, confirming that each part of the MEA design contributes positively to the model's final output quality.

## 6. Paper Figures
![Figure 2: FlexEdit support both (a) single image and (b) multiple image editing, including replace/add an object. The free-shape mask input indicate the localization information, highly user-friendly than asking user to input full mask.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: The architecture of the FlexEdit framework. FlexEdit integrates visual prompts and human instructions for complex image editing. It utilizes a VLLM backbone for multi-modal instruction understanding, a Q-Former for refining the hidden states, and a Mask Enhanced Adapter (MEA) for merging image and language model outputs. The final image generation is achieved through a diffusion model.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: We train model to understand free-shape mask by having it predict the full mask from a given free-form mask. The picture shows two examples of this process.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative results for free-shape mask guided image editing in multiple image setting. We compare the subject image with no background and complex background.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Qualitative results comparison on single image edit.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7: Example of the different types of the free-shape mask from FSMI-Edit benchmark.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_7.jpg' | relative_url }})
![Figure 8: In the multiple images editing datasets creation process, we use Adobe Photoshop to extract the full mask from the result image, then redraw the mask in different shape, and write prompts based on the task to serve as input instructions.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_8.jpg' | relative_url }})
![Figure 9: In the single image editing datasets creation process, we use Adobe Photoshop to draw different shaped masks in specified areas of the scene image [pic1] based on the task requirements. Then we write prompts based on the task to serve as input instructions.]({{ '/images/08-2024/FlexEdit:_Marrying_Free-Shape_Masks_to_VLLM_for_Flexible_Image_Editing/figure_9.jpg' | relative_url }})
