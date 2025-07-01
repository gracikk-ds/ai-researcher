---
title: HumanEdit:_A_High-Quality_Human-Rewarded_Dataset_for_Instruction-based_Image_Editing
layout: default
date: 2024-12-05
---
![Figure 1: Data examples of instruction-guided image editing in HumanEdit . Our dataset encompasses six distinct editing categories. In the images, gray shapes represent masks, which are provided for every photograph. Moreover, approximately half of the dataset includes instructions that are sufficiently detailed to enable editing without masks. It is important to note that, for conciseness, masks are depicted directly on the original images within this paper; however, in the dataset, the original images and masks are stored separately.]({{ '/images/12-2024/HumanEdit:_A_High-Quality_Human-Rewarded_Dataset_for_Instruction-based_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the gap between existing instruction-based image editing datasets and real-world human preferences. Current large-scale datasets are often generated automatically using large language and vision models with minimal human oversight. This results in noisy data, low-quality edits, and a general misalignment with the nuanced and diverse ways humans would naturally request image manipulations. These shortcomings limit the practical applicability and reliability of models trained on such data.

## 2. Key Ideas and Methodology
The paper introduces **HumanEdit**, a dataset created through a meticulous, multi-stage "human-rewarded" annotation pipeline to ensure high quality and alignment with human intent.

-   **Core Principle**: The central idea is that extensive human involvement—from data creation to quality control—is crucial for building a robust and realistic editing dataset.
-   **Methodology**: The data collection follows a four-stage process:
    1.  **Annotator Selection**: Human annotators are recruited, trained on best practices for using editing tools (DALL-E 2), and selected based on a qualifying quiz.
    2.  **Image Curation**: High-resolution, high-quality images are sourced from platforms like Unsplash and vetted by annotators for editing suitability.
    3.  **Data Pair Generation**: Annotators create diverse editing instructions, define corresponding masks, generate the edited image using DALL-E 2, and write a descriptive caption.
    4.  **Human-Rewarded Review**: Submissions undergo a two-tier quality review by administrators. High-quality submissions are rewarded and included in the dataset, while poor ones are rejected or returned for revision, ensuring the final dataset's accuracy and reliability.

## 3. Datasets Used / Presented
The paper presents the **HumanEdit** dataset, specifically designed for instruction-guided image editing.

-   **HumanEdit-full**: Contains 5,751 high-resolution image-instruction pairs. Each data point consists of an original image, an editing instruction, a corresponding mask, and the ground-truth edited image. The dataset is divided into six distinct editing categories: `Add` (801), `Remove` (1,813), `Replace` (1,370), `Action` (659), `Counting` (698), and `Relation` (410).
-   **HumanEdit-core**: A smaller subset of 400 samples from the full dataset, intended for rapid evaluation and testing.
-   **Non-Mask Editing**: Approximately 46.5% of the dataset features instructions that are detailed enough to support editing without an explicit mask, increasing its versatility.

## 4. Main Results
The authors benchmarked several state-of-the-art models on HumanEdit, providing key insights into their capabilities.

-   **Mask vs. Mask-Free**: Mask-provided models consistently and significantly outperform mask-free models across all evaluation metrics (L1, L2, CLIP-I, DINO, CLIP-T), demonstrating the value of precise region specification.
-   **Top Performing Model**: Among the benchmarked methods, **GLIDE** emerged as the top performer in the mask-provided setting, achieving the best scores on most metrics (e.g., L1 of 0.0391, CLIP-I of 0.9388 on HumanEdit-full) and across the majority of editing categories.
-   **Task Difficulty**: The results show that models handle `Add` tasks relatively well but struggle with more complex categories like `Relation` and `Action`. This highlights specific weaknesses in current models and points to clear directions for future research.
-   **Author's Takeaway**: HumanEdit serves as a high-quality, reliable benchmark that better reflects human preferences, enabling more meaningful evaluation and fostering the development of more capable and precise image editing models.

## 5. Ablation Studies  *(If none are reported, write “Not performed”)*
Not performed. The paper's contribution is a new dataset and a benchmark of existing methods, rather than a new model with components that could be ablated.

## 6. Paper Figures
![Figure 2: Overview of data collection process.]({{ '/images/12-2024/HumanEdit:_A_High-Quality_Human-Rewarded_Dataset_for_Instruction-based_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: More examples of instruction-guided image editing in HumanEdit.]({{ '/images/12-2024/HumanEdit:_A_High-Quality_Human-Rewarded_Dataset_for_Instruction-based_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: (a) The distribution chart of the first 30 objects in the editing instructions for HumanEdit. (b) The word cloud representation of the objects present in the editing instructions for HumanEdit.]({{ '/images/12-2024/HumanEdit:_A_High-Quality_Human-Rewarded_Dataset_for_Instruction-based_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 7: Qualitative comparisons between mask-provided baselines. The first three rows show the original images, corresponding masks, and ground truth edited images from DALL-E 2. The subsequent four rows present results generated by Blended Latent Diffusion SDXL, GLIDE, aMUSEd, and Meissonic, respectively.]({{ '/images/12-2024/HumanEdit:_A_High-Quality_Human-Rewarded_Dataset_for_Instruction-based_Image_Editing/figure_7.jpg' | relative_url }})
