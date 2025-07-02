---
title: Generalized_Consistency_Trajectory_Models_for_Image_Manipulation
layout: default
date: 2024-03-19
---
## Generalized Consistency Trajectory Models for Image Manipulation
**Authors:**
- Beomsu Kim, h-index: 11, papers: 21, citations: 893
- Jong Chul Ye, h-index: 8, papers: 16, citations: 264

**ArXiv URL:** http://arxiv.org/abs/2403.12510v3

**Citation Count:** 4

**Published Date:** 2024-03-19

![Figure 1: An illustration of GCTM and its applications – solid arrows can be implemented by a single forward pass of the GCTM network. GCTMs learn to traverse the Flow Matching ODE which is capable of interpolating two arbitrary distributions q ( x 0 ) and q ( x 1 ) . GCTMs allow (a) one-step inference of ODE velocity, (b) one-step traversal between arbitrary time intervals of the ODE, (c) improved gradient-guidance by using exact posterior sample instead of posterior mean, and (d) one-step generation of varying outputs x 0 given a fixed input x 1 .]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Diffusion models are powerful for image generation and manipulation but are computationally expensive due to their iterative sampling process. Consistency Trajectory Models (CTMs) accelerate this by enabling one-step generation; however, they are fundamentally limited to translating Gaussian noise to data. This restricts their direct application in versatile tasks like image-to-image translation or restoration, which require mapping between two complex, non-Gaussian data distributions. The authors address this gap by proposing a generalized framework that extends CTMs to operate between arbitrary distributions.

## 2. Key Ideas and Methodology
The paper introduces Generalized Consistency Trajectory Models (GCTMs), which learn to translate between any two distributions, q(x₀) and q(x₁), in a single function evaluation. The core idea is to leverage the theory of Conditional Flow Matching (FM) to define an Ordinary Differential Equation (ODE) between two arbitrary distributions, generalizing the Probability Flow ODE used in standard diffusion. The authors prove that standard CTMs are a special case of GCTMs. A key aspect of the methodology is the flexible design of the joint distribution "coupling" `q(x₀, x₁)` which encodes the relationship between source and target data. The paper explores three main couplings:
- **Independent coupling:** For unconditional generation from noise.
- **Optimal Transport (OT) coupling:** To accelerate unconditional generation by finding straighter, more efficient ODE paths.
- **Supervised coupling:** For paired tasks like image-to-image translation and restoration.

## 3. Datasets Used / Presented
- **CIFAR10:** Used for unconditional image generation experiments.
- **Pix2Pix datasets (Edges→Shoes, Night→Day, Facades):** Used to evaluate supervised image-to-image translation performance.
- **FFHQ (64x64 & 256x256):** Used for various image restoration tasks (super-resolution, deblurring, inpainting) in both zero-shot and supervised settings.
- **ImageNet (256x256):** Used to demonstrate the scalability of GCTM for high-resolution image restoration.

## 4. Main Results
GCTMs demonstrate strong performance and efficiency, often with just a single function evaluation (NFE=1).
- **Unconditional Generation:** On CIFAR10, GCTM with OT coupling achieves a competitive FID of 5.32, outperforming other teacher-less models and matching teacher-based CTMs.
- **Image-to-Image Translation:** On the Edges→Shoes task, GCTM (FID 40.3) significantly outperforms baselines like Pix2Pix (FID 77.0) and SDE-based methods like Palette (FID 334.1 at NFE=5), while producing images with higher fidelity (lower LPIPS).
- **Image Restoration:** In zero-shot restoration on FFHQ, GCTM outperforms prior methods like DPS and CM. In supervised settings, it achieves a superior balance between perceptual quality (LPIPS) and distortion metrics (PSNR/SSIM) compared to baselines.

## 5. Ablation Studies
The authors performed several ablation studies to validate the design choices of GCTM:
- **Coupling:** For unconditional generation, using Optimal Transport (OT) coupling instead of independent coupling was shown to accelerate training convergence by up to 2.5 times and improve final image quality (FID of 18.2 vs. 24.7).
- **Gaussian Perturbation:** For image-to-image tasks, adding small Gaussian noise to the source image is crucial. Training without it was unstable (FID > 30), whereas adding it enabled stable training and superior performance by facilitating one-to-many mappings.
- **Time Discretization (`σ_max`):** For image-to-image translation, using a larger `σ_max` (e.g., 500 vs. 80), which places more discretization steps near the source distribution (t=1), leads to faster convergence and a lower final FID.

## 6. Paper Figures
![Figure 2: CIFAR10 unconditional samples with NFE = 1.]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_2.jpg' | relative_url }})
![Figure 3: Training acceleration.]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_3.jpg' | relative_url }})
![Figure 4: Qualitative evaluation of image-to-image translation on Edges → Shoes (top), Night → Day (middle) and Facades (bottom). NFE = 5 for I 2 SB and Palette.]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_4.jpg' | relative_url }})
![Figure 5: Reg. vs. GCTM.]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_5.jpg' | relative_url }})
![Figure 6: Image editing with GCTM, NFE = 1.]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_6.jpg' | relative_url }})
![Figure 7: Latent manipulation with image-to-image GCTM, NFE = 1.]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_7.jpg' | relative_url }})
![Figure 8: Ablation study of GCTM.]({{ '/images/03-2024/Generalized_Consistency_Trajectory_Models_for_Image_Manipulation/figure_8.jpg' | relative_url }})
