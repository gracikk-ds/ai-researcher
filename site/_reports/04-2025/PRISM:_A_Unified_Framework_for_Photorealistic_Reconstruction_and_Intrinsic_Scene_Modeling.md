---
title: PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling
layout: default
date: 2025-04-19
---
## PRISM: A Unified Framework for Photorealistic Reconstruction and Intrinsic Scene Modeling
**Authors:**
- Alara Dirik, h-index: 5, papers: 9, citations: 158
- Anna Frühstück, h-index: 6, papers: 8, citations: 154

**ArXiv URL:** http://arxiv.org/abs/2504.14219v2

**Citation Count:** None

**Published Date:** 2025-04-19

![Fig. 1. We propose PRISM, a unified framework for conditional generation of RGB image and its intrinsic channels (referred to as X layers) simultaneously. It supports a variety of tasks, including text-to-RGBX generation, RGB-to-X decomposition, and X-to-RGBX conditional generation. PRISM achieves plausible results on both local material editing on masked region and global image relighting through conditioning on selected intrinsic layers and text prompts.]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing generative models often treat intrinsic image decomposition (predicting properties like albedo, normals, depth) and conditional image generation as separate tasks, requiring different models. This can lead to inconsistencies between the generated image and its underlying physical properties. Furthermore, methods that adapt pre-trained models for perception tasks often sacrifice the original text-to-image generation capability. The authors address this gap by proposing a single, unified framework that can simultaneously perform photorealistic image generation, intrinsic decomposition, and conditional editing, ensuring consistency across all outputs while preserving the foundational model's generative power.

## 2. Key Ideas and Methodology
The core idea of the paper is PRISM, a unified framework that perceives and generates an image as a composition of its intrinsic components. PRISM is built by fine-tuning a pre-trained text-to-image diffusion transformer (DiT).

The key methodological contributions are:
-   **Joint RGBX Generation:** The model is trained to simultaneously generate an RGB image and its corresponding intrinsic maps (X layers: albedo, normals, depth, and irradiance). This is achieved by expanding the model's input token capacity to process all five modalities (RGB+X) at once, allowing their latent representations to be jointly refined through shared attention mechanisms.
-   **Unified Multi-Tasking:** Through a flexible conditioning strategy involving random masking of input modalities during training, a single PRISM model can perform diverse tasks without architectural changes:
    1.  **Text-to-RGBX:** Generating an image and all its intrinsic maps from only a text prompt.
    2.  **RGB-to-X:** Decomposing a given RGB image into its intrinsic maps.
    3.  **X-to-RGBX:** Generating an image by conditioning on a text prompt and any subset of intrinsic maps (e.g., for relighting or material editing).

## 3. Datasets Used / Presented
PRISM was trained on a combination of synthetic and real datasets to learn the relationship between images and their intrinsic properties:
-   **InteriorVerse:** A synthetic dataset of over 50,000 indoor scenes, providing ground truth for normals, depth, and albedo.
-   **HyperSim:** A photorealistic synthetic dataset of over 70,000 rendered images, providing normals, depth, albedo, and diffuse irradiance.
-   **Internal Commercial Dataset:** 50,000 high-quality real-world interior images (RGB only) to enhance realism.
-   Text captions for all images were generated using BLIP-2. The model was evaluated on the test sets of these datasets as well as standard benchmarks like NYU-v2, ETH3D, ImageNet, IIW, and MAW for various tasks.

## 4. Main Results
PRISM demonstrates competitive or state-of-the-art performance across its multiple functions:
-   **Intrinsic Decomposition:** On the HyperSim dataset, PRISM outperforms specialized methods, achieving a PSNR of 19.9 for normals and 18.5 for irradiance, compared to the 19.8 and 14.1 from the strong baseline Zeng et al. [2024].
-   **Conditional Generation:** When conditioned on normal maps for generation on ImageNet, PRISM achieves a Frechet Inception Distance (FID) of 5.3, significantly better than ControlNet (8.9) and T2I-Adapter (9.5).
-   **Zero-Shot Depth Estimation:** Despite being trained only on indoor scenes, PRISM achieves competitive depth estimation results on the NYU-v2 dataset with an Absolute Relative Error of 0.061.

