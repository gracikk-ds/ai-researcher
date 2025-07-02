---
title: UltraEdit:_Instruction-based_Fine-Grained_Image_Editing_at_Scale
layout: default
date: 2024-07-07
---
## UltraEdit: Instruction-based Fine-Grained Image Editing at Scale
**Authors:**
- Haozhe Zhao, h-index: 8, papers: 24, citations: 518
- Baobao Chang, h-index: 9, papers: 24, citations: 533

**ArXiv URL:** http://arxiv.org/abs/2407.05282v2

**Citation Count:** 63

**Published Date:** 2024-07-07

![Figure 1: Examples of U LTRA E DIT . Free-form ( left ) and region-based ( right ) image editing.]({{ '/images/07-2024/UltraEdit:_Instruction-based_Fine-Grained_Image_Editing_at_Scale/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing datasets for instruction-based image editing suffer from three main drawbacks that limit model performance: 1) a lack of diversity in editing instructions, which are either hard to scale (human-rated) or creatively limited (LLM-generated); 2) significant image bias, as they often rely on text-to-image (T2I) models that produce a narrow range of styles and content; and 3) a lack of support for region-based editing, where edits are confined to a specific area (mask), hindering fine-grained control. This paper addresses these gaps by creating a large-scale, diverse, and high-quality dataset.

## 2. Key Ideas and Methodology
The authors introduce ULTRAEDIT, a dataset created through a novel, systematic pipeline designed to overcome the limitations of prior work. The core methodology involves three stages:
1.  **Instruction Generation**: To create diverse instructions, the pipeline combines the creativity of Large Language Models (LLMs) with high-quality, in-context examples initially written by human raters.
2.  **Free-form Sample Generation**: To reduce image bias, the pipeline uses real images from public datasets (e.g., COCO) as "anchors." It generates a source image that visually resembles the anchor and then uses prompt-to-prompt (P2P) editing to create the target image, grounding the data in real-world visual diversity.
3.  **Region-based Sample Generation**: The pipeline automatically generates region masks from instructions using object detection and segmentation models. It then employs a modified inpainting diffusion process to apply edits precisely within the masked area, enabling fine-grained control.

## 3. Datasets Used / Presented
*   **ULTRAEDIT (Presented)**: A new large-scale dataset containing approximately 4.1 million instruction-based editing samples. It includes ~4M free-form samples and ~108K region-based samples with corresponding masks.
*   **MagicBrush & Emu Edit Test (Used for Evaluation)**: Standard benchmarks used to evaluate the performance of models trained on ULTRAEDIT against existing state-of-the-art methods.

## 4. Main Results
Models trained on ULTRAEDIT set new state-of-the-art records on established benchmarks.
*   **On MagicBrush**: The model trained on ULTRAEDIT significantly outperforms baselines like InstructPix2Pix. When provided with a region mask, it achieves top performance in both single-turn and challenging multi-turn editing scenarios, demonstrating superior fine-grained control (e.g., achieving a DINO score of 0.8982 in single-turn and 0.8505 in multi-turn editing with a region).
*   **On Emu Edit Test**: The model's performance scales effectively with the size of the training data. A model trained on 3M ULTRAEDIT samples surpassed the proprietary Emu Edit baseline (trained on 10M samples) in instruction-following ability (CLIPdir score of 0.1076 vs. 0.1066).

The key takeaway is that using real image anchors and including region-based data are crucial for building more robust and generalizable image editing models.

## 5. Ablation Studies
*   **Real Image Anchors**: The authors compared models trained on data generated with and without real image anchors. The results show that using anchors consistently improves model performance across all data scales (e.g., at 1.5M samples, CLIPdir score improved from 0.0720 to 0.0952). This confirms that anchors effectively mitigate image bias and enable models to benefit from larger datasets.
*   **Free-form vs. Region-based Editing**: The study explored the impact of mixing free-form and region-based data during training. It was found that including region-based data, even in smaller quantities, improves performance on free-form tasks. Conversely, a larger volume of free-form data helps with region-based editing, highlighting a synergistic relationship between the two data types.

## 6. Paper Figures
![Stage III: Region-based Editing Samples. Upon the free-form editing samples, we create additional region-based editing data using an automatic editing region extraction method. Given an imageinstruction pair ⟨ I ⋆ , T e ⟩ , we first detect all objects within I ⋆ using recognize-anything [ 74 ] and prompt LLM with the object list , soruce caption T s , target caption T t and editing instruction T e to identify the object to be edited. Then we employ GroundingDINO [ 38 ] and SAM [ 31 ] to obtain bounding boxes and fine-grained mask of this target object. For edits involving transformation over the entire image ( e.g ., “turn this into an oil paint”), we mark the whole image as the editing region. We save an expanded version of the original mask (which becomes a contour) as the editing region I m . Finally, the bounding box and fine-grained mask will be fused into a soft mask (see Figure 2) to help smooth the transition between inpainting area and the rest of the image. While producing the source image I s is the same as in Stage II, we adopt a modified inpainting pipeline to produce the target image I t to take the editing region I m into consideration:]({{ '/images/07-2024/UltraEdit:_Instruction-based_Fine-Grained_Image_Editing_at_Scale/figure_2.jpg' | relative_url }})
![Figure 4: Qualitative comparison of images generated by our data generation pipeline with other zero-shot image editing methods.]({{ '/images/07-2024/UltraEdit:_Instruction-based_Fine-Grained_Image_Editing_at_Scale/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative evaluation. (Top) On four distinct tasks on Emu Edit, listed from top to bottom: background, color, global, style; (Bottom) Multi-turn editing on MagicBrush.]({{ '/images/07-2024/UltraEdit:_Instruction-based_Fine-Grained_Image_Editing_at_Scale/figure_5.jpg' | relative_url }})
![Figure 6: Ablations on region-based editing . We report CLIPout as the main metric.]({{ '/images/07-2024/UltraEdit:_Instruction-based_Fine-Grained_Image_Editing_at_Scale/figure_6.jpg' | relative_url }})
