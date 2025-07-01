---
title: InstructGIE:_Towards_Generalizable_Image_Editing
layout: default
date: 2024-03-08
---
![Fig. 1: Demo results of the proposed InstructGIE framework on various image manipulation tasks to both humans and scenes. By our proposed method, our model can generalize to generate the desired output with great detail qualities.]({{ '/images/03-2024/InstructGIE:_Towards_Generalizable_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limited generalization capabilities of recent diffusion-based image editing models. These models often fail to perform edits described by instructions (textual or visual) that were not explicitly seen during training, leading to poor quality or inaccurate results. While in-context learning has shown promise in language models, its application to vision tasks like image editing is underdeveloped. Existing methods are not specifically tailored for editing, resulting in outputs with corrupted details and an inability to handle diverse, unseen instructions.

## 2. Key Ideas and Methodology
The paper introduces **InstructGIE**, a framework designed to enhance the generalization of image editing by improving performance from both visual and text-based instructions.

- **Core Principle:** The model's ability to generalize is improved by enhancing its in-context learning capacity and standardizing its interpretation of language commands.

- **High-level Approach:** The framework is built upon a ControlNet and Stable Diffusion backbone and introduces four key technical contributions:
    1.  **Reformed Conditioned Latent Diffusion Model (RCLDM):** It replaces standard vision encoders (like ConvNet or ViT) with a **VMamba-based module**. This leverages VMamba's larger effective receptive field to better capture global context from visual prompt examples.
    2.  **Editing-Shift Matching (ESM):** A training strategy that calculates the semantic "shift" between input and output images using CLIP embeddings. A dedicated loss function forces the model's predicted edit to match the semantic shift of the ground-truth example, improving contextual understanding.
    3.  **Language Instruction Unification (LIU):** A frozen lightweight Large Language Model (LLM) is used to process and reformulate user-provided text instructions into a standardized format. This ensures that different phrasings of the same command lead to consistent and predictable edits.
    4.  **Selective Area Matching (SAM):** A training-only optimization technique that uses a segmentation model (Mask2Former) to identify and focus on critical, high-detail regions like human faces. A targeted loss is applied to these areas to rectify corrupted details and improve output quality without relying on negative prompts.

## 3. Datasets Used / Presented
The authors introduce a new dataset specifically designed for generalizable, in-context image editing.

- **Dataset Name:** **Visual Prompt Dataset for Image Editing**
- **Description:** The dataset was created by first using a fine-tuned GPT-3 model to generate editing instructions and corresponding image captions. Then, Prompt-to-Prompt and Stable Diffusion were used to generate the actual images.
- **Size and Content:** It contains approximately 12,000 images corresponding to around 2,000 unique editing instructions. A key feature is that each instruction is paired with at least two different input-output image examples, which is crucial for training models to learn from context.
- **Usage:** The dataset was used for training and evaluating the InstructGIE model and for comparing it against baseline methods.

## 4. Main Results
InstructGIE demonstrated superior performance over existing state-of-the-art methods in both quantitative metrics and qualitative examples, especially on unseen, out-of-domain tasks.

- **Quantitative Insights:**
    - **Image Quality (FID ↓):** InstructGIE achieved an FID score of **7.57**, significantly outperforming SDEdit (21.67), InstructPix2Pix (17.87), and PromptDiffusion (13.75).
    - **Instruction Following (CLIP DirSim ↑):** The model scored **0.27** in CLIP directional similarity, indicating better alignment with instructions compared to SDEdit (0.11), InstructPix2Pix (0.17), and PromptDiffusion (0.21).

- **Author-claimed Impact:** The framework generates higher-quality images with better detail and more accurately follows complex editing instructions. It shows robust generalization to novel tasks that are challenging for previous models.

## 5. Ablation Studies
The authors conducted a comprehensive ablation study by systematically removing each of the four main components of InstructGIE to validate their individual contributions.

- **Without RCLDM (VMamba Module):** Removing the VMamba-based encoder resulted in a weaker understanding of visual instructions, causing FID to increase to 10.15 and CLIP DirSim to drop to 0.13.
- **Without ESM (Editing-Shift Matching):** Disabling this loss function degraded the model's ability to learn the editing context, increasing FID to 9.23 and decreasing CLIP DirSim to 0.15.
- **Without LIU (Language Unification):** Without standardizing text prompts, the model produced inconsistent results for semantically identical instructions, and FID rose to 10.37.
- **Without SAM (Selective Area Matching):** Removing the targeted detail-correction loss led to the largest drop in perceptual quality, with FID increasing to 11.31 and visible distortions appearing in human faces.

## 6. Paper Figures
![Fig. 2: Overall architecture of InstructGIE. The lower pipeline is for both training and inference processes where the model obtains unified editing instructions outputted by Instruction Unification Module U and combines with visual prompted input Img VPcon]({{ '/images/03-2024/InstructGIE:_Towards_Generalizable_Image_Editing/figure_2.jpg' | relative_url }})
![Fig. 3: Effective Reception Field (ERF) of ConvNet, ViT, VMamba based model architectures.]({{ '/images/03-2024/InstructGIE:_Towards_Generalizable_Image_Editing/figure_3.jpg' | relative_url }})
![Fig. 4: Dataset generation process Our dataset generation consists of two phases. Data Generation is to generate sets of image pairs under one editing caption. Data Processing is randomly pick image pairs under the same editing instruction and concatenate them together as one input for training.]({{ '/images/03-2024/InstructGIE:_Towards_Generalizable_Image_Editing/figure_4.jpg' | relative_url }})
