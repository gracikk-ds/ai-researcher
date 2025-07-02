---
title: REED-VAE:_RE-Encode_Decode_Training_for_Iterative_Image_Editing_with_Diffusion_Models
layout: default
date: 2025-04-26
---
## REED-VAE: RE-Encode Decode Training for Iterative Image Editing with Diffusion Models
**Authors:**
- Gal Almogpapers: 1, 
- Ohad Friedpapers: 1, 

**ArXiv URL:** http://arxiv.org/abs/2504.18989v1

**Citation Count:** None

**Published Date:** 2025-04-26

![Figure 1: REED-VAE (top) preserves image quality over multiple editing iterations, allowing users to perform multiple edit operations using a combination of frameworks and techniques. The Vanilla VAE (bottom) accumulates many artifacts and noise along the way, becoming very apparent once multiple iterative edit operations are performed. The total edit sequence consists of 14 steps, of which only the last 4 are shown here for brevity and to highlight the differences in the final picture. Four types of edit operations are performed: text-guided editing [ BHE23 ], external editing (not diffusion-based), mask-guided editing [ AFL23 ], and example-guided editing [ YGZ ∗ 23 ].]({{ '/images/04-2025/REED-VAE:_RE-Encode_Decode_Training_for_Iterative_Image_Editing_with_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a practical limitation in modern generative AI: the inability to perform multiple, sequential edits on an image using a mix of different tools. While latent diffusion models excel at single edits, applying them iteratively causes significant image degradation. This is because switching between diffusion-based methods (which operate in a latent space) and traditional pixel-based editing tools requires repeated conversions through a Variational Autoencoder (VAE). Each conversion cycle is lossy, accumulating noise and artifacts that quickly destroy image quality, restricting creative workflows.

## 2. Key Ideas and Methodology
The paper introduces a novel training scheme called **RE-Encode Decode (REED)** to make VAEs robust to iterative use. The core principle is to train the VAE's decoder specifically for the task of repeated reconstruction.

The methodology consists of three main components:
1.  **Iterative Training:** Instead of training on a single encode-decode pass, the model is trained to reconstruct an image after it has undergone `k` sequential encode-decode cycles.
2.  **Dynamic Incrementation:** The training process uses a curriculum learning approach where the number of iterations, `k`, is gradually increased (from 4 up to 20) as the training progresses and the model's performance on the simpler task plateaus.
3.  **First-Step Loss:** The training objective is modified to compute the loss between the output of the *first* iteration and the output of the *k-th* iteration. This forces the model to focus on minimizing the degradation introduced at each step, rather than simply reconstructing the original image from scratch.

To ensure compatibility with existing diffusion models, the authors only fine-tune the VAE's decoder, keeping the original encoder weights frozen.

## 3. Datasets Used / Presented
*   **Training Dataset:** The REED-VAE was fine-tuned on a subset of the **LAION-5B** dataset, which is the same large-scale image-text dataset used to train the original Stable Diffusion model.
*   **Evaluation Dataset:** Experiments were conducted on the **ImagenHub** dataset, a benchmark for evaluating image generation and editing models. As no standard benchmark for iterative editing exists, the authors adapted the dataset by creating pairs of "inverse edit operations" (e.g., "add a hat" and "remove the hat") to cycle through for quantitative evaluation.

## 4. Main Results
The primary result is that REED-VAE successfully preserves image quality and editability over many iterations, whereas the standard VAE leads to severe artifact accumulation.
*   **Quantitative Improvement:** When integrated into various state-of-the-art editing frameworks (like InstructPix2Pix, MagicBrush, and Paint by Example), REED-VAE consistently improved all quality metrics (MSE, LPIPS, SSIM, FID, PSNR) at 5, 15, and 25 edit iterations. For example, with MagicBrush at 25 iterations, the perceptual LPIPS score improved from 0.80 to 0.69, and the FID score improved from 295.8 to 223.8.
*   **Qualitative Improvement:** Visual examples clearly show that after a sequence of edits, images processed with REED-VAE remain sharp and coherent, while those processed with the standard VAE are noisy and distorted.
*   The authors claim that REED-VAE enables practical, multi-method iterative image editing, serving as a benchmark for this new task.

## 5. Ablation Studies
The authors performed a detailed ablation study to validate the contribution of each component of the REED training scheme on a pure iterative encode-decode task.

*   **Iterative Training (IT):** Introducing iterative training with a fixed number of steps (`k=5`) significantly improved performance over the baseline Vanilla-VAE.
*   **First-Step Loss (FSL):** Adding the FSL to the iterative training further improved results by making the iterative learning task easier for the model.
*   **Dynamic Incrementation (DI):** The full model, combining IT, FSL, and DI, achieved the best performance. This component was crucial for enabling the model to generalize to a high number of iterations. At 25 iterations, the full REED-VAE model reduced the LPIPS error from 0.70 (baseline) to 0.28 and the FID score from 137.0 to 7.8, demonstrating a dramatic reduction in quality degradation.

## 6. Paper Figures
![Figure 2: Even without a diffusion model in the pipeline, the Vanilla-VAE (top row) accumulates artifacts and exhibits significant distortion very quickly throughout encode-decode iterations. The tiger’s features lose their distinct shapes and edges, appearing more globular and less defined. The color palette is altered, with a noticeable increase in blue tones and a decrease in the richness of the orange and greens. Fine details such as the grass and the fur are largely lost or blurred. REED-VAE (bottom row), produces successive images that are robust to such artifacts and distortions. The tiger retains its shape, color, and surface details, demonstrating remarkably high fidelity to the original image. The subtle variations in orange and white hues are preserved, and fine elements remain visible.]({{ '/images/04-2025/REED-VAE:_RE-Encode_Decode_Training_for_Iterative_Image_Editing_with_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3: Given an input image (a) we perform 20 encode-decode iterations and present the the results in image (top) and frequency domain (bottom). Vanilla-VAE (b) exhibits significant loss of highfrequency information (evidenced by the dimming and blurring of the outer regions of the spectrum), and dominance of low-frequency features (evidenced by the enlarged central bright region). In addition, it also introduced new high-frequency features that are not seen in the input image, indicating an introduction of repetitive artifacts. Trying to apply smoothing after each encode-decode iteration (c) solves some of these problems at the cost of blurring the image. REED-VAE (d) demonstrates superior performance in preserving image fidelity across all frequency bands.]({{ '/images/04-2025/REED-VAE:_RE-Encode_Decode_Training_for_Iterative_Image_Editing_with_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4: Examples of types of edit sessions made possible with REED-VAE. Using the Vanilla-VAE (right), significant noise and artifacts accumulate quickly after multiple edit operations. Intermediate edit operations are omitted to highlight the final edited image. Four types of edit operations are performed: text-guided editing [ BHE23 ], external editing (not diffusion-based), mask-guided editing [ AFL23 ], and example-guided editing [ YGZ ∗ 23 ].]({{ '/images/04-2025/REED-VAE:_RE-Encode_Decode_Training_for_Iterative_Image_Editing_with_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5: Row 1: Null-Text Inversion (NTI) is used to iteratively invert the image and regenerate it from the inverted latent. Row 2: the VanillaVAE is used to iteratively encode and decode the image. Row 3: NTI is used with REED-VAE to iteratively invert the image and regenerate it from the inverted latent. Vanilla NTI loses fidelity to the original image and is not resilient to iterative degradation. Full sequences for Vanilla NTI and NTI + REED are available in the Supplementary Material.]({{ '/images/04-2025/REED-VAE:_RE-Encode_Decode_Training_for_Iterative_Image_Editing_with_Diffusion_Models/figure_5.jpg' | relative_url }})
