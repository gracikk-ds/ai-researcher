---
title: How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?
layout: default
date: 2024-07-16
---
![Figure 1: The overall pipeline of recent text generation works. It utilizes a ControlNet for guiding the text generation process, employing a glyph image with a standard font as the control information. Control information at different stages is generated in the same manner and directly added to the skip features in the U-Net decoder.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenges in generating high-quality multilingual text in images using diffusion models. While ControlNet-based frameworks are promising, they struggle with the unique characteristics of text control information (i.e., glyph images). Unlike general conditions like Canny edges, glyphs are sparse, with high-density information in local areas, and require precise, fine-grained detail. The paper investigates how this specific type of control information influences the generation process at different stages to optimize its use and improve performance.

## 2. Key Ideas and Methodology
The core idea is to enhance text generation quality by systematically analyzing and optimizing the role of control information. The proposed framework, **TextGen**, is built on these insights.

-   **Input Feature Enhancement**: To better capture fine-grained character details from sparse glyph images, the authors introduce a **Fourier Enhancement Convolution (FEC)** block. This block operates in both spatial and frequency domains, allowing it to overcome the limitations of standard convolutions and focus on relevant texture information.
-   **Two-Stage Control**: The generation process is split into two stages to align with the different roles of control information over time. The **global control stage** (early steps) establishes the overall image structure and style, while the **detail control stage** (later steps) refines local text details. This design naturally unifies text generation and editing tasks into a single inference paradigm.
-   **Output Feature Balancing**: During inference, a Fourier-based enhancement method is used to balance the features injected into the U-Net decoder. It selectively suppresses low-frequency components from the control feature to emphasize the high-frequency details crucial for rendering crisp text textures.

## 3. Datasets Used / Presented
-   **TG-2M (Presented)**: The authors construct a new lightweight, high-quality multilingual dataset for training. It contains 2.53 million images (1.3M English, 1.23M Chinese) with 9.54 million text lines, filtered from several public datasets like MARIO-10M and Wukong.
-   **AnyWord (Used)**: The model's performance is evaluated on the public AnyWord benchmark for both Chinese and English text generation.

## 4. Main Results
-   TextGen significantly outperforms existing state-of-the-art methods while using less training data. On the AnyWord benchmark, it achieves a sentence accuracy (ACC) of **73.36% for English** and **67.92% for Chinese**.
-   This represents a relative improvement of 9.1% for English and 2.9% for Chinese over a strong baseline (AnyText) trained on the same TG-2M dataset.
-   The authors claim their method achieves state-of-the-art performance by effectively optimizing control information, and the insights gained can inspire future research in the field.

## 5. Ablation Studies
Ablation studies were performed on a 200k subset of the TG-2M dataset to validate each component of TextGen.

-   **Fourier Enhancement Convolution (FEC)**: Adding the FEC block significantly improved performance, increasing Chinese sentence accuracy by 25.48 percentage points and English accuracy by 1.39 percentage points over a basic ControlNet.
-   **Two-Stage Framework (TS)**: Incorporating the two-stage generation process further improved accuracy by 1.87 points for Chinese and 0.79 points for English.
-   **Inference Fourier Enhancement (IFE)**: Applying the proposed feature balancing during inference provided the largest single boost for English, increasing accuracy by 7.15 points, and further improved Chinese accuracy by 0.95 points, demonstrating its effectiveness in refining final output quality.

## 6. Paper Figures
![Figure 2: Differences between text control information and general ControlNet control information, including anime line drawings, M-LSD lines, and Canny edges. General controls focus on the overall structure and tolerate localized errors, while text control requires precise detail.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_2.jpg' | relative_url }})
![Figure 3: Visualization of the impact of control at different denoising stages. Control information is removed in the gray segments of the color bar during denoising. (a) Since visual text generation requires much detail texture, control information in later stages still plays an important role. (b) Even with only glyph and position images as control information, early-stage control influences non-text regions, ensuring the text region is coherent and matches the background.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_3.jpg' | relative_url }})
![Figure 4: The pipeline of our TextGen. It comprises two stages: the global control stage and the detail control stage. Control information utilizes a Fourier Enhancement Convolution (FEC) block and a Spatial Convolution (SC) block to extract features. During inference, we introduce a novel denoising paradigm to unify generation and editing based on our framework design. Best shown in color.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_4.jpg' | relative_url }})
![Figure 6: (a) The Spatial Convolution Block. (b) The Frequency Enhancement Convolution Block.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_6.jpg' | relative_url }})
![Figure 7: Qualitative comparison of generation performance in English texts. Our TextGen can generate more artistic and realistic texts.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_7.jpg' | relative_url }})
![Figure 8: Comparison of generation in Chinese.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_8.jpg' | relative_url }})
![Figure 9: Visualization of editing performance.]({{ '/images/07-2024/How_Control_Information_Influences_Multilingual_Text_Image_Generation_and_Editing?/figure_9.jpg' | relative_url }})
