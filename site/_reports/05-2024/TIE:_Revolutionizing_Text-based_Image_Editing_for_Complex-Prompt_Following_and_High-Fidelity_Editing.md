---
title: TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing
layout: default
date: 2024-05-27
---
## TIE: Revolutionizing Text-based Image Editing for Complex-Prompt Following and High-Fidelity Editing
**Authors:**
- Xinyu Zhang
- Lin Ma

**ArXiv URL:** http://arxiv.org/abs/2405.16803v1

**Citation Count:** 2

**Published Date:** 2024-05-27

![Figure 1: Illustration of our proposed framework as a Chain-of-Thought (CoT) process.]({{ '/images/05-2024/TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-guided image editing models, including both traditional diffusion models and those integrated with Multimodal Large Language Models (MLLMs), struggle with two key challenges. They often fail to accurately interpret complex, multi-part editing instructions and have difficulty preserving the unedited regions of an image, resulting in low-fidelity outputs with unwanted changes. The authors aim to bridge this gap by creating a framework that can robustly follow complex prompts while maintaining high fidelity to the original image.

## 2. Key Ideas and Methodology
The core of the proposed framework, TIE, is a Chain-of-Thought (CoT) pipeline that leverages the reasoning capabilities of MLLMs to guide a diffusion model. The methodology consists of three main phases:
1.  **CoT Reasoning:** A fine-tuned LISA model (a lightweight MLLM) first performs a CoT process on the user's complex instruction. This involves decomposing the instruction into simpler sub-tasks, localizing the corresponding region in the image for each sub-task, and generating a detailed description of that region.
2.  **Mask and Prompt Generation:** Based on this reasoning, the LISA model generates a precise segmentation mask for the area to be edited and a new, semantically aligned "inpainting prompt" that describes the desired change for that specific area.
3.  **Inpainting:** The original image, the generated mask, and the new inpainting prompt are fed into a pre-existing diffusion inpainting model (Kandinsky-2.2) to synthesize the final, high-fidelity edited image.

## 3. Datasets Used / Presented
The authors constructed a new pipeline dataset for fine-tuning their model. They started with 1,376 samples from the **MagicBrush** dataset. For each sample, they summarized multiple editing instructions into a single complex instruction. They then used **GPT-4V** to generate the corresponding CoT data (instruction decomposition, region localization, and detailed descriptions). This new dataset, containing the source/target images, masks, complex instructions, and CoT reasoning, was used to fine-tune the LISA model.

## 4. Main Results
The proposed model demonstrates superior performance compared to state-of-the-art MLLM-based and pure diffusion-based editing models.
-   **Quantitative:** In comparisons, the model achieved higher scores in prompt following and image fidelity. For instance, on the Alignment metric (measuring instruction adherence), the model scored 57, outperforming other MLLM models (scores of 43, 48, 33) and diffusion models (scores ranging from 27 to 52). It also showed strong performance in image fidelity (CLIP-I) and overall coherence.
-   **Qualitative:** Visual results show the model accurately executes complex edits (e.g., adding, removing, and changing multiple objects/attributes) while preserving the background and unchanged objects, unlike competing models which often lose or conflate instructions.

## 5. Ablation Studies
-   **Effectiveness of CoT Process:** The authors compared their full model with a version that omits the CoT process (using the base LISA-13B model directly). Without CoT, the model produced inaccurate, overly broad masks (e.g., masking an entire wall instead of just a star on it) and failed to generate correct edits. The CoT process was shown to be crucial for precise region understanding and high-quality inpainting.
-   **Effectiveness of Fine-tuning:** The fine-tuned LISA model (LISA-13B-sft) was compared against the base LISA-13B and GPT-4V using in-context learning. While all models showed similar reasoning capabilities, the fine-tuned model generated significantly more precise segmentation masks, accurately isolating the target object. This demonstrates the benefit of jointly fine-tuning on both CoT reasoning and mask generation.

## 6. Paper Figures
![Figure 2: Illustration of data preparation for CoT fine-tuning.]({{ '/images/05-2024/TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Visualization comparison with MLLM SOTA models.]({{ '/images/05-2024/TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Visualization comparison with stable diffusion (SD) SOTA models.]({{ '/images/05-2024/TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Image editing for complex-prompt.]({{ '/images/05-2024/TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Effectiveness of CoT process.]({{ '/images/05-2024/TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing/figure_6.jpg' | relative_url }})
![Figure 7: Effectiveness of fine-tuning.]({{ '/images/05-2024/TIE:_Revolutionizing_Text-based_Image_Editing_for_Complex-Prompt_Following_and_High-Fidelity_Editing/figure_7.jpg' | relative_url }})
