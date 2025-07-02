---
title: AnyText2:_Visual_Text_Generation_and_Editing_With_Customizable_Attributes
layout: default
date: 2024-11-22
---
## AnyText2: Visual Text Generation and Editing With Customizable Attributes
**Authors:**
- Yuxiang Tuo, h-index: 3, papers: 3, citations: 98
- Liefeng Bo, h-index: 3, papers: 4, citations: 39

**ArXiv URL:** http://arxiv.org/abs/2411.15245v1

**Citation Count:** None

**Published Date:** 2024-11-22

![Figure 1. AnyText2 can accurately generate multilingual text within images and achieve a realistic integration. Furthermore, it allows for customized attributes for each line, such as controlling the font style through font files, mimicking an image using a brush tool, and specifying the text color. Additionally, AnyText2 enables customizable attribute editing of text within images.]({{ '/images/11-2024/AnyText2:_Visual_Text_Generation_and_Editing_With_Customizable_Attributes/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-to-image (T2I) models struggle with precise control over text attributes like font and color, which limits their use in applications such as logo design and advertising. This paper introduces AnyText2 to address this gap, enabling customizable and accurate multilingual text generation and editing within images.

## 2. Key Ideas and Methodology
The core of AnyText2 is a novel `WriteNet+AttnX` architecture built upon a pre-trained T2I model. The methodology has two main components:
- **WriteNet+AttnX Architecture:** Unlike previous methods that entangle text and image generation, `WriteNet` is a streamlined module that focuses solely on rendering text features. This decouples it from the main image generation U-Net, improving inference speed and image realism. Trainable `AttnX` layers are then inserted into the U-Net's decoder to seamlessly fuse the text features with the image content.
- **Text Embedding Module:** To enable attribute customization, this module uses separate encoders for glyphs, position, font, and color. It can extract font styles and colors from reference images or accept direct user input (e.g., font files, color pickers), allowing for fine-grained control over each line of text independently.

## 3. Datasets Used / Presented
- **Training Dataset:** The model was trained on `AnyWord-3M`, a large-scale multilingual dataset of 3.53 million images. The authors improved this dataset by re-generating the original captions with QWen-VL to create longer, more descriptive prompts.
- **Evaluation Benchmark:** Performance was evaluated on the `AnyText-benchmark`, which consists of 2,000 images (1,000 Chinese from Wukong, 1,000 English from LAION-400M) designed to test text generation accuracy, image realism (FID), and prompt-following (CLIPScore).

## 4. Main Results
AnyText2 demonstrates state-of-the-art performance, outperforming its predecessor AnyText and other leading models like GlyphDraw2.
- **Quantitative:** Compared to AnyText (long caption version), AnyText2 improves Sentence Accuracy by 9.3% for English and 3.3% for Chinese. It also achieves a superior FID score (24.32 vs. 31.38 for Chinese), indicating higher image realism, and a better CLIPScore, showing enhanced prompt-following ability.
- **Qualitative:** The model generates highly accurate multilingual text that is seamlessly integrated into the image, with precise control over font and color attributes.

## 5. Ablation Studies
The authors conducted several ablation studies to validate their design choices:
- **Component Contribution:** Adding the position and font encoders to the baseline model significantly boosted text accuracy. The `WriteNet` architecture (compared to a ControlNet-like design) slightly reduced text accuracy but substantially improved image realism (FID score) and increased inference speed by 19.8%.
- **Caption Length:** Training with longer, more descriptive captions was found to slightly decrease raw text accuracy but significantly enhance the model's ability to follow complex prompts, as measured by CLIPScore. The authors opted for long captions to prioritize prompt-following capabilities.

## 6. Paper Figures
![Figure 2. The framework of AnyText2, which is designed with a WriteNet+AttnX architecture to integrate text generation capability into pre-train diffusion models, and there is a Text Embedding Module to provide various conditional control for text generation.]({{ '/images/11-2024/AnyText2:_Visual_Text_Generation_and_Editing_With_Customizable_Attributes/figure_2.jpg' | relative_url }})
![Figure 3. By adjusting the strength coefficient α from 0 to 1 shows that the text-image fusion is gradually improving.]({{ '/images/11-2024/AnyText2:_Visual_Text_Generation_and_Editing_With_Customizable_Attributes/figure_3.jpg' | relative_url }})
![Figure 4. Examples of customizing text attributes. The first row demonstrates font style control using a user-specified font file. The second row showcases selecting a text region from an image to mimic its font style. The third row illustrates the control of text color.]({{ '/images/11-2024/AnyText2:_Visual_Text_Generation_and_Editing_With_Customizable_Attributes/figure_4.jpg' | relative_url }})
![Figure 5. Qualitative comparison of AnyText2 and other methods. From the perspectives of text accuracy, text-image integration, attribute customization, and multilingual support, AnyText2 demonstrated significant advantages.]({{ '/images/11-2024/AnyText2:_Visual_Text_Generation_and_Editing_With_Customizable_Attributes/figure_5.jpg' | relative_url }})
