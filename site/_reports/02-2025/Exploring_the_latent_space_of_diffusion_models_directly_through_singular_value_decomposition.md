---
title: Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition
layout: default
date: 2025-02-04
---
![Figure 1. Our framework overview for image editing. (1) During the denoising process, we select one time step T x for introducing new attributes. (2) Two latent codes x T x and z T x +∆ τ , guided by a pair of text prompts, is fed into our proposed AVI algorithm. (3) The AVI outputs a latent code y pred to replace x T x to continue the denoising process with the guidance of the original text prompt. Note that the SVD is performed channel-wise.]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The latent space of diffusion models, despite its potential for versatile image editing, remains largely under-explored. Current editing methods often rely on manipulating auxiliary spaces (like the U-Net's feature maps) or require computationally expensive fine-tuning and extra data collection. This paper addresses the gap by directly investigating the diffusion model's latent space (denoted as X) to enable more efficient, flexible, and interpretable image editing, akin to the well-understood latent space manipulation in GANs.

## 2. Key Ideas and Methodology
The core idea is that semantic attributes are encoded within the singular vectors and singular values of latent codes, which can be manipulated directly using Singular Value Decomposition (SVD). The authors identify three key properties of the latent space:
1.  **Small Neighbourhood:** Subspaces formed by singular vectors remain semantically stable across denoising timesteps.
2.  **Encoded Attributes:** Attributes are captured by the singular vectors and their corresponding singular values.
3.  **Mobility in Order:** The importance (rank) of singular vectors tied to specific attributes changes with the timestep; coarse attributes (e.g., pose) are high-rank in later steps, while fine-grained attributes (e.g., texture) are high-rank in earlier steps.

Based on these properties, the paper proposes an **Attribute Vector Integration (AVI)** framework. To learn an attribute (e.g., "young"), AVI takes two latent codes: a source code `x` from an original prompt ("a person") at a later timestep `Tx`, and a target code `z` from a target prompt ("a young person") at an earlier timestep `Tx + Δτ`. It then integrates the top singular vectors from both codes and uses a small MLP to predict new singular values `S` to create a final edited latent code. The process is guided by a composite loss function that balances attribute transfer with identity preservation.

## 3. Datasets Used / Presented
The study does not introduce new datasets but utilizes pre-trained diffusion models and generates images for analysis and experiments.
*   **Unconditional Models:** Models trained on **CelebA-HQ**, **LSUN-Cat**, and **LSUN-Church** were used for initial investigations into how attributes are encoded in the latent space across different timesteps.
*   **Conditional Model:** **Stable Diffusion (v2.1)** was the primary model used for the proposed image editing framework. All editing experiments and comparisons were conducted by generating images from pairs of text prompts to learn and apply specific attributes (e.g., gender, age, style).

## 4. Main Results
The proposed method demonstrates strong performance both qualitatively and quantitatively.
*   In a quantitative comparison with state-of-the-art methods on four attribute editing tasks (Female, Male, Old, Young), the proposed method achieved the highest CLIP scores across all tasks (e.g., 28.4 for "Female" vs. 26.6 for the next best), indicating superior alignment with the target text prompt. It also achieved competitive FID (image quality) and LPIPS (identity preservation) scores, often outperforming other methods.
*   The authors claim their work provides novel insights into the latent space of diffusion models and presents an effective, data-free framework for image editing that operates directly and efficiently on this space.

## 5. Ablation Studies
An ablation study was conducted to validate the contribution of each of the four loss terms (`L1`, `L2`, `L3`, `L4`) in the training objective.
*   **Without `L1` (target loss):** The model failed to introduce the desired attributes, as there was no guidance to move the latent toward the target.
*   **Without `L2` (source loss):** The generated images lost identity and became too similar to the target image, failing to preserve the original structure.
*   **Without `L3` (target singular value regularization):** The resulting images suffered from color saturation artifacts.
*   **Without `L4` (source singular value regularization):** The overall image quality was noticeably degraded.

## 6. Paper Figures
![Figure 2. Impact of singular values on their main singular vectors on Unconditional Diffusion Models (CelebA-HQ dataset on the left and LSUN-Cat and LSUN-Church datasets on the right). Fine-grained attributes, such as colours and texture appearances, are changing with respect to their singular values at earlier diffusion time steps.]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_2.jpg' | relative_url }})
![Figure 3. Representative examples shown on the attributes that one single singular vector affects across the time steps in Stable Diffusion Models (ver-2.1). Starting from the second column, the rows show the impact of singular values, and the columns present the attributes that different singular vectors may affect. Texts on the left side of images denote the attributes that a singular vector affects. It is noticeable that attribute vectors (e.g., belt details) ordered in lower places at later time steps (e.g, last row under 0.7 T ) ascended to higher places at earlier time steps (e.g, 0.6 T )]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_3.jpg' | relative_url }})
![Figure 4. Impact of singular values on their main singular vectors on Stable Diffusion Models (ver 2.1).]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_4.jpg' | relative_url }})
![Figure 5. Geodesic Distance across subspaces constructed by singular vectors of different datasets at various diffusion time steps. It is noticeable that the variance of stable diffusion is less than diffusion models trained on the CelebA-HQ dataset, thus we tend to consider the geodesic distance on subspaces to maintain semantically similar across all time steps.]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_5.jpg' | relative_url }})
![Figure 6. Examples of image edition on various learned attributes.]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_6.jpg' | relative_url }})
![Figure 7. Linear interpolation on learned attributes.]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_7.jpg' | relative_url }})
![Figure 8. Ablation study on proposed loss terms.]({{ '/images/02-2025/Exploring_the_latent_space_of_diffusion_models_directly_through_singular_value_decomposition/figure_8.jpg' | relative_url }})
