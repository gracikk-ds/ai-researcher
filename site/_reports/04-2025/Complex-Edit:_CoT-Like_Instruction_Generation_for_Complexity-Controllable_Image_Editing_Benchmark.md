---
title: Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark
layout: default
date: 2025-04-17
---
![Figure 1. An illustration of our Complex-Edit Benchmark. This figure presents a structured progression of instruction complexity in image editing tasks, highlighting the transition from atomic edits to highly intricate transformations.]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current benchmarks for instruction-based image editing primarily rely on simple, single-step commands (e.g., "remove the car"). This fails to capture real-world scenarios that often demand complex, multi-part transformations. This gap in evaluation capabilities hinders the rigorous assessment of advanced editing models and impedes progress in developing systems that can handle intricate user requests. The authors address this by creating a benchmark to systematically evaluate models across a spectrum of instruction complexities.

## 2. Key Ideas and Methodology
The paper introduces **Complex-Edit**, a benchmark with complexity-controllable instructions, and a corresponding evaluation framework. The core methodology is a "Chain-of-Edit" data generation pipeline that uses GPT-4o to create instructions in three stages:
1.  **Sequence Generation**: For an input image, generate a sequence of simple, "atomic" editing instructions (e.g., "add a cat", "make the car blue").
2.  **Simplification**: Refine each atomic instruction to its essential editing command.
3.  **Instruction Compounding**: Progressively merge the simplified atomic instructions into a single, coherent, complex instruction. The complexity level (from C1 to C8) is controlled by the number of atomic edits combined.

For evaluation, the authors propose a VLM-based auto-evaluation pipeline that assesses performance on three key metrics: **Instruction Following (IF)**, **Identity Preservation (IP)**, and **Perceptual Quality (PQ)**.

## 3. Datasets Used / Presented
The paper presents the **Complex-Edit** benchmark dataset. It contains two sets of images:
*   **Realistic Images**: 531 images sourced from the EMU-Edit test set.
*   **Synthetic Images**: 531 images generated using FLUX.1, based on the captions from the realistic images.

For each image, the dataset provides a series of editing instructions with eight increasing complexity levels (C1 to C8), allowing for granular analysis of model performance as tasks become more difficult.

## 4. Main Results
The benchmark reveals several key insights:
*   Proprietary, closed-source models (e.g., Imagen3, GPT-4o) significantly outperform open-source models. This performance gap widens as instruction complexity increases.
*   Increasing instruction complexity primarily degrades a model's ability to preserve unchanged image regions (Identity Preservation) and maintain overall aesthetic quality (Perceptual Quality).
*   A Chain-of-Thought-like sequential editing approach, where atomic edits are applied one by one, substantially degrades performance across all metrics compared to executing the single complex instruction directly.
*   The authors observe a "curse of synthetic data": when given highly complex instructions for real images, models (including GPT-4o) tend to produce outputs that lose realism and adopt an overly synthetic or painterly aesthetic.

## 5. Ablation Studies
The authors performed several meta-evaluations on their VLM-based auto-grader design and tested different editing strategies:
*   **Evaluation Method**: Direct numeric scoring (e.g., 0-10) by the VLM correlated better with human judgment than token probability-based scoring. Providing detailed rubrics further improved correlation.
*   **CoT for Evaluation**: Using Chain-of-Thought for the *evaluator* VLM was beneficial for the IF and IP metrics but detrimental for the PQ metric.
*   **Instruction Input for PQ**: Excluding the editing instruction when evaluating Perceptual Quality resulted in a better alignment with human perception of image quality.
*   **Best-of-N Strategy**: For the editing models, generating N candidate images and selecting the best one (using their overall score) consistently improved results for both direct and sequential editing. It was particularly effective at improving Identity Preservation and Perceptual Quality in the sequential approach.

## 6. Paper Figures
![Figure 10. A real image edited with a C 8 instruction. Outputs from certain models tend to lose the realistic style completely.]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_10.jpg' | relative_url }})
![Figure 11. A real image edited with a C 8 instruction by GPT-4o. Outputs from GPT-4o severely lose the realistic style. See additional results in Fig. 22 .]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_11.jpg' | relative_url }})
![Figure 2. An overview of our data collection pipeline. The pipeline consists of three distinct stages: 1) Stage #1 Sequence Generation : for each image, a series of atomic instructions is produced; 2) Stage #2 Simplification : each fundamental instruction is refined to eliminate extraneous details, preserving only the essential description of the editing process; 3) Stage #3 Instruction Compounding : several atomic instructions are integrated into one comprehensive instruction.]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_2.jpg' | relative_url }})
![Figure 4. An illustration of 24 types of atomic editing operations in 9 categories.]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_4.jpg' | relative_url }})
![Figure 5. Examples of evaluation results for Instruction Following and Identity Preservation.]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_5.jpg' | relative_url }})
![Figure 6. Examples of evaluation results for Perceptual Quality.]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_6.jpg' | relative_url }})
![Figure 9. Outputs from open-source and proprietary models via direct editing. See results with more models in Figs. 17 and 18 .]({{ '/images/04-2025/Complex-Edit:_CoT-Like_Instruction_Generation_for_Complexity-Controllable_Image_Editing_Benchmark/figure_9.jpg' | relative_url }})
