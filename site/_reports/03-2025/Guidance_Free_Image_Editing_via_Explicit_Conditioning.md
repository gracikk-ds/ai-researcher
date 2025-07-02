---
title: Guidance_Free_Image_Editing_via_Explicit_Conditioning
layout: default
date: 2025-03-22
---
## Guidance Free Image Editing via Explicit Conditioning
**Authors:**
- Mehdi Noroozi, h-index: 1, papers: 3, citations: 1
- Sourav Bhattacharya, h-index: 3, papers: 14, citations: 25

**ArXiv URL:** http://arxiv.org/abs/2503.17593v1

**Citation Count:** None

**Published Date:** 2025-03-22

![Figure 1. Image editing performance for the context image in (a) with the instruction prompt: ”Make her a bride”. CFG (Eq. 10 ) are shown with × 1 pass ( s I = 1 . 0 , s P = 1 . 0 ) in (d), × 2 passes ( s I = 1 . 0 , s P = 7 . 5 ) in (e), and × 3 passes ( s I = 1 . 6 , s P = 7 . 5 ) in (f). Our proposed explicit conditioning result with a single pass is shown in (c).]({{ '/images/03-2025/Guidance_Free_Image_Editing_via_Explicit_Conditioning/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the significant computational cost associated with current state-of-the-art conditional diffusion models. These models heavily rely on Classifier-Free Guidance (CFG), a technique that improves image quality and adherence to conditions (like text prompts) but requires multiple denoising passes per time step—up to three for image editing tasks. This multi-pass requirement makes the image generation process slow and computationally expensive. The paper aims to create a new conditioning mechanism that eliminates the need for CFG, thereby reducing inference time and computational overhead without sacrificing output quality.

## 2. Key Ideas and Methodology
The core idea is **Explicit Conditioning (EC)**, a novel method that embeds conditioning information directly into the diffusion process itself, making guidance unnecessary.

-   **Core Principle:** Instead of diffusing an image into a standard noise distribution (e.g., a simple Gaussian) and feeding the condition as an auxiliary input to the model, EC diffuses the image into a *purposefully designed* target distribution. This target distribution is a Gaussian whose mean and variance are functions of the conditioning information (e.g., a context image and a text prompt).
-   **Methodology:** The framework is built on Stable Diffusion. For image editing, the condition consists of a context image (`c_I`) and an instruction prompt (`c_P`).
    1.  The context image's latent mean and variance are obtained using the pre-trained Stable Diffusion VAE encoder.
    2.  A small, custom-trained "prompt VAE" maps the text prompt's CLIP embeddings to a corresponding mean and variance in the same latent space.
    3.  These two sets of means and variances are combined to define a new target Gaussian distribution.
    4.  The diffusion process then learns to reverse the path from this condition-infused Gaussian back to the edited image, requiring only a single denoising pass during inference.
-   **Theoretical Foundation:** The authors argue that by making the conditioning information part of the endpoint distribution, the denoising score function becomes inherently conditional. This obviates the need to approximate a joint score by combining separate conditional and unconditional models, which is the basis of CFG.

## 3. Datasets Used / Presented
-   **Instruct-pix2pix:** This dataset was used for both fine-tuning the model for instruction-based image editing and for evaluation. The paper reports results on the full test set of this dataset.

## 4. Main Results
The paper demonstrates that Explicit Conditioning (EC) outperforms the standard CFG-based approach in both quality and efficiency for instruction-based image editing.

-   **Quantitative Insights:** Using Directional CLIP Similarity (DCS) and the authors' proposed Directional Visual Similarity (DVS) metrics (higher is better), the single-pass EC method surpasses the computationally expensive three-pass CFG method.
    -   **EC (1 pass):** Achieved a DCS of 0.191 and a DVS of 0.576.
    -   **CFG (3 passes):** Achieved a DCS of 0.177 and a DVS of 0.448.
    -   **CFG (1 pass):** Scored significantly lower with a DCS of 0.114 and a DVS of 0.390.
-   **Author-claimed Impact:** The proposed EC method generates higher-quality and more diverse images than CFG-based methods while being three times faster, as it requires only a single denoising pass.

## 5. Ablation Studies
The authors performed an ablation study to assess the impact of providing the full 77 CLIP tokens from the text prompt as an additional input to the UNet's cross-attention mechanism, alongside the main EC mechanism.

-   **Experiment:** They compared their EC model's performance with and without these extra CLIP tokens.
-   **Results:**
    -   **With extra tokens:** DCS score was 0.191.
    -   **Without extra tokens:** DCS score was 0.178.
-   The study showed that including the extra tokens provides a performance boost in the DCS metric and leads to faster training convergence, likely due to better consistency with the pre-trained text-to-image model's architecture. The effect on the DVS metric was negligible.

## 6. Paper Figures
![Figure 2. Explicit conditioning training: We obtain the mean and variance encoder of the context image via the SD encoder, shown in blue. For the instruction prompt, we use our prompt VAE encoder, shown in yellow, that has the same latent dimension as the SD, i.e., 4 × 64 × 64 . It takes the pooled CLIP embeddings, shown in red, as input and maps them to the corresponding mean and variance. The context and prompt mean and variances are fused to form a Gaussian used for sampling in the diffusion process, as in Eq. 14 . We keep the full 77 CLIP embeddings, shown in purple, as input to the UNet for the sake of consistency with the internalization.]({{ '/images/03-2025/Guidance_Free_Image_Editing_via_Explicit_Conditioning/figure_2.jpg' | relative_url }})
![Figure 3. Inference: We call the denoising model recursively starting from a point sampled from a Gaussian that its mean and variance is a fusion of context image and instruction prompt.]({{ '/images/03-2025/Guidance_Free_Image_Editing_via_Explicit_Conditioning/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative evaluations, failure cases. (a) input context image, (b) CFG × 3 passes, i.e. s I = 1 . 6 , s P = 7 . 5 . (c) our proposed × 1 pass explicit conditioning.]({{ '/images/03-2025/Guidance_Free_Image_Editing_via_Explicit_Conditioning/figure_4.jpg' | relative_url }})
![Figure 5. Qualitative evaluations. (a) input context image, (b) CFG × 1 pass, i.e. s I = 1 . 0 , s P = 1 . 0 (c) CFG × 3 passes, i.e. s I = 1 . 6 , s P = 7 . 5 . (d) our proposed × 1 pass explicit conditioning. Our method outperforms CFG while being × 3 faster.]({{ '/images/03-2025/Guidance_Free_Image_Editing_via_Explicit_Conditioning/figure_5.jpg' | relative_url }})
