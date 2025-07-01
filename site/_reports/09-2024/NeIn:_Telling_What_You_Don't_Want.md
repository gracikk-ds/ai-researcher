---
title: NeIn:_Telling_What_You_Don't_Want
layout: default
date: 2024-09-09
---
![Figure 1. The failures of recent text-guided image editing methods in understanding the negative queries.]({{ '/images/09-2024/NeIn:_Telling_What_You_Don't_Want/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a significant gap in text-guided image editing: the inability of Vision-Language Models (VLMs) to understand negation. While humans frequently use negative instructions (e.g., "a street scene *without* a car"), standard vision-language datasets are heavily biased towards positive descriptions, containing very few negative examples. This causes even state-of-the-art models to fail on negative queries, often paradoxically adding the object they were instructed to exclude. The paper aims to solve this problem by creating a dedicated resource for training and evaluating negation understanding.

## 2. Key Ideas and Methodology
The paper's core contribution is the creation of **NeIn (Negative Instruction)**, the first large-scale dataset designed to teach and benchmark negation in image editing. The central hypothesis is that models can learn to understand negation if provided with sufficient and appropriate training data.

The methodology is an automated two-stage pipeline built on existing VLMs:
1.  **Generation:** For a source image from the MS-COCO dataset, the pipeline first uses BLIP to identify objects that are *not* present in the image. It then formulates a "negative instruction" describing the source image (e.g., "The image does not have a boat"). Finally, it uses a fine-tuned InstructPix2Pix model to generate a synthetic target image that *contains* the absent object, creating a counter-example.
2.  **Filtering:** To ensure data quality, the generated samples are filtered. BLIP and LLaVA-NeXT are used to discard pairs where the generated image is low-quality, does not contain the new object, or has deviated too far from the original image content.

## 3. Datasets Used / Presented
The paper introduces the **NeIn** dataset, which is derived from MS-COCO.
*   **Name:** NeIn (Negative Instruction)
*   **Size:** It contains 366,957 quintuplets in total, where each quintuplet consists of a source image, original caption, selected object, negative sentence, and a synthetic target image.
*   **Usage:** The dataset is split into a training set of 342,775 queries and an evaluation set of 24,182 queries, intended for fine-tuning and benchmarking image editing models on their ability to handle negation.

## 4. Main Results
The authors benchmarked five state-of-the-art image editing models and found that they all struggled with negative instructions out-of-the-box.
*   Baseline models like InstructPix2Pix and MagicBrush achieved very low **Removal Scores** (3.8% and 5.1% respectively, via LLaVA-NeXT), indicating they failed to remove the specified object. They also had poor image quality scores (e.g., high FID).
*   However, after fine-tuning these same models on the NeIn training set, their performance improved dramatically. The fine-tuned InstructPix2Pix and MagicBrush models achieved **Removal Scores of 93.6% and 92.2%**, respectively, and high **Retention Scores** (~98%), showing they could correctly remove the specified object while preserving the rest of the image.

The author-claimed takeaway is that existing VLMs fail at negation due to a data gap, and fine-tuning on the NeIn dataset effectively teaches them this crucial linguistic capability.

## 5. Ablation Studies
The paper's primary comparative analysis functions as an ablation on the impact of the NeIn dataset. The authors compare the performance of two key models, InstructPix2Pix and MagicBrush, with and without being fine-tuned on NeIn.

*   **Experiment:** The performance of the original, pre-trained models was compared against versions that were fine-tuned on the NeIn training set.
*   **Impact:** The results demonstrated a massive improvement across all metrics for the fine-tuned models. For example, fine-tuning InstructPix2Pix on NeIn caused its Removal Score (measured by LLaVA-NeXT) to jump from 3.8% to 93.6% and its FID (image realism) score to improve from 10.60 to 4.08. This directly validates the effectiveness of the NeIn dataset for teaching models to understand and execute negative commands.

## 6. Paper Figures
![Figure 2. The process to create our dataset. It consists of two main steps: generation and filtering. ITM and VQA are image-text matching and visual question answering, respectively.]({{ '/images/09-2024/NeIn:_Telling_What_You_Don't_Want/figure_2.jpg' | relative_url }})
![Figure 3. Illustration for fine-tuning and benchmarking process.]({{ '/images/09-2024/NeIn:_Telling_What_You_Don't_Want/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative results of five SOTA methods on NeIn’s evaluation samples (first two samples) and random image-prompt pairs (last two samples). The fine-tuned InstructPix2Pix ( 3 rd column) and MagicBrush ( 5 th column) on NeIn’s training set are highlighted.]({{ '/images/09-2024/NeIn:_Telling_What_You_Don't_Want/figure_4.jpg' | relative_url }})
