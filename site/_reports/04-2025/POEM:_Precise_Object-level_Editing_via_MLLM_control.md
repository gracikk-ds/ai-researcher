---
title: POEM:_Precise_Object-level_Editing_via_MLLM_control
layout: default
date: 2025-04-10
---
![Fig. 1. POEM. Existing text-based instruction editing methods (top) struggle with precise object-level shape and layout edits. Image interaction-based approaches (middle) perform better but require significant manual user effort. Instead, we propose (bottom) leveraging MLLMs to interpret instructional prompts and automatically generate precise object masks and numerical transformations to support image editing pipelines.]({{ '/images/04-2025/POEM:_Precise_Object-level_Editing_via_MLLM_control/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of precise object-level image editing. Existing text-based methods (e.g., InstructPix2Pix) excel at global style changes but struggle with specific, localized modifications like moving or resizing an object by an exact amount, often causing unintended alterations to the entire image. Conversely, interaction-based methods that use masks or drag-and-drop controls offer high precision but demand significant manual user effort. The paper aims to bridge this gap by creating a framework that achieves the high accuracy of interaction-based methods through simple, text-based instructions, thus minimizing manual intervention.

## 2. Key Ideas and Methodology
The core idea is to decouple the complex task of visual reasoning from the image generation process. The paper introduces **POEM (Precise Object-level Editing via MLLM control)**, a multi-stage pipeline that uses Multimodal Large Language Models (MLLMs) to interpret user commands and generate precise editing parameters.

The methodology consists of two main stages:
1.  **Reasoning Stage:** An MLLM first analyzes the input image and text prompt to identify objects and their locations (visual grounding). These initial detections are refined into precise segmentation masks using Grounded-SAM. A separate, math-proficient LLM then parses the instruction, scene context, and object coordinates to compute an exact affine transformation matrix (e.g., for scaling, rotation, translation).
2.  **Editing Stage:** The computed transformation is applied to the initial object mask to create a target mask. A pre-trained diffusion model is then guided by both the original and target masks to synthesize the final image, modifying only the specified object while preserving the background and overall visual coherence.

## 3. Datasets Used / Presented
The authors introduce **VOCEdits**, a new benchmark dataset designed specifically for evaluating precise, object-level image editing.
*   **Source:** It is built upon the PASCAL VOC 2012 dataset.
*   **Content:** The dataset contains 3,030 unique samples derived from 505 images. Each sample includes an image, a natural language instructional prompt (e.g., "make the cat 30% larger"), a ground-truth transformation matrix, and the corresponding object segmentation masks before and after the transformation.
*   **Usage:** It is used to quantitatively evaluate the framework's ability to perform accurate detection, transformation, and image synthesis.

## 4. Main Results
POEM's performance was evaluated on the VOCEdits dataset and compared against state-of-the-art text-based editing models. The primary metric was the Intersection over Union (IoU) between the final edited object's mask and the ground-truth target mask.
*   POEM achieved an average IoU of **38.4%**.
*   This result surpassed other leading methods, including IP2P (34.4%), TurboEdit (33.8%), and LEDITS++ (35.0%).
*   The authors claim that POEM produces more faithful and precise edits, particularly for translation and scaling operations, demonstrating the effectiveness of its MLLM-guided reasoning pipeline.

## 5. Ablation Studies
The paper systematically evaluates each component of the POEM pipeline:
*   **Visual Grounding:** The QwenVL-7B model was chosen for object detection, as it achieved a 55.5% bounding box IoU, significantly outperforming InternVL-8B (17.4%).
*   **Detection Refinement:** Using Grounded-SAM to refine object masks dramatically improved segmentation IoU from 27.3% (with a standard SAM) to 84.2%, confirming its superior accuracy.
*   **Edit Operation Parsing:** The QwenMath LLM, which uses external tools for calculation, proved far more effective at computing transformation matrices (49.2% transformed mask IoU) compared to the DeepSeek model (25.3% IoU).
*   **Impact of Segmentation Error:** By providing the parsing step with a perfect "oracle" mask instead of a predicted one, the transformed mask IoU increased from 49.2% to 55.6%. This shows that while the transformation logic is the main source of error, initial segmentation quality also plays a role.

## 6. Paper Figures
![Fig. 2. Overview of our approach. An image and a user edit prompt are fed into the reasoning stage, where we analyze the scene and extract object-level masks and precise transformation parameters for appearance and shape edits. During the editing stage, we apply these edits during inference without any additional training or fine-tuning.]({{ '/images/04-2025/POEM:_Precise_Object-level_Editing_via_MLLM_control/figure_2.jpg' | relative_url }})
![Fig. 3. Detailed pipeline of POEM. Given an image and an edit prompt, we first use an MLLM to analyze the scene and identify objects. Then, we refine the detections and enhance object masks using Grounded SAM. Next, we use a text-based LLM to predict the transformation matrix of the initial segmentation mask. Finally, we perform an image-to-image translation guided by the previous steps to generate the edited image. This structured pipeline enables precise object-level editing with high visual fidelity while preserving spatial and visual coherence.]({{ '/images/04-2025/POEM:_Precise_Object-level_Editing_via_MLLM_control/figure_3.jpg' | relative_url }})
![Fig. 5. Qualitative results. We compare POEM with state-of-the-art image editing models across a diverse set of edit instructions, including geometric transformations (e.g., translation, scaling), appearance changes, and combinations of both. The specific prompts used are “Scale the bus by 0.56" , “Move the pear left by 150px and make it red" , “Scale the mug only vertically to 200px" , “Make the sword gold" , “Scale the orange by 2 and move it left by 150px" , and “Move the ball left by 90px and make it blue" .]({{ '/images/04-2025/POEM:_Precise_Object-level_Editing_via_MLLM_control/figure_5.jpg' | relative_url }})
