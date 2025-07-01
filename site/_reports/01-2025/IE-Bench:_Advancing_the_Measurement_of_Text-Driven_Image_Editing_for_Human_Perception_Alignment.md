---
title: IE-Bench:_Advancing_the_Measurement_of_Text-Driven_Image_Editing_for_Human_Perception_Alignment
layout: default
date: 2025-01-17
---
![Figure 3. Statistics of IE-DB prompts. (a) Word cloud of IE-Bench DB prompts. (b) Proportion of different types]({{ '/images/01-2025/IE-Bench:_Advancing_the_Measurement_of_Text-Driven_Image_Editing_for_Human_Perception_Alignment/figure_3.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of accurately evaluating text-driven image editing models. Existing evaluation metrics often fail to align with human perception because they either assess quality from a single perspective (e.g., only text-image consistency or only source-image similarity) or they are designed for text-to-image generation and ignore the crucial input of the source image. The relationship between the source and edited image is dynamic and context-dependent, requiring a more nuanced evaluation approach. This work aims to fill the gap by providing a dedicated benchmark suite, including a dataset and a metric, that holistically evaluates edited images by considering the source image, text prompt, and alignment with human judgment.

## 2. Key Ideas and Methodology
The paper introduces **IE-Bench**, a benchmark suite comprising a new dataset (**IE-DB**) and a novel evaluation model (**IE-QA**).

The core idea of **IE-QA** is to create a source-aware, multi-modal quality assessment model that mirrors human evaluation. The model's architecture is designed to assess three key aspects simultaneously:
1.  **Image-Text Alignment**: A text-visual branch uses CLIP encoders and cross-attention to measure how well the edited image conforms to the text prompt.
2.  **Source-Target Relationship**: A dedicated branch explicitly models the connection between the source and edited images. It extracts features from both using a visual encoder, concatenates them, and processes them to measure appropriate preservation or modification of content.
3.  **Visual Quality**: The model incorporates techniques from high-performing no-reference image quality assessment (IQA) methods to evaluate the overall aesthetic and technical quality of the edited image.

The model is trained to predict human-provided Mean Opinion Scores (MOS) using a combined correlation and ranking loss function.

## 3. Datasets Used / Presented
The paper presents a new dataset called the **Text-driven Image Editing Database (IE-DB)**, which was created to train and validate the IE-QA model.
*   **Name**: IE-DB
*   **Size & Composition**: The dataset contains 301 diverse source images (from real-world, CG, AIGC, and art sources), paired with manually crafted editing prompts. These prompts were used with 5 different image editing models to generate a collection of edited images.
*   **Annotations**: The dataset includes a total of **3,010 Mean Opinion Scores (MOS)** collected from 25 human subjects who rated the quality of the edited images based on text-image consistency and source-target fidelity.

## 4. Main Results
The proposed IE-QA model demonstrates superior performance in aligning with human subjective scores compared to existing metrics. When evaluated on the IE-DB dataset using 10-fold cross-validation, IE-QA achieved the following scores (higher is better for SROCC/PLCC/KRCC, lower for RMSE):
*   **SROCC**: 0.7520
*   **PLCC**: 0.7498
*   **KRCC**: 0.5541
*   **RMSE**: 1.045

These results significantly outperform prior IQA methods like IP-IQA (SROCC of 0.6124) and human-aligned metrics like HPS-v2 (SROCC of 0.2111), as well as objective metrics like CLIP-T (SROCC of 0.1503). The author-claimed takeaway is that explicitly modeling the source-target relationship and text-image alignment is critical for creating an evaluation metric that accurately reflects human perception of image editing quality.

## 5. Ablation Studies
The authors performed several ablation experiments to validate the contributions of each component of the IE-QA model.
*   **Text-Image Alignment**: Removing the text-image alignment module caused a significant drop in performance (SROCC decreased from 0.7520 to 0.6949), confirming the importance of evaluating adherence to the text prompt.
*   **Source Connection**: Removing the source image as an input and its corresponding branch also degraded performance (SROCC fell to 0.7103), proving that awareness of the source image is essential for accurate evaluation.
*   **Source-Target Fusion**: Comparing different fusion strategies, simple feature concatenation (SROCC 0.7520) was found to be more effective than cross-attention (SROCC 0.7422).
*   **Additional Parameters**: An experiment was run to ensure the performance gain was not merely due to an increased parameter count from the source branch. The model with the source branch removed but with an equivalent number of parameters added elsewhere performed worse (SROCC 0.7354), demonstrating that the model's architectural design, not just its size, is responsible for the improvement.

## 6. Paper Figures
![Figure 4. Z-score MOS distributions of different editing methods.]({{ '/images/01-2025/IE-Bench:_Advancing_the_Measurement_of_Text-Driven_Image_Editing_for_Human_Perception_Alignment/figure_4.jpg' | relative_url }})
![Figure 5. Network architecture of IE-QA.]({{ '/images/01-2025/IE-Bench:_Advancing_the_Measurement_of_Text-Driven_Image_Editing_for_Human_Perception_Alignment/figure_5.jpg' | relative_url }})
![Figure 6. Demo of scores in IE-QA.]({{ '/images/01-2025/IE-Bench:_Advancing_the_Measurement_of_Text-Driven_Image_Editing_for_Human_Perception_Alignment/figure_6.jpg' | relative_url }})
