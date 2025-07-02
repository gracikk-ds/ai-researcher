---
title: EditAR:_Unified_Conditional_Generation_with_Autoregressive_Models
layout: default
date: 2025-01-08
---
## EditAR: Unified Conditional Generation with Autoregressive Models
**Authors:**
- Jiteng Mu, h-index: 9, papers: 13, citations: 359
- Xiaolong Wang

**ArXiv URL:** http://arxiv.org/abs/2501.04699v1

**Citation Count:** 6

**Published Date:** 2025-01-08

![Figure 1. We propose EditAR, a unified conditional autoregressive model for diverse conditional generation tasks. We demonstrate that without task-specific designs, a single autoregressive model achieves strong performance across diverse tasks, including texture manipulation, object replacement, object removal, local editing, canny-to-image, depth-to-image, and segmentation-to-image.]({{ '/images/01-2025/EditAR:_Unified_Conditional_Generation_with_Autoregressive_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Recent progress in controllable image generation is dominated by diffusion models. However, these models often require task-specific architectural designs and training procedures, making it difficult to create a single, unified model that can handle a wide variety of tasks like image editing, object removal, and condition-based generation (e.g., from depth or segmentation maps). The authors identify this lack of a unified framework as a key challenge. They propose that autoregressive models, which naturally use a unified token-based representation for all inputs, are a promising but underexplored path toward creating a single foundational model for diverse conditional generation tasks.

## 2. Key Ideas and Methodology
The paper introduces **EditAR**, a single, unified autoregressive framework for various conditional image generation and editing tasks.

-   **Core Principle:** The core idea is to extend a text-to-image autoregressive model to accept an additional *image* condition. Both the text instruction and the conditional image (e.g., an image to be edited, a depth map, or an edge map) are fed into a single transformer model, which then predicts the output image token by token.
-   **Methodology:** EditAR builds on the LlamaGen architecture. The conditional image is first tokenized into a sequence of discrete indices by a VQ-Encoder. This sequence is then provided as a prefix to the autoregressive transformer, along with the text instruction embeddings. The model is trained to predict the tokens of the target output image. To switch between different tasks (e.g., editing vs. depth-to-image), the model relies solely on different phrasing in the input text prompt.
-   **Key Addition:** To enhance the semantic alignment between the generated image and the input conditions, the authors introduce a **distillation loss**. This loss encourages the feature space of the autoregressive model to align with that of a powerful, pre-trained vision foundation model (DINOv2), thereby injecting general visual knowledge into the model.

## 3. Datasets Used / Presented
EditAR is trained on a combination of datasets to support its diverse capabilities:
-   **SEED-Data-Edit-Unsplash:** 1.5 million examples used for general image editing tasks like modifying styles, objects, and colors.
-   **PIPE Dataset:** 1.8 million examples used for object addition and removal tasks.
-   **COCOStuff:** Used for training segmentation mask-to-image translation.
-   **MultiGen-20M:** Used for training Canny edge-to-image and depth-to-image translation.
-   **PIE-Bench:** A benchmark with 700 examples across 10 editing types, used for evaluation of image editing performance.

## 4. Main Results
EditAR demonstrates strong, competitive performance across a range of tasks using a single model, outperforming many specialized methods.
-   **Image Editing:** On the PIE-Bench dataset, EditAR outperforms other feed-forward methods like InstructPix2Pix and MGIE. It achieves a better balance between preserving background details and accurately applying the requested edit, narrowing the performance gap to more complex inversion-based methods.
-   **Image Translation:** EditAR achieves the best (lowest) FID scores on Canny edge-to-image, depth-to-image, and segmentation-to-image tasks compared to specialized baselines like ControlNet and unified models like UniControlNet. For instance, in Canny edge translation, EditAR achieves an FID of 13.91, surpassing ControlNet's 14.73.
-   **Author-claimed Impact:** The work provides the first evidence that a single autoregressive model using a standard next-token prediction paradigm can unify and excel at a wide variety of conditional image generation tasks, paving the way for a new class of unified generative models.

## 5. Ablation Studies
-   **Distillation Loss:** The authors studied the impact of the distillation loss. Experiments show that adding this loss, particularly when distilling from DINOv2, significantly improves the model's ability to localize objects for editing and enhances the overall text-to-image alignment. Without distillation, the model's performance degrades.
-   **Classifier-Free Guidance (CFG) Strength:** The effect of the guidance hyperparameter (η) was analyzed. A low value (η=1.0) resulted in edits that weakly followed the text prompt, while a high value (η=7.5) improved text alignment at the cost of reduced image reconstruction quality. A value of η=3.0 was found to provide the best trade-off between following the instruction and preserving the original image content.

## 6. Paper Figures
![Figure 2. Overview of EditAR, which can take various types of image conditions to perform image editing or translation. An image I c is mapped through a VQ-Encoder E I to obtain corresponding token indices. Corresponding text instructions are mapped to latent embeddings c T via a text encoder E T . Both image token indices and text embeddings are input to the autoregressive transformer F to predict the target token indices s . To enhance the text-to-image alignment, a distillation loss is introduced during training to minimize the differences between the latent features of the autoregressive model, F and that of a feature encoder E distill . The output sequence s is lastly decoded into a realistic image via a VQ-Decoder D I during inference.]({{ '/images/01-2025/EditAR:_Unified_Conditional_Generation_with_Autoregressive_Models/figure_2.jpg' | relative_url }})
![Figure 3. Comparison of EditAR (Ours) to feed-forward methods (InstructPix2Pix [ 4 ], MGIE [ 17 ]) and inversion-based approaches (Prompt-to-Prompt [ 22 ], PnPInversion [ 28 ]) on various edits. Our method preserves input details well and has strong text-to-image alignment. In contrast, baseline results exhibit unrealistic visuals, including exaggerated edits or not following instructions, unrealistic modifications, or are unable to localize objects accurately.]({{ '/images/01-2025/EditAR:_Unified_Conditional_Generation_with_Autoregressive_Models/figure_3.jpg' | relative_url }})
![Figure 4. Visual comparisons to baseline methods on various image translation tasks. Our method, EditAR, produces photo-realistic results, preserves input details, and offers substantial sample diversity.]({{ '/images/01-2025/EditAR:_Unified_Conditional_Generation_with_Autoregressive_Models/figure_4.jpg' | relative_url }})
![Figure 5. Studies on distillation loss. From left to right, we show the input image, results w/out distillation, and distillation results with DINOv2 and CLIP. The top example shows improved object localization. The bottom shows better text-to-image alignment.]({{ '/images/01-2025/EditAR:_Unified_Conditional_Generation_with_Autoregressive_Models/figure_5.jpg' | relative_url }})
![Figure 6. Ablation of classifier-free guidance values.]({{ '/images/01-2025/EditAR:_Unified_Conditional_Generation_with_Autoregressive_Models/figure_6.jpg' | relative_url }})
