---
title: Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models
layout: default
date: 2025-06-23
---
## Inverse-and-Edit: Effective and Fast Image Editing by Cycle Consistency Models
**Authors:**
- Ilia Beletskii
- Aibek Alanov

**ArXiv URL:** http://arxiv.org/abs/2506.19103v1

**Citation Count:** None

**Published Date:** 2025-06-23

![Figure 1: (a): Visual comparison of results produced by our fine-tuned model and the baseline. (b): Quantitative evaluation of the reconstruction quality of our method and the baseline on the MS-COCO validation set.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Diffusion models for image editing are either computationally expensive (full-step models) or suffer from poor image inversion quality (distilled, fast models). High-quality inversion is essential for preserving the structure and semantics of the source image, which is a prerequisite for precise editing. The authors address this gap by developing a method to significantly improve the inversion and reconstruction capabilities of fast, few-step diffusion models, aiming to achieve the quality of full-step methods with the efficiency of distilled ones.

## 2. Key Ideas and Methodology
The core of the paper is a novel framework, **Inverse-and-Edit**, that enhances the inversion quality of consistency models.

-   **Core Principle:** The authors introduce a **cycle-consistency optimization strategy**. The core idea is that an image, when inverted to its latent representation and then generated back, should be nearly identical to the original.
-   **Methodology:** The method takes a pretrained forward consistency model (fCM for inversion) and a backward consistency model (CM for generation). It introduces a fine-tuning stage where only the fCM is optimized. The optimization objective is to minimize the perceptual difference (measured by LPIPS loss) between the original input image and the image reconstructed after a full inversion-generation cycle. This cycle is computationally feasible because it only involves a few steps (e.g., four for inversion, four for generation).
-   **Editing with Guidance:** To enable precise editing control, the authors adapt the **Guide-and-Rescale** mechanism. During the generation (denoising) phase, the model is guided by energy functions that align the self-attention maps and internal features of the generated image with those cached during the initial inversion of the source image. This preserves the original layout and details while incorporating the edit from the target prompt.

## 3. Datasets Used / Presented
-   **MS-COCO:** The training split was used for the cycle-consistency fine-tuning process. The validation split, containing over 2,700 high-resolution images, was used for the quantitative evaluation of image reconstruction performance.
-   **Pie-Bench:** A standard benchmark dataset with 420 images was used for both qualitative and quantitative evaluation of text-guided image editing performance across a broad range of edit types.
-   **Custom Dataset:** A small, custom set of 60 images was used to evaluate specific, challenging editing tasks like object replacement, local emotion changes, and appearance modifications.

## 4. Main Results
The proposed method achieves state-of-the-art performance for fast image editing, matching or exceeding full-step models while being significantly more efficient.

-   **Image Reconstruction:** On the MS-COCO dataset, the method achieves a LPIPS score of **0.309** in just 4 steps. This is a significant improvement over other fast methods like iCD (0.372) and is close to the performance of the 50-step DDIM inversion (0.268), demonstrating superior reconstruction fidelity.
-   **Image Editing:** On the Pie-Bench dataset, the method outperforms all other accelerated models and is competitive with full-step methods. It achieves a DINOv2 score of **0.747** (measuring content preservation) and a LPIPS of **0.296**, showing a strong balance between editability and preserving the original image's structure. For comparison, the full-step Guide-and-Rescale (GaR) model scores 0.721 and 0.277, respectively, but requires over 10x more computation.

The authors claim their method enables high-quality editing in just four steps, making it a practical and effective solution.

## 5. Ablation Studies
The paper presents ablation studies to validate the contributions of its two main components: the cycle-consistency fine-tuning and the guidance mechanism.

-   **Effect of Cycle-Consistency Fine-tuning:** Comparing the baseline iCD model to the proposed model without guidance ("Ours w/o guidance"), the fine-tuning process dramatically improves content preservation. The DINOv2 score increases from **0.599 to 0.719**, and the LPIPS reconstruction error drops from **0.38 to 0.312**. This confirms that the proposed optimization is the key to better inversion quality.
-   **Effect of Guidance:** Adding the guidance mechanism to the fine-tuned model ("Ours with guidance") further improves performance. It increases the DINOv2 score from **0.719 to 0.747** and lowers the LPIPS score from **0.312 to 0.296**. This shows that guidance enhances detail preservation and structural consistency during editing. Applying the same guidance to the baseline iCD model yields much weaker results, proving that high-quality inversion is a prerequisite for effective guidance.

## 6. Paper Figures
![Figure 2: (a): Visual comparison of editing results produced by our fine-tuned model and the baseline. (b): Quantitative evaluation of the editing results from our method and the baseline.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_2.jpg' | relative_url }})
![Figure 3: Visualization of editing results produced by prompt switching (second column) and by our method with guidance (third column).]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_3.jpg' | relative_url }})
![Figure 4: Schematic illustration of the Cycle-Consistency method with guidance. Image editing is performed by noising over four steps using the fine-tuned forward consistency model, followed by denoising with corrections from the guider energy function.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_4.jpg' | relative_url }})
![Figure 5: Examples of image reconstruction obtained from our method and from other approaches.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_5.jpg' | relative_url }})
![Figure 7: Examples of image editing results obtained using our method with guidance and other approaches.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_7.jpg' | relative_url }})
