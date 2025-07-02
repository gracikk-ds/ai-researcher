---
title: RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers
layout: default
date: 2025-06-03
---
## RelationAdapter: Learning and Transferring Visual Relation with Diffusion Transformers
**Authors:**
- Yan Gong
- Yin Zhang

**ArXiv URL:** http://arxiv.org/abs/2506.02528v1

**Citation Count:** None

**Published Date:** 2025-06-03

![Figure 1: Our framework, RelationAdapter, can effectively perform a variety of image editing tasks by relying on exemplar image pairs and the original image. These tasks include (a) low-level editing, (b) style transfer, (c) image editing, and (d) customized generation.]({{ '/images/06-2025/RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of existing visual prompt-based image editing methods. Current approaches, particularly those using a single reference image, often struggle to capture complex, non-rigid transformations. Methods that do use exemplar pairs (a source and its edited target) tend to concatenate them directly with the query image, which is inefficient, consumes high memory, and can degrade the model's performance. The paper aims to create a more generalizable and efficient framework that can learn and transfer complex visual transformations from minimal examples.

## 2. Key Ideas and Methodology
The core idea is to explicitly learn the visual relationship from an exemplar image pair and apply this transformation to a new query image. The methodology is built on two main components integrated into a Diffusion Transformer (DiT) architecture.

-   **RelationAdapter**: A lightweight, dual-branch adapter module that processes an exemplar pair. It uses a SigLIP vision encoder to extract features from the source and target exemplars. These relational features are then injected into the DiT's attention layers using a "Decoupled Attention Injection" mechanism. This avoids simple concatenation, allowing for more efficient and effective control over the generation process.
-   **In-Context Editor**: The main framework that integrates the RelationAdapter. It introduces "Positional Encoding Cloning," which copies positional encodings from the source condition to the noisy latent tokens to ensure precise spatial alignment and reduce structural distortions. It also uses a "noise-free" paradigm for the source image condition, preserving its details throughout the denoising process to improve fidelity.

## 3. Datasets Used / Presented
The authors introduce **Relation252K**, a new large-scale benchmark dataset for visual prompt-driven image editing.

-   **Size and Content**: It contains 251,580 training instances generated from 33,274 image pairs, covering 218 diverse editing tasks.
-   **Domain and Creation**: The dataset was created semi-automatically using MidJourney for high-fidelity image generation and GPT-4o for annotating image pairs with captions and edit instructions.
-   **Usage**: It is used to train the model and comprehensively evaluate its generalization and adaptability across four main categories: Low-Level Image Processing, Image Style Transfer, Image Editing, and Customized Generation.

## 4. Main Results
The proposed method demonstrates superior performance over existing baselines in both quantitative and qualitative evaluations.

-   Compared to the `Edit Transfer` baseline, RelationAdapter reduces the Mean Squared Error (MSE) from 0.043 to 0.020 and increases the CLIP Image Similarity (CLIP-I) from 0.827 to 0.905.
-   Against the `VisualCloze` baseline, the model reduces MSE from 0.049 to 0.025 and improves CLIP-I from 0.802 to 0.894.
-   The authors claim that RelationAdapter significantly improves a model's ability to understand and transfer editing intent, leading to notable gains in generation quality and overall performance.

## 5. Ablation Studies
The paper includes an ablation study to validate the effectiveness of the proposed `RelationAdapter` module.

-   **Experiment**: The full model was compared against a variant where the RelationAdapter was removed, and visual prompt features were instead directly concatenated with the condition tokens (an "in-context learning" baseline).
-   **Impact**: On seen tasks, removing the RelationAdapter increased MSE from 0.044 to 0.055 and decreased CLIP-I from 0.852 to 0.787. A similar performance degradation was observed on unseen tasks.
-   **Conclusion**: This result confirms that the decoupled attention mechanism of RelationAdapter is crucial for enhancing performance by efficiently integrating visual information and reducing feature redundancy.

## 6. Paper Figures
![Figure 2: The overall architecture and training paradigm of RelationAdapter. We employ the RelationAdapter to decouple inputs by injecting visual prompt features into the MMAttention module to control the generation process. Meanwhile, a high-rank LoRA is used to train the In-Context Editor on a large-scale dataset. During inference, the In-Context Editor encodes the source image into conditional tokens, concatenates them with noise-added latent tokens, and directs the generation via the MMAttention module.]({{ '/images/06-2025/RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers/figure_2.jpg' | relative_url }})
![Figure 3: Overview of the four main task categories in our dataset. Each block lists representative sub-tasks (with ellipses indicating more), along with image-pair examples.]({{ '/images/06-2025/RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers/figure_3.jpg' | relative_url }})
![Figure 4: Overview of the annotation pipeline using GPT-4o. GPT-4o generates a set of source caption , target caption , and edit instruction describing the transformation from I src to I tar .]({{ '/images/06-2025/RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers/figure_4.jpg' | relative_url }})
![Figure 5: Compared to baselines, RelationAdapter demonstrates outstanding instruction-following ability, image consistency, and editing effectiveness on both seen and unseen tasks.]({{ '/images/06-2025/RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers/figure_5.jpg' | relative_url }})
![Figure 6: Ablation study results . Our strategy shows better editorial consistency.]({{ '/images/06-2025/RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers/figure_6.jpg' | relative_url }})
![Result Result Result Input Images Input Images Input Images Figure 7: The generated results of RelationAdapter. RelationAdapter can understand the transformations in example image editing pairs and apply them to the original image to achieve high-quality image editing. It demonstrates a certain level of generalization capability on unseen tasks.]({{ '/images/06-2025/RelationAdapter:_Learning_and_Transferring_Visual_Relation_with_Diffusion_Transformers/figure_7.jpg' | relative_url }})
