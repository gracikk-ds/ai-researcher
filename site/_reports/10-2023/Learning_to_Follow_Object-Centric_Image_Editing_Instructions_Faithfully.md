---
title: Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully
layout: default
date: 2023-10-29
---
## Learning to Follow Object-Centric Image Editing Instructions Faithfully
**Authors:**
- Tuhin Chakrabarty, h-index: 21, papers: 46, citations: 1515
- Smaranda Muresan

**ArXiv URL:** http://arxiv.org/abs/2310.19145v1

**Citation Count:** 7

**Published Date:** 2023-10-29

![Figure 1: (a) Input Image (b) Edited image from InstructPix2Pix ( Brooks et al. , 2023 ) with the instruction Add a lighthouse.]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address key challenges in natural language-guided image editing with diffusion models. Existing methods often struggle with:
1.  **Underspecification:** Failing to infer the implicit details of an instruction (e.g., where to place an added object).
2.  **Grounding:** Incorrectly localizing the specific region of the image that needs to be edited.
3.  **Faithfulness:** Making excessive or unwanted changes to parts of the image that should remain untouched.

The authors argue these issues are largely caused by the noisy and sometimes nonsensical automatically-generated training data used by prior models like InstructPix2Pix.

## 2. Key Ideas and Methodology
The paper's core idea is that improving the quality of the training data and enhancing the supervision signal during fine-tuning can produce more precise and faithful edits.

Their methodology involves a multi-stage data curation pipeline and a novel fine-tuning approach:
*   **Data Curation:** They start with an existing dataset and use a pipeline of modern AI models to refine it. This involves:
    1.  Using a Large Language Model (LLM) with Chain-of-Thought prompting to filter nonsensical instructions and identify the target object for the edit.
    2.  Employing an object detector (GroundingDINO) and a segmentation model (SAM) to create a precise mask of the target object.
    3.  Generating several edited image candidates using Stable Diffusion Inpainting with the mask.
    4.  Using a Visual Question Answering (VQA) model to rank the candidates and select the one that is most faithful to the original image content.
*   **Enhanced Supervision:** During fine-tuning, they provide the diffusion model with an additional supervision signal. Instead of just the input image, they provide an image where the region to be edited is explicitly highlighted by either a bounding box or a segmentation mask.

## 3. Datasets Used / Presented
The authors curate their own training and test data.
*   **Training Data:** They create a high-quality dataset of **52,208 instruction-image pairs** by filtering and improving the original InstructPix2Pix dataset using their curation pipeline.
*   **Test Data:** They create a new test set of **465 pairs** to evaluate model robustness and generalization, split into:
    *   **In-domain (200 pairs):** Curated from InstructPix2Pix data.
    *   **Out-of-domain (265 pairs):** Sourced from the **MagicBrush** dataset (manually annotated real-world images) and a **Visual-Metaphors** dataset.

## 4. Main Results
The authors’ best model, **InstructPix2Pix+EntityMask**, which uses the improved data and segmentation mask supervision, significantly outperforms all baselines.
*   On the automatic **TIFA** faithfulness metric, their model scored **65.84**, compared to **62.24** for the baseline InstructPix2Pix.
*   In human evaluations, their model achieved a score of **69.8** on in-domain data and **65.1** on out-of-domain data. This was a substantial improvement over the baseline InstructPix2Pix, which scored **49.3** (in-domain) and **25.2** (out-of-domain).

The authors conclude that high-quality annotations and grounded supervision signals are critical for achieving precise and faithful image editing.

## 5. Ablation Studies
The authors perform ablations by comparing different levels of supervision during fine-tuning.
*   **Bounding Box vs. Segmentation Mask Supervision:** They compared their model trained with bounding box supervision (`+BoundingBox`) against their best model trained with more precise segmentation masks (`+EntityMask`). The `+EntityMask` model performed better across all metrics (e.g., 69.8 vs. 62.8 on in-domain human evaluation), demonstrating that a more precise supervision signal leads to better edits.
*   **Enhanced Supervision vs. Baseline:** Both of their models (`+BoundingBox` and `+EntityMask`) significantly outperformed the original `InstructPix2Pix` baseline. This shows that the combination of cleaner data and any form of grounded supervision (box or mask) yields substantial improvements in both instruction following and faithfulness.

## 6. Paper Figures
![Figure 2: Steps to create parallel data: (a) Input Image + Edit Instruction; (b) Image with grounding in the form of a bounding box for the entity where transformation has to be made; (c) Masked localized segment of the grounded image where the transformation has to be made; (d) Final output.]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_2.jpg' | relative_url }})
![Figure 3: Examples of noisy edit instructions and image-pairs: (a) Make her look like an android ; (b) Make the rocky mountains look like a chessboard ; (c) Replace her with a bird ; (d) Have it be a lighthouse .]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_3.jpg' | relative_url }})
![Figure 4: Steps to create high-quality training parallel data: Given an input image, caption, and edit instruction we first use Chain-of-Thought (CoT) prompting with ChatGPT to identify whether the edit instruction is sensible and if it is, what is the entity that needs to be transformed. Using the LLM-generated edit entity we use GroundingDINO to localize it and SAM (Segment Anything Mask) to segment it. We then use Stable Diffusion Inpainting to generate 3 images and filter out the best image with the help of VQA.]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_4.jpg' | relative_url }})
![Figure 5: (a) Bounding Box supervision (b) Segmentation Mask supervision. Edit instruction: make the skirt red .]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_5.jpg' | relative_url }})
![Figure 6: Human evaluation framework (a) Input Image with Edit Instruction (b) Example of a bad edit]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_6.jpg' | relative_url }})
![Figure 7: Sample generations for an image from (a) instruct-pix2pix dataset (b) Magicbrush dataset. The images displayed are following order (i) input-image, (ii) Grounded-Inpainting, (iii) X-Decoder, (iv) InstructPix2Pix, (v) InstructPix2Pix+BoundingBox, (vi) InstructPix2Pix+EntityMask]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_7.jpg' | relative_url }})
![Figure 8: Sample edits showing < Input, InstructPix2Pix, InstructPix2Pix+Entity Mask > for the metaphors and corresponding edit instructions (a) [" Her song is like a cloud of heavy smoke ", "Add more smoke near the microphone"] (b) [" My heart is a garden tired with autumn ", "Change the heart such that it is made of autumn leaves"] (c) [" My head is like a vase growing ","Replace the body of the purple vase with the face of a man"] (d) [" The river is a ribbon wide ", "Add a landscape"]]({{ '/images/10-2023/Learning_to_Follow_Object-Centric_Image_Editing_Instructions_Faithfully/figure_8.jpg' | relative_url }})
