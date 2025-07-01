---
title: New_Job,_New_Gender?_Measuring_the_Social_Bias_in_Image_Generation_Models
layout: default
date: 2024-01-01
---
![Figure 1: Examples of Biased Generation Detected by BiasPainter.]({{ '/images/01-2024/New_Job,_New_Gender?_Measuring_the_Social_Bias_in_Image_Generation_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the critical problem of social bias in modern image generation models. They argue that existing methods for evaluating this bias are inadequate, suffering from low accuracy (e.g., 40% for race detection), a reliance on costly and unscalable manual annotation, and a lack of comprehensive analysis across diverse demographic groups. This gap hinders the ability of developers to effectively identify and mitigate harmful stereotypes perpetuated by these AI systems.

## 2. Key Ideas and Methodology
The paper introduces **BiasPainter**, an automated framework for measuring social bias. Its core principle is that when an image of a person is edited using a demographically neutral prompt (e.g., "a photo of a lawyer"), the person's core attributes—gender, race, and age—should not change.

The methodology involves five stages:
1.  **Collect Seed Images:** A diverse set of 54 photos of people across different races, genders, and ages is collected.
2.  **Collect Neutral Prompts:** A list of 228 gender-, race-, and age-neutral prompts is compiled, covering professions, personality traits, objects, and activities.
3.  **Generate Images:** Each seed image is edited by the target model using every prompt.
4.  **Assess Properties:** The framework automatically assesses the gender, race (via skin tone), and age of the person in both the original and edited images using computer vision techniques and the Face++ API.
5.  **Detect Bias:** It quantifies the change between the original and edited images. Significant and consistent changes for a given prompt reveal a learned bias in the model.

## 3. Datasets Used / Presented
- **Seed Images:** 54 images were manually selected from the **VGG-Face2** dataset, representing 3 races (White, Black, East Asian), 2 genders, and 3 age groups.
- **Neutral Prompts:** 228 prompts were created from lists sourced from the U.S. Bureau of Labor Statistics and various dictionaries, then manually filtered to ensure demographic neutrality. The prompts cover 62 professions, 70 personality traits, 57 objects, and 39 activities.

## 4. Main Results
- **High Accuracy:** Human evaluation confirmed that BiasPainter's automatic bias detection is **90.8% accurate**, a significant improvement over prior work.
- **Bias Identification:** The framework successfully identified specific biases in six major models (including Stable Diffusion, Midjourney, and DALL-E 2). For example, models consistently associated "secretary" with females and "CEO" with males, and "brave" with older individuals.
- **Model Comparison:** Stable Diffusion models were found to be generally more biased than others. InstructPix2Pix exhibited the least bias concerning age and gender.
- **Mitigation Potential:** The authors demonstrated that insights from BiasPainter can guide bias mitigation. Adding a simple corrective phrase to a prompt ("maintain the same gender") reduced, but did not eliminate, the measured bias.

## 5. Ablation Studies
The authors performed ablation studies to determine the optimal thresholds for detecting significant changes in age and race (skin tone).
- **Age Threshold:** They tested age difference thresholds of 15, 25, and 35 years. A threshold of **25 years** was found to best align with human perception of a significant age change.
- **Race (Skin Tone) Threshold:** They tested grayscale value difference thresholds of 10, 20, and 30. A threshold of **20** was selected as it best matched human judgments of a significant change in skin tone.

## 6. Paper Figures
![Figure 2: The Overview Framework of BiasPainter]({{ '/images/01-2024/New_Job,_New_Gender?_Measuring_the_Social_Bias_in_Image_Generation_Models/figure_2.jpg' | relative_url }})
![Figure 3: Image Processing Pipeline to Access the Skin Tone Information]({{ '/images/01-2024/New_Job,_New_Gender?_Measuring_the_Social_Bias_in_Image_Generation_Models/figure_3.jpg' | relative_url }})
![Figure 4: Visualization of Profession Word Bias Scores in Stable Diffusion 1.5]({{ '/images/01-2024/New_Job,_New_Gender?_Measuring_the_Social_Bias_in_Image_Generation_Models/figure_4.jpg' | relative_url }})
