---
title: InteractEdit:_Zero-Shot_Editing_of_Human-Object_Interactions_in_Images
layout: default
date: 2025-03-12
---
## InteractEdit: Zero-Shot Editing of Human-Object Interactions in Images
**Authors:**
- Jiun Tian Hoe, h-index: 2, papers: 8, citations: 128
- Yap-Peng Tan, h-index: 5, papers: 18, citations: 49

**ArXiv URL:** http://arxiv.org/abs/2503.09130v1

**Citation Count:** 0

**Published Date:** 2025-03-12

![Figure 1. Sample results of editing Human-Object Interaction in the source image (left). Existing methods overly preserve the structure, making interaction edits ineffective. Our method focuses on modifying interactions while maintaining the subject and object identity.]({{ '/images/03-2025/InteractEdit:_Zero-Shot_Editing_of_Human-Object_Interactions_in_Images/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenging task of Human-Object Interaction (HOI) editing in images. Existing image editing methods excel at tasks like changing object attributes or styles but struggle to modify the complex relationship between a human and an object. This is because HOI editing often requires substantial, non-rigid structural changes to the scene (e.g., altering a person's pose from "holding a skateboard" to "riding a skateboard") while preserving the visual identities of the subject and object. Current methods tend to overfit to the source image's structure, making them ineffective for such edits. Furthermore, the field lacks a standardized benchmark for evaluating HOI editing performance, hindering progress.

## 2. Key Ideas and Methodology
The paper introduces **InteractEdit**, a novel framework for zero-shot HOI editing that does not require reference images of the target interaction.

-   **Core Hypothesis**: The key to effective HOI editing is to regularize the model's fine-tuning process to prevent overfitting to the source structure, thereby balancing the need for structural modification with identity preservation.
-   **Methodology**: The framework operates in two main stages:
    1.  **Disassembly and Regularized Inversion**: The source image is first disassembled into its constituent components—subject, object, and background—using a multi-concept extraction technique (Break-A-Scene). To learn the visual identity of these components without memorizing their spatial layout, the framework employs a regularized fine-tuning strategy on a pretrained diffusion model. This involves:
        -   **Low-Rank Adaptation (LoRA)**: Constrains the updates to the model's attention weights, capturing only essential appearance attributes while ignoring rigid structural details.
        -   **Selective Fine-Tuning**: Freezes the Query (WQ) weights in the attention mechanism to retain the model's pretrained knowledge of interactions, while only training the Key (WK) and Value (WV) weights to adapt to the source image's appearance.
    2.  **Editing and Reassembly**: The learned components are reassembled via a new text prompt describing the target interaction (e.g., "a photo of [subject] riding [object]"). The diffusion model, guided by the fine-tuned LoRA weights and the new prompt, then generates the edited image.

## 3. Datasets Used / Presented
The authors introduce a new benchmark, **IEBench (InteractEdit Benchmark)**, to standardize the evaluation of HOI editing.

-   **Composition**: IEBench is constructed from the HICO-DET dataset. It contains 28 source images, 13 objects, and 25 actions, forming 100 unique source-to-target interaction pairs.
-   **Usage**: It is used to evaluate models on two novel metrics:
    1.  **HOI Editability**: An objective score (0 or 1) indicating whether the target interaction was successfully generated, as determined by a state-of-the-art HOI detector (PViC).
    2.  **Identity Consistency (IC)**: A cosine similarity score measuring how well the visual identities of the subject and object are preserved between the source and edited images, using DINOv2 embeddings.
-   An **Overall Score** is calculated as the average of these two metrics.

## 4. Main Results
InteractEdit was benchmarked against 16 existing methods on IEBench.

-   **Quantitative Performance**: InteractEdit significantly outperformed all baselines. It achieved the highest **Overall Score** of 0.5308, a 25.8% improvement over the second-best method. It also obtained the top **HOI Editability** score of 0.504, demonstrating a superior ability to modify interactions, while maintaining a competitive **Identity Consistency** score of 0.558.
-   **User Study**: In a preference study involving 30 participants, 68.2% chose InteractEdit's results as the best among six competing methods.
-   **Author-claimed Impact**: The paper establishes a strong new baseline for zero-shot HOI editing, demonstrating that balancing interaction modification with identity preservation is key to success.

## 5. Ablation Studies
The authors conducted ablation studies to validate the contributions of each key component of InteractEdit.

-   **Disassembling HOI**: Removing the component disassembly step caused the HOI Editability score to drop from 0.504 to 0.401, showing that separating the subject, object, and background is crucial for effective editing.
-   **Selective Fine-Tuning (SFT)**: When SFT was disabled (i.e., all attention parameters were fine-tuned), the HOI Editability score fell to 0.466. This confirms that SFT is vital for preserving the model's pretrained knowledge about interactions.
-   **LoRA Regularization**: Removing LoRA resulted in a sharp decline in HOI Editability to 0.274. This highlights LoRA's critical role in preventing overfitting and enabling the non-rigid structural changes required for interaction editing.
-   **Combined Effect**: A baseline model without any of these components achieved a very low HOI Editability score of 0.165, underscoring the synergistic effect of the proposed techniques.

## 6. Paper Figures
![Figure 2. Overview of the InteractEdit framework. HOI components are disassembled into subject, object, and background clues during inversion (Sec. 3.3 ). LoRA regularization enables non-rigid edits by capturing essential attributes while ignoring fine-grained structural details (Sec. 3.4 ). Selective fine-tuning preserves interaction priors while adapting to the source image’s identity (Sec. 3.5 ). Editing reassembles these components with the target interaction, using trained LoRA weights to guide the diffusion model (Sec. 3.6 ).]({{ '/images/03-2025/InteractEdit:_Zero-Shot_Editing_of_Human-Object_Interactions_in_Images/figure_2.jpg' | relative_url }})
![Figure 3. Qualitative comparison with baselines. The Source column shows the source image and its original interaction. Two target interactions are generated per instance. Our method achieves the best HOI editability. More comparisons are in Figs. 6 and 7 (supplementary).]({{ '/images/03-2025/InteractEdit:_Zero-Shot_Editing_of_Human-Object_Interactions_in_Images/figure_3.jpg' | relative_url }})
![hold skateboard → ride skateboard Figure 4. Qualitative ablation study. The row below image shows the source and target interaction.]({{ '/images/03-2025/InteractEdit:_Zero-Shot_Editing_of_Human-Object_Interactions_in_Images/figure_4.jpg' | relative_url }})
