---
title: SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models
layout: default
date: 2023-12-11
---
## SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models
**Authors:**
- Yuzhou Huang
- Ying Shan

**ArXiv URL:** http://arxiv.org/abs/2312.06739v1

**Citation Count:** 77

**Published Date:** 2023-12-11

![Figure 1. We propose SmartEdit, an instruction-based image editing model that leverages Multimodal Large Language Models (MLLMs) to enhance the understanding and reasoning capabilities of instruction-based editing methods. With the specialized design, our SmartEdit is capable of handling complex understanding (the instructions that contain various object attributes like location, relative size, color, and in or outside the mirror) and reasoning scenarios.]({{ '/images/12-2023/SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current instruction-based image editing models, such as InstructPix2Pix, often fail when given complex instructions. This failure stems from their reliance on simple CLIP text encoders, which lack the sophisticated understanding and reasoning capabilities required for complex tasks. The authors identify two main failure scenarios: 1) **Complex Understanding**, where an instruction refers to an object by specific attributes like location (e.g., "leftmost apple"), relative size, or context (e.g., "the dog in the mirror"), and 2) **Complex Reasoning**, where world knowledge is needed to identify the target object (e.g., "remove the object that can tell the time"). The paper aims to address this gap by creating a model that can robustly handle such instructions.

## 2. Key Ideas and Methodology
The core idea of SmartEdit is to replace the simple text encoder with a powerful **Multimodal Large Language Model (MLLM)**, specifically LLaVA, to leverage its advanced language understanding and reasoning abilities.

To effectively integrate the MLLM with the diffusion model, the authors introduce a **Bidirectional Interaction Module (BIM)**. Standard methods often have a unidirectional information flow where text features modulate image features. The BIM, however, enables a comprehensive, two-way interaction. It takes the instruction-derived features from the MLLM and the image features from a visual encoder and uses a series of cross-attention blocks to allow them to query and enrich each other. The resulting refined text and image features are then injected into the UNet of the latent diffusion model to guide the editing process.

## 3. Datasets Used / Presented
**Training Datasets:** SmartEdit is trained on a diverse collection of data to build both perceptual and reasoning skills.
- **Editing Datasets:** Standard datasets like InstructPix2Pix and MagicBrush.
- **Perception Datasets:** Segmentation datasets (COCO-Stuff, RefCOCO, etc.) to enhance the model's understanding of object position and concepts.
- **VQA Dataset:** LLaVA-Instruct-150k to align the MLLM.
- **Author-Synthesized Dataset:** A small, high-quality dataset of 476 paired examples created specifically for complex understanding and reasoning scenarios to "stimulate" the model's advanced capabilities.

**Evaluation Dataset:** The authors introduce a new benchmark called **Reason-Edit**.
- It contains 219 image-text pairs specifically designed to test complex understanding and reasoning scenarios.
- There is no overlap between Reason-Edit and the training data.

## 4. Main Results
On the newly proposed Reason-Edit benchmark, SmartEdit significantly outperforms previous state-of-the-art methods.
- Using the authors' proposed manual evaluation metric, **Instruction-Alignment (Ins-align)**, SmartEdit-13B achieves a score of **81.7%** on reasoning tasks. This is a substantial improvement over the next-best model, InstructDiffusion, which scored only **48.3%**.
- Qualitatively, SmartEdit successfully edits images based on complex instructions involving relative positions, reasoning about object functions, and mirrored reflections, whereas other methods fail to understand the instruction or produce low-quality edits.
- The authors claim that SmartEdit paves the way for the practical application of complex, instruction-based image editing by successfully integrating the reasoning power of MLLMs into the generative process.

## 5. Ablation Studies
The authors conducted several ablation studies to validate their design choices.

- **Bidirectional Interaction Module (BIM):** The importance of the BIM was tested by comparing the full model against two variants: 1) a "plain" version with no BIM, and 2) a "SimpleCA" version with only unidirectional attention. Removing the BIM entirely caused a significant performance drop (Ins-align on reasoning tasks fell from 78.9% to 69.4%). The unidirectional version also performed worse (72.2%), confirming that the bidirectional interaction is crucial for effectively fusing image and text information.

- **Dataset Utilization:** The study validated the proposed data strategy.
    - Training with only **editing data** resulted in poor performance (Ins-align ~23% on reasoning).
    - Adding **segmentation data** improved results (Ins-align ~31%), enhancing perceptual understanding.
    - Adding the **synthetic complex data** provided a larger boost, especially for reasoning (Ins-align ~57%).
    - The best performance was achieved when training on **all datasets combined** (Ins-align ~79%), demonstrating that the perception-focused and reasoning-focused datasets play complementary and essential roles.

## 6. Paper Figures
![Figure 2. For more complex instructions or scenarios, InstructPix2Pix fails to follow the instructions.]({{ '/images/12-2023/SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models/figure_2.jpg' | relative_url }})
![Figure 3. The overall framework of SmartEdit. For the instruction, we first append the r [IMG] tokens to the end of instruction c . Together with image x , they will be sent into LLaVA, which can then obtain the hidden states corresponding to these r [IMG] tokens. Then the hidden state is sent into the QFormer and gets feature f . Subsequently, the image feature v output by the image encoder E ϕ interacts with f through a bidirectional interaction module (BIM), resulting in f ′ and v ′ . The f ′ and v ′ are input into the diffusion models to achieve the instruction-based image editing task.]({{ '/images/12-2023/SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models/figure_3.jpg' | relative_url }})
![Figure 4. The network design of the BIM Module. In this module, the input information f and v will undergo bidirectional information interaction through different cross-attention.]({{ '/images/12-2023/SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models/figure_4.jpg' | relative_url }})
![Figure 5. Qualitative comparison on Reason-Edit. When compared to several existing instruction-based image editing methods that have undergone further fine-tuning on our synthetic editing dataset, our approach demonstrates superior editing capabilities in complex scenarios.]({{ '/images/12-2023/SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models/figure_5.jpg' | relative_url }})
![Figure 6. The effectiveness of the BIM Module.]({{ '/images/12-2023/SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models/figure_6.jpg' | relative_url }})
![Figure 7. The significance of joint training with multiple datasets.]({{ '/images/12-2023/SmartEdit:_Exploring_Complex_Instruction-based_Image_Editing_with_Multimodal_Large_Language_Models/figure_7.jpg' | relative_url }})
