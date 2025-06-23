---
title: response_mgie_gemini-2
layout: default
---
![Figure 1: We introduce MLLM-Guided Image Editing (MGIE) to improve instruction-based image editing for various editing aspects. The top is the input instruction, and the right is the jointly derived expressive instruction by MGIE.]({{ '/images/mgie/figure_1.png' | relative_url }})

*Figure 1: We introduce MLLM-Guided Image Editing (MGIE) to improve instruction-based image editing for various editing aspects. The top is the input instruction, and the right is the jointly derived expressive instruction by MGIE.*


## 1. Motivation of the Paper
The authors address a key limitation in instruction-based image editing: human commands are often too brief and ambiguous for models to interpret correctly. For example, an instruction like "make it more healthy" is context-dependent and lacks specific detail. Existing methods, which often rely on text encoders trained for static image description (like CLIP), struggle to capture the *transformative intent* behind such commands, leading to inaccurate or unintended edits.

## 2. Key Ideas and Methodology
The paper introduces **MLLM-Guided Image Editing (MGIE)**, a framework that leverages a Multimodal Large Language Model (MLLM) to bridge the gap between brief human commands and the explicit guidance needed for high-quality editing.

*   **Core Idea:** The central principle is to use an MLLM to derive a more detailed and explicit "expressive instruction" by reasoning over both the input image and the user's brief command. For instance, given an image of a pizza and the instruction "make it more healthy," the MLLM might generate the expressive instruction, "The pizza includes vegetable toppings, such as tomatoes and herbs."

*   **Methodology:** MGIE consists of two main components trained jointly in an end-to-end manner:
    1.  **MLLM for Guidance:** An MLLM is trained to generate concise, expressive instructions. It then produces latent visual tokens that represent the "imagination" of the intended edit.
    2.  **Guided Diffusion Model:** A lightweight "edit head" transforms these visual tokens into actionable guidance for a latent diffusion model. The diffusion model uses this guidance, along with the original image, to perform the edit, ensuring that changes are applied accurately while preserving irrelevant regions.

## 3. Datasets Used / Presented
*   **Pre-training:** The model is pre-trained on **IPr2Pr**, a large-scale dataset containing 1 million image-instruction-goal triplets.
*   **Evaluation:** Performance is comprehensively evaluated on four diverse benchmarks, each targeting a different editing style:
    *   **EVR (5.7K examples):** Photoshop-style modifications.
    *   **GIER (29.9K examples):** Global photo optimization (e.g., color, tone).
    *   **MA5k (24.8K examples):** Adjustments to photo properties like contrast and brightness.
    *   **MagicBrush (10.5K examples):** Localized, fine-grained object editing.

## 4. Main Results
*   MGIE significantly outperforms the state-of-the-art baseline (InstructPix2Pix) and a text-only LLM variant (LGIE) across all four evaluation datasets in both zero-shot and fine-tuned settings.
*   In zero-shot evaluation on the MagicBrush dataset, MGIE improves the DINO visual similarity score from 71.46 to 82.22 and the CLIP Visual Similarity (CVS) from 85.22 to 91.14, indicating much better alignment with the intended edit.
*   Human evaluations corroborate the quantitative findings. Users rated MGIE's outputs as superior in terms of instruction following, relevance to the ground truth, and overall quality.
*   The authors conclude that deriving explicit, visually-aware expressive instructions is crucial for enhancing the performance and reliability of instruction-based image editing.

## 5. Ablation Studies
*   **Training Strategy:** The authors compared their end-to-end (E2E) training with pipeline approaches (using expressive instructions with a frozen or fine-tuned baseline). The E2E approach performed best, demonstrating that jointly training the MLLM and diffusion model is critical for learning to effectively use the generated guidance.
*   **Instruction Loss:** Removing the loss for training the MLLM to generate concise instructions (`L_ins`) caused a significant drop in performance, highlighting the importance of explicitly learning to produce high-quality guidance.
*   **Prompting Strategy:** An ablation on the prompt used to generate expressive instructions showed that asking "what will this image be like if..." yielded more relevant visual guidance than asking "how to edit this image...".
*   **Number of Visual Tokens:** Performance was found to improve with up to 4 visual tokens for guidance and then plateaued, indicating that a small number of tokens is sufficient to convey the editing intent.

## 6. Paper Figures
![Figure 10: CLIP-S across images and expressive instructions (full / short / summarized).]({{ '/images/mgie/figure_10.png' | relative_url }})

*Figure 10: CLIP-S across images and expressive instructions (full / short / summarized).*


![Figure 11: CLIP-S across images and expressive instructions by the “ how ” or “ what ” prompt.]({{ '/images/mgie/figure_11.png' | relative_url }})

