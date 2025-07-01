---
title: Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis
layout: default
date: 2025-03-19
---
![Figure 1. (a) The VAE [ 38 ] reconstruction deteriorates the detailed information of person images, especially the facial regions and complex textures. These issues worsen for the generated latent with small deviations. A small deviation ϵ = 0 . 2 is added to demonstrate the often case of generated latent. (b) Our methods preserve this detailed information better than other LDM-based methods by introducing multi-focal conditions.]({{ '/images/03-2025/Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key limitation in Pose-Guided Person Image Synthesis (PGPIS) methods that use Latent Diffusion Models (LDMs). While LDMs are powerful, their initial image-to-latent compression step is lossy and often degrades high-frequency details. This results in generated images with blurry clothing textures and distorted or inconsistent facial features, which is a critical problem for creating realistic and identity-preserving person images. Existing LDM-based methods condition on the entire source image, which struggles to focus on these small but perceptually vital regions.

## 2. Key Ideas and Methodology
The paper introduces the **Multi-focal Conditioned Latent Diffusion (MCLD)** model to overcome detail loss by explicitly conditioning the diffusion process on disentangled features from sensitive "focal" regions.

- **Core Hypothesis:** By isolating and separately conditioning on pose-invariant features from the face and clothing, the model can better preserve identity and fine-grained appearance details during synthesis.

- **High-level Approach:** The model uses a two-branch conditioning architecture built on Stable Diffusion.
    1.  **Multi-focal Feature Extraction:** Three key conditions are extracted from the source image:
        *   **Face Identity:** A cropped face region is fed into a pretrained face recognition model to obtain a pose-invariant identity embedding (`F_emb`).
        *   **Appearance Texture:** The source image is warped into a UV texture map using DensePose to disentangle clothing appearance from pose. This map is then encoded to get both a low-level structural representation (`A_ref`) and a high-level semantic embedding (`A_emb`).
        *   **Global Context:** A standard CLIP embedding of the full source image (`I_emb`) provides overall context.
    2.  **Multi-focal Condition Aggregation (MFCA):** A novel module intelligently fuses these conditions and injects them into the UNet denoiser via cross-attention. It selectively injects different conditions at different stages of the UNet (e.g., global context in the encoder, fine textures in the decoder) to optimize information flow.
    3.  **Pose Control:** A ControlNet-like Pose Guider uses DensePose maps to guide the generation toward the target pose.

- **Theoretical Foundations:** The method is built upon Latent Diffusion Models (LDMs) and leverages pretrained encoders (CLIP, face recognition models) for feature extraction and ControlNet principles for pose guidance.

## 3. Datasets Used / Presented
- **DeepFashion In-Shop Clothes Retrieval Benchmark:** This dataset, containing 52,712 high-resolution fashion model images, was used for training and evaluation. Following prior work, the authors created 101,966 training pairs and 8,570 validation pairs. The model was evaluated on generated images at 256×176 and 512×352 resolutions.

## 4. Main Results
MCLD demonstrates superior performance in preserving both image quality and identity compared to other LDM-based methods.

- **Quantitative Insights:**
    - On the DeepFashion dataset (512×352), MCLD achieves a state-of-the-art SSIM of **0.7557** and PSNR of **18.211**, outperforming methods like CFLD (SSIM 0.7478, PSNR 17.645).
    - It significantly improves the FID score among LDM-based methods, achieving **7.079** compared to CFLD's 7.149.
    - For face preservation, MCLD achieves a face similarity (FStgt) of **0.344** and face distance (dist_tgt) of **26.31**, indicating better identity preservation than competing methods like CFLD (FStgt 0.286, dist_tgt 27.54).

- **Author-claimed Impact:** The proposed multi-focal conditioning strategy effectively mitigates detail degradation in LDMs, enabling the generation of more realistic and identity-consistent person images, along with flexible appearance editing capabilities.

## 5. Ablation Studies
The authors conducted a thorough ablation study to validate the contributions of the multi-focal conditions and the MFCA aggregation module.

- **Experiment 1 (Baseline vs. Concatenation):** Starting with a baseline using only the global image condition (B1), they incrementally added appearance (B2) and face (B3) conditions using simple concatenation. This showed slight improvements but led to unstable performance, as the model struggled to balance the parallel conditions.

- **Experiment 2 (MFCA vs. Concatenation):** They replaced simple concatenation with their proposed MFCA module.
    - **Removing Global Context (B4):** Using only face and appearance conditions with MFCA resulted in a loss of semantic context for clothing styles.
    - **Removing Face Condition (B5):** Using global and appearance conditions with MFCA improved texture quality but failed to preserve facial identity.
    - **Full Model (Ours):** The full model, using all three conditions (Image, Appearance, Face) aggregated via MFCA, achieved the best performance across all metrics (e.g., SSIM improved from 0.7463 in B1 to **0.7557**).

This confirms that all three focal conditions are necessary and that the proposed MFCA module is critical for effectively integrating them to achieve superior results.

## 6. Paper Figures
![Figure 2. The overall pipeline of our proposed Multi-focal Conditioned Diffusion Model. (a) Face regions and appearance regions are first extracted from the source person images; (b) multi-focal condition aggregation module ϕ is used to fuse the focal embeddings as c emb ; (c) ReferenceNet R is used to aggregate information from the appearance texture map, denoted as c ref ; (d) Densepose provides the pose control to be fused into UNet with noise by Pose Guider.]({{ '/images/03-2025/Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis/figure_2.jpg' | relative_url }})
![Figure 3. Qualitative Comparison with several state-of-the-art models on the Deepfashion dataset. The inputs to our models are the target pose p t and the source person image I . From left to right the results are of NTED, CASD, PIDM, CFLD and ours respectively.]({{ '/images/03-2025/Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative ablation comparison. Refer to Tab. 3 for baseline settings.]({{ '/images/03-2025/Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis/figure_4.jpg' | relative_url }})
![Figure 5. Appearance editing results. Our method accepts flexible editing of given identities, poses, and clothes. This is achieved only by modifying some regions of conditions, and no need for any masking or further training.]({{ '/images/03-2025/Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis/figure_5.jpg' | relative_url }})
![Figure 6. Failure cases caused by (1) Wrong target pose, (2) Incomplete texture map, (3) Squeezed texture map, (4) Missing face information, (5) Significant view changes.]({{ '/images/03-2025/Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis/figure_6.jpg' | relative_url }})
