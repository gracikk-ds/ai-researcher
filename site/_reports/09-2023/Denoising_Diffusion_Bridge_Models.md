---
title: Denoising_Diffusion_Bridge_Models
layout: default
date: 2023-09-29
---
## Denoising Diffusion Bridge Models
**Authors:**
- Linqi Zhou, h-index: 5, papers: 7, citations: 457
- Stefano Ermon, h-index: 82, papers: 354, citations: 58193

**ArXiv URL:** http://arxiv.org/abs/2309.16948v3

**Citation Count:** 81

**Published Date:** 2023-09-29

![Figure 1: A schematic for Denoising Diffusion Bridge Models. DDBM uses a diffusion process guided by a drift adjustment (in blue) towards an endpoint x T = y . They lears to reverse such a bridge process by matching the denoising bridge score (in orange), which allows one to reverse from x T to x 0 for any x T = y ∼ q data ( y ) . The forward SDE process shown on the top is unidirectional while the probability flow ODE shown at the bottom is deterministic and bidirectional. White nodes are stochastic while grey nodes are deterministic.]({{ '/images/09-2023/Denoising_Diffusion_Bridge_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Standard diffusion models are designed to map data to random noise, which makes them ill-suited for tasks like image-to-image translation where the input is another structured data distribution, not noise. Current methods to adapt diffusion models for such tasks are often cumbersome (e.g., conditioning, projected sampling) and not theoretically principled. The authors aim to address this gap by creating a unified and scalable framework that naturally models the transport between two arbitrary distributions, while still leveraging the powerful design principles that have made standard diffusion models successful.

## 2. Key Ideas and Methodology
The paper introduces Denoising Diffusion Bridge Models (DDBMs), a framework based on *diffusion bridges*—stochastic processes that are conditioned to start and end at two specific distributions.

-   **Core Principle:** Instead of learning to reverse a data-to-noise process, DDBMs learn to reverse a bridge process that directly maps a source distribution to a target distribution. The key is to learn the conditional score of this bridge, `∇_xt log q(xt | xT)`, where `xt` is the intermediate state and `xT` is the target sample.
-   **Methodology:**
    -   A novel **Denoising Bridge Score Matching** objective is proposed, which makes learning the bridge score tractable and scalable, analogous to the standard denoising score matching loss.
    -   The framework is designed to be a strict generalization of standard diffusion models. This allows it to adapt and extend successful design choices from prior work, such as the network parameterization and preconditioning from EDM (Karras et al., 2022).
    -   A **hybrid sampler** is introduced that combines deterministic ODE steps with stochastic SDE steps. This injects noise during sampling to prevent the deterministic "averaged" or blurry outputs that can occur when reversing a bridge from a fixed starting point.
-   **Theoretical Foundation:** The model is built upon the theory of diffusion bridges and Doob's h-transform, which provides the mathematical basis for conditioning a diffusion process on a future endpoint.

## 3. Datasets Used / Presented
The model was evaluated on both image translation and unconditional generation tasks.

-   **Image-to-Image Translation (Pixel-space):**
    -   **Edges→Handbags:** 64x64 images, used for translating edge maps to colored images.
    -   **DIODE-Outdoor:** 256x256 images, used for translating surface normal maps to outdoor RGB scenes.
-   **Image-to-Image Translation (Latent-space):**
    -   **Day→Night:** 256x256 images, translated in a 32x32 latent space to test applicability with autoencoders.
-   **Unconditional Generation:**
    -   **CIFAR-10** and **FFHQ-64x64:** Used to verify that DDBM can reduce to a standard diffusion model and achieve comparable state-of-the-art performance.

## 4. Main Results
DDBM demonstrates significant improvements over existing methods in image-to-image translation, particularly in a low-step sampling regime.

-   On **Edges→Handbags**, DDBM (VP variant) achieved a FID score of **1.83**, substantially outperforming strong baselines like I2SB (7.43) and Rectified Flow (25.3).
-   On the higher-resolution **DIODE** dataset, DDBM (VP) achieved a FID of **4.43**, again surpassing I2SB (9.34) and SDEdit (31.14).
-   For **unconditional generation**, DDBM achieved FID scores of **2.06** on CIFAR-10 and **2.44** on FFHQ-64x64, matching the performance of the state-of-the-art EDM model (2.04 and 2.53, respectively).
-   The authors claim that DDBM is a general and powerful framework for distribution translation that achieves state-of-the-art results while unifying concepts from diffusion and transport models.

## 5. Ablation Studies
The authors performed several ablations to validate their design choices.

-   **Hybrid Sampler vs. ODE Sampler:** Introducing stochasticity via the hybrid sampler was critical for performance. On Edges→Handbags, using a pure ODE sampler resulted in blurry images, while the hybrid sampler produced sharper results and significantly improved the FID score.
-   **Guidance Scale (`w`):** The performance of VP (Variance Preserving) bridges was highly dependent on the guidance term (`w=1`), whereas VE (Variance Exploding) bridges were less sensitive. This suggests VP bridges rely more heavily on the Doob's h-transform to guide the path.
-   **Effect of Preconditioning and Sampler:** The contributions of the generalized preconditioning and the custom hybrid sampler were evaluated incrementally. On Edges→Handbags, a baseline model achieved a FID of 11.76. Adding the authors' proposed components progressively improved the FID to **1.83**, demonstrating that both contributions are essential for the model's success.

## 6. Paper Figures
![Figure 2: VE bridge (left) and VP bridge (right) with their SDE (top) and ODE (bottom) visualization.]({{ '/images/09-2023/Denoising_Diffusion_Bridge_Models/figure_2.jpg' | relative_url }})
![Figure 3: Qualitative comparison with the most relevant baselines.]({{ '/images/09-2023/Denoising_Diffusion_Bridge_Models/figure_3.jpg' | relative_url }})
![Figure 4: Ablation studies on Euler step ratio s and guidance scale w : w = 1 for all ablation on s and s is set to the best-performing value for each dataset for ablation on w .]({{ '/images/09-2023/Denoising_Diffusion_Bridge_Models/figure_4.jpg' | relative_url }})
![Figure 5: Generation on CIFAR-10 and FFHQ64 × 64 .]({{ '/images/09-2023/Denoising_Diffusion_Bridge_Models/figure_5.jpg' | relative_url }})
