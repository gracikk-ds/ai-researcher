---
title: ACE++:_Instruction-Based_Image_Creation_and_Editing_via_Context-Aware_Content_Filling
layout: default
date: 2025-01-05
---
## ACE++: Instruction-Based Image Creation and Editing via Context-Aware Content Filling
**Authors:**
- Chaojie Mao, h-index: 8, papers: 11, citations: 272
- Jingren Zhou, h-index: 9, papers: 11, citations: 494

**ArXiv URL:** http://arxiv.org/abs/2501.02487v3

**Citation Count:** 21

**Published Date:** 2025-01-05

![Figure 1: The illustration of ACE++ framework. The input paradigm of LCU++ is tokenized according to the respective methods of the editor and the creator, achieving different functional suites through full or partial fine-tuning.]({{ '/images/01-2025/ACE++:_Instruction-Based_Image_Creation_and_Editing_via_Context-Aware_Content_Filling/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of creating a universal image editing model that can handle a wide variety of tasks, from creation to complex editing, based on user instructions. While powerful foundational text-to-image models like FLUX.1-dev exist, adapting them for diverse editing tasks is inefficient. The primary issue is the discrepancy between the input format of standard text-to-image generation and the multimodal inputs required for editing (e.g., reference images, masks). This mismatch leads to slow convergence and high adaptation costs when fine-tuning these foundational models. The paper aims to create a framework that efficiently leverages the generative priors of these models for a broad set of instruction-based editing and creation tasks.

## 2. Key Ideas and Methodology
The core of the paper is ACE++, a framework built upon the FLUX.1-dev diffusion transformer. Its methodology is defined by two key contributions:

*   **LCU++ (Improved Long-context Condition Unit):** This is an enhanced input paradigm that modifies how conditional information (like an input image and its corresponding mask) is fed into the model. Instead of concatenating these inputs with the text tokens along the sequence dimension (as in the original ACE), LCU++ concatenates them with the noisy latent image along the *channel dimension*. This approach is more efficient as it avoids increasing the sequence length for the attention mechanism and is less disruptive to the context perception learned during the model's original text-to-image pre-training.

*   **Two-Stage Training Scheme:** To minimize fine-tuning efforts, the authors propose a two-stage process.
    1.  **Stage 1 (Single-Condition Pre-training):** The base text-to-image model is first adapted using tasks that do not require a reference image (0-ref tasks), such as inpainting. This stage familiarizes the model with channel-wise conditional inputs. The authors note that existing specialized models like FLUX.1-Fill-dev can serve as a pre-trained starting point for this stage.
    2.  **Stage 2 (Multi-condition Fine-tuning):** The model from Stage 1 is then fine-tuned on a comprehensive dataset including all task types (0-ref and N-ref) to enable it to follow general, multi-modal instructions.

The training objective is also designed to be context-aware, with a loss function that separately computes the reconstruction loss for reference inputs and the generation loss for the target output.

## 3. Datasets Used / Presented
The paper does not introduce a new dataset. Instead, it utilizes the existing dataset collected for the original **ACE (Han et al., 2024a)** paper. This dataset is designed for multi-task, instruction-based image generation and editing, covering eight categories of tasks such as controllable generation, inpainting, single-image editing, reference-based generation, and editing. The framework is trained on this diverse data to achieve its all-round capabilities.

## 4. Main Results
The paper's evaluation is entirely qualitative, presented through extensive visual examples. The key results demonstrate ACE++'s proficiency across a wide spectrum of tasks:
*   **Reference-based Generation:** The model successfully generates new images while maintaining the identity of a subject (e.g., a cartoon duck, a specific person) in various scenes, styles, and contexts (Figures 3 & 4).
*   **Local and General Editing:** ACE++ performs high-quality local editing, such as inpainting, object removal, and colorization, while preserving the surrounding image structure (Figure 5). It also handles flexible, open-ended instructions for global changes like altering the scene, background, or artistic style (Figure 6).
*   **Local Reference Editing:** The model can perform zero-shot tasks like virtual try-on or placing a reference object into a new scene by combining a reference image, a target image, and a text prompt (Figure 7).

The authors claim that the qualitative analysis showcases the superiority of ACE++ in generating high-quality images that accurately follow user instructions.

## 5. Ablation Studies
Not performed. The paper does not include an ablation study section to quantitatively justify its design choices, such as comparing channel-wise vs. sequence-wise concatenation or evaluating the impact of the two-stage training scheme against a single-stage approach.

## 6. Paper Figures
![Figure 2: The illustration of two-stage training scheme.]({{ '/images/01-2025/ACE++:_Instruction-Based_Image_Creation_and_Editing_via_Context-Aware_Content_Filling/figure_2.jpg' | relative_url }})
![Figure 3: The visualization of subject-driven generation.]({{ '/images/01-2025/ACE++:_Instruction-Based_Image_Creation_and_Editing_via_Context-Aware_Content_Filling/figure_3.jpg' | relative_url }})
![Figure 4: The visualization of portrait-consistency generation.]({{ '/images/01-2025/ACE++:_Instruction-Based_Image_Creation_and_Editing_via_Context-Aware_Content_Filling/figure_4.jpg' | relative_url }})
![Figure 5: The visualization of local editing.]({{ '/images/01-2025/ACE++:_Instruction-Based_Image_Creation_and_Editing_via_Context-Aware_Content_Filling/figure_5.jpg' | relative_url }})
![Figure 6: The visualization of the flexible instruction or descriptions]({{ '/images/01-2025/ACE++:_Instruction-Based_Image_Creation_and_Editing_via_Context-Aware_Content_Filling/figure_6.jpg' | relative_url }})
