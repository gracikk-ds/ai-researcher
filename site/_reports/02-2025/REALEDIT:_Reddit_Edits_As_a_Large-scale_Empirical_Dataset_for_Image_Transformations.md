---
title: REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations
layout: default
date: 2025-02-05
---
## REALEDIT: Reddit Edits As a Large-scale Empirical Dataset for Image Transformations
**Authors:**
- Peter Sushko, h-index: 1, papers: 1, citations: 1
- Ranjay Krishna, h-index: 7, papers: 13, citations: 196

**ArXiv URL:** http://arxiv.org/abs/2502.03629v2

**Citation Count:** 1

**Published Date:** 2025-02-05

![Figure 1. We visualize edits made by our model. We introduce R EAL E DIT , a large-scale image editing dataset sourced from Reddit with real-world user edit requests and human-edits. By finetuning on R EAL E DIT , our resultant model outperforms existing models by up to 165 Elo points with human judgment and delivers real world utility to real user requests online.]({{ '/images/02-2025/REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing image editing models, despite performing well on academic benchmarks, struggle to meet the demands of real-world users. The authors identify a critical gap: the datasets used to train these models rely on synthetic or artificially generated edits, which lack the diversity and ecological validity of authentic user requests. This misalignment results in models that fail at common, practical tasks like photo restoration or subtle object removal, which are frequently requested in online communities like Reddit.

## 2. Key Ideas and Methodology
The paper's core idea is to bridge the gap between model capabilities and user needs by creating a dataset of real-world image editing tasks. The authors introduce **REALEDIT**, a large-scale dataset sourced from authentic user requests and human-provided edits on Reddit.

Their methodology consists of three main parts:
1.  **Dataset Curation**: They collected over 57,000 image-instruction-edit triplets from the r/PhotoshopRequest and r/estoration subreddits. User-provided instructions were automatically refined using a Vision-Language Model (VLM) to be clear and concise.
2.  **Model Finetuning**: They finetuned an existing model, InstructPix2Pix, on the 48K training examples from REALEDIT. This adapts the model to the distribution of real-world editing tasks.
3.  **Inference Enhancement**: To improve the generation quality of human faces and fine details—a common focus in real requests—they replaced the model's standard decoder with OpenAI's Consistency Decoder during inference.

## 3. Datasets Used / Presented
The paper introduces one primary dataset:
*   **REALEDIT**: A new, large-scale dataset for text-guided image editing. It contains over 57,000 examples (48K for training and 9.3K for testing), comprising a total of 151,000 images (input and human-edited outputs). The data is sourced from Reddit posts between 2012 and 2021, reflecting genuine user needs such as photo restoration, object removal, and creative edits. It was used to train and benchmark the authors' proposed model and to demonstrate its utility in improving fake image detection.

## 4. Main Results
The model trained on REALEDIT demonstrated superior performance over existing state-of-the-art models on real-world tasks.
*   **Human Evaluation**: The proposed model achieved an Elo rating of **1184**, outperforming the next-best baseline by **165 points** in pairwise comparisons by human judges.
*   **Automated Metrics**: The model achieved a VIEScore (an automated metric for overall quality) of **3.68**, a **92% relative improvement** over the next-best score of 1.89.
*   **Broader Impact**: The REALEDIT dataset was used to improve a deepfake detection model, increasing its F1-score by **14 percentage points** on an in-the-wild test set, underscoring the dataset's value beyond image editing.

## 5. Ablation Studies
The authors performed several ablation studies to validate their design choices:

*   **Instruction Processing**: They compared a model trained on raw, noisy user instructions with one trained on instructions refined by GPT-4. Using the refined instructions improved model performance, increasing the overall VIEScore (VIE_O) from 2.06 to 2.42.
*   **Data Filtering**: A model was trained on a filtered subset of REALEDIT, aligned with the pre-training distribution of the InstructPix2Pix backbone, versus the original, more diverse data. The filtering process significantly improved performance, boosting the VIE_O score from 2.35 to 3.48.
*   **Consistency Decoder**: The effect of adding OpenAI's Consistency Decoder at inference was tested. While it caused a minor drop in quantitative metrics (e.g., VIE_O from 3.54 to 3.48), it provided significant qualitative improvements in the aesthetic generation of faces, patterns, and other fine details.

## 6. Paper Figures
![Figure 2. Baselines struggle on simple, practical tasks, such as restoring a damaged photograph. Our model is successful.]({{ '/images/02-2025/REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations/figure_2.jpg' | relative_url }})
![Figure 3. Dataset curation pipeline. We source data from r/estoration and r/PhotoshopRequest. From the posts, we extract input images and edit instructions. The instructions are processed using a VLM to isolate the editing task. From the comments, we collect up to 5 human-edited outputs per post.]({{ '/images/02-2025/REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations/figure_3.jpg' | relative_url }})
![Figure 4. Key differences in the distribution of our test set compared to MagicBrush and Emu Edit test sets. MagicBrush and Emu Edit tend to be similar in distribution to each other, but starkly different from R EAL E DIT .]({{ '/images/02-2025/REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations/figure_4.jpg' | relative_url }})
![Figure 5. Real requests completed on Reddit. We deployed our model on r/PhotoshopRequest to complete in-the-wild requests. We received positive feedback from users on the examples above.]({{ '/images/02-2025/REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations/figure_5.jpg' | relative_url }})
![Figure 6. The baseline misclassifies both images as real, whereas our model correctly spots the fake (right) that spawned the 2005 Paris Hilton “Stop Being Poor” meme.]({{ '/images/02-2025/REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations/figure_6.jpg' | relative_url }})
![Figure 7. Examples of the R EAL E DIT model on R EAL E DIT test set images compared to other editing models. Our edits are often more semantically correct as well as more visually appealing.]({{ '/images/02-2025/REALEDIT:_Reddit_Edits_As_a_Large-scale_Empirical_Dataset_for_Image_Transformations/figure_7.jpg' | relative_url }})
