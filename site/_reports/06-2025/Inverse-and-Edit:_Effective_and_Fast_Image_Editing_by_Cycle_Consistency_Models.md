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
The authors address the trade-off between speed and quality in diffusion-based image editing. While full-step diffusion models produce high-quality edits, they are computationally intensive and slow. Conversely, accelerated "distilled" models are fast but suffer from poor *inversion quality*—the inability to accurately reconstruct an original image. This poor reconstruction limits their ability to perform precise edits while preserving the image's core structure and semantic content.

## 2. Key Ideas and Methodology
The paper's core idea is to enhance the inversion capability of fast consistency models to enable high-fidelity editing in very few steps (e.g., four). The methodology is built on two key contributions:

-   **Cycle-Consistency Optimization:** The authors propose a fine-tuning strategy for a pair of consistency models: a forward model (fCM) for inversion and a backward model (CM) for generation. They optimize the fCM by running a full inversion-generation cycle and minimizing the perceptual difference (LPIPS loss) between the original and the final reconstructed image. The CM is kept frozen to maintain its high-quality generation capabilities. This "global" alignment ensures the inverted latent accurately represents the source image.
-   **Guidance Mechanism Adaptation:** The framework adapts the "Guide-and-Rescale" technique. During the inversion (noising) phase, it caches self-attention maps and features. These are then used as a guidance signal during the generation (denoising) phase to ensure the edited output remains structurally consistent with the original image, offering a controllable balance between editability and content preservation.

## 3. Datasets Used / Presented
-   **MS-COCO:** The training split was used to fine-tune the model. The validation split, containing over 2,700 high-resolution images, was used for the quantitative evaluation of image reconstruction performance.
-   **Pie-Bench:** A standard benchmark with 420 images was used for both qualitative and quantitative evaluation of various text-guided image editing tasks.
-   **Custom Dataset:** A curated set of 60 images was used to assess performance on specific challenging edits, such as object replacement and local attribute modification.

## 4. Main Results
-   **Image Reconstruction:** The proposed method significantly outperforms other fast (4-step) inversion methods. It achieves an LPIPS score of 0.309, a marked improvement over the baseline iCD (0.372) and GNRi (0.424), bringing it much closer to the performance of a full 50-step DDIM model (0.268).
-   **Image Editing:** In editing tasks, the method achieves a state-of-the-art balance between edit quality and content preservation among accelerated models. It obtains results comparable to full-step methods like Guide-and-Rescale while being substantially more efficient.
-   **Author-claimed impact:** The proposed framework achieves editing quality that matches or surpasses traditional full-step diffusion models but with a significant reduction in computational cost, making high-quality editing much faster.

## 5. Ablation Studies
-   **Impact of Cycle-Consistency Fine-tuning:** To isolate the effect of their optimization strategy, the authors compared their fine-tuned model (without guidance) to the baseline iCD model. The fine-tuning alone dramatically improved content preservation, boosting the DINOv2 score from 0.599 to 0.719 and lowering the LPIPS error from 0.38 to 0.312.
-   **Impact of Guidance:** Adding the guidance mechanism to their fine-tuned model further improved content preservation (DINOv2 score increased to 0.747, LPIPS dropped to 0.296). The study also showed that simply applying guidance to the baseline iCD model was insufficient to achieve the same level of quality, highlighting that the improved inversion is the critical component.

## 6. Paper Figures
![Figure 2: (a): Visual comparison of editing results produced by our fine-tuned model and the baseline. (b): Quantitative evaluation of the editing results from our method and the baseline.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_2.jpg' | relative_url }})
![Figure 3: Visualization of editing results produced by prompt switching (second column) and by our method with guidance (third column).]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_3.jpg' | relative_url }})
![Figure 4: Schematic illustration of the Cycle-Consistency method with guidance. Image editing is performed by noising over four steps using the fine-tuned forward consistency model, followed by denoising with corrections from the guider energy function.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_4.jpg' | relative_url }})
![Figure 5: Examples of image reconstruction obtained from our method and from other approaches.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_5.jpg' | relative_url }})
![Figure 7: Examples of image editing results obtained using our method with guidance and other approaches.]({{ '/images/06-2025/Inverse-and-Edit:_Effective_and_Fast_Image_Editing_by_Cycle_Consistency_Models/figure_7.jpg' | relative_url }})
