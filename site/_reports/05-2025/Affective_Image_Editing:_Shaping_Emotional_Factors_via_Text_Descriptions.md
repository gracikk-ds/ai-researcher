---
title: Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions
layout: default
date: 2025-05-24
---
![Fig. 1 Illustration of the proposed AIEdiT method: Given text descriptions that express users’ emotional requests, AIEdiT creates affective images that evoke specific emotions through fine-grained text descriptions. In comparison, general text-driven editing methods ( e.g. , MagicBrush ( Zhang et al , 2024 ) and InstructPix2Pix ( Brooks et al , 2023 )) fail to translate users’ emotional requests. Meanwhile, relevant affective image editing methods either focus on limited emotional factors ( e.g. , color tune in AIFormer ( Weng et al , 2023 )) or use coarse-grained control instructions ( e.g. , emotion categories in EmoEdit ( Yang et al , 2025 )).]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key limitation in existing text-driven image editing methods: their inability to understand and execute users' emotional requests. While general editing models focus on literal instructions, current affective editing methods are too restrictive. They either manipulate limited emotional factors (e.g., only color tone) or rely on coarse-grained emotion categories (e.g., "happy," "sad"), which prevents users from expressing nuanced and subjective feelings. The paper aims to bridge this gap by developing a method that can comprehensively shape multiple emotional factors across an image based on fine-grained, descriptive text.

## 2. Key Ideas and Methodology
The paper introduces **AIEdiT**, a novel framework for Affective Image Editing using Text descriptions. Its core principle is to translate abstract emotional requests into concrete visual manipulations.

- **High-level Approach:** AIEdiT is built upon a pre-trained latent diffusion model. It uses a multi-stage process to interpret and apply emotional edits.
- **Key Components:**
    1.  **Emotional Spectrum:** A continuous emotional embedding space is constructed using a BERT encoder and contrastive learning. This component captures universal emotional priors from text, allowing the model to understand the relationships between different emotional expressions.
    2.  **Emotional Mapper:** A Transformer-based module translates the abstract emotional request (from the Emotional Spectrum) and text semantics (from CLIP) into a visually-concrete representation that can effectively guide the diffusion model's denoising process.
    3.  **MLLM Supervision:** To ensure the edited images accurately evoke the intended emotion without requiring a target image, a Multimodal Large Language Model (MLLM) is used as a supervisor during training. The MLLM provides rich, multi-faceted descriptions of emotional cues in an image, and the model is trained to align its output with these descriptions.

## 3. Datasets Used / Presented
The authors introduce the **EmoTIPS** (Emotion-aligned Text and Image Pair Set) dataset to facilitate the training and evaluation of their model.

- **Name & Size:** EmoTIPS contains 1 million affective images, with 3,000 samples reserved for evaluation.
- **Domain & Creation:** The images are sourced from the EmoSet dataset. For each image, a corresponding emotional text description was generated using an MLLM (ShareGPT4V) guided by a Chain-of-Thought prompting strategy. The dataset was then filtered using automated validation criteria (keyword detection, emotion classification, text-image retrieval) and human evaluation to ensure high quality and emotional consistency.
- **Use:** The dataset is used to train the emotional spectrum and the emotional mapper, and to evaluate the final performance of AIEdiT.

## 4. Main Results
AIEdiT demonstrates superior performance over existing state-of-the-art methods in both quantitative and qualitative evaluations.

- **Quantitative Insights:** Compared to general text-editing (e.g., ControlNet) and affective-editing (e.g., EmoEdit) methods, AIEdiT achieved the best scores across all metrics:
    - **Image Quality (FID):** 27.93 (lower is better)
    - **Semantic Clarity (Sem-C):** 0.685 (higher is better)
    - **Emotional Alignment (KLD):** 2.4373 (lower is better)
- **User Study:** In a user preference study, AIEdiT was preferred 39.68% of the time, significantly outperforming all other methods.
- **Author-claimed Impact:** The results show that AIEdiT can successfully interpret nuanced emotional requests from text and manipulate corresponding visual factors to produce high-quality, emotionally faithful images.

## 5. Ablation Studies
The authors performed a series of ablation studies to validate the contribution of each key component of AIEdiT. Removing any component resulted in a noticeable drop in performance.

- **W/o ESB (Emotional Spectrum Building):** Without the pre-built emotional spectrum, the model struggled to understand the user's emotional intent, leading to irrelevant edits (e.g., adding fireworks to convey "solitude").
- **W/o MCA (Multi-head Cross-Attention):** Removing the cross-attention blocks in the emotional mapper resulted in inaccurate content changes, such as the appearance of random, unrelated objects.
- **W/o KSE (Key Semantic Extraction):** Disabling the module for key semantic extraction and scaling hindered the model's ability to fully translate the intensity of the emotional request (e.g., making a beach dirty but not "disgusting").
- **W/o SAL (Sentiment Alignment Loss):** Removing the MLLM supervision loss caused the model to fail at shaping emotional factors meaningfully, resulting in nonsensical transformations (e.g., changing a cemetery into a brick wall).

## 6. Paper Figures
![Fig. 2 Visualization of the annotation process which a Chain-ofThought prompting strategy.]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_2.jpg' | relative_url }})
![Fig. 3 Visualization of the three validation criteria: keyword detection, emotion classification, and text-image retrieval.]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_3.jpg' | relative_url }})
![Fig. 4 Randomly selected samples from the EmoTIPS dataset.]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_4.jpg' | relative_url }})
![Fig. 5 Overview of the proposed AIEdiT model. (a) To represent universal emotional priors encapsulated in text descriptions, we build the continuous emotional spectrum and extract nuanced emotional requests (Sec. 4.1 ); (b) To manipulate emotional factors, We design the emotional mapper to translate visually-abstract emotional requests into visually-concrete semantic representations (Sec. 4.2 ); (c) To ensure specific emotions are effectively evoked, we introduce the MLLM to supervise emotional understanding (Sec. 4.3 ); During inference, we strategically distort the visual semantic representations and shape the corresponding emotional factors unser the guidance of text descriptions (Sec. 4.4 ). The emotional mapper is designed as a multi-modal Transformer, facilitating global interaction among input conditions, composed of a stack of Multi-head Self-Attention (MSA) blocks, Multi-head Cross-Attention (MCA) blocks, and Feed-Forward Networks (FFN). During the training, we keep the latent diffusion model frozen to preserve its generative ability.]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_5.jpg' | relative_url }})
![Fig. 6 Visualization of MLLM prompts used for emotional supervision.]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_6.jpg' | relative_url }})
![Fig. 7 Visualization of the correspondences between manipulated emotional factors and the number of noise-adding steps t = 25 , 37 , 49 .]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_7.jpg' | relative_url }})
![Fig. 8 Visual quality comparisons with general text-driven image editing methods and affective image editing methods. AIEdiT could understand emotional requests and shape corresponding emotional factors based on text descriptions.]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_8.jpg' | relative_url }})
![Fig. 9 Ablation study results with different variants of the AIEdiT. After removing the proposed modules, the created images cannot accurately reflect users’ emotional requests.]({{ '/images/05-2025/Affective_Image_Editing:_Shaping_Emotional_Factors_via_Text_Descriptions/figure_9.jpg' | relative_url }})
