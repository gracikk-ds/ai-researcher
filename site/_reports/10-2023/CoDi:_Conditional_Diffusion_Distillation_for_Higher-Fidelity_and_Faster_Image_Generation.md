---
title: CoDi:_Conditional_Diffusion_Distillation_for_Higher-Fidelity_and_Faster_Image_Generation
layout: default
date: 2023-10-02
---
![Figure 1. Our proposed CoDi efficiently distills a conditional diffusion model from an unconditional one, enabling rapid generation of high-quality images under various conditional settings. We demonstrate CoDi’s capabilities through generated results across various tasks.]({{ '/images/10-2023/CoDi:_Conditional_Diffusion_Distillation_for_Higher-Fidelity_and_Faster_Image_Generation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the high computational cost and slow inference speed of large-scale diffusion models, which hinder their practical application in real-time conditional image generation tasks like super-resolution, image editing, and inpainting. Existing methods to accelerate these models, such as distillation, often struggle to efficiently and effectively incorporate new conditional inputs without compromising the rich prior knowledge learned during the initial large-scale pre-training. The paper aims to bridge this gap by creating a method that can both adapt a pre-trained model to new conditions and drastically reduce the required number of sampling steps in a single, unified process.

## 2. Key Ideas and Methodology
The core idea of the paper is **CoDi (Conditional Diffusion Distillation)**, a novel framework that distills a conditional diffusion model directly from a pre-trained unconditional one in a single stage. This avoids the suboptimal two-stage approaches of either finetuning then distilling, or distilling then finetuning.

The methodology involves two key components:
1.  **Model Adaptation:** The authors adapt a pre-trained Latent Diffusion Model (LDM) to accept new image-based conditions (e.g., a low-resolution image for super-resolution) by incorporating a ControlNet-like adapter. This adapter duplicates the encoder blocks of the U-Net and integrates their features, allowing for new conditional control without corrupting the original model's weights.
2.  **Conditional Consistency Loss:** A novel loss function is introduced to enforce consistency in the model's predictions across different diffusion timesteps. This loss has two parts: a noise self-consistency term that enables distillation (few-step generation), and a conditional guidance term in the signal space that ensures the output adheres to the provided condition (e.g., the ground-truth high-resolution image). This joint optimization allows the model to learn the new task while simultaneously learning to generate high-quality results in just 1-4 steps.

The paper also introduces a parameter-efficient version, **PE-CoDi**, where only the adapter's parameters are trained, making it highly efficient for adapting to multiple tasks.

## 3. Datasets Used / Presented
The method was evaluated on several standard conditional generation benchmarks:
*   **DF2K:** Used for the real-world super-resolution task. The authors evaluated their model on 3,000 randomly degraded image pairs generated using the Real-ESRGAN degradation pipeline.
*   **ImageNet:** Used for the inpainting task. The model was trained and tested on ImageNet images with random masks applied, evaluated at a 512x512 resolution.
*   **WebLI:** A large-scale web dataset used for the text-guided depth-to-image generation task.
*   **InstructPix2Pix Dataset:** Used to evaluate text-guided image editing, comparing CoDi's performance against the original InstructPix2Pix model.

The base model for all experiments was a Latent Diffusion Model pre-trained on an internal text-to-image dataset, noted as being comparable to StableDiffusion v1.4.

## 4. Main Results
CoDi demonstrates state-of-the-art performance in few-step conditional image generation, significantly outperforming previous distillation methods and often matching or exceeding the performance of full-step diffusion models.
*   **Super-resolution:** In 4 steps, CoDi achieves an FID of 19.637, which is comparable to the baseline LDM using 250 steps (FID 19.200) and significantly better than other 4-step distillation methods like GD-II (FID 23.675).
*   **Inpainting:** In 4 steps, CoDi achieves an FID of 14.700, outperforming the 50-step ControlNet baseline (FID 14.895).
*   **Image Editing:** Qualitatively, CoDi produces results in a single step that are visually comparable to the original InstructPix2Pix model running for 200 steps.

The author-claimed takeaway is that CoDi provides a new state-of-the-art approach for distilling conditional diffusion models, enabling high-fidelity and diverse image generation in very few steps (1-4) across a wide range of tasks.

## 5. Ablation Studies
The authors performed several ablation studies to validate their design choices, primarily on the super-resolution task.
*   **Impact of Pre-training:** Initializing the model with pre-trained weights from a text-to-image model significantly outperforms random initialization, confirming that CoDi effectively leverages the prior knowledge of the base model.
*   **Distillation Process:** The study showed that simply adding a ControlNet adapter yielded negligible improvement. The key performance gains came from the proposed conditional consistency distillation. Specifically, using the distillation model's own prediction to guide the process (distilling PF-ODE) and adding the noise-consistency loss were both critical for achieving the final high-quality results.
*   **Sampling Strategy:** Training with a single, consistent timestep `t` for all samples in a batch led to better performance in the target few-step (1-4) inference regime compared to training with mixed timesteps.
*   **Conditional Guidance (CG):** Removing the conditional guidance term from the loss function resulted in lower-quality, over-saturated images, even though it sometimes led to a better FID score. Including the guidance term was crucial for improving visual quality (LPIPS) and preventing the model from converging to a poor local minimum.

## 6. Paper Figures
![Figure 2. Sampled results between distilled models learned with alternative conditional guidance. Left curves shows the quantitative performance between the LPIPS and FID in { 1 , 2 , 4 , 8 } steps. Right part show the visual results where each result comes from the 1 sampling step (top) or 4 sampling steps (bottom). The distance function from the left to right is ∥ x − E ( D (ˆ x θ ( z t , c ))) ∥ 2 2 , ∥ D ( x ) − D (ˆ x θ ( z t , c )) ∥ 2 2 , F lpips ( D ( x ) , D (ˆ x θ ( z t , c )) , and our default ∥ x − ˆ x θ ( z t ) ∥ 2 2 , respectively.]({{ '/images/10-2023/CoDi:_Conditional_Diffusion_Distillation_for_Higher-Fidelity_and_Faster_Image_Generation/figure_2.jpg' | relative_url }})
![LR CM-II CoDi (Ours) HR Ground Truth Mask CM-II PF-CoDi (Ours) Figure 4. We show the results sampled in 4 steps by different models. Samples generated according to the low-resolution images (left) and masks (right) respectively. Please see our supplement for many more examples such as visual comparisons with the other methods.]({{ '/images/10-2023/CoDi:_Conditional_Diffusion_Distillation_for_Higher-Fidelity_and_Faster_Image_Generation/figure_4.jpg' | relative_url }})
![Figure 5. Samples generated according to the depth image (left) from ControlNet sampled in 4 steps (middle), and ours from the unconditional pretraining sampled in 4 steps (right). Please see our supplement for many more examples.]({{ '/images/10-2023/CoDi:_Conditional_Diffusion_Distillation_for_Higher-Fidelity_and_Faster_Image_Generation/figure_5.jpg' | relative_url }})
![Figure 6. Generated edited image according to the input image and the instruction (bottom) from Instructed Pix2Pix (IP2P) sampled in 200 steps and ours sampled in 1 step. Please see our supplement for many more examples.]({{ '/images/10-2023/CoDi:_Conditional_Diffusion_Distillation_for_Higher-Fidelity_and_Faster_Image_Generation/figure_6.jpg' | relative_url }})
