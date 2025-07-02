---
title: Complex_Scene_Image_Editing_by_Scene_Graph_Comprehension
layout: default
date: 2022-03-24
---
## Complex Scene Image Editing by Scene Graph Comprehension
**Authors:**
- Zhongping Zhang
- Huayan Wang, h-index: 7, papers: 15, citations: 416

**ArXiv URL:** http://arxiv.org/abs/2203.12849v2

**Citation Count:** 6

**Published Date:** 2022-03-24

![Figure 1: Prior work on text-to-image editing generally follow two approaches: (A), editing the entire image ( e.g ., Imagic [ 11 ] or Dreambooth [ 31 ]), or (B), localizing the Region of Interest (RoI) through user-provided bounding boxes or object detection ( e.g ., GroundedSAM [ 12 , 19 ]+Stable Diffusion [ 30 ]). In our work, shown in (C), we localize the RoI (outlined by the red bounding box) and predict the desired region (outlined by the purple bounding box) for the target object using a scene graph of an input image. This enables us to perform many editing operations in complex scenes, such as relationship change and object replacement, which were not supported by prior work.]({{ '/images/03-2022/Complex_Scene_Image_Editing_by_Scene_Graph_Comprehension/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-guided image editing methods struggle with complex scenes. When an image contains multiple objects of the same type (e.g., several chairs), these methods often fail to identify and manipulate the correct target object based on a text description alone. They either edit the image globally or rely on object detectors that cannot resolve ambiguity based on spatial or semantic relationships, leading to incorrect edits.

## 2. Key Ideas and Methodology
The authors propose the Scene Graph Comprehension Network (SGC-Net) to address these challenges. The core idea is to use scene graphs—which represent objects and their relationships—to precisely understand the user's intent.

The methodology is a two-stage process:
1.  **Region of Interest (RoI) Prediction:** An RNN-based module takes a modified scene graph (representing the desired edit, e.g., `<chair - right of - table>`) as input. It comprehends the relationships to predict an accurate bounding box (RoI) for the target object's new state or location.
2.  **Region-based Image Editing:** A conditional diffusion model, built upon Stable Diffusion and ControlNet, takes the original image, the predicted RoI, and a text prompt as input. It then performs the specified edit (e.g., object addition, removal, or relationship change) within the localized region while preserving the background. This model is trained without requiring paired before-and-after images.

## 3. Datasets Used / Presented
*   **CLEVR:** A synthetic dataset of 3D shapes with ground truth before-and-after image pairs. It was used for quantitative evaluation of editing tasks like object addition, removal, and relationship changes.
*   **Visual Genome (VG):** A large-scale dataset of real-world images with dense scene graph annotations. As it lacks ground truth edited pairs, it was used for qualitative evaluation and human preference studies.

## 4. Main Results
SGC-Net significantly outperforms baseline methods on both datasets.
*   On **CLEVR**, the method achieves an 8-point improvement in Structural Similarity Index Measure (SSIM) compared to the next-best method (SIMSG) for relationship change tasks (92.32% vs 85.95%). It also drastically reduces Mean Absolute Error (MAE) for object removal.
*   On **Visual Genome**, human evaluators preferred SGC-Net's edits by a large margin, with preference rates being 9-33% higher than for baselines like GLIDE, Stable Diffusion, and SIMSG across various editing tasks.

The authors claim their method effectively performs complex, localized edits by comprehending semantic relationships, which prior work could not handle.

## 5. Ablation Studies
The authors performed ablation studies on the CLEVR dataset to validate the contributions of their two main components.
*   **Scene Graph vs. Text for RoI Prediction:** They replaced the scene-graph-based RoI prediction with a text-only version. This demonstrated the value of scene graphs for localization, as performance dropped significantly (SSIM decreased from 79.48 to 71.50).
*   **Custom Editing Module vs. Standard Inpainting:** They replaced their region-based editing module with a standard Stable Diffusion model. This showed the effectiveness of their editing approach, as using the standard model also resulted in a performance drop (SSIM decreased from 79.48 to 74.94).

## 6. Paper Figures
![Figure 2: SGC-Net overview. Our approach consists of two sequential stages: (A) RoI prediction, which localizes the RoI based on a modified scene graph. Specifically, a scene graph encoder takes the modified scene graph as input and outputs a bounding box. (B) Regionbased image editing: During inference, we take the image masked by predicted bounding boxes as input and outputs the modified image. During training, we randomly mask out objects to simulate the output of our RoI prediction module, and train our model to reconstruct the original image. Thus, our model does not require image pairs before and after editing.]({{ '/images/03-2022/Complex_Scene_Image_Editing_by_Scene_Graph_Comprehension/figure_2.jpg' | relative_url }})
![Figure 3: Qualitative examples for editing 256 × 256 images on CLEVR. Tasks from top to bottom: semantic relationship change, object addition, object replacement, and object removal. Blank image means the corresponding approach is not capable of this task. We outline the RoI by red bounding boxes. We observe that SGC-Net can accurately predict the RoI and edit objects in complex scenes. See Section 4.1 for discussion.]({{ '/images/03-2022/Complex_Scene_Image_Editing_by_Scene_Graph_Comprehension/figure_3.jpg' | relative_url }})
![Figure 4: Qualitative examples for editing 512 × 512 images on Visual Genome. The original region of the target object, desired region for the target object are outlined by red bounding box and purple bounding box respectively. We simplify the scene graphs for better visualiation. SGC-Net not only predicts desired regions for the target objects but also edits these regions based on user modifications better than prior work. See Section 4.2 for discussion.]({{ '/images/03-2022/Complex_Scene_Image_Editing_by_Scene_Graph_Comprehension/figure_4.jpg' | relative_url }})
![Figure 5: In-the-wild text-to-image editing results. SGC-Net can be adapted to text prompts with localization methods ( e.g ., Grounded-SAM [ 12 , 19 ]). See Section 4.3 for discussion.]({{ '/images/03-2022/Complex_Scene_Image_Editing_by_Scene_Graph_Comprehension/figure_5.jpg' | relative_url }})
![Figure 6: Limitations of SGC-Net. (A) Attribute editing: SGC-Net lacks the ability to modify object attributes. (B) Inserting objects in small RoI: While SGC-Net can effectively alleviate the background guessing issue, we still observe some failure cases on Visual Genome when the RoI is small. See Section 4.4 for discussion.]({{ '/images/03-2022/Complex_Scene_Image_Editing_by_Scene_Graph_Comprehension/figure_6.jpg' | relative_url }})
