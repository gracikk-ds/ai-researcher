---
title: Image_Editing_As_Programs_with_Diffusion_Models
layout: default
date: 2025-06-04
---
## Image Editing As Programs with Diffusion Models
**Authors:**
- Yujia Hupapers: 2, 
- Xinchao Wang

**ArXiv URL:** http://arxiv.org/abs/2506.04158v1

**Citation Count:** 0

**Published Date:** 2025-06-04

![Figure 1: Visual results of our IEAP. Rows 1 and 3 showcase complex multi-step edits (Row 1 is further decomposed into individual instructions), while Row 2 shows single-instruction edits. Single instructions are underlined if needing to be reduced to atomic operations.]({{ '/images/06-2025/Image_Editing_As_Programs_with_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing instruction-driven image editing models, particularly those based on Diffusion Transformers (DiTs), struggle significantly with complex instructions that require changes to the image layout. While they perform well on "structurally-consistent" edits like style or color changes, they often fail on "structurally-inconsistent" edits such as adding, removing, moving, or resizing objects. This paper addresses this gap by proposing a method to robustly handle edits that demand spatial reasoning and scene recomposition.

## 2. Key Ideas and Methodology
The paper introduces **Image Editing As Programs (IEAP)**, a framework that treats complex image editing as an executable program. The core idea is to decompose a high-level instruction into a sequence of simpler, modular steps.

The methodology uses a Vision-Language Model (VLM) with Chain-of-Thought (CoT) reasoning to parse the user's command into a series of **atomic operations**. These five operations—RoI Localization, RoI Inpainting, RoI Editing, RoI Compositing, and Global Transformation—are the fundamental building blocks for any edit. Each operation is implemented by a specialized, lightweight LoRA adapter on a shared DiT backbone (FLUX.1-dev), which are then executed sequentially by a neural program interpreter to produce the final image.

## 3. Datasets Used / Presented
-   **Training**: The models were trained using relevant subsets of the **AnyEdit** dataset, which were filtered by GPT-4o to improve quality. The **CelebHQ-FM** dataset was also integrated to cover facial expression edits.
-   **Evaluation**: The framework was benchmarked on the **MagicBrush test set** and the **AnyEdit test set**.

## 4. Main Results
-   IEAP significantly outperforms state-of-the-art open-source methods. On the AnyEdit test set, it achieved a GPT-4o quality score of **4.41**, surpassing the next best model, ICEdit (4.13). On the MagicBrush test set, it obtained top scores for CLIP image similarity (0.922) and DINO similarity (0.897).
-   The authors claim that by modularizing and sequencing edits, IEAP can robustly handle complex, multi-step instructions that confound conventional end-to-end approaches, delivering superior accuracy and semantic fidelity.

## 5. Ablation Studies
Module-wise ablation studies were conducted to validate the contribution of each component on the AnyEdit local semantic editing task.
-   Replacing the **CoT reduction pipeline** with a standard end-to-end approach caused a marked performance drop across all metrics (GPT-4o score fell from 4.42 to 4.10).
-   Substituting the specialized **RoI Inpainting** module with a generic one led to a severe drop in quality, with the GPT-4o score decreasing to 3.65 and producing unnatural fillings.
-   Removing other components like **LLM-guided Layout Reconfiguration** and **RoI Editing** also resulted in noticeable performance declines, confirming that each step in the programmatic pipeline is crucial for handling complex layout-altering edits.

## 6. Paper Figures
![Figure 2: Results of our preliminary experiments. Figure (a) shows the GPT-4o scores for three editing types across instruction faithfulness and semantic consistency, ranging from 1 to 5. Figure (b) shows the representative failure cases from local semantic editing.]({{ '/images/06-2025/Image_Editing_As_Programs_with_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3: Our pipeline. The original instruction is first parsed by a VLM into atomic operations, which are then sequentially executed via a neural program interpreter.]({{ '/images/06-2025/Image_Editing_As_Programs_with_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4: Example procedure. Figure (a) and Figure (b) illustrate the procedures of action change and movement respectively.]({{ '/images/06-2025/Image_Editing_As_Programs_with_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5: Comparison results of ours with baseline methods on representative editing cases. Others exhibit poor performance even on some common editing operations, while our approach demonstrates superior effectiveness across all operations.]({{ '/images/06-2025/Image_Editing_As_Programs_with_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6: Comparisons on Complex Instructions with Leading Multimodal Models. Our method achieves comparable or even better edit completeness and pre-post consistency. multiple sequential edits. Unlike competing approaches, which frequently omit specified instructions or introduce extraneous alterations unrelated to the editing directives, our framework faithfully executes each instruction while maintaining superior image consistency and instance preservation.]({{ '/images/06-2025/Image_Editing_As_Programs_with_Diffusion_Models/figure_6.jpg' | relative_url }})
![Figure 7: Qualitative ablation of action change operation.]({{ '/images/06-2025/Image_Editing_As_Programs_with_Diffusion_Models/figure_7.jpg' | relative_url }})
