---
title: Learning_Complex_Non-Rigid_Image_Edits_from_Multimodal_Conditioning
layout: default
date: 2024-12-13
---
## Learning Complex Non-Rigid Image Edits from Multimodal Conditioning
**Authors:**
- Nikolai Warnerpapers: 2, 
- Irfan Essa, h-index: 2, papers: 5, citations: 11

**ArXiv URL:** http://arxiv.org/abs/2412.10219v1

**Citation Count:** 0

**Published Date:** 2024-12-13

![Figure 1. Given a single image, multiple controllable identitypreserving edits can be specified with different text captions. Given a masked insertion scene and reference image containing a person to insert, our fine-tuned model inserts them into the scene controllable as controlled by a given text caption. Text and image-based inference on unseen images using an image + text model. Where captions are unavailable, we train the text and image model on a blank caption.]({{ '/images/12-2024/Learning_Complex_Non-Rigid_Image_Edits_from_Multimodal_Conditioning/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of performing complex, non-rigid image edits on human subjects, specifically inserting a person from a reference image into a new scene with a different pose. Current generative models often struggle with this task on "in-the-wild" data, failing to simultaneously preserve the person's identity, follow user control (via text or pose), and generate plausible interactions with objects in the scene. The paper aims to bridge this gap by developing a model that is highly controllable and robust in diverse, real-world scenarios.

## 2. Key Ideas and Methodology
The core idea is to enhance a diffusion-based inpainting model with multimodal conditioning to guide the generation process. The authors propose a framework that finetunes a pre-trained Stable Diffusion model using a combination of three inputs:
1.  **Reference Image:** A cropped image of the person to preserve their identity, fed into the model via cross-attention.
2.  **Text Caption:** A textual description of the desired pose change or action (e.g., "He lunges with his right leg"). This provides high-level semantic control.
3.  **2D Pose Skeleton:** A target pose skeleton (17 keypoints) to provide explicit structural guidance.

A key methodological contribution is the use of a multimodal Large Language Model (GPT-4V) to automatically generate "scene difference captions" by comparing pairs of frames from videos. This creates a large-scale, albeit noisy, dataset for training the model to understand text-based edit instructions without expensive manual annotation. The image, text, and pose information are projected into a common embedding space and used to condition the diffusion model's U-Net.

## 3. Datasets Used / Presented
The authors create and use a new dataset derived from several public, human-centric video sources. This dataset is used for training and evaluation.

*   **Source Datasets:** Kinetics-700, NTU-RGB+D, Charades, and Fit3D.
*   **Processing and Annotation:** Videos are processed to sample pairs of keyframes that show significant motion of a single person. For a subset of these pairs, the authors use GPT-4V to automatically generate captions describing the change in pose between the two frames. This results in a training set of image pairs, corresponding poses, and noisy text captions.
*   **Dataset Size:** After processing, the dataset includes 13,400 videos from Kinetics (yielding ~5,800 captions) and 65,775 sub-videos from NTU-RGB+D (yielding ~7,700 captions).

## 4. Main Results
The primary evaluation was a human user study, as standard metrics like FID (photorealism) and PCKh (pose adherence) do not fully capture identity preservation or contextual plausibility.

*   **Identity Preservation:** The full model (`img-pose-text`) achieved the highest identity preservation score from human raters (68.5% for scenes without objects, 41% for scenes with objects), outperforming the image-only baseline (61% and 25%, respectively).
*   **Controllability & Interactions:** Adding text and pose conditioning significantly improved the model's ability to follow instructions and generate plausible interactions. In scenes with objects, the full model also achieved the highest rating for plausible interactions (33%), a notable improvement over the baseline (24%).
*   **Author's Takeaway:** The results demonstrate that combining image, text, and pose conditioning enables controllable, identity-preserving, non-rigid edits on in-the-wild images, showing superior performance in complex scenes with person-object interactions compared to baseline methods.

## 5. Ablation Studies
The authors performed an ablation study by training and evaluating four different model configurations based on the conditioning signals used.

1.  **Img-Only (Baseline):** Conditioned only on the reference image.
2.  **Img-Text:** Conditioned on the reference image and a text caption.
3.  **Img-Pose:** Conditioned on the reference image and a target pose.
4.  **Img-Pose-Text (Full Model):** Conditioned on all three inputs.

*   **Impact of Conditioning:** The user study revealed that adding pose and text conditioning (`Img-Pose-Text`) yielded the best results for identity preservation (68.5%) and plausible object interactions (33%). While adding only pose (`Img-Pose`) also improved performance over the baseline, adding only text (`Img-Text`) sometimes degraded identity preservation. This indicates that all three modalities contribute to the final performance, with the combination being the most effective for achieving both control and quality.

## 6. Paper Figures
![Figure 2. Complex edits are achievable through weakly annotated supervision of a portion of the overall dataset, and finetuning jointly on text. Given a masked scene to insert a person into ("Scene") and a segmented crop of the person ("Ref"), the person is inserted into the scene. For comparison, we also provide the ground truth image that is paired with the caption and input. Given a scene, and person to insert, our model is capable of multiple non-rigid edits that preserve the identity of the person, despite a relatively small set of 13,487 weakly annotated captioned image pairs out of 78,000 videos. See Appendix Table 1 for dataset details and Section 3.3 for details on our weakly annotated captions.]({{ '/images/12-2024/Learning_Complex_Non-Rigid_Image_Edits_from_Multimodal_Conditioning/figure_2.jpg' | relative_url }})
![Figure 3. Comparison of our approach to baselines for identity preservation and controllability of in-the-wild images. The input image is controlled using the prompts below each row, and the human subject is transferred to new frames for relevant models (our’s and Kulal et al.). No baseline achieves comparable identity-preserving non-rigid edits on in-the-wild data. Baselines either insert a person without controllability (Kulal et al.), or are controllable but fail to generalize to in-the-wild images (MASACtrl, PIDM). Our approach maintains similar photorealism to Kulal et al., with improved controllability. * PIDM works well on its training dataset but is brittle in the wild, likely due to its fashion-related training dataset. † Kulal et al. results are from the re-trained model with image conditioning only.]({{ '/images/12-2024/Learning_Complex_Non-Rigid_Image_Edits_from_Multimodal_Conditioning/figure_3.jpg' | relative_url }})
![Figure 4. System diagram illustrating the process of generating a desired edit using multiple inputs including noise target latent, binary mask, masked target latent, reference image, and change of scene prompt. The Affordance Diffusion Network on the right is the formulation proposed by [ 16 ], our improvements to controllability come from the framework described on the left. We study combinations of pose and weakly annotated text conditioning to learn more controllable and complex image edits that still preserve the identity of a person in a scene. No other work to our knowledge combines controllable non-rigid edits with identity preservation, and works in the wild.]({{ '/images/12-2024/Learning_Complex_Non-Rigid_Image_Edits_from_Multimodal_Conditioning/figure_4.jpg' | relative_url }})
![Figure 5. Using pose conditioning is insufficient to specify personobject interactions. Combining textual embeddings allows the model to contextualize how the person interacts with their surroundings. For example, the exercise ball or bicycle are faithfully maintained with text on Rows 3 and 4, but not with just pose. We show qualitative improvement of person-object interactions by conditioning on weakly generated captions, combined with reference images and pose data. We use the pose from the ground truth combined with the pose from the reference image for conditioning, fed through a single learnable dense layer.]({{ '/images/12-2024/Learning_Complex_Non-Rigid_Image_Edits_from_Multimodal_Conditioning/figure_5.jpg' | relative_url }})