*Figure 11: CLIP-S across images and expressive instructions by the “ how ” or “ what ” prompt.*


![Figure 2: Overview of MLLM-Guided Image Editing ( MGIE ), which leverages MLLMs to enhance instruction-based image editing. MGIE learns to derive concise expressive instructions and provides explicit visual-related guidance for the intended goal. The diffusion model jointly trains and achieves image editing with the latent imagination through the edit head in an end-to-end manner.]({{ '/images/mgie/figure_2.png' | relative_url }})

*Figure 2: Overview of MLLM-Guided Image Editing ( MGIE ), which leverages MLLMs to enhance instruction-based image editing. MGIE learns to derive concise expressive instructions and provides explicit visual-related guidance for the intended goal. The diffusion model jointly trains and achieves image editing with the latent imagination through the edit head in an end-to-end manner.*


![Figure 3: Trade-off curve for image editing . We set α X as 7.5 and vary α V in [1 . 0 , 2 . 2] . For both edit (X-axis) and input consistency (Yaxis), higher is better.]({{ '/images/mgie/figure_3.png' | relative_url }})

*Figure 3: Trade-off curve for image editing . We set α X as 7.5 and vary α V in [1 . 0 , 2 . 2] . For both edit (X-axis) and input consistency (Yaxis), higher is better.*


![Figure 4: CLIP-S across images (input / goal) and expressive instructions.]({{ '/images/mgie/figure_4.png' | relative_url }})

*Figure 4: CLIP-S across images (input / goal) and expressive instructions.*


![Figure 5: Human eval of expressive instructions quality.]({{ '/images/mgie/figure_5.png' | relative_url }})

*Figure 5: Human eval of expressive instructions quality.*


![Figure 6: Human eval of image editing results in terms of instruction following, ground-truth relevance, and overall quality.]({{ '/images/mgie/figure_6.png' | relative_url }})

*Figure 6: Human eval of image editing results in terms of instruction following, ground-truth relevance, and overall quality.*


![Figure 7: Qualitative comparison between InsPix2Pix, LGIE, and our MGIE. For the 1st example, MGIE can showcase the clear “ lightning ” in the sky and its reflection on the water. For the 2nd one, although LGIE accurately targets the Christmas tree, only MGIE removes it in the background. For photo optimization (the 3rd example), InsPix2Pix fails to adjust the brightness, and LGIE makes the whole photo white and obviously distinct. In contrast, MGIE follows the instruction to brighten as well as sharpen it. Moreover, in the 4th one, MGIE puts the “ glaze ” only on the donuts, but baselines even draw the entire image in strawberry pink.]({{ '/images/mgie/figure_7.png' | relative_url }})

*Figure 7: Qualitative comparison between InsPix2Pix, LGIE, and our MGIE. For the 1st example, MGIE can showcase the clear “ lightning ” in the sky and its reflection on the water. For the 2nd one, although LGIE accurately targets the Christmas tree, only MGIE removes it in the background. For photo optimization (the 3rd example), InsPix2Pix fails to adjust the brightness, and LGIE makes the whole photo white and obviously distinct. In contrast, MGIE follows the instruction to brighten as well as sharpen it. Moreover, in the 4th one, MGIE puts the “ glaze ” only on the donuts, but baselines even draw the entire image in strawberry pink.*


![Figure 8: Qualitative comparison of expressive instructions by LGIE and our MGIE. Due to the limitation of the single modality, LGIE can only have language-based insight but may derive irrelevant or even wrong explanations for image editing ( e.g. , “ two people still in the foreground ” for GIER). With access to images, MGIE provides explicit visual imagination after the editing such as “ baby on the beach with a shark ” or “ bring out details of leaves and trunk ”. More surprisingly, we can link “ lightsaber or spaceship ” from Star Wars and describe “ chewing on the stick ” for the dog, which is aligned with the intended goal.]({{ '/images/mgie/figure_8.png' | relative_url }})

*Figure 8: Qualitative comparison of expressive instructions by LGIE and our MGIE. Due to the limitation of the single modality, LGIE can only have language-based insight but may derive irrelevant or even wrong explanations for image editing ( e.g. , “ two people still in the foreground ” for GIER). With access to images, MGIE provides explicit visual imagination after the editing such as “ baby on the beach with a shark ” or “ bring out details of leaves and trunk ”. More surprisingly, we can link “ lightsaber or spaceship ” from Star Wars and describe “ chewing on the stick ” for the dog, which is aligned with the intended goal.*


![Figure 9: CLIP-S across images and expressive instructions by different sizes of MGIE.]({{ '/images/mgie/figure_9.png' | relative_url }})

*Figure 9: CLIP-S across images and expressive instructions by different sizes of MGIE.*
