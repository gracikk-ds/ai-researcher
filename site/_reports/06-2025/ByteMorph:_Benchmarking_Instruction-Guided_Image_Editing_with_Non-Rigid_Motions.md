---
title: ByteMorph:_Benchmarking_Instruction-Guided_Image_Editing_with_Non-Rigid_Motions
layout: default
date: 2025-06-03
---
## ByteMorph: Benchmarking Instruction-Guided Image Editing with Non-Rigid Motions
**Authors:**
- Di Chang
- Peng Wang

**ArXiv URL:** http://arxiv.org/abs/2506.03107v2

**Citation Count:** 0

**Published Date:** 2025-06-03

![Figure 1 Overview of ByteMorph . a) We first construct ByteMorph-6M and ByteMorph-Bench, a large-scale dataset and a corresponding evaluation benchmark with data that covers a diverse range of non-rigid motions. b) We then fine-tune ByteMorpher, a diffusion transformer model initialized with pretrained weights from Flux.1-dev [ 3 ], using the data collected in ByteMorph-6M. The distribution of ByteMorph-6M is shown in c).]({{ '/images/06-2025/ByteMorph:_Benchmarking_Instruction-Guided_Image_Editing_with_Non-Rigid_Motions/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a significant gap in instruction-guided image editing. Existing methods and datasets predominantly focus on static edits (e.g., style changes, attribute modification) or rigid transformations. They largely fail to handle complex, non-rigid motions such as camera movements, human articulation, object deformations, and dynamic interactions. This limitation prevents current models from performing expressive, motion-oriented edits, which are crucial for more realistic and dynamic visual content manipulation. The paper aims to bridge this gap by creating a dedicated framework for benchmarking and developing models capable of these non-rigid transformations.

## 2. Key Ideas and Methodology
The core of the work is **ByteMorph**, a comprehensive framework for non-rigid motion editing. The methodology has two main components: a data generation pipeline and a baseline model.

-   **Data Generation:** Instead of using static image pairs, the authors generate data from video. They use a Vision-Language Model (VLM) to create a "motion caption" (e.g., "the camera zooms in") for a given source image. This caption guides a video generation model (Seaweed) to synthesize a short, dynamic video clip that realistically performs the described motion. Frame pairs are then sampled from this video to create high-fidelity source-target image pairs. A VLM is used again to generate a precise editing instruction for each pair. This process ensures that the transformations are natural and temporally coherent.

-   **Model (ByteMorpher):** The authors propose `ByteMorpher`, a baseline model built by fine-tuning a pre-trained Diffusion Transformer (DiT) model (FLUX.1-dev). During training, the model receives the source image latent, a noised version of the target image latent, and the text instruction. It is trained to predict the noise added to the target latent, thereby learning to perform the specified motion-based edit.

## 3. Datasets Used / Presented
The paper introduces two new assets:

-   **ByteMorph-6M:** A large-scale training dataset containing over 6.4 million instruction-based image editing pairs. It is specifically designed to cover a wide range of non-rigid motions, including camera motion (zoom, pan), human motion (pose, expression), object motion (deformation, movement), and human-object interactions. It was generated using the video synthesis pipeline described above and is used to train the `ByteMorpher` model.

-   **ByteMorph-Bench:** A carefully curated evaluation benchmark consisting of 613 challenging, high-quality test pairs not seen during training. It is categorized into the five non-rigid motion types and is used to quantitatively and qualitatively evaluate the performance of various editing models.

## 4. Main Results
The paper presents a comprehensive evaluation on `ByteMorph-Bench`, comparing `ByteMorpher` against both open-source and commercial models.

-   `ByteMorpher` significantly outperforms existing open-source methods across all non-rigid motion categories. For instance, in the "Object Motion" category, `ByteMorpher` achieves a VLM-Score of 89.07, substantially higher than prior models like InstructPix2Pix (36.47) and even a fine-tuned InstructMove (87.97).

-   When compared to leading industry models, `ByteMorpher` demonstrates competitive performance. While models like GPT-4o-image excel at following instructions, they often struggle with preserving the subject's identity. `ByteMorpher` provides a better balance, achieving strong instruction adherence while maintaining high visual consistency with the source image. These results validate the effectiveness of the specialized `ByteMorph-6M` dataset and the `ByteMorpher` model for the task of non-rigid motion editing.

## 5. Ablation Studies
The authors performed an ablation study to validate the effectiveness of their proposed `ByteMorph-6M` dataset.

-   **Experiment:** They took two existing open-source models, `InstructMove` and `OminiControl`, and fine-tuned them on the `ByteMorph-6M` training set.
-   **Impact:** Both models showed significant performance improvements across all evaluation metrics on the `ByteMorph-Bench`. For example, the VLM-Score for `InstructMove` on the "Camera Zoom" task increased from 70.66 to 82.29 after fine-tuning. Qualitatively, the fine-tuned models demonstrated a substantially improved ability to follow complex motion instructions. This ablation confirms that the dataset itself is a key contribution, enabling existing architectures to learn non-rigid transformations effectively.

## 6. Paper Figures
![Figure 2 Overview of Synthetic Data Construction . Given a source frame extracted from the real video, our pipeline proceeds in three steps. a) A Vision-Language Model (VLM) creates a Motion Caption from the instruction template database to animate the given frame. b) This caption guides a video generation model [ 45 ] to create a natural transformation. c) We sampled frames uniformly from the generated dynamic videos with a fixed interval and treated each pair of neighbouring frames as an image editing pair. We re-captioned the editing instruction by the same VLM, as well as the general description of each sampled frame (not shown in the figure).]({{ '/images/06-2025/ByteMorph:_Benchmarking_Instruction-Guided_Image_Editing_with_Non-Rigid_Motions/figure_2.jpg' | relative_url }})
![Figure 3 Overview of ByteMorpher’s training. We fine-tuned the Diffusion Transformer backbone from the pre-trained Flux.1-dev [ 3 ] text-to-image model on the ByteMorph-6M. We feed the source image and target image into the same frozen VAE encoder and obtain source and target latents. The position encoding for both latents is shared with exactly the same embeddings. The target latent is added with noise and further concatenated with the source latent along the sequence length dimension. The DiT is fine-tuned with the MSE loss, where the difference between the noise and the latter half of the output from DiT (corresponding to the noisy target latent input) is minimized.]({{ '/images/06-2025/ByteMorph:_Benchmarking_Instruction-Guided_Image_Editing_with_Non-Rigid_Motions/figure_3.jpg' | relative_url }})
![Figure 4 Qualitative comparison of ByteMorpher and other methods from the industry on ByteMorph-Bench. GPT-4o-Image and ByteMorpher demonstrate strong instruction-following quality while GPT-4o-Image struggles to preserve the identity and appearance in the source image. On the other hand, Gemini-2.0-flash-image and SeedEdit 1.6 preserve ID well but cannot consistently follow the motion editing instructions.]({{ '/images/06-2025/ByteMorph:_Benchmarking_Instruction-Guided_Image_Editing_with_Non-Rigid_Motions/figure_4.jpg' | relative_url }})
