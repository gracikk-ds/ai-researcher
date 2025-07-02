---
title: One-Step_is_Enough:_Sparse_Autoencoders_for_Text-to-Image_Diffusion_Models
layout: default
date: 2024-10-28
---
## One-Step is Enough: Sparse Autoencoders for Text-to-Image Diffusion Models
**Authors:**
- Viacheslav Surkov, h-index: 2, papers: 2, citations: 17
- David Bau, h-index: 1, papers: 1, citations: 13

**ArXiv URL:** http://arxiv.org/abs/2410.22366v4

**Citation Count:** 13

**Published Date:** 2024-10-28

![Figure 1: Enabling features learned by sparse autoencoders results in interpretable changes in SDXL Turbo’s, SDXL’s, and Flux-schnell’s image generation processes. The image captions correspond to feature codes comprised of transformer block name and feature index.]({{ '/images/10-2024/One-Step_is_Enough:_Sparse_Autoencoders_for_Text-to-Image_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Modern text-to-image diffusion models, while powerful, operate as "black boxes," with their internal decision-making processes being poorly understood. While the field of mechanistic interpretability has made strides in explaining Large Language Models (LLMs), similar in-depth analyses for diffusion models have been lacking. The authors aim to bridge this gap by applying Sparse Autoencoders (SAEs)—a technique successful in LLMs—to decompose the complex, intermediate representations of diffusion models into a sparse set of human-interpretable features. The ultimate goal is to enable a deeper understanding, analysis, and control over the image generation process.

## 2. Key Ideas and Methodology
The core idea is to train SAEs on the internal activations of a text-to-image model to discover interpretable and causally effective features. The authors focus on SDXL Turbo, a fast, few-step diffusion model.

- **Methodology**: Instead of analyzing the entire residual stream, the authors train SAEs specifically on the *updates* (the output of a block minus its input) computed by key transformer blocks within SDXL Turbo's U-Net. They identify four high-impact blocks (`down.2.1`, `mid.0`, `up.0.0`, `up.0.1`) and train a separate SAE for each.
- **Experimental Design**: To support their analysis, the authors developed several tools:
    - **SDLens**: A library to cache and manipulate the intermediate activations of SDXL models.
    - **SAEPaint**: An interactive application for visualizing features and performing interventions (e.g., adding a "tiger texture" feature) during image generation.
    - **RIEBench**: A new quantitative benchmark for representation-based image editing. It uses prompts from PIEBench and segmentation masks from grounded SAM2 to measure how effectively transferring features between two image generations (e.g., changing a "pig" to a "bunny") can edit the final image.

The central hypothesis is that these learned SAE features will be monosemantic (represent a single concept), causally influence the output, and reveal functional specialization among the model's components.

## 3. Datasets Used / Presented
- **SAE Training Dataset**: The authors generated a large-scale dataset by processing 1.5 million prompts from the **LAION-COCO** dataset through the 1-step SDXL Turbo model. They used their SDLens library to cache the update vectors from the four selected transformer blocks, resulting in approximately 384 million training vectors per block.
- **RIEBench (Presented)**: The authors created this new benchmark for evaluating representation-based editing. It leverages prompts from **PIEBench** across nine editing categories (e.g., "change object," "change style") and uses **grounded SAM2** to generate segmentation masks for targeted feature extraction and intervention.

## 4. Main Results
- **Feature Interpretability and Causality**: The learned SAE features were found to be highly interpretable and causally effective. Activating a single feature during generation produces a predictable and localized change in the output image, such as adding a specific texture, object part, or style (e.g., Figure 1 shows adding cat ears, fire, or changing styles).
- **Generalization Across Models and Steps**: SAEs trained solely on 1-step SDXL Turbo generations successfully generalize to the 4-step version, the full multi-step SDXL Base model, and even a different architecture (Flux-schnell) without any additional training.
- **Block Specialization**: The analysis revealed clear functional specialization among the transformer blocks: `down.2.1` controls high-level composition and layout, `up.0.0` adds fine-grained details, and `up.0.1` manages color, texture, and style.
- **Quantitative Performance**: On the RIEBench benchmark, SAE-based feature interventions consistently outperformed neuron-level interventions and activation steering baselines. SAEs achieved higher CLIP similarity to the target edit for a given perceptual distance (LPIPS) from the original image, demonstrating more precise and effective control.

## 5. Ablation Studies
- **Identifying Influential Blocks**: The authors performed a qualitative ablation by zeroing out the updates from each of the 11 cross-attention transformer blocks in SDXL Turbo. This experiment showed that most blocks had a minor impact, while four (`down.2.1`, `mid.0`, `up.0.0`, `up.0.1`) had a significant and distinct effect on the final image, justifying the decision to focus SAE training on them.
- **SAE Hyperparameters**: The paper includes a study on the effect of the expansion factor (`nf`) and sparsity level (`k`). Results in Figure 2 show that explained variance increases with both parameters, confirming that a larger dictionary and allowing more active features improve the SAE's ability to reconstruct the original activations.
- **Intervention Timesteps**: The authors experimented with applying interventions across different intervals of the multi-step denoising process. They found that intervening from the beginning of the process causes large perturbations, while later interventions have a more subtle effect. This also revealed that features from different blocks have different effective time windows (e.g., `up.0.1` "style" features are most effective later in generation).

## 6. Paper Figures
![Figure 4: We perform a feature transfer experiment , computing semantic image segmentation masks using grounded SAM2 [ 48 ] for a source and a target image. We collect features inside the mask of the source image at SDXL Turbo’s intermediate layers and insert them during the target forward pass. The resulting image is a blend of the two forward passes.]({{ '/images/10-2024/One-Step_is_Enough:_Sparse_Autoencoders_for_Text-to-Image_Diffusion_Models/figure_4.jpg' | relative_url }})
