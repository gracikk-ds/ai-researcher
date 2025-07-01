---
title: Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation
layout: default
date: 2023-07-17
---
![Figure 1. Editability and fidelity trade-off of diffusion-based image manipulation. The leftmost is the input image. For each manipulation, we add increasing noise levels from left to right and then denoise the image. Different semantics require different levels of noise to manipulate.]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
    - The authors address the "editability-fidelity trade-off" inherent in standard diffusion-based image manipulation. Existing methods that add noise to an image and then denoise it with a text prompt face a dilemma: adding too much noise harms the image's fidelity (preserving original content), while adding too little noise limits the model's ability to make significant edits. This trade-off restricts the practical application of diffusion models for high-quality, controllable image manipulation.

## 2. Key Ideas and Methodology
    - The core idea is to avoid direct iterative editing with a diffusion model and instead use it as a powerful "supervisor" to train a separate, efficient, feedforward image manipulator. This framework is named Selective Diffusion Distillation (SDD).
    - The methodology involves two main stages:
        1.  **Selection:** For a given text prompt, the method first identifies the most semantically relevant diffusion timesteps. It introduces a novel metric, the Hybrid Quality Score (HQS), which is calculated from the entropy and L1 norm of the diffusion model's gradient. HQS effectively pinpoints the timesteps that provide the most useful guidance for a specific edit.
        2.  **Distillation:** A lightweight image manipulator (e.g., a StyleGAN-based network) is trained. The manipulator's output is fed into the pre-trained diffusion model at the selected timesteps. The diffusion model then provides a loss signal (gradient) that guides the manipulator to produce images that align with the target text prompt while maintaining high fidelity.
    - The key assumption is that a pre-trained diffusion model's knowledge can be effectively distilled into a more efficient network, and that different semantic edits are best guided by different, identifiable stages of the diffusion process.

## 3. Datasets Used / Presented
    - The method was evaluated on several standard datasets to demonstrate its versatility across different domains:
    - **CelebA-HQ:** Used for human face manipulation tasks like changing expressions, hairstyles, and converting to celebrity likenesses.
    - **AFHQ-cat:** Used for manipulating images of cat faces, such as changing breed or color.
    - **LSUN-car:** Used for car image manipulation, including changing color, style (e.g., "classic", "SUV"), and make.

## 4. Main Results
    - Compared to diffusion-based baselines (SDEdit, DDIB, DiffAE), SDD achieves superior performance by successfully decoupling editability and fidelity.
    - Quantitatively, SDD obtains the best scores in both fidelity and semantic alignment, achieving a Fréchet Inception Distance (FID) of **6.066** (lower is better) and a directional CLIP similarity of **0.2337** (higher is better). This significantly outperforms the best fine-tuned baseline (FID of 16.761).
    - The authors claim that SDD successfully avoids the trade-off problem, enabling fast, high-quality, and semantically accurate image manipulation with a single forward pass at inference time.

## 5. Ablation Studies
    - The authors performed an ablation study on their proposed HQS-based timestep selection strategy to validate its effectiveness. Four strategies were compared for training the manipulator:
    1.  **Random:** Sampling timesteps randomly from the entire range. This resulted in minimal changes to the input image and poor editing quality.
    2.  **Small Threshold HQS:** Using a low HQS threshold, which includes many timesteps. This showed slight improvement over random.
    3.  **Large Threshold HQS:** Using a high HQS threshold, selecting fewer, more relevant timesteps. This led to a noticeable improvement in manipulation accuracy.
    4.  **Largest HQS:** Using only the timestep(s) with the highest HQS score. This strategy produced the most accurate and visually compelling semantic manipulations, confirming that HQS effectively identifies the most critical timesteps for guidance. The CLIP similarity score improved from **0.2146** (Random) to **0.2190** (Largest HQS).

## 6. Paper Figures
![Figure 2. Core concept of SDD. Our method involves two steps: 1) selecting the semantically-related timestep and 2) distilling the appropriate semantic knowledge into an image manipulator, f ϕ .]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_2.jpg' | relative_url }})
![Figure 3. General framework of Selective Diffusion Distillation (SDD) . Top: selection stage . We build an HQS indicator to select appropriate timesteps. Bottom: distillation stage . We use the selected timesteps and the pretrain diffusion model p θ to train the image manipulator f ϕ .]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_3.jpg' | relative_url }})
![Figure 4. Effect of our Hybrid Quality Score (HQS) . Left : The curve of HQS at different timesteps when the prompt is “angry”. Right : Gradient visualization of the corresponding timestep and editing results of training our image manipulator using only this timestep.]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_4.jpg' | relative_url }})
![Figure 5. The manipulation results of SDD of various domains (CelebA-HQ [ 23 ], AFHQ-cat [ 8 ], LSUN-car [ 47 ]) and various attributes. We keep the image fidelity and make it coherent with the text.]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_5.jpg' | relative_url }})
![Figure 6. The visual comparison between SDD and diffusionbased image manipulations. α ranges from zero to one and represents the noise level. SDEdit and DDIB fail to manipulate the semantics at a noise level of 0.7, while SDD successfully manipulates the semantics with less distortion.]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_6.jpg' | relative_url }})
![Figure 7. Comparison of SDD and StyleCLIP in pose manipulation . Text prompt: “side view”. The results demonstrate that the diffusion model provides superior semantic guidance, enabling a broader range of manipulations.]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_7.jpg' | relative_url }})
![Figure 8. Visual result of Ablation Study . The average HQS score of timesteps used for training increases from left to right and so does the accuracy of manipulation.]({{ '/images/07-2023/Not_All_Steps_are_Created_Equal:_Selective_Diffusion_Distillation_for_Image_Manipulation/figure_8.jpg' | relative_url }})
