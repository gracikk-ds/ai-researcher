---
title: Text_Guided_Image_Editing_with_Automatic_Concept_Locating_and_Forgetting
layout: default
date: 2024-05-30
---
![Figure 1: Original image presents a red car. When the input text instruction is an image of a yellow bus , Stable Diffusion focuses on modifying the color but preserves the old shape. By analyzing the scene description of the image, concepts that users intend to edit are located and forgotten in the denoising steps for an improved output.]({{ '/images/05-2024/Text_Guided_Image_Editing_with_Automatic_Concept_Locating_and_Forgetting/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Text-guided image editing models often fail to accurately modify images according to text prompts, resulting in generations that retain unwanted attributes (e.g., shape, color) from the source image. This is due to the semantic gap between text and image modalities. Existing solutions often require manual user guidance like masks, which is not scalable.

## 2. Key Ideas and Methodology
The paper introduces "Locate and Forget" (LaF), a method that automatically identifies and removes conflicting concepts.
*   **Locate**: The model generates a caption for the input image and compares its syntactic parse tree with that of the target prompt. This comparison automatically pinpoints the concepts to be edited out.
*   **Forget**: During the diffusion process, LaF uses the target prompt for positive guidance and the identified "forgetting concepts" for negative guidance. This is achieved by extending Classifier-Free Guidance (CFG) with a controllable negative unlearning term.

## 3. Datasets Used / Presented
The method was evaluated on three benchmarks:
*   **TedBench**: 100 real-world, single-concept editing tasks.
*   **MagicBrush**: 545 complex, synthetic editing tasks.
*   **Human Prompt Generated Dataset**: 700 aesthetic-focused editing tasks.

## 4. Main Results
*   LaF significantly outperformed baselines (HIVE, IP2P, SD) in text-image alignment (CLIP-T) and editing effectiveness (CLIP-D). Unlike competitors that often copied the input, LaF successfully performed the intended semantic changes.
*   In a human study, LaF was rated highest in alignment, fidelity, and overall user preference (3.42/5).
*   The authors claim their method enhances editing results by effectively bridging the gap between textual instructions and visual reality, rather than simply replicating input content.

## 5. Ablation Studies
An ablation study was performed on the forgetting guidance coefficient (`η`).
*   A moderate `η` value (around 2.5) was found to be optimal for balancing concept removal and image quality.
*   Increasing `η` more effectively removes original attributes, but an excessively high value degrades overall semantic coherence and image quality, demonstrating the importance of this parameter.

## 6. Paper Figures
![Figure 2: Our framework for our method Locate and Forget (LaF). LaF consists of two parts: 1) Alignment of the input text prompt with the visual scene information: By comparing the textual instructions to the scene description of the image’s contents, the LaF model can identify the specific concepts and attributes in the visual scene that need to be edited. 2) Selective forgetting during the diffusion process: During the denoising steps, identified forgettable elements as a form of negative guidance to be removed, which allows to selectively forget the influence of the visual elements that are not aligned with the user’s intent.]({{ '/images/05-2024/Text_Guided_Image_Editing_with_Automatic_Concept_Locating_and_Forgetting/figure_2.jpg' | relative_url }})
![Figure 3: Visual comparisons between Hive, IP2P, SD and our method in dataset MagicBrush. The red annotations indicate the visual concepts in the original image that need to be edited, while the blue annotations represent the new visual elements that should be introduced based on the provided textual prompt.]({{ '/images/05-2024/Text_Guided_Image_Editing_with_Automatic_Concept_Locating_and_Forgetting/figure_3.jpg' | relative_url }})
![Figure 4: Visual editing results under Varying Forgetting Guidance η . Example images are respectively "Skillet filled with salami, broccoli and other vegetables." and "A tennis ball on a tennis court."]({{ '/images/05-2024/Text_Guided_Image_Editing_with_Automatic_Concept_Locating_and_Forgetting/figure_4.jpg' | relative_url }})
![Figure 5: Impact of Forgetting Guidance values on CLIP-T across different Datasets]({{ '/images/05-2024/Text_Guided_Image_Editing_with_Automatic_Concept_Locating_and_Forgetting/figure_5.jpg' | relative_url }})
![Figure 6: Impact of Forgetting Guidance values on IS across different Datasets]({{ '/images/05-2024/Text_Guided_Image_Editing_with_Automatic_Concept_Locating_and_Forgetting/figure_6.jpg' | relative_url }})
