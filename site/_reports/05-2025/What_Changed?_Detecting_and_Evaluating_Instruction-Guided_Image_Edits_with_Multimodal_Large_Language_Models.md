---
title: What_Changed?_Detecting_and_Evaluating_Instruction-Guided_Image_Edits_with_Multimodal_Large_Language_Models
layout: default
date: 2025-05-26
---
## What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models
**Authors:**
- Lorenzo Baraldi
- Rita Cucchiara, h-index: 5, papers: 40, citations: 85

**ArXiv URL:** http://arxiv.org/abs/2505.20405v1

**Citation Count:** 0

**Published Date:** 2025-05-26

![Figure 1. Qualitative examples from DICE. Our approach detects differences between an original image and an edited one, identifying the involved objects and the type of edit. Further, DICE evaluates each difference to determine its coherence with the editing prompt.]({{ '/images/05-2025/What_Changed?_Detecting_and_Evaluating_Instruction-Guided_Image_Edits_with_Multimodal_Large_Language_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of evaluating instruction-guided image editing models. Existing evaluation metrics often fail to align with human judgment and lack explainability, making it difficult to assess the quality of generated edits accurately. These metrics typically rely on global image features or opaque, pre-trained models, providing little insight into why an edit is considered good or bad. This paper aims to bridge this gap by creating an interpretable and reliable evaluation framework that analyzes edits at a local, object level.

## 2. Key Ideas and Methodology
The core idea is a two-step pipeline called **DICE (DIfference Coherence Estimator)**, which first detects localized changes and then evaluates their coherence with the user's instruction. Both steps are built upon an autoregressive Multimodal Large Language Model (MLLM).

- **Difference Detector:** This component takes an original and an edited image as input and identifies all object-level differences. For each difference, it outputs the type of edit (ADD, REMOVE, EDIT), a textual description of the change, and its bounding box coordinates. It is trained in two stages: first on pairs of similar real-world images to learn comparison, and then fine-tuned on synthetically generated inpainted images to specialize in detecting edits.
- **Coherence Estimator:** For each difference detected, this second model assesses whether the change is consistent with the user's textual editing prompt. It outputs a binary "Yes/No" decision along with a textual rationale, making the evaluation process transparent and explainable.

## 3. Datasets Used / Presented
- **LVIS:** Used to create training data for the difference detector. The authors generate 118k pairs of similar real images for pre-training and a further 97k synthetic image pairs using inpainting (LaMa, Kandinsky 2.2) for fine-tuning.
- **EmuEdit:** A small set of 116 samples from this dataset was manually annotated to train the coherence estimator.
- **DICE-D (new):** A new benchmark dataset created by the authors for evaluation. It contains 800 edited images from I2EBench, with manually annotated bounding boxes, edit commands, and coherence labels for each difference.

## 4. Main Results
- **Difference Detection:** The proposed DICE model, using Idefics3-8B as a backbone, significantly outperforms other MLLMs. It achieves a class-agnostic mean Average Precision (AP) of 22.3, a substantial improvement over Qwen2-VL (2.3 AP) and mPLUG-Owl3 (5.2 AP).
- **Coherence Estimation:** DICE accurately assesses the correctness of detected edits, achieving an AP of 15.5, far surpassing other models.
- **Correlation with Human Judgment:** When integrated with existing metrics like CLIP, DICE improves their alignment with human perception. For background preservation (CLIP-I), Pearson's correlation with human ratings increases from 51.1 to 54.5. For prompt adherence (CLIP-T), it increases from 21.5 to 24.6.

## 5. Ablation Studies
The authors performed several ablation studies to validate their design choices for the difference detector:
- **Two-Stage Training:** Training the model on both real image pairs (Stage 1) and synthetic inpainted images (Stage 2) yields the best results. Removing the first stage and training only on synthetic data reduces the class-agnostic AP from 22.3 to 16.8, demonstrating the value of the pre-training step.
- **Confidence Score:** Incorporating a predicted confidence score for each detected difference improves localization performance. Using the confidence score results in a 22.3 AP, whereas using a fixed confidence value of 1.0 lowers it to 16.8 AP.

## 6. Paper Figures
![Figure 2. Illustration of DICE. We employ an MLLM and fine-tune it for two different tasks. In the first stage (difference detection), the MLLM is trained to detect semantic differences between the original image and the edited one. In the second stage (coherence estimation), the MLLM is instructed to analyze and assess the coherence of each detected difference with respect to the given user prompt.]({{ '/images/05-2025/What_Changed?_Detecting_and_Evaluating_Instruction-Guided_Image_Edits_with_Multimodal_Large_Language_Models/figure_2.jpg' | relative_url }})
![Figure 3. Qualitative samples of DICE applied on images edited by MGIE [ 16 ] and InstructDiffusion [ 18 ] models.]({{ '/images/05-2025/What_Changed?_Detecting_and_Evaluating_Instruction-Guided_Image_Edits_with_Multimodal_Large_Language_Models/figure_3.jpg' | relative_url }})
