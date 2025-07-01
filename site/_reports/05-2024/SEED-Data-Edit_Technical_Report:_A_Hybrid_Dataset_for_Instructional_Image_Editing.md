---
title: SEED-Data-Edit_Technical_Report:_A_Hybrid_Dataset_for_Instructional_Image_Editing
layout: default
date: 2024-05-07
---
![Figure 1: Data examples of instruction-guided image editing in SEED-Data-Edit, which includes (1) High-quality editing data produced by an automatic pipeline (first row), (2) Real-world scenario data scraped from the internet that more accurately reflects user image editing intentions (second row), (3) High-precision multi-turn editing data annotated by Photoshop experts (third row).]({{ '/images/05-2024/SEED-Data-Edit_Technical_Report:_A_Hybrid_Dataset_for_Instructional_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The primary challenge in instruction-guided image editing is the lack of high-quality, large-scale, and diverse datasets. This scarcity hinders the development of models that can accurately interpret open-form language instructions, handle complex or iterative edits, and produce realistic results while preserving the semantic integrity of the original image. The authors aim to address this gap by creating a comprehensive dataset that covers a wide spectrum of editing scenarios.

## 2. Key Ideas and Methodology
The paper introduces **SEED-Data-Edit**, a unique hybrid dataset for training image editing models. The core idea is to combine three distinct types of data to create a robust and versatile resource:
1.  **Automated Pipeline Data:** To achieve large scale and diversity, two automated pipelines generate millions of editing pairs. One focuses on object addition/removal, while the other generates changes in style, color, or material.
2.  **Real-world Scenario Data:** To capture the complexity and nuance of practical user requests, data is scraped from online forums where users request edits from Photoshop experts.
3.  **Human-annotated Multi-turn Data:** To simulate iterative editing processes, Photoshop experts perform and document multiple sequential edits on a single image.

To demonstrate the dataset's utility, the authors fine-tune a pre-trained Multimodal Large Language Model (MLLM) called **SEED-X**. The resulting model, **SEED-X-Edit**, leverages the SEED-X architecture's ability to preserve fine-grained details from the source image, which is crucial for high-precision editing.

## 3. Datasets Used / Presented
The paper presents the **SEED-Data-Edit** dataset, which contains approximately 3.7 million image editing pairs in total. It is composed of three sub-datasets:
*   **Automated Pipeline-generated Data:** 3.5 million pairs. This includes 1.5M object addition/removal edits on images from Unsplash and 2.0M style/attribute edits on images from OpenImages.
*   **Real-world Scenario Data:** 52,000 pairs. These are scraped from Photoshop request forums (e.g., Reddit) and manually re-annotated to ensure instruction quality.
*   **Multi-turn Editing Data:** 95,000 pairs, organized into 21,000 multi-turn sequences with up to five rounds of edits each. This data was created by Photoshop experts editing images from Unsplash, SAM, and JourneyDB.

## 4. Main Results
The paper provides a qualitative comparison of its fine-tuned model, SEED-X-Edit, against baseline models like MagicBrush, MGIE, and HQ-Edit. The visual results demonstrate that SEED-X-Edit adheres more accurately to editing instructions. For instance, it can correctly apply an edit to a specific object among multiple similar ones (e.g., adding sunglasses to only one animal) and successfully execute object removal where other models fail. The authors claim these promising results showcase the effectiveness of the SEED-Data-Edit dataset for advancing the field of instructional image editing.

## 5. Ablation Studies
Not performed. The paper's evaluation focuses on a qualitative comparison between the final SEED-X-Edit model and other existing methods, rather than ablating components of their own dataset or methodology.

## 6. Paper Figures
![Figure 2: The automated pipelines for generating editing pairs, which constitutes the first part of SEED-Data-Edit. In pipeline (a), an object is first segmented and subsequently removed with an inpainting module, which results in a set of “Remove” and “Add” editing samples. In pipeline (b), an image-guided text-to-image generation model is utilized to generate source images and target images based on the original image, the original caption and the target caption after editing.]({{ '/images/05-2024/SEED-Data-Edit_Technical_Report:_A_Hybrid_Dataset_for_Instructional_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: More examples of instruction-guided image editing in SEED-Data-Edit, which integrates three distinct types of data: (a) Large-scale automated pipeline-generated edits (first and second row), (b) Real-world scenario data, where amateur photographers post their images along with editing requests, which are addressed by Photoshop experts (third and fourth row), and (c) Multi-turn editing data annotated by Photoshop experts on real images (fifth and sixth row).]({{ '/images/05-2024/SEED-Data-Edit_Technical_Report:_A_Hybrid_Dataset_for_Instructional_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: The comparison of language-guided image editing between existing methods and SEEDX-Edit. Through find-tuning with SEED-Data-Edit, SEED-X-Edit is able to adhere to editing instructions more accurately.]({{ '/images/05-2024/SEED-Data-Edit_Technical_Report:_A_Hybrid_Dataset_for_Instructional_Image_Editing/figure_4.jpg' | relative_url }})
