---
title: MagicBrush:_A_Manually_Annotated_Dataset_for_Instruction-Guided_Image_Editing
layout: default
date: 2023-06-16
---
![Figure 1: M AGIC B RUSH provides 10K manually annotated real image editing triplets (source image, instruction, target image), supporting both single-turn and multi-turn instruction-guided editing.]({{ '/images/06-2023/MagicBrush:_A_Manually_Annotated_Dataset_for_Instruction-Guided_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-guided image editing models are often trained on automatically synthesized datasets, which contain significant noise and do not fully capture the diversity of real-world editing needs. Other zero-shot methods require extensive manual tuning to produce desirable results. This creates a gap between current model capabilities and practical, high-quality image editing. The authors address this by creating a large-scale, manually annotated dataset to facilitate the development of more robust and accurate instruction-guided editing models.

## 2. Key Ideas and Methodology
The paper introduces **MAGICBRUSH**, the first large-scale, manually annotated dataset for instruction-guided real image editing. The core methodology is a rigorous three-stage crowdsourcing pipeline:
1.  **Worker Selection:** Crowd-workers on Amazon Mechanical Turk (AMT) were carefully selected through a qualification quiz and a graded trial period to ensure high-quality contributions.
2.  **Data Collection:** Qualified workers used the DALL-E 2 platform to perform edits on real images from the MS COCO dataset. For each image, they proposed a natural language instruction (e.g., "Let the cat have blue eyes") and interactively generated a corresponding target image. The process supports both single-turn edits and complex, iterative multi-turn edit sessions.
3.  **Post-Verification:** The generated data triplets (source image, instruction, target image) were manually verified for quality, consistency, and photorealism.

## 3. Datasets Used / Presented
The paper presents the **MAGICBRUSH** dataset.
*   **Name:** MAGICBRUSH
*   **Size:** It comprises over 10,000 (10,388) manually annotated edit turns, organized into 5,313 edit sessions.
*   **Domain:** It consists of open-domain real images sourced from the MS COCO dataset.
*   **Usage:** It is designed for training and evaluating instruction-guided image editing models, supporting single-turn, multi-turn, mask-provided, and mask-free scenarios. The authors use it to fine-tune and evaluate the InstructPix2Pix model.

## 4. Main Results
The main result is that models fine-tuned on MAGICBRUSH show significant performance improvements.
*   **Quantitative:** The InstructPix2Pix model, when fine-tuned on MAGICBRUSH, substantially outperforms its original version and other strong baselines across automatic metrics like L1 distance, CLIP-I, and DINO similarity.
*   **Human Evaluation:** In a multi-choice comparison against three other top models, the fine-tuned InstructPix2Pix was selected as the best for instruction consistency 51% of the time and for image quality 49% of the time, far surpassing all competitors.
*   **Takeaway:** The authors claim that MAGICBRUSH effectively trains models for real-world editing tasks and that the results highlight a significant gap between existing methods and human-level editing quality, motivating future research.

## 5. Ablation Studies
The paper's primary analysis serves as an ablation study on the impact of the MAGICBRUSH dataset itself. The authors compare the performance of the off-the-shelf InstructPix2Pix model with the same model after fine-tuning it on their new dataset.
*   **Experiment:** The performance of the original InstructPix2Pix is compared against the fine-tuned version on the MAGICBRUSH test set.
*   **Impact:** Fine-tuning on MAGICBRUSH leads to dramatic improvements. In a direct one-on-one human comparison, the fine-tuned model was preferred over the original for consistency in 68% of cases and for image quality in 61% of cases. This demonstrates that training on the high-quality, manually curated data in MAGICBRUSH is crucial for enhancing model performance in instruction-following and photorealism.

## 6. Paper Figures
![Figure 2: The three-stage crowdsourcing workflow designed for dataset construction.]({{ '/images/06-2023/MagicBrush:_A_Manually_Annotated_Dataset_for_Instruction-Guided_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Statistics for the M AGIC B RUSH dataset.]({{ '/images/06-2023/MagicBrush:_A_Manually_Annotated_Dataset_for_Instruction-Guided_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: An overview of keywords in edit instructions. The inner circle depicts the types of edits and outer circle showcases the most frequent words used within each type.]({{ '/images/06-2023/MagicBrush:_A_Manually_Annotated_Dataset_for_Instruction-Guided_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative evaluation of multi-turn editing scenario. We provide all baselines their desired input formats (e.g., masks and local descriptions for GLIDE).]({{ '/images/06-2023/MagicBrush:_A_Manually_Annotated_Dataset_for_Instruction-Guided_Image_Editing/figure_5.jpg' | relative_url }})
