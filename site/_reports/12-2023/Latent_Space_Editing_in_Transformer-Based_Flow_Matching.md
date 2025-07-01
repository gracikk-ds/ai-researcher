---
title: Latent_Space_Editing_in_Transformer-Based_Flow_Matching
layout: default
date: 2023-12-17
---
![Figure 1: Latent Flow Matching for image editing. Starting from the original image, we extract the latent feature x from the frozen encoder. Then, Flow Matching is applied in latent space to transfer the trajectory between the latent feature and standard Gaussian noise by integration on the vector field. An editing operation can be triggered in u -space and Prompt by your own desire. The edited feature will be fed back to the decoder to generate the final edited image.]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the problem of image editing in the context of two recent and powerful advances in generative modeling: Flow Matching (FM) and transformer-based backbones (U-ViT). While these technologies offer improved training efficiency and scalability over traditional diffusion models with UNets, the structure of their latent spaces and their potential for controlled image manipulation were previously unexplored. The paper aims to fill this gap by developing methods for semantic image editing that are specifically tailored to the unique architecture of transformer-based Flow Matching models.

## 2. Key Ideas and Methodology
The core idea is to identify and manipulate a semantic latent space within a transformer-based Flow Matching framework to enable intuitive image editing.

- **Model and Architecture**: The methodology is built upon a generative model that uses a standard VAE to encode images into a latent space, where a transformer-based U-ViT is trained using the efficient Flow Matching objective.
- **Discovery of "u-space"**: The authors discovered that the most effective space for semantic manipulation is not in the model's bottleneck (as in UNets) but at the very beginning of the U-ViT architecture, before the image patches are processed by attention blocks. They term this the "u-space".
- **Semantic Direction Editing**: To perform edits, semantic directions (e.g., for "age" or "smile") are first learned in a supervised manner by contrasting the u-space representations of images with and without the desired attribute. During image generation, these directions are added to the latent code to steer the output.
- **Adaptive ODE Solvers**: To overcome the limitation of previous methods that only work with fixed-step ODE solvers, the authors introduce a semantic direction interpolation technique. This allows them to use more efficient adaptive step-size solvers by interpolating between pre-calculated semantic directions at any arbitrary time step required by the solver.
- **Local Prompt Editing**: For text-based control, they propose a simple yet powerful method that directly scales the attention values between specific text prompt tokens and image patches. This allows for fine-grained local edits like adding, removing, or reweighting concepts without the overhead of complex attention map storage.

## 3. Datasets Used / Presented
- **CelebA-HQ (256x256)**: Used primarily for experiments involving semantic direction manipulation in u-space, such as altering facial attributes like gender, smile, and age.
- **MultiModal-CelebA-HQ (256x256)**: A dataset of faces with rich text captions, used for developing and testing the text-prompt-based editing methods.
- **MS COCO (256x256)**: A large-scale, diverse dataset of common objects and scenes, used to validate the generalizability of the proposed text-based editing techniques beyond the domain of human faces.

## 4. Main Results
- The paper successfully demonstrates that the identified "u-space" enables controllable, accumulative, and composable edits. Multiple attributes (e.g., "smile" + "young" + "male") can be sequentially applied to an image, with each edit building cleanly on the previous one.
- The proposed local prompt editing method is shown to be highly effective, outperforming the popular Prompt-to-Prompt method in preserving the unedited parts of an image (measured by lower LPIPS scores) while successfully applying the desired changes.
- The semantic direction interpolation method is validated, showing that efficient adaptive ODE solvers can be used for editing without a significant loss in quality compared to more computationally expensive fixed-step solvers.

## 5. Ablation Studies
- **Guidance Injection Timing**: The authors analyzed the effect of when the semantic guidance is applied during the sampling process. They found that injecting the guidance only in the early timesteps (e.g., the first 30-50 out of 100 steps) yielded the best results. Injecting for too few steps was ineffective, while injecting throughout the entire process degraded image quality and failed to preserve the original content.
- **Location of Editing Space**: An ablation on using intermediate layers of the U-ViT for editing was performed. It was found that these deeper feature spaces were too high-dimensional, leading to unstable results and justifying the choice of the "u-space" at the model's input stage.
- **PCA on u-space**: The authors attempted to find semantic directions in an unsupervised manner using PCA on the u-space. This failed to produce consistent semantic edits, confirming that their supervised, contrastive method for finding directions was necessary.

## 6. Paper Figures
![Figure 2: The location ablation of the guidance injection when editing male . Early time step injection is best, injection during full time step will lead to over-constraining. The first row is signal injection before the first 5, 10, 20, 30, 50, and 100 steps of the backward ODE process. The second row is guidance injection evenly throughout 100 steps.]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_2.jpg' | relative_url }})
![Figure 3: Compose multiple attributes sequentially. We gradually enforce three different semantic directions on a single reference image. The semantic direction of the three attributes is simply averaged by scale w = 2 .]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_3.jpg' | relative_url }})
![Figure 4: Relative error comparison between adaptive and euler ODE solvers with different time steps.]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_4.jpg' | relative_url }})
![Figure 5: Comparison of LPIPS scores with prompt-toprompt (Hertz et al. 2022) when changing the reweighting scale from 1 to 5.]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_5.jpg' | relative_url }})
![Figure 6: Appending new prompts sequentially . We can inject semantic meaning directly into the subject while keeping it almost unchanged. To do so, we start by sampling the first image based on the initial prompt. Then, we append the remaining prompts one by one.]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_6.jpg' | relative_url }})
![✍ ) hair, rosy cheeks, high cheekbones. Figure 7: Prompt reweighting, removing, replacing in MM-CelebA-HQ dataset . Our method can gradually scale the target prompt, remove the target prompt, and be robust to noise during prompt removal.]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_7.jpg' | relative_url }})
![Figure 8: Prompt reweighting on the real images of MS COCO dataset by weighting down (left) and weighting up (right).]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_8.jpg' | relative_url }})
![Figure 9: More sequential editing result by shuffling the order of the prompts. The same set of semantic manipulations can be composed in different orders.]({{ '/images/12-2023/Latent_Space_Editing_in_Transformer-Based_Flow_Matching/figure_9.jpg' | relative_url }})
