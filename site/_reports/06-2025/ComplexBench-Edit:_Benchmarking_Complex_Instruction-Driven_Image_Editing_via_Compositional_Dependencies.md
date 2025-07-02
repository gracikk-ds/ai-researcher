---
title: ComplexBench-Edit:_Benchmarking_Complex_Instruction-Driven_Image_Editing_via_Compositional_Dependencies
layout: default
date: 2025-06-15
---
## ComplexBench-Edit: Benchmarking Complex Instruction-Driven Image Editing via Compositional Dependencies
**Authors:**
- Chenglin Wang
- Kai Zhang

**ArXiv URL:** http://arxiv.org/abs/2506.12830v1

**Citation Count:** None

**Published Date:** 2025-06-15

![Figure 1: Comparison between parallel and chain multi-instruction image editing. Parallel editing applies independent instructions simultaneously, while chain editing involves dependent instructions that must be executed in sequence.]({{ '/images/06-2025/ComplexBench-Edit:_Benchmarking_Complex_Instruction-Driven_Image_Editing_via_Compositional_Dependencies/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current text-driven image editing models excel at following single, simple instructions. However, they struggle with real-world scenarios that require executing complex, multi-step directives. The authors identify a critical gap in both model capability and evaluation: existing models often fail to handle "chain" instructions, where one editing operation is dependent on the outcome of a previous one. Furthermore, existing benchmarks do not adequately test for these compositional and sequential reasoning abilities, and their consistency metrics are often flawed, penalizing correct edits.

## 2. Key Ideas and Methodology
To address these limitations, the authors introduce two main contributions:

1.  **ComplexBench-Edit:** A novel benchmark specifically designed to evaluate image editing models on complex, multi-instruction, and chain-dependent tasks. The benchmark is constructed through a multi-stage pipeline that starts with filtering images from MSCOCO to ensure object diversity and reduce ambiguity. It then uses a Multimodal Large Language Model (MLLM) to generate instructions at three complexity levels (Parallel, Two-chain, Three-chain), followed by an automated feasibility check and human review to ensure quality and logical consistency. The benchmark also includes a novel **vision consistency metric** that evaluates preservation of non-edited regions by excluding the bounding boxes of modified objects from L1/L2 distance calculations.

2.  **Chain-of-Thought (CoT) Reasoning for Image Editing:** A simple, training-free method to enhance a model's ability to follow complex instructions. This approach uses an MLLM to first generate a detailed, step-by-step reasoning plan (the "Chain-of-Thought") for how to execute the user's instructions. This rationale is then concatenated with the original prompt and fed to the editing model, providing it with a richer, more structured understanding of the task.

## 3. Datasets Used / Presented
The paper presents **ComplexBench-Edit**, a new benchmark dataset for complex image editing.
*   **Source:** Images are curated from the MSCOCO dataset.
*   **Content:** It contains image-instruction pairs designed to test complex editing capabilities. The instructions are categorized into three hierarchical levels of complexity:
    1.  **Parallel:** Three logically independent editing instructions.
    2.  **Two-chain:** A two-step dependent instruction chain plus one independent instruction.
    3.  **Three-chain:** A sequence of three interdependent instructions.
*   **Usage:** The dataset is used to systematically benchmark and compare the performance of various state-of-the-art image editing models.

## 4. Main Results
The experiments demonstrate the effectiveness of both the benchmark and the proposed CoT method.

*   **Editing Performance:** On ComplexBench-Edit, the proposed `Gemini-CoT` method achieved the highest average performance score (40.47), consistently outperforming all other models, including the powerful standard `Gemini` (36.70) and other recent models like `Step1X-Edit` (24.05). The performance gap widened as instruction complexity and chain length increased, highlighting the challenge of sequential editing for most models.
*   **Vision Consistency:** In preserving non-edited regions, `OmniGen` performed best (lowest average L1 error of 0.0377), while high-performing editors like `Gemini-CoT` showed higher error (0.0846). This suggests a trade-off between aggressive, high-quality editing and background preservation.
*   **Human Evaluation:** The `Gemini-CoT` method was strongly preferred by human evaluators in pairwise comparisons against leading models, winning against standard `Gemini` in 67% of cases and against `OmniGen` in 76% of cases.

The authors conclude that ComplexBench-Edit is effective at differentiating model capabilities in complex scenarios and that CoT reasoning is a powerful technique for improving sequential instruction following.

## 5. Ablation Studies
The paper performs an ablation study on the effect of the Chain-of-Thought (CoT) reasoning module by comparing the performance of the `Gemini` model with and without the CoT-generated rationale.

*   **Experiment:** The performance of `Gemini` was compared against `Gemini-CoT` on the ComplexBench-Edit dataset.
*   **Impact:** The addition of CoT significantly improved performance across all task complexities. Quantitatively, the average editing performance score increased from 36.70 for the standard `Gemini` model to **40.47** for `Gemini-CoT`. Qualitatively, the model with CoT was able to correctly follow a multi-step instruction (e.g., add two distinct objects and modify one), while the model without CoT failed to execute all steps faithfully. This demonstrates that the CoT module effectively enhances the model's ability to deconstruct and execute complex, sequential edits.

## 6. Paper Figures
![Figure 2: Overview of the data creation pipeline of ComplexBench-Edit.]({{ '/images/06-2025/ComplexBench-Edit:_Benchmarking_Complex_Instruction-Driven_Image_Editing_via_Compositional_Dependencies/figure_2.jpg' | relative_url }})
![Figure 4: Diagram of the proposed Chain-of-Thought (CoT) reasoning approach for image editing.]({{ '/images/06-2025/ComplexBench-Edit:_Benchmarking_Complex_Instruction-Driven_Image_Editing_via_Compositional_Dependencies/figure_4.jpg' | relative_url }})
![Figure 5: Comparison of image editing results w/ and w/o CoT.]({{ '/images/06-2025/ComplexBench-Edit:_Benchmarking_Complex_Instruction-Driven_Image_Editing_via_Compositional_Dependencies/figure_5.jpg' | relative_url }})
