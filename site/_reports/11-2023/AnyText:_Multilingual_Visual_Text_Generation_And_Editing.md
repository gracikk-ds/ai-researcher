---
title: AnyText:_Multilingual_Visual_Text_Generation_And_Editing
layout: default
date: 2023-11-06
---
## AnyText: Multilingual Visual Text Generation And Editing
**Authors:**
- Yuxiang Tuo, h-index: 3, papers: 3, citations: 98
- Xuansong Xie, h-index: 5, papers: 10, citations: 150

**ArXiv URL:** http://arxiv.org/abs/2311.03054v5

**Citation Count:** 83

**Published Date:** 2023-11-06

![Figure 1: Selected samples of AnyText. For text generation, AnyText can render the specified text from the prompt onto the designated position, and generate visually appealing images. As for text editing, AnyText can modify the text content at the specified position within the input image while maintaining consistency with the surrounding text style. Translations are provided in parentheses for non-English words in prompt, blue boxes indicate positions for text editing. See more in A.6.]({{ '/images/11-2023/AnyText:_Multilingual_Visual_Text_Generation_And_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a significant limitation in modern text-to-image diffusion models: their inability to generate accurate, legible, and coherent visual text. Current models often produce text that is blurred, misspelled, or nonsensical, which limits their practical applications in areas like advertising, design, and digital art. This subpar performance is attributed to two main factors: the lack of large-scale, multilingual image-text datasets with detailed text annotations, and the use of text encoders that are "character-blind" and cannot effectively process the visual structure of text.

## 2. Key Ideas and Methodology
The paper introduces **AnyText**, a diffusion-based framework for high-quality multilingual text generation and editing. The core idea is to augment a standard diffusion pipeline with dedicated modules that understand both the semantics of the prompt and the visual form (glyphs) of the text to be rendered.

The methodology is built on a text-control diffusion pipeline with three key components:
*   **Auxiliary Latent Module:** This module operates similarly to ControlNet. It takes spatial control signals—a rendered image of the text glyphs, a precise position map, and an optional masked image for editing—and encodes them into an auxiliary latent feature map. This map guides the diffusion model to place the text correctly.
*   **Text Embedding Module:** This is a key innovation for multilingual accuracy. Instead of relying solely on a standard text encoder, the model renders the desired text into an image, which is then fed through a pre-trained OCR model's encoder. The resulting feature embedding, which captures the text's visual stroke information, replaces a placeholder token in the main prompt's embeddings. This makes the model aware of the text's appearance, independent of language.
*   **Text Perceptual Loss:** To further refine writing accuracy, a perceptual loss is applied directly in the image space. The generated text region is compared to the ground-truth text region by feeding both through an OCR model and calculating the Mean Squared Error between their intermediate feature representations, providing direct supervision on writing quality.

## 3. Datasets Used / Presented
The authors introduce a new large-scale dataset, **AnyWord-3M**, created specifically for this task.
*   **Name:** AnyWord-3M
*   **Size:** It contains approximately 3 million image-text pairs with over 9 million lines of annotated text.
*   **Domain:** The dataset is multilingual and diverse, sourced from public datasets like LAION, Wukong, and various OCR benchmarks (e.g., COCO-Text, RCTW, MLT). It covers scenes with street views, posters, advertisements, and more.
*   **Usage:** The majority of the dataset (AnyWord-3M) is used for training the AnyText model. A subset of 1,000 images for English and 1,000 for Chinese was held out to create the **AnyText-benchmark** for evaluation.

## 4. Main Results
AnyText significantly outperforms existing state-of-the-art text generation models in both quantitative metrics and qualitative results.
*   On the **AnyText-benchmark**, AnyText (v1.1) achieved a **Sentence Accuracy (Sen. Acc) of 72.4%** for English text generation, surpassing the next best competitor (TextDiffuser at 59.2%).
*   The improvement was even more dramatic for Chinese text generation, where AnyText achieved a **Sen. Acc of 69.2%**. In contrast, competing models like TextDiffuser and GlyphControl scored below 7%, demonstrating their inability to handle complex, non-Latin scripts.
*   Qualitatively, AnyText generates text that is seamlessly integrated into the image, respecting background textures, lighting, and perspective, while other models often produce text that looks pasted on or is stylistically inconsistent.

## 5. Ablation Studies
The authors conducted several ablation experiments on a smaller Chinese dataset to validate the effectiveness of each proposed component.
*   **Text Embedding Module:** This was the most impactful component. Replacing the standard text encoder with the proposed OCR-based embedding module caused the most significant performance gain, boosting Sentence Accuracy from **20.2% to 46.0%**. This confirms that encoding the visual form of the text is crucial for accuracy.
*   **Text Perceptual Loss:** Adding the text perceptual loss further improved Sentence Accuracy from **46.0% to 50.0%**, demonstrating its effectiveness in refining the final rendered text.
*   **Position Information:** Explicitly providing a precise position map, in addition to the implicit position in the glyph image, was shown to improve performance and is essential for rendering text in curved or irregular regions.
*   **Editing Capability:** Enabling the text editing branch during training resulted in a slight decrease in text generation performance, indicating a trade-off between the two distinct tasks.

## 6. Paper Figures
![Figure 2: The framework of AnyText, which includes text-control diffusion pipeline, auxiliary latent module, text embedding module, and text perceptual loss.]({{ '/images/11-2023/AnyText:_Multilingual_Visual_Text_Generation_And_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Illustration of generating text in curved or irregular regions, left images are text positions provided by the user.]({{ '/images/11-2023/AnyText:_Multilingual_Visual_Text_Generation_And_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Illustration of generating text in multiple languages.]({{ '/images/11-2023/AnyText:_Multilingual_Visual_Text_Generation_And_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative comparison of AnyText and state-of-the-art models or APIs in English text generation. All captions are selected from the English evaluation dataset in AnyText-benchmark.]({{ '/images/11-2023/AnyText:_Multilingual_Visual_Text_Generation_And_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Comparative examples between GlyphDraw, ControlNet, and AnyText in Chinese text generation, all taken from the original GlyphDraw paper.]({{ '/images/11-2023/AnyText:_Multilingual_Visual_Text_Generation_And_Editing/figure_6.jpg' | relative_url }})
