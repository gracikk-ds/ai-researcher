---
title: DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models
layout: default
date: 2024-10-15
---
![Figure 1: DreamSteerer enables efficient editability enhancement for a source image with any existing T2I personalization models, leading to significantly improved editing fidelity in various challenging scenarios. When the structural difference between source and reference images are significant, it can naturally adapt to the source while maintaining the appearance learned from the personal concept.]({{ '/images/10-2024/DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Recent text-to-image (T2I) personalization methods like DreamBooth can learn a user-specified concept (e.g., a pet dog) from a few images and generate it in new contexts. However, they perform poorly on a related but distinct task: editing a *source image* to include the personalized concept. A naive combination of personalization and editing frameworks often leads to distorted results, poor structural alignment with the source image, and failure to adapt the personalized concept naturally. The authors aim to bridge this gap by developing a method that enhances the editability of existing personalized diffusion models, enabling high-fidelity, source-conditioned personalized editing.

## 2. Key Ideas and Methodology
The paper introduces **DreamSteerer**, an efficient, plug-in fine-tuning method to augment existing T2I personalization models. Its methodology is built on three core ideas:

- **Editability Driven Score Distillation (EDSD):** The core hypothesis is that a personalized model's poor editability can be improved by "steering" it towards the behavior of the original, more general pre-trained model, which has better editability. DreamSteerer formulates this as a novel score distillation objective. It fine-tunes the personalized model's parameters to make its noise prediction on a slightly edited image match the noise prediction of the pre-trained model on the original source image. This effectively distills the pre-trained model's robust editing capability into the specialized model.

- **Mode Shifting Regularization with Spatial Feature Guided Sampling:** The authors identify that EDSD alone can cause "mode trapping," where the model generates a hybrid of the source and reference concepts. To solve this, they introduce a regularization term. They first generate a set of guided images that combine the personalized concept's appearance with the source image's structure (guided by UNet self-attention features). Then, they use a standard diffusion loss on these guided images to regularize the EDSD optimization, shifting the model's distribution away from the trapped mode and towards a more editable state.

- **Automatic Subject Masking:** To ensure edits are localized to the relevant subject and the background is preserved, the final editing step uses a modified Delta Denoising Score (DDS-SM). This method automatically extracts a mask for the subject using cross-attention maps and applies the editing delta only within that masked region.

## 3. Datasets Used / Presented
DreamSteerer is evaluated as a plug-in on three established personalization baselines: **Textual Inversion**, **DreamBooth**, and **Custom Diffusion**.
- **Personalization Concepts:** 16 diverse concepts (toys, animals, accessories, etc.) from the **Dream-Matcher** and **ViCo** datasets were used to train the baseline personalized models.
- **Source Images for Editing:** 70 random real-world images were used as editing targets for each baseline.
- **One-Shot Evaluation:** A subset of 20 cat and dog images was used to test performance in a data-hungry, one-shot personalization scenario.

## 4. Main Results
DreamSteerer significantly improves the editing performance of all three baselines across multiple metrics.
- **Improved Source Image Fidelity:** Compared to the baselines, DreamSteerer achieves better structural and perceptual alignment with the source image. For instance, with DreamBooth, it improves the LPIPS (VGG) score by 7.3% (lower is better) and the SSIM score by 1.8% (higher is better).
- **Preserved Concept Identity:** The method maintains or slightly improves the semantic similarity to the personalized concept, as measured by CLIP-I scores.
- **Superior User Preference:** In a user study, results from DreamSteerer were strongly preferred over the baselines, with preference scores increasing by +44.5% against Textual Inversion, +29.7% against DreamBooth, and +49.7% against Custom Diffusion.
- **Robustness in Data-Hungry Scenarios:** In one-shot personalization, DreamSteerer still shows substantial gains, improving DreamBooth's LPIPS (Alex) score by 27.9% and SSIM by 5.2%.

The authors claim DreamSteerer serves as a pivotal bridge from general text-driven editing to the more complex and practical task of personalized image editing.

## 5. Ablation Studies
The paper presents comprehensive ablation studies to validate each component of DreamSteerer.
- **Effect of EDSD:** Removing EDSD results in a significant drop in source image alignment. For the DreamBooth baseline, this leads to a worse LPIPS score (0.246 vs. 0.229) and a lower SSIM score (0.753 vs. 0.768), confirming that EDSD is crucial for enhancing editability and structural preservation.
- **Effect of Mode Shifting Regularization:** Removing the mode shifting regularization causes a severe loss of the target subject's appearance, reflected in lower CLIP-I scores (e.g., 0.745 vs. 0.761 for DreamBooth). While source alignment scores become exceptionally high, the edit fails to incorporate the personalized concept. This demonstrates the regularization is essential for balancing concept fidelity with editability and avoiding mode collapse.

## 6. Paper Figures
![Figure 2: Source class bias of DreamBooth trained for "plushie_tortoise".]({{ '/images/10-2024/DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3: Overall framework of DreamSteerer (the gradient flows are illustrated with dashed lines).]({{ '/images/10-2024/DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4: The effect of different regularization strategies on the editing and generation results of a DreamBooth baseline. The source prompt is "a photo of a cat sitting next to a mirror".]({{ '/images/10-2024/DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5: Illustration on the effect of the proposed components on editing with a DreamBooth baseline (1st row shows the editing results; 2nd row shows the editing directions, where brown means zero).]({{ '/images/10-2024/DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6: Ablation study on EDSD and Mode Shifting Regularization.]({{ '/images/10-2024/DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models/figure_6.jpg' | relative_url }})
![Figure 7: Comparison of one-shot performance.]({{ '/images/10-2024/DreamSteerer:_Enhancing_Source_Image_Conditioned_Editability_using_Personalized_Diffusion_Models/figure_7.jpg' | relative_url }})
