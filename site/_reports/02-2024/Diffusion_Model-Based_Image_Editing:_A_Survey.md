---
title: Diffusion_Model-Based_Image_Editing:_A_Survey
layout: default
date: 2024-02-27
---
![Fig. 1: Statistical overview of research publications in diffusion model-based image editing. Top: learning strategies. Middle: input conditions. Bottom: editing tasks.]({{ '/images/02-2024/Diffusion_Model-Based_Image_Editing:_A_Survey/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the gap in academic literature concerning diffusion model-based image editing. While diffusion models have become a dominant tool for image generation and editing, existing survey papers tend to focus on broader topics like image generation or restoration, or provide only a cursory overview of image editing. This paper aims to provide the first exhaustive and dedicated survey specifically on 2D image editing using diffusion models, offering a structured and in-depth analysis of the rapidly growing body of work in this subfield.

## 2. Key Ideas and Methodology
The paper's primary contribution is a comprehensive categorization of over 100 diffusion-based image editing methods from multiple perspectives:
*   **Learning Strategy**: Methods are grouped into three main classes: *training-based* (requiring extensive pre-training), *testing-time finetuning* (requiring per-image optimization), and *training/finetuning-free* (working off-the-shelf).
*   **Input Conditions**: The survey analyzes the 10 most common types of user inputs that guide the editing process, such as text, masks, reference images, and sketches.
*   **Editing Tasks**: The paper classifies editing capabilities into three broad categories—semantic, stylistic, and structural—covering 12 specific task types.

Beyond the survey, the authors introduce **EditEval**, a new systematic benchmark for evaluating text-guided image editing methods. A key part of this benchmark is a novel quantitative metric, **LMM Score**, which leverages the visual-language understanding of Large Multimodal Models (LMMs) like GPT-4V to assess the quality of edited images based on four criteria: Editing Accuracy, Contextual Preservation, Visual Quality, and Logical Realism.

## 3. Datasets Used / Presented
The authors present **EditEval**, a new benchmark dataset constructed for evaluating image editing methods.
*   **Name**: EditEval
*   **Content**: It consists of 150 high-quality, diverse images sourced from the Unsplash repository.
*   **Usage**: Each image is paired with a source text description, a target text description, and a corresponding editing instruction, all generated with the help of GPT-4V. The dataset is organized to cover 7 common editing tasks, including object addition, object removal, style change, and action change. It is used to quantitatively and qualitatively evaluate a wide range of state-of-the-art editing algorithms.

## 4. Main Results
The evaluation conducted using the EditEval benchmark yielded several key insights:
*   No single editing method consistently outperforms others across all tasks, and most methods exhibit significant performance variance depending on the specific image and instruction.
*   The proposed **LMM Score** shows a very strong Pearson correlation with subjective scores from a human user study (correlation coefficients often above 0.85), validating it as a reliable and scalable alternative to human evaluation.
*   When compared to existing metrics like CLIPScore and TIFA Score, the LMM Score demonstrates a significantly higher alignment with human judgments across all seven tested editing tasks, making it a more faithful metric for this domain.

The authors conclude that their systematic categorization and the new EditEval benchmark provide a valuable resource for understanding and advancing the field of diffusion-based image editing.

## 5. Ablation Studies
While not a traditional model-focused paper, the authors conduct comparative analyses to validate their proposed LMM Score metric:

*   **Metric Comparison**: The LMM Score was compared against three other metrics: CLIPScore, Directional CLIP Similarity, and TIFA Score. The comparison, based on correlation with human user study results, showed that LMM Score consistently achieved the highest correlation across all 7 editing tasks. For instance, in tasks like "Object Addition" and "Style Change," LMM Score's correlation was significantly higher than the others, which struggled to align with user preferences.

*   **Metric Component Analysis**: The paper analyzed the correlation between each of the four sub-scores of the LMM Score (Editing Accuracy, Contextual Preservation, Visual Quality, Logical Realism) and the corresponding scores from the user study. The results showed a strong alignment for all components, particularly for "Editing Accuracy," which had a correlation coefficient above 0.87 for most tasks. This confirms that the metric's design effectively captures the distinct aspects of quality that humans perceive.

## 6. Paper Figures
![Fig. 3: Common framework of instructional image editing methods. The sample images are from InstructPix2Pix [179], InstructAny2Pix [189] and MagicBrush [275].]({{ '/images/02-2024/Diffusion_Model-Based_Image_Editing:_A_Survey/figure_3.jpg' | relative_url }})
![Fig. 4: Testing-time finetuning framework with different finetuning components. The sample images are from Custom-Edit [196].]({{ '/images/02-2024/Diffusion_Model-Based_Image_Editing:_A_Survey/figure_4.jpg' | relative_url }})
