---
title: DialogPaint:_A_Dialog-based_Image_Editing_Model
layout: default
date: 2023-03-17
---
![Fig. 1 An example of interactive editing]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current text-to-image models are not well-suited for image editing because they struggle to interpret conversational or ambiguous user instructions (e.g., "change it to something else"). The authors identify a practical need for a more intuitive editing process, as users often prefer to refine an existing image through an interactive, multi-turn dialogue rather than creating a new one from a single, precise prompt. The paper aims to bridge this gap by creating a model that can engage in natural dialogue to clarify user intent and perform iterative image modifications.

## 2. Key Ideas and Methodology
The core idea is to decouple instruction understanding from image manipulation using a two-stage pipeline. The system, named DialogPaint, first uses a dedicated **Dialogue Model** to interact with the user. This model, fine-tuned from the Blender dialogue model, processes the conversational history to resolve ambiguity and generate a clear, explicit editing command. This command is then passed to an **Image Editing Model**, which is built upon the Stable Diffusion (InstructPix2Pix) architecture. This second model executes the precise instruction on the input image. To improve edit quality, the authors introduce an unconditional diffusion guidance mechanism with two separate guidance scales to better balance the influence of the original image and the text-based editing instruction.

## 3. Datasets Used / Presented
The authors constructed two new datasets using a self-instruct methodology with `text-davinci-003`:
*   **Dialogue Dataset**: Contains 10,000 multi-round dialogue samples designed for image editing tasks. It was generated using image captions from CUB-200-2011, COCO, DeepFashion, and FFHQ, and was used to fine-tune the Dialogue Model.
*   **Image Editing Dataset**: Consists of 6,468 pairs of original images, editing instructions, and resulting edited images. The edited images were generated using several existing text-to-image models. This dataset was used to fine-tune the Image Editing Model.

## 4. Main Results
DialogPaint demonstrates strong performance in both dialogue generation and image editing quality.
*   **Objective Metrics**: The model achieves a low Perplexity of 1.578 on dialogue, a Fréchet Inception Distance (FID) of 1.52, and a Precision-Recall Distance (PRD) of 1.56, indicating high-quality and realistic image generation.
*   **Subjective Metrics**: In a user study with 100 participants, the model received a high Mean Opinion Score (MOS) of 4.32 out of 5 for image quality and an overall satisfaction score of 4.22 out of 5.
The key takeaway is that the dialogue-driven framework enables robust, interactive, and multi-turn image editing, successfully handling vague instructions and preserving image details better than baseline models.

## 5. Ablation Studies
Not performed. The paper provides a qualitative comparison against the InstructPix2Pix baseline but does not report ablation experiments that isolate the impact of individual components of the DialogPaint model.

## 6. Paper Figures
![Fig. 2 The processing of dialogue and image editing dataset construction]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_2.jpg' | relative_url }})
![Fig. 3 Example of Dialogue Dataset Construction]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_3.jpg' | relative_url }})
![Fig. 4 Example of Image Editing Dataset]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_4.jpg' | relative_url }})
![Fig. 5 Model Architecture for Dialogue-Based Image Editing]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_5.jpg' | relative_url }})
![Fig. 6 Performance Contrast: DialogPaint vs. InstructPix2Pix with Identical Single-Turn Instructions]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_6.jpg' | relative_url }})
![Fig. 7 Comprehensive Demonstration of DialogPaint’s Multi-Turn Editing Capabilities]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_7.jpg' | relative_url }})
![Fig. 8 Challenging Scenarios for DialogPaint: Illustrative Cases of Imperfect Edits]({{ '/images/03-2023/DialogPaint:_A_Dialog-based_Image_Editing_Model/figure_8.jpg' | relative_url }})
