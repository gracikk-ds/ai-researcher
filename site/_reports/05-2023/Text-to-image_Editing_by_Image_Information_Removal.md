---
title: Text-to-image_Editing_by_Image_Information_Removal
layout: default
date: 2023-05-27
---
## Text-to-image Editing by Image Information Removal
**Authors:**
- Zhongping Zhang, h-index: 10, papers: 28, citations: 544
- Bryan A. Plummer, h-index: 22, papers: 76, citations: 4066

**ArXiv URL:** http://arxiv.org/abs/2305.17489v2

**Citation Count:** 13

**Published Date:** 2023-05-27

![Figure 1. We aim to edit the specific content of the input image according to text descriptions while preserving text-irrelevant image content. Prior work based on large-scale diffusion models has followed two major approaches for image editing: (A), finetuning the pretrained models or text embeddings ( e.g ., Imagic [ 9 ] or Dreambooth [ 29 ]), or (B), introducing structural guidance as additional constraint to control the spatial information of the generated image ( e.g ., ControlNet [ 40 ] or MaskSketch [ 2 ]). In our work, shown in (C), our approach conditions on both the original image and the structural guidance, to better preserve the text-irrelevant content of the image. E.g ., our model successfully preserves the original attributes of the airplane (outlined by the green bounding box) in the generated image. In contast, previous methods such as Imagic (A) and ControlNet (B) not only alter the sky and background but also modify the attributes of the airplane (outlined by the red bounding boxes), which is unwanted in this example.]({{ '/images/05-2023/Text-to-image_Editing_by_Image_Information_Removal/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-to-image editing methods based on diffusion models face significant challenges. Fine-tuning-based approaches (e.g., Imagic) often overfit to the input image, require lengthy inference times, and struggle to preserve content not specified in the text prompt. Conversely, methods that rely on structural guidance like edge maps (e.g., ControlNet) fail to retain crucial non-structural attributes such as color and texture. The authors address the practical problem of creating an editing model that can make specific, text-guided changes while robustly preserving the text-irrelevant content of the original image, without the drawbacks of long inference times or overfitting.

## 2. Key Ideas and Methodology
The paper introduces IIR-Net, a model that leverages the original image as an additional control signal for a pretrained diffusion model to better preserve context. The core hypothesis is that by selectively removing information from this control signal, the model can be forced to perform the desired edit instead of simply copying the input (the "identical mapping" issue).

The methodology centers on an **Image Information Removal (IIR) module** that processes the input image before it is fed to the diffusion model's control network. The IIR module performs two key operations:
1.  **Color-related Information Removal:** It uses Grounded-SAM to identify the Region of Interest (RoI) based on the text prompt and converts this region to grayscale, erasing its original color information.
2.  **Texture-related Information Removal:** It applies Gaussian noise to the image. The noise intensity is adjustable, allowing for more aggressive texture removal when needed (e.g., changing "grass" to "sand") while preserving it for simpler color edits.

The final control signal is a concatenation of this modified image and a Canny edge map, which guides the diffusion process to generate an edited image that is faithful to both the text prompt and the original image's preserved content.

## 3. Datasets Used / Presented
The model's performance was evaluated on three standard datasets to cover various editing scenarios:
*   **CUB-200-2011:** An object-centric dataset of 200 bird species (~11.8k images). Used to evaluate fine-grained, part-based object editing.
*   **Outdoor Scenes:** A dataset of ~8.5k images from webcams showing various scenes. Used to test scene-level attribute editing (e.g., changing season or time of day).
*   **COCO:** A large-scale dataset with complex scenes (~123k images). Used to evaluate region-based editing on diverse objects within complex backgrounds.

For evaluation, 150 test images were randomly selected from each dataset.

## 4. Main Results
IIR-Net demonstrated a superior trade-off between editability (alignment with text) and fidelity (preserving original content) compared to state-of-the-art methods.
*   **Quantitative Metrics:** On the COCO dataset, IIR-Net achieved a much better fidelity score (LPIPS of 0.301, lower is better) compared to Imagic (0.567), while also improving the editability score (CLIP score of 24.30 vs. 21.53, higher is better).
*   **User Study:** In a user study on COCO images, edits from IIR-Net were preferred 68.3% of the time, significantly outperforming ControlNet (33.3%), Text2LIVE (30.0%), and Imagic (23.3%).
*   **Inference Speed:** The method is highly efficient, with an inference time of ~5 seconds, which is comparable to ControlNet and two orders of magnitude faster than Imagic (~483 seconds).

The authors claim their approach achieves the best editability-fidelity trade-off results and is highly preferred by users.

## 5. Ablation Studies
The paper reports on two key ablation experiments to validate the effectiveness of the IIR module.
1.  **Effect of the IIR Module:** The model was tested without the IIR module, using the unmodified original image as input. This resulted in the model failing to perform any edits and simply outputting the original image, confirming that the IIR module is essential for overcoming the "identical mapping" issue.
2.  **Effect of Noise Augmentation:** The noise level within the IIR module was varied. The results showed that low noise is sufficient for color editing tasks (e.g., changing a "white airplane" to "green"). However, a higher noise level was necessary to successfully perform texture editing (e.g., changing "grass" to "sand"). This demonstrates that the noise component is crucial for texture-related tasks and provides a controllable mechanism for different types of edits.

## 6. Paper Figures
![Figure 2. IIR-Net Overview. Our model mainly consists of two modules: (A) Conditional Latent Diffusion Model: We introduce the original image x as additional control to our model to preserve the text-irrelevant features of x . See Section 3.1 for detailed discussion; (B) Image Information Removal Module: We erase the image information mainly by two operations. First, we convert RGB values to the gray values in the RoI to exclude the color information. Second, we add Gaussian noise to the input image to partially erase the texture-related information. This module is applied to address the identical mapping issue. See Section 3.2 for detailed discussion.]({{ '/images/05-2023/Text-to-image_Editing_by_Image_Information_Removal/figure_2.jpg' | relative_url }})
![Figure 3. Qualitative comparison on CUB and Ourdoor Scenes. From top to bottom: input image, Text2LIVE [ 1 ], Imagic [ 9 ], ControlNet [ 40 ], and ours. Generated images have 512 pixels on their shorter side. See Section 4.2 for discussion.]({{ '/images/05-2023/Text-to-image_Editing_by_Image_Information_Removal/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative comparison for various editing tasks on the COCO dataset. From top to bottom: color editing, scene attribute transfer, texture editing, and style transfer. Generated images have 512 pixels on their shorter side. Objects that are the target of modification are in red bounding boxes and whereas objects that should be preserved are in green bounding boxes. See Section 4.2 for discussion.]({{ '/images/05-2023/Text-to-image_Editing_by_Image_Information_Removal/figure_4.jpg' | relative_url }})
![Figure 5. Ablation Study. We perform experiments to evaluate the effectiveness of our color removal and texture removal operations. Images generated without our image information removal module are outlined by the blue bounding box. See Section 4.2 for discussion.]({{ '/images/05-2023/Text-to-image_Editing_by_Image_Information_Removal/figure_5.jpg' | relative_url }})
![Figure 6. Failure cases include inconsistencies with the original image in non-rigid image editing task (top); challenges in notably modifying the brightness of the image (middle), and inaccurate localization or segmentation (bottom). See Section 5 for discussion.]({{ '/images/05-2023/Text-to-image_Editing_by_Image_Information_Removal/figure_6.jpg' | relative_url }})
