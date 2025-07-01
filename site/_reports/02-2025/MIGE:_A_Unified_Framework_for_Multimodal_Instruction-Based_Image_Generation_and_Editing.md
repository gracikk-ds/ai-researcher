---
title: MIGE:_A_Unified_Framework_for_Multimodal_Instruction-Based_Image_Generation_and_Editing
layout: default
date: 2025-02-28
---
![Figure 1: Demonstrating the comprehensive capabilities of MIGE. As a unified framework, MIGE excels in subject-driven generation and instruction-based editing while performing well in the new compositional task of instruction-based subject-driven editing.]({{ '/images/02-2025/MIGE:_A_Unified_Framework_for_Multimodal_Instruction-Based_Image_Generation_and_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of existing diffusion-based models, which typically handle subject-driven image generation and instruction-based image editing as separate, isolated tasks. This separation leads to poor generalization, struggles with limited high-quality data for each specific task, and prevents models from tackling more complex, compositional instructions. For instance, subject-driven generation methods often require per-subject fine-tuning, while instruction-based editors can struggle to maintain global consistency. The core problem is the lack of a unified framework that can leverage the complementary strengths of both tasks to improve overall performance and enable novel capabilities like instruction-based subject-driven editing.

## 2. Key Ideas and Methodology
The paper introduces **MIGE (Multimodal Instruction-based Generation and Editing)**, a unified framework designed to jointly train on and execute both tasks.

-   **Core Principle:** The central idea is to unify both tasks through a standardized input-output representation. Subject-driven generation is framed as creating an image on a "blank canvas," while instruction-based editing is treated as modifying an existing image. This is achieved using two key unification strategies:
    1.  **Unified Multimodal Instructions:** The model accepts interleaved image and text instructions (e.g., "replace the pillow in `<imagehere>` with `<imagehere>`"), where `<imagehere>` is a placeholder for visual content. This allows for flexible and rich task specifications.
    2.  **Unified Conditional Input:** A conditional input structurally differentiates the tasks. For editing, the VAE-encoded source image is concatenated with noise. For generation, an all-zero tensor is used as the "blank canvas."

-   **Methodology:** MIGE's architecture consists of a multimodal encoder and a transformer-based diffusion model (initialized from PIXART-α). A key innovation is a **feature fusion mechanism** within the encoder. Unlike prior work that relies solely on semantic features (from CLIP), MIGE combines these with fine-grained visual features from a VAE encoder. This fusion allows the model to better preserve the specific details and identity of reference subjects during generation and editing.

## 3. Datasets Used / Presented
MIGE is trained on a large, composite dataset constructed from multiple sources and is evaluated on standard benchmarks as well as a newly proposed one.

-   **Training Datasets:**
    -   **Subject-Driven Generation:** Constructed from KOSMOS-G, UNIMO-G, and Subjects200k datasets.
    -   **Instruction-Based Editing:** Aggregated and filtered from existing datasets, including InstructPix2Pix, MagicBrush, and SEED-Data-Edit.
    -   **Instruction-Based Subject-Driven Editing:** A new dataset created using custom pipelines. For *subject addition*, ~200k samples were generated from SA-1B. For *subject replacement*, ~110k samples were created by processing SEED-Data-Edit and IDM-VTON datasets.

-   **Evaluation Benchmarks:**
    -   **DreamBench:** Used to evaluate subject-driven generation (750 prompts).
    -   **EmuEdit & MagicBrush:** Used to evaluate instruction-based editing.
    -   **MIGEBench (New):** A benchmark of 1,000 samples (500 for addition, 500 for replacement) proposed by the authors to evaluate the novel task of instruction-based subject-driven editing.

## 4. Main Results
MIGE demonstrates strong performance across all tasks, outperforming existing universal models and remaining competitive with task-specific ones.

-   **Subject-Driven Generation:** On DreamBench, MIGE achieves a DINO score of 0.744, outperforming other universal models in subject preservation while maintaining competitive text fidelity.
-   **Instruction-Based Editing:** On the MagicBrush benchmark, MIGE surpasses all other universal models on all metrics, showing superior instruction following (CLIP-T: 0.306) and detail preservation (L1 error: 0.055).
-   **Instruction-Based Subject-Driven Editing:** On the new MIGEBench, MIGE significantly outperforms all baselines in both subject addition and replacement tasks, demonstrating its emergent compositional capabilities.

The authors conclude that unifying these tasks within a single framework not only improves performance on individual tasks but also unlocks the ability to handle more complex, compositional image manipulation.

## 5. Ablation Studies
The paper conducts several ablation studies to validate the key components of the MIGE framework.

-   **Effectiveness of Joint Training:** Models were trained on individual task datasets separately. Compared to the fully-trained MIGE, these single-task models showed consistently lower performance across all metrics. This confirms that joint training allows for mutual reinforcement between tasks, enhancing overall capability.
-   **Effectiveness of Feature Fusing:** A version of MIGE was trained without the VAE visual feature fusion mechanism (`wo_VAE feature`). This model showed a noticeable drop in detail preservation, with the DINO score on DreamBench decreasing and the L1 error on MagicBrush increasing from 0.055 to 0.098. This highlights the importance of fusing visual features for preserving fine-grained subject details.
-   **Effectiveness of Multimodal Instructions:** MIGE was compared to a variant trained only on text instructions (`wo_multimodal instruction`). The multimodal version achieved significantly better results, especially in pixel-level accuracy. For example, the L1 error on MagicBrush was reduced from 0.170 to 0.055, demonstrating that visual context in instructions enables more precise and faithful edits.

## 6. Paper Figures
![Figure 2: Demonstration of MIGE as a unified framework for processing multimodal instructions and conditional inputs across diverse tasks and scenarios.]({{ '/images/02-2025/MIGE:_A_Unified_Framework_for_Multimodal_Instruction-Based_Image_Generation_and_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Overall framework of MIGE. MIGE consists of two components: a multimodal encoder for processing multimodal instructions and a transformer-based diffusion model for modeling input-output relationships. The encoder incorporates a feature fusion mechanism to integrate visual and semantic features from reference image.]({{ '/images/02-2025/MIGE:_A_Unified_Framework_for_Multimodal_Instruction-Based_Image_Generation_and_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Data construction pipelines for instruction-based subject-driven image editing.]({{ '/images/02-2025/MIGE:_A_Unified_Framework_for_Multimodal_Instruction-Based_Image_Generation_and_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative comparison for subject-driven image generation (top rows) and instruction-based image editing (bottom rows). We compare the universal model and task-specific models on the two tasks, respectively. The prompts listed in the figure are used for MIGE and vary according to the usage of each model.]({{ '/images/02-2025/MIGE:_A_Unified_Framework_for_Multimodal_Instruction-Based_Image_Generation_and_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Qualitative results on the benchmark for the subject addition and subject replacement. The upper section compares subject addition results, while the lower section compares subject replacement. During testing, the <imagehere> placeholder in the multimodal instruction is replaced according to the image sequence. MIGE demonstrates flexibility in editing and excels in subject preservation ability and input-output consistency.]({{ '/images/02-2025/MIGE:_A_Unified_Framework_for_Multimodal_Instruction-Based_Image_Generation_and_Editing/figure_6.jpg' | relative_url }})
