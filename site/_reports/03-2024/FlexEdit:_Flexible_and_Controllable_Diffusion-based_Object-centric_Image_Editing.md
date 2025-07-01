---
title: FlexEdit:_Flexible_and_Controllable_Diffusion-based_Object-centric_Image_Editing
layout: default
date: 2024-03-27
---
![Fig. 1: Our framework could achieve robust and flexible control over several text-guided object-centric editing scenarios, including a) replacing objects with controllable size and position , b) adding new objects in a natural way without additional mask input , and c) removing objects without compromising the quality of the original image.]({{ '/images/03-2024/FlexEdit:_Flexible_and_Controllable_Diffusion-based_Object-centric_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing diffusion-based image editing methods struggle with object-centric tasks. They offer limited control over the size and position of edited objects, often producing unrealistic results when the source and target objects have different shapes. Furthermore, these methods perform inconsistently in object addition and removal scenarios, failing to preserve background details or accurately execute the edit. FlexEdit aims to address these gaps by providing a flexible and controllable framework that excels at various object-centric editing tasks.

## 2. Key Ideas and Methodology
The authors introduce FlexEdit, a framework for flexible and controllable object editing built on Stable Diffusion. The core of the method is the **FlexEdit block**, which iteratively refines the noisy latent representation at each denoising step. This block consists of two main components:
1.  **Latent Optimization**: Adjusts the latent code using specific loss functions to enforce user-defined constraints. For object replacement, it controls size and position. For object addition, a separation loss prevents overlap with existing objects.
2.  **Latent Blending**: Preserves the background by blending the optimized latent with the original source latent. This is guided by an **adaptive binary mask**, which is dynamically generated from attention maps and combines both source and target object regions to ensure a seamless edit.

## 3. Datasets Used / Presented
The framework is evaluated on three object-centric editing benchmarks:
- **SynO**: A new synthetic dataset created by the authors, containing over 1600 samples for object replacement, addition, and removal.
- **MagicO**: A curated subset of the MagicBrush dataset with 254 real-image samples for object-centric tasks.
- **PieBenchO**: A curated subset of the PieBench dataset with 217 real-image samples focused on similar object-centric edits.
The authors also propose new evaluation metrics (CLIP-O, CLIP-NO) to specifically measure object editing success, alongside LPIPS to evaluate background preservation.

## 4. Main Results
FlexEdit demonstrates a superior trade-off between editing quality and background preservation compared to prior state-of-the-art methods. Quantitatively, across the SynO, MagicO, and PieBenchO datasets, it consistently achieves higher CLIP scores—indicating better semantic alignment with the text prompt—while maintaining low LPIPS scores, signifying minimal background distortion. Qualitatively, FlexEdit successfully handles challenging edits, such as replacing a "car" with a "turtle," where it generates the correct object shape and texture while preserving the original background, a task where other methods often fail.

## 5. Ablation Studies
The authors performed several ablation studies to validate their design choices:
- **Latent Blending Mask**: Removing the adaptive mask or using only the source/target mask resulted in significant content loss, artifacts, or incomplete edits. The full adaptive mask with dilation produced the best, most seamless results.
- **Loss Constraints**: Disabling the separation loss for object addition caused the new object to incorrectly merge with existing objects. Disabling the position and size control losses for object replacement led to random and uncontrolled edits, confirming the necessity of these constraints for controllable editing.
- **Inversion Method**: FlexEdit's performance was shown to be robust across different inversion techniques (DDIM, Direct, Null-text), consistently yielding high-quality results.

## 6. Paper Figures
![Fig. 2: We show an editing scenario when edited object monkey and source object bear are distinct in shape. Our FlexEdit could achieve flexible shape transformation editing while preserving high fidelity to the source image’s background information.]({{ '/images/03-2024/FlexEdit:_Flexible_and_Controllable_Diffusion-based_Object-centric_Image_Editing/figure_2.jpg' | relative_url }})
![Fig. 3: Overview of FlexEdit framework. Given an input image I , we first bring it to the intermediate source latents through an inversion process. Subsequently, the denoising process starts from z ∗ T cloned from z T after the inversion process and progresses toward z ∗ 0 , which is then decoded to get the edited image I ∗ . At each denoising step, our FlexEdit block manipulates the noisy latent code through two main submodules: latent optimization (shown in blue ), and latent blending (shown in orange ). This is to achieve editing semantics as well as to maintain high fidelity to the source image. If the iterative process (shown in green ) is not executed, our FlexEdit would return z ∗ t .]({{ '/images/03-2024/FlexEdit:_Flexible_and_Controllable_Diffusion-based_Object-centric_Image_Editing/figure_3.jpg' | relative_url }})
![Fig. 4: Visualization of different versions of cross-attention maps and dynamic binary masks for edited object, i.e. truck during the denoising diffusion process.]({{ '/images/03-2024/FlexEdit:_Flexible_and_Controllable_Diffusion-based_Object-centric_Image_Editing/figure_4.jpg' | relative_url }})
