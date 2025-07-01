---
title: A_Diffusion-Based_Framework_for_Occluded_Object_Movement
layout: default
date: 2025-04-02
---
![(f) Ours (e) DiffEditor (d) DragDiffusion Figure 1: Comparison with other methods for occluded object movement. Given a real-world image, our method can seamlessly move the occluded object to a user-specified position while completing the occluded portion.]({{ '/images/04-2025/A_Diffusion-Based_Framework_for_Occluded_Object_Movement/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The paper addresses the challenging task of seamlessly moving an occluded object within an image. Existing image editing methods struggle with this task because it requires two distinct steps: completing the unseen (occluded) portion of the object and then relocating the now-complete object to a new position harmoniously. Current methods either fail to complete the object (e.g., drag-style editors) or generate unrealistic content when attempting to fill in the missing parts (e.g., standard inpainting models). The authors aim to bridge this gap by leveraging the powerful generative capabilities and real-world knowledge embedded in pre-trained diffusion models.

## 2. Key Ideas and Methodology
The core of the paper is **DiffOOM**, a diffusion-based framework that decouples the problem into two parallel branches: de-occlusion and movement.

*   **De-occlusion Branch:** This branch focuses on completing the object. It takes a cropped image patch of the object as input. To focus the model, the background is initialized with a uniform color (**Color Fill**). During the diffusion process, a **Latent Hold** strategy preserves the visible parts of the object by replacing the updated latent with the original inverted latent at each step. It uses attention maps to progressively estimate the object's full mask, which guides the generation. A Low-Rank Adaptation (**LoRA**) module is fine-tuned on the visible parts to ensure the generated content is stylistically consistent.

*   **Movement Branch:** This branch places the completed object. It initializes the full image by filling the object's original location with noise. It then uses **Latent Optimization** to guide the diffusion process to generate the de-occluded object (from the first branch) at the user-specified target location. To avoid quality degradation, a **Latent Resizing** technique (decode -> pixel resize -> encode) is used instead of direct latent-space resizing. Finally, **Local Text Guidance** is applied to the target region to ensure the moved object blends seamlessly with its new surroundings.

## 3. Datasets Used / Presented
The authors created a specialized evaluation dataset derived from the **COCOA (Common Objects in Context-Amodal)** dataset.
*   **Description:** They filtered the COCOA training and validation sets to select images containing significantly occluded objects.
*   **Size and Usage:** The final dataset consists of 120 images with 150 distinct object samples. For each sample, the visible mask and category name are provided. To create a comprehensive test suite, 8 random target positions were generated for each sample, resulting in a total of 1200 test cases for evaluation.

## 4. Main Results
The proposed method, DiffOOM, demonstrates superior performance over existing methods in both de-occlusion and object movement tasks.
*   **De-occlusion:** Compared to PCNet, DiffOOM achieves better image realism (KID score of 0.0142 vs. 0.0186, lower is better) and prompt fidelity (CLIP-T score of 30.49 vs. 29.57, higher is better).
*   **Occluded Object Movement:** DiffOOM outperforms methods like SD Inpainting, DragDiffusion, and DiffEditor. It achieves the best score for removing artifacts from the original position (DINO-OP of 0.561) and for ensuring the moved object is harmonious with its new background (CLIP-TP of 0.960), while matching the best performance for successful relocation (DINO-TP of 0.742).
*   A comprehensive user study with 60 volunteers also confirmed that DiffOOM's results are preferred over other methods in over 75% of cases across all criteria (artifact removal, placement accuracy, and realism).

## 5. Ablation Studies
Ablation studies were performed to validate the contribution of each key component in the framework.

*   **Color Fill (CF):** Removing this strategy hurts the model's ability to accurately move the object, lowering the DINO-TP score from 0.742 to 0.717, as it can lead to over-generation.
*   **Attention Guidance (AG):** Removing the attention guidance mechanism leads to artifacts being left at the object's original position, worsening the DINO-OP score from 0.561 to 0.612.
*   **LoRA:** Removing the LoRA module for style consistency results in a mismatch between the original and generated parts of the object, reducing the DINO-TP score.
*   **Latent Resizing (LR):** Replacing the proposed latent resizing with direct pixel resizing causes severe degradation of the moved object, leading to a significant drop in the DINO-TP score from 0.742 to 0.695.
*   **Local Text Guidance (LTG):** Removing local text guidance at the target location reduces the harmony of the final result, as reflected by a lower CLIP-TP score.

## 6. Paper Figures
![Figure 2: Overview of proposed framework (a) and LoRA tuning process (b). (a) We decouple the task of occluded object movement into de-occlusion and movement, handled by parallel branches. Both branches are built upon Stable Diffusion V1.5 and operate simultaneously. The de-occlusion branch leverages the prior knowledge within the diffusion models to complete the occluded portion, while the movement branch mainly places the completed object at the target position. (b) To ensure the content generated by the de-occlusion branch aligns with the characteristics of the target object, we equip this branch with LoRA, which is fine-tuned using a masked diffusion loss that applies exclusively to the visible portions of the object.]({{ '/images/04-2025/A_Diffusion-Based_Framework_for_Occluded_Object_Movement/figure_2.jpg' | relative_url }})
![Figure 3: (a)-(b) showcase process of obtaining ¯ I s as Equ. (4). (b) marks 1 − ¯ M v with white mask. (c) (f) are results from variants of De-occlusion Branch. (c) is generated by filling 1 − ¯ M v with noise as Equ. (5). (d) introduces color-fill strategy as Equ. (6). (e) is generated under the guidance of progressively updating masks. (f) is the full Deocclusion Branch. (g) showcases the progressively updating masks based on the refined cross-attention map ¯ R C t .]({{ '/images/04-2025/A_Diffusion-Based_Framework_for_Occluded_Object_Movement/figure_3.jpg' | relative_url }})
![(d) (e) (f) Figure 4: (a) and (d) are source images, and the others are results from variants of Movement Branch. The starting and ending points of the yellow arrows represent the original and target positions of the moved object. (b) is result with direct resizing as Equ. (8). (c) introduces the latent resizing operation as Equ. (9), alleviating the severe degradation. (e) and (f) are results w/o and w/ local text guidance, which helps the object integrate into surroundings more appropriately.]({{ '/images/04-2025/A_Diffusion-Based_Framework_for_Occluded_Object_Movement/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative comparison on de-occlusion. PCNet struggles with the completion of large-scale occlusion and complex objects, while our method can generate high-quality content consistent with the target object.]({{ '/images/04-2025/A_Diffusion-Based_Framework_for_Occluded_Object_Movement/figure_5.jpg' | relative_url }})
![Figure 6: Qualitative comparison on occluded object movement. The target objects are marked by yellow masks. The starting and ending points of the orange arrows represent the original and target positions of the moved object.]({{ '/images/04-2025/A_Diffusion-Based_Framework_for_Occluded_Object_Movement/figure_6.jpg' | relative_url }})
![Figure 7: Examples of integrating our framework with MasaCtrl and DragDiffusion. Our framework enables two editing methods to perform precise editing in complex scenes.]({{ '/images/04-2025/A_Diffusion-Based_Framework_for_Occluded_Object_Movement/figure_7.jpg' | relative_url }})
