---
title: LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing
layout: default
date: 2024-06-25
---
![Figure 1: Given a few reference images of the same identity, our framework learns a personalized identity prior and applies diverse non-rigid image editing for a test image guided by a textual description, leading to high identity-preserved edited results.]({{ '/images/06-2024/LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of non-rigid image editing, such as altering a subject's pose, expression, or viewpoint, while preserving its unique identity. Existing text-to-image diffusion models often fail to maintain subject consistency because they lack a personalized identity prior. Conversely, methods that do learn a personalized prior are typically designed for subject generation, not fine-grained editing, or are limited to specific domains like faces and require numerous reference images. This paper introduces and tackles the novel task of learning a personalized identity prior from a few reference images to enable high-fidelity, text-guided, non-rigid editing for general subjects.

## 2. Key Ideas and Methodology
The paper presents LIPE (Learning Personalized Identity Prior for Non-rigid Image Editing), a two-stage framework.

1.  **Personalized Prior Learning:** The first stage fine-tunes a pre-trained text-to-image model (SDXL) on a small set (3-5) of reference images. The key innovation is an "editing-oriented data augmentation" strategy. It uses a vision-language model (LLaVa) to create detailed captions for the reference images (the identity dataset) and leverages GPT-4 to generate diverse, action-focused text-image pairs for the subject's class (the regularization dataset). This enhances the model's ability to render the specific subject in various non-rigid states without forgetting general concepts.

2.  **Non-rigid Image Editing:** The second stage uses a novel editing method called NIMA (Non-rigid Image editing via identity-aware MAsk blend). NIMA automatically extracts a precise mask of the subject by analyzing cross-attention maps within the diffusion model. During the editing process, it uses this mask to blend the inverted latents of the original image (preserving the background) with the newly generated latents for the target edit, ensuring that only the subject is modified according to the text prompt.

## 3. Datasets Used / Presented
The authors introduce a new dataset named **LIPE** specifically for this task.
*   **Content:** The dataset contains 28 diverse subjects, including everyday objects (backpacks, toys), animals (cats, dogs, bears), and human faces.
*   **Structure:** Each subject instance is accompanied by 3-5 reference images for learning the identity prior and one test image for evaluating editing performance.
*   **Usage:** It serves as a comprehensive benchmark to evaluate the proposed method and facilitate future research in personalized non-rigid editing.

## 4. Main Results
LIPE was compared against leading methods like Imagic, MasaCtrl, and MyStyle, as well as a strong baseline (DreamCtrl).
*   **Qualitative:** Visual results show LIPE produces edits that are significantly more faithful to the subject's identity and the text prompt while maintaining background consistency, outperforming all baselines.
*   **Quantitative (User Study):** In a 30-person user study, LIPE achieved the highest scores across all criteria: Identity Consistency (0.95 vs. 0.75 for the next best), Background Consistency (0.89 vs. 0.81), and Editing Satisfaction (0.74 vs. 0.65).
*   **Quantitative (Metrics):** LIPE also scored highest on identity preservation metrics like DINOv2-I (0.88) and CLIP-I (0.92) and showed strong alignment between text and image changes (CLIP-D: 0.08). The authors conclude that their method successfully learns and applies a personalized prior for high-quality non-rigid editing.

## 5. Ablation Studies
The paper reports on two key ablation experiments to validate its design choices.

1.  **Without Editing-Oriented Data:** A model was trained without the proposed detailed, action-descriptive captions. This version struggled to generate the specific non-rigid actions (e.g., "head facing the camera") described in the text prompt, demonstrating the importance of the curated data for learning fine-grained control.
2.  **Without NIMA (Mask Blending):** The editing was performed without the identity-aware mask blending mechanism. This resulted in significant, unwanted changes to the image background, confirming that the mask is crucial for precisely controlling the edited region and preserving background consistency.

## 6. Paper Figures
![Figure 2: The pipeline for data augmentation in learning personalized identity prior. (a) We make detailed editing-oriented captions for reference images by harnessing the large language and vision assistant. (b) We leverage the GPT-4 and pre-trained T2I model to generate diverse editing-oriented text-image pairs for the subject’s class, which serves as the regularization dataset.]({{ '/images/06-2024/LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Illustration of Non-rigid Image editing via identity-aware MAsk blend (NIMA). (a) Given a test image, we first invert it to obtain the inverted latents { x i } for image reconstruction, to further obtain the subject mask M s for the source image. (b) Afterward, to achieve non-rigid image editing, we generate the target image by blending the source x t and target ˆ x T information with the generated masks ( M s , M e t ).]({{ '/images/06-2024/LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Identity-aware attention map.]({{ '/images/06-2024/LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Comparisons with previous work on general objects. The red font highlights the editing directions. Left to right: Reference images, Test image, Imagic [ 30 ], MasaCtrl [ 9 ], DreamCtrl, and Our method.]({{ '/images/06-2024/LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Comparisons with previous work on human face. Left to right: Reference images, Test image, Imagic [ 30 ], MasaCtrl [ 9 ], DreamCtrl, MyStyle [ 51 ], and Our method. The text on the arrow represents the target prompt utilized during the editing process, aligning with the semantic direction of the StyleGAN[16] utilized in MyStyle[51].]({{ '/images/06-2024/LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7: Ablation Study. In the ablation study, we confirmed the effectiveness of the two strategies in our method. Adding action-descriptive captions while learning the personalized identity prior helps the model comprehend non-rigid properties to assist with editing. Obtaining target mask information in advance during the editing process helps the method control the outcomes more precisely.]({{ '/images/06-2024/LIPE:_Learning_Personalized_Identity_Prior_for_Non-rigid_Image_Editing/figure_7.jpg' | relative_url }})
