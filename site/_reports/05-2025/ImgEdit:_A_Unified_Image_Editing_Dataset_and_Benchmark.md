---
title: ImgEdit:_A_Unified_Image_Editing_Dataset_and_Benchmark
layout: default
date: 2025-05-26
---
![Figure 1: Singleand MultiTurn Edit Types. (Left) Single-turn tasks include add, remove, replace, alter, background change, motion change, style, object extraction, visual edit, and hybrid edit. (Right) Multi-turn tasks include content memory, content understanding, and version backtracking.]({{ '/images/05-2025/ImgEdit:_A_Unified_Image_Editing_Dataset_and_Benchmark/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the widening performance gap between proprietary, closed-source image editing models (like GPT-4o) and their open-source counterparts. They identify the primary cause of this gap as the lack of high-quality, large-scale, publicly available training datasets and comprehensive evaluation benchmarks. Existing datasets often suffer from low image resolution, simplistic prompts, and poor editing quality. Similarly, current benchmarks lack diverse evaluation dimensions, fail to stratify tasks by difficulty, and do not adequately assess complex capabilities like multi-turn interactions.

## 2. Key Ideas and Methodology
The paper introduces **ImgEdit**, a unified framework to address these limitations. The core of the work is a four-part contribution:
1.  **Automated Data Pipeline:** A multi-stage pipeline is developed to generate high-quality data. It starts with high-resolution images, uses an open-vocabulary detector and segmentation model for grounding, employs GPT-4o to generate diverse and complex editing prompts, creates edited images using state-of-the-art generative models, and finally uses GPT-4o again for strict quality filtering.
2.  **ImgEdit Dataset:** The output of this pipeline is a new, large-scale dataset.
3.  **ImgEdit-E1 Model:** To validate the dataset's quality, the authors train a new editing model, `ImgEdit-E1`. Its architecture integrates a Vision-Language Model (Qwen2.5-VL-7B) for instruction understanding, a SigLIP vision encoder for low-level features, and a Diffusion-in-Transformer (FLUX) backbone for image generation.
4.  **ImgEdit-Bench & Judge:** A comprehensive benchmark (`ImgEdit-Bench`) is introduced to evaluate models on basic, challenging, and multi-turn tasks. For scalable evaluation, they also release `ImgEdit-Judge`, an evaluation model fine-tuned to align with human preferences.

## 3. Datasets Used / Presented
*   **Presented: ImgEdit Dataset:** A new dataset containing 1.2 million high-quality image-editing pairs. It is composed of 1.1 million single-turn edits across 10 categories (e.g., add, remove, object extraction, style transfer) and 110,000 multi-turn conversational edits designed to test content memory, understanding, and version backtracking. The data was generated using the authors' pipeline, starting from images in the LAION-Aesthetics dataset.
*   **Presented: ImgEdit-Bench:** A new benchmark dataset with 811 manually curated test cases designed to evaluate instruction adherence, editing quality, and detail preservation across a range of difficulties.

## 4. Main Results
*   The `ImgEdit` dataset is shown to be of higher quality than existing datasets, achieving a superior GPT-4o quality score (4.71) and a much lower "fake score" (0.050), indicating its edits are more realistic and harder to detect as synthetic.
*   The `ImgEdit-E1` model, trained on the new dataset, significantly outperforms previous open-source models across a wide range of editing tasks. Its performance is notably strong on novel tasks introduced in the dataset, such as object extraction and hybrid edits.
*   Qualitative and quantitative results show that `ImgEdit-E1` closes the gap with proprietary models like GPT-4o, achieving comparable results on several tasks while surpassing all other open-source competitors.

## 5. Ablation Studies *(If none are reported, write “Not performed”)*
Not performed. The authors state in the appendix that since the paper's core contribution is the dataset and benchmark framework, detailed ablation studies on the `ImgEdit-E1` model architecture and training process were not conducted.

## 6. Paper Figures
![Figure 2: The Data Pipeline and Model Architecture. (Left) Our pipeline includes pre-filter, grounding and segmentation, caption generation, in-painting and post-processing, leveraging lots of state-of-the-arts models. (Right) ImgEdit-E1 includes a Qwen2.5-VL-7B [ 4 ] as text and image encoder, a SigLIP [68] provides low-level feature, and FLUX [13] as DiT backbone.]({{ '/images/05-2025/ImgEdit:_A_Unified_Image_Editing_Dataset_and_Benchmark/figure_2.jpg' | relative_url }})
![Figure 3: Data Composition of ImgEdit .]({{ '/images/05-2025/ImgEdit:_A_Unified_Image_Editing_Dataset_and_Benchmark/figure_3.jpg' | relative_url }})
![Figure 6: Qualitative Comparison Among Different Editing Models . ImgEdit-E1 surpasses all existing open-source models in instruction adherence, detail preservation, and visual quality, achieving results comparable to those of GPT-4o. Furthermore, owing to the novel editing tasks introduced in ImgEdit, it is capable of performing editing and extraction tasks while preserving identity consistency.]({{ '/images/05-2025/ImgEdit:_A_Unified_Image_Editing_Dataset_and_Benchmark/figure_6.jpg' | relative_url }})
