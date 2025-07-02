---
title: Disentangling_Instruction_Influence_in_Diffusion_Transformers_for_Parallel_Multi-Instruction-Guided_Image_Editing
layout: default
date: 2025-04-07
---
## Disentangling Instruction Influence in Diffusion Transformers for Parallel Multi-Instruction-Guided Image Editing
**Authors:**
- Hui Liu
- Haoliang Li, h-index: 3, papers: 10, citations: 27

**ArXiv URL:** http://arxiv.org/abs/2504.04784v1

**Citation Count:** 0

**Published Date:** 2025-04-07

![Figure 1. Comparison of our proposed Instruction Influence Disentanglement (IID) framework with step-by-step editing and compositing all instructions into a single one for multi-instruction image editing.]({{ '/images/04-2025/Disentangling_Instruction_Influence_in_Diffusion_Transformers_for_Parallel_Multi-Instruction-Guided_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Instruction-guided image editing models, particularly those based on Diffusion Transformers (DiTs), struggle with executing multiple instructions concurrently. Existing approaches face significant limitations:
*   **Step-by-step editing:** Applying instructions sequentially leads to accumulated errors, image degradation, and distortion.
*   **Single-prompt editing:** Merging all instructions into one prompt often results in "instruction conflicts," where the model prioritizes one edit while ignoring others.
The authors address the gap of enabling parallel, non-conflicting execution of multiple editing instructions within a single denoising process for DiT-based models.

## 2. Key Ideas and Methodology
The paper introduces **Instruction Influence Disentanglement (IID)**, a framework for parallel multi-instruction editing in DiTs.

*   **Core Principle:** The key idea is to isolate the influence of each instruction to its specific target region, preventing interference with other edits.
*   **Methodology:** The approach involves three main steps:
    1.  **Head-wise Mask Generation:** At a predefined diffusion timestep `S`, the framework analyzes the self-attention maps within the DiT. To create a mask for a specific instruction, it subtracts the averaged attention map of all *other* instructions from that instruction's own attention map. This isolates the unique region of influence for each edit.
    2.  **Adaptive Latent Blending:** The latent representations corresponding to each instruction are blended together using their respective masks to create a single, composite latent image. Instructions are adaptively ordered to equalize their editing influence.
    3.  **Disentangled Denoising:** A new, composite attention mask is constructed to guide the subsequent denoising steps. This mask ensures that each part of the concatenated instruction prompt only attends to its designated image region, enabling parallel and faithful execution of all edits in a single pass.

## 3. Datasets Used / Presented
*   **MagicBrush Dataset:** The test split, comprising 535 editing sessions with up to three instructions each, was used for quantitative evaluation and comparison against baselines.
*   **Custom Dataset:** The authors collected 50 real-world images with complex, multi-part instructions to conduct a human preference study, reflecting more practical editing scenarios.

## 4. Main Results
*   **Quantitative Improvement:** IID significantly outperforms the standard step-by-step editing approach across all metrics. When applied to the FluxEdit model, IID reduced L1/L2 error and improved CLIP-I, DINO, and CLIP-T scores, demonstrating higher image fidelity and better instruction alignment. For instance, on FluxEdit, IID improved the CLIP-I score from 0.8487 to 0.8855.
*   **Qualitative and Human Evaluation:** Qualitative results show that IID produces sharper, more coherent images and completes all instructions more successfully than sequential editing. In a human preference study, participants strongly preferred IID's outputs for both instruction completion and preservation of original image details.
*   **Author Takeaway:** The IID framework effectively mitigates cumulative errors and instruction conflicts, enabling robust and parallel multi-instruction editing in DiT-based models.

## 5. Ablation Studies
*   **Mask Generation Timestep (S):** The choice of the predefined step `S` is critical. For the Omnigen model, an early step (`S=15`) is necessary to avoid disrupting instruction-related semantics during latent blending. FluxEdit was more resilient to the choice of `S`.
*   **Layer for Mask Extraction:** Masks were extracted from different layers of the DiT. The penultimate layer was found to be optimal, as it strikes a balance between rich semantic information and focused spatial attention. Lower layers produced dispersed masks, while the final layer was too focused on image reconstruction.
*   **Attention Map Type:** The study analyzed two types of attention maps. For FluxEdit, both attention between instruction-image tokens (`Āzp`) and among image tokens (`Āzz`) were effective for mask generation. For Omnigen, only `Āzz` was suitable due to its architectural design where instruction information propagates more slowly.

## 6. Paper Figures
![Figure 2. Illustration of our proposed IID framework. T denotes the total number of diffusion steps, while S represents the pre-defined step for mask generation and multi-instruction influence disentanglement. ¯ z S [ M i ] corresponds to the token sequence of the noised image ¯ z S associated with the mask M i for the instruction P i (ideally representing the tokens pertinent to the editing area specified by P i ).]({{ '/images/04-2025/Disentangling_Instruction_Influence_in_Diffusion_Transformers_for_Parallel_Multi-Instruction-Guided_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3. The visualization of attention map between the instruction tokens and noise image tokens ¯ A ZP and among noise image tokens ¯ A ZZ . Attention weights are extracted from the penultimate layer. “Avg” represents the averaging attention map across all heads.]({{ '/images/04-2025/Disentangling_Instruction_Influence_in_Diffusion_Transformers_for_Parallel_Multi-Instruction-Guided_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative comparisons. The top two rows of images are based on FluxEdit, while the bottom two rows are based on Omnigen. Single results represent use the one instruction to edit the input image.]({{ '/images/04-2025/Disentangling_Instruction_Influence_in_Diffusion_Transformers_for_Parallel_Multi-Instruction-Guided_Image_Editing/figure_4.jpg' | relative_url }})