The authors claim that PRISM is the first unified framework to successfully integrate intrinsic perception and conditional generation, showing that this joint approach improves alignment and consistency across modalities.

## 5. Ablation Studies
-   **Joint vs. Single-Modality Prediction:** The authors trained single-task variants of PRISM that only predict one intrinsic map (e.g., albedo). The full, multi-task PRISM model consistently outperformed these specialized variants (e.g., albedo PSNR of 19.3 for the full model vs. 18.4 for the single-task version), demonstrating the benefit of joint prediction.
-   **White Balance Alignment:** To test the alignment between albedo and irradiance, the authors measured the reconstruction error of the diffuse image component. The full PRISM model achieved a significantly lower reconstruction error (RMSE of 0.085) compared to a model using separately predicted channels (0.130), indicating that joint generation resolves the white balance ambiguity more effectively.
-   **Preservation of Generation Quality:** The text-to-image generation capability of PRISM was compared to its original base model. On an indoor scene dataset, PRISM achieved a slightly better FID score (14.98 vs. 19.01), confirming that the unified training strategy does not degrade the core generative quality.

## 6. Paper Figures
![Fig. 2. Pipeline of our PRISM model. RGB image and its corresponding X intrinsic channels are encoded into latent space via a fixed VAE Encoder. A Diffusion Transformer is applied on the tokens of the latent of all channels simultaneously and conditioned by the text embedding from an input text prompt. Denoised tokens are passing through a fixed decoder for RGB+X generation. During training, intrinsic channels are randomly ablated which makes PRISM a unified framework for text-to-image generation, intrinsic decomposition, and conditional image generation with any subset of intrinsic images.]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_2.jpg' | relative_url }})
![Fig. 3. Sample results generated with PRISM. Our model is capable of text, text+X and X conditioned generation and can inherently perform image decomposition and re-composition under different material, geometry and lighting conditions. Condition channels are highlighted in orange .]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_3.jpg' | relative_url }})
![Fig. 4. Visual comparison of our PRISM model against baseline methods on synthetic datasets. All input images and ground truths are from the HyperSim dataset, except for the classroom scene (b, right).]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_4.jpg' | relative_url }})
![Fig. 5. Visual comparison of RGB reconstruction from predicted albedo and irradiance for the white balance alignment. We compare PRISM model against Zeng et al. [ 2024 ] and ground truth reconstructions.]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_5.jpg' | relative_url }})
![Fig. 6. Relighting with text prompt. Starting from an input RGB image, intrinsic layers are predicted using PRISM. We then apply PRISM with a text prompt describing a new light condition together with all predicted intrinsic layers except irradiance map. Our relit results preserve the geometric and material properties of the original scenes while achieving plausible appearance under desired lighting conditions.]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_6.jpg' | relative_url }})
![Fig. 7. Material editing. PRISM allows text conditioned material editing for a masked region of the input image. While keeping the predicted depth and irradiance fixed, albedo and normal channels are only conditioned outside the mask to allow the changes in the selected region conditioned by text prompt. Our results preserve the identity outside the mask while updating the appearance inside the mask with consistent lighting.]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_7.jpg' | relative_url }})
![Fig. 8. Out of Domain Examples. Our fine-tune preserves the generalization of the base model. Here we show PRISM’s intrinsic decomposition on out-of-domain cases such as outdoor, portrait, landscape, and top-down photography.]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_8.jpg' | relative_url }})
![Fig. 9. Sample RGB, text+X, X+RGB conditioned results generated with PRISM on the InteriorVerse test set. Condition channels are highlighted in orange .]({{ '/images/04-2025/PRISM:_A_Unified_Framework_for_Photorealistic_Reconstruction_and_Intrinsic_Scene_Modeling/figure_9.jpg' | relative_url }})
