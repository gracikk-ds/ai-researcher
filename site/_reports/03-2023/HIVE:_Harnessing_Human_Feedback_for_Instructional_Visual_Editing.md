---
title: HIVE:_Harnessing_Human_Feedback_for_Instructional_Visual_Editing
layout: default
date: 2023-03-16
---
## HIVE: Harnessing Human Feedback for Instructional Visual Editing
**Authors:**
- Shu Zhang
- Ran Xu

**ArXiv URL:** http://arxiv.org/abs/2303.09618v2

**Citation Count:** 116

**Published Date:** 2023-03-16

![Figure 1. We show four groups of representative results. In each triplet, from left to right are: the original image, InstructPix2Pix [ 7 ] using our data (IP2P-Ours), and HIVE. We observe that HIVE leads to more acceptable results than the model without human feedback. For instance, in the left two examples, IP2P-Ours understands the editing instruction “remove” and “change to blue” individually, but fails to understand the corresponding objects. Human feedback resolves this ambiguity, as shown in other examples as well.]({{ '/images/03-2023/HIVE:_Harnessing_Human_Feedback_for_Instructional_Visual_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the problem that state-of-the-art instructional image editing models, while powerful, often produce results that do not fully align with user instructions or preferences. These models can misinterpret the objects to be edited, misunderstand the desired change, or make excessive, unwanted alterations to the rest of the image. The paper aims to bridge this gap by incorporating human feedback into the model's training process, a technique successfully used to align large language models (LLMs) but less explored for diffusion-based image editors due to technical challenges.

## 2. Key Ideas and Methodology
The core idea is a framework named **HIVE (Harnessing Human Feedback for Instructional Visual Editing)**, which refines a diffusion model using human preferences. The methodology consists of three main steps:

1.  **Instructional Supervised Training**: First, a baseline diffusion model (similar to InstructPix2Pix) is trained on a large dataset of (original image, text instruction, edited image) triplets.
2.  **Reward Model Training**: For a given image and instruction, multiple edited outputs are generated. Human annotators then rank these outputs from best to worst. This comparison data is used to train a reward model (RM) that learns to predict a scalar score reflecting human preference for an edited image.
3.  **Human Feedback-based Fine-tuning**: The trained reward model is integrated into the fine-tuning process of the baseline diffusion model. The authors propose two scalable methods to do this without expensive on-policy reinforcement learning:
    *   **Condition Reward Loss**: The reward score is quantized into discrete levels (e.g., "The image quality is five out of five") and used as an additional text condition during fine-tuning. This guides the model to generate outputs associated with high rewards.
    *   **Weighted Reward Loss**: The reward score is used to calculate a weight for each training example's loss, effectively prioritizing examples that are highly preferred by humans.

A key technique used to enrich the training data is **cycle consistency augmentation**, where the model is trained on invertible instruction pairs (e.g., "add a dog" ↔ "remove the dog") to improve robustness.

## 3. Datasets Used / Presented
The authors created and used three new datasets to support the HIVE framework:
*   **Training Dataset**: A new dataset of **1.1 million** (image, instruction, edited image) triplets, which is combined with the existing 281K triplets from InstructPix2Pix.
*   **Reward Dataset**: A dataset containing **3.6K** image-instruction pairs with multiple, human-ranked outputs, used specifically for training the reward model.
*   **Evaluation Dataset**: A new dataset of **1,000** real-world images, each annotated with five human-written instructions, used for user studies and qualitative evaluation.

## 4. Main Results
*   **Quantitative Metrics**: HIVE demonstrates a superior trade-off between image consistency and edit consistency. On a synthetic benchmark, HIVE achieves higher CLIP image similarity (consistency with the input) for any given level of directional CLIP similarity (consistency with the edit instruction) compared to baseline models.
*   **User Studies**: In a pairwise comparison on real-world images, HIVE was significantly preferred by human evaluators over the baseline model (IP2P-Ours). HIVE won **49.3%** of the comparisons, while the baseline won **24.2%** (26.5% were ties).
*   **Author-claimed Impact**: The paper demonstrates that harnessing human feedback is a viable and effective approach to align instructional image editing models with user preferences, leading to more accurate and desirable edits.

## 5. Ablation Studies
*   **Reward Fine-tuning Method**: The **Condition Reward Loss** and **Weighted Reward Loss** methods were compared. User studies showed they performed similarly, with the conditional method having a slight edge in performance and stability.
*   **Cycle Consistency**: Including cycle consistency augmentation during training provided a "notable margin" of improvement. In a user study, the model with this augmentation was preferred over the one without it (41.2% vs. 29.9% win rate).
*   **Training Data Size**: Reducing the training dataset to 50% of its size resulted in a minor performance drop, while reducing it to 10% led to a significant degradation in editing ability.
*   **Edit Type Analysis**: HIVE's performance gains were most pronounced for instructions involving "add/remove objects" and "manipulate objects," indicating improved object-level understanding.

## 6. Paper Figures
![“Add food on the table” Figure 12. Failure examples.]({{ '/images/03-2023/HIVE:_Harnessing_Human_Feedback_for_Instructional_Visual_Editing/figure_12.jpg' | relative_url }})
![Figure 2. Overall architecture of HIVE. The first step is to train a baseline HIVE without human feedback. In the second step, we collect human feedback to rank variant outputs for each image-instruction pair, and train a reward model to learn the rewards. In the third step, we fine-tune diffusion models by integrating the estimated rewards.]({{ '/images/03-2023/HIVE:_Harnessing_Human_Feedback_for_Instructional_Visual_Editing/figure_2.jpg' | relative_url }})
![Edited image Figure 3. Model architecture for reward R (˜ x, c ) . Here the reward model evaluates human preference for an edited image of a hand selecting an orange compared to the original input image of the hand selecting an apple. The input to the reward model includes both images and a text instruction. The output is a score indicating the degree of preference for the edited image based on the input image and instruction.]({{ '/images/03-2023/HIVE:_Harnessing_Human_Feedback_for_Instructional_Visual_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Comparisons between IP2P-Official (InstructPix2Pix official model), IP2P-Ours (InstructPix2Pix using our data) and HIVE. HIVE can boost performance by understanding the instruction correctly.]({{ '/images/03-2023/HIVE:_Harnessing_Human_Feedback_for_Instructional_Visual_Editing/figure_4.jpg' | relative_url }})
![Figure 7. Human feedback tends to help HIVE avoid unwanted excessive image modifications.]({{ '/images/03-2023/HIVE:_Harnessing_Human_Feedback_for_Instructional_Visual_Editing/figure_7.jpg' | relative_url }})
