---
title: StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation
layout: default
date: 2025-05-26
---
![Figure 1: Stylized samples of our StyleAR. Our StyleAR is capable of generating images that are highly consistent in style with the reference images across a diverse range of styles, and highly aligned in semantics with the input prompts of various categories.]({{ '/images/05-2025/StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Autoregressive (AR) models excel at text-to-image generation but lag behind diffusion models in the complex task of style-aligned generation. This gap exists because style alignment typically requires "triplet data" (a reference style image, a text prompt, and a corresponding stylized output image) for instruction tuning. Acquiring such high-quality triplet data at a large scale is a significant challenge. The authors aim to overcome this data bottleneck and enable AR models to perform high-fidelity, style-aligned image generation, a domain currently dominated by diffusion-based methods.

## 2. Key Ideas and Methodology
The core of the paper is **StyleAR**, a framework that customizes an AR model for style-aligned generation using only binary text-image data, thus bypassing the need for difficult-to-acquire triplet data.

-   **Data Curation Strategy**: The authors first generate a dataset of stylized images using a diffusion model. However, for training, they discard the reference style image and only use the generated stylized image and its corresponding text prompt as a binary pair. This avoids inheriting the performance limitations of the data-generation model. Crucially, they mix this stylized data with a large volume of standard, non-stylized (raw) text-image data at an optimal 3:1 raw-to-stylized ratio to enhance the model's ability to extract rich style features.

-   **Model and Training**: StyleAR uses a frozen CLIP image encoder and a trainable perceiver resampler to convert a reference style image into "style tokens". To prevent "content leakage" (where objects from the style image appear in the output), they introduce a **style-enhanced tokens** technique. During inference, this technique uses the Segment Anything Model (SAM) to identify and subtract the semantic features of the main object in the style reference, isolating the pure style.

-   **Post-Training**: The model's prompt alignment is further improved using Direct Preference Optimization (DPO).

## 3. Datasets Used / Presented
-   **Stylized Training Data**: A custom dataset of 16,000 images was created. The authors selected 80 distinct artistic styles (from WikiArt and other sources) and used the InstantStyle model to generate 200 semantically diverse images for each style.
-   **Raw Training Data**: During each training epoch, 49,368 images were sampled from the `laion2b-en-aesthetic-square-cleaned` dataset and mixed with the stylized data.
-   **Evaluation Suite**: A custom benchmark was created by collecting 10 diverse style images and 20 varied text prompts. 800 images were generated in total for evaluation across all compared methods.

## 4. Main Results
StyleAR demonstrates a superior balance between prompt adherence and style consistency compared to leading diffusion-based methods.

-   **Quantitative Metrics**: In quantitative tests, StyleAR achieved the second-highest prompt adherence (CLIP-T: 0.2893) and second-highest style consistency (CLIP-I: 0.7456, DINO: 0.6136). It outperformed methods that were strong in one area but weak in the other (e.g., InstantStyle has high prompt adherence but low style consistency). The method with the highest style score, IP-Adapter, suffered from severe content leakage, which StyleAR successfully avoids.
-   **User Study**: Human evaluators rated StyleAR as the best model for style consistency by a significant margin, while its prompt adherence and image quality were rated on par with the top-performing competitor.

The authors claim that StyleAR is the first work to successfully enable an AR model to achieve state-of-the-art, style-aligned text-to-image generation using a scalable binary data training approach.

## 5. Ablation Studies
-   **Training Data Composition**: The authors tested the impact of mixing raw images with stylized images at different ratios. Using only stylized data resulted in poor style consistency. The chosen 1:3 ratio of stylized-to-raw data provided the best balance of prompt adherence and style consistency. Increasing the ratio further led to content leakage and "overfitting" to the style image.
-   **Style-Enhanced (SE) Tokens**: A version of StyleAR without the SE token mechanism was tested. The results showed that without this component, the model suffered from significant content leakage, where semantic elements from the style reference appeared in the generated images, resulting in chaotic outputs. The SE tokens were crucial for maintaining prompt control and image quality.
-   **DPO Post-Training**: Comparing the model with and without DPO showed that the post-training step measurably improved prompt adherence and slightly enhanced style consistency.

## 6. Paper Figures
![Figure 2: The pipeline of our method. a) We first investigate a novel stylized image data curation to form binary data with high prompt adherence and prevent low style consistency. b) We use a mixed dataset to enhance rich stylistic features learning. c) With the designed data curation and model framework, our method achieve high prompt adherence and style consistency.]({{ '/images/05-2025/StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation/figure_2.jpg' | relative_url }})
![Figure 3: The framework of our StyleAR. During training, we utilize a frozen CLIP [ 24 ] image encoder along with a trainable perceiver [ 13 ; 1 ] resampler module to efficiently extracted features. Subsequently, style tokens are combined with the injected Gaussian noise and concatenated with multimodal tokens by replacing the placeholder tokens. During inference, we incorporate SAM [ 15 ] to remove irrelevant semantic contents in the reference style image.]({{ '/images/05-2025/StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation/figure_3.jpg' | relative_url }})
![Figure 4: Qualitative comparison. We conducted a comprehensive qualitative evaluation by comparing our StyleAR with various existing methods which are all diffusion-based, including InstantStyle [38], IP-Adapter [51], StyleAligned [10], StyleCrafter [18], StyleShot [9].]({{ '/images/05-2025/StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation/figure_4.jpg' | relative_url }})
![Figure 6: Qualitative comparison of integration with additional conditions. We show the comparison results of control generation with Ours and diffusion models.]({{ '/images/05-2025/StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation/figure_6.jpg' | relative_url }})
![Figure 7: Ablation study of composition of training datasets. We investigate the impact of the composition of training datasets in our StyleAR. The compared training datasets include pure stylized image data, the ratios of stylized image data to raw image data are 1:3, 1:6 and 1:30 respectively.]({{ '/images/05-2025/StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation/figure_7.jpg' | relative_url }})
![Figure 8: Ablation study of style-enhanced (SE) tokens. We investigate the style-enhanced tokens technique in our StyleAR. The ablation study demonstrates the effectiveness.]({{ '/images/05-2025/StyleAR:_Customizing_Multimodal_Autoregressive_Model_for_Style-Aligned_Text-to-Image_Generation/figure_8.jpg' | relative_url }})
