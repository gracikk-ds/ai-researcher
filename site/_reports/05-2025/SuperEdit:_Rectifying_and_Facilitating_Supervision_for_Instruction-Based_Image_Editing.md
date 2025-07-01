---
title: SuperEdit:_Rectifying_and_Facilitating_Supervision_for_Instruction-Based_Image_Editing
layout: default
date: 2025-05-05
---
![Figure 1. (a) Our editing method works well with real and high-resolution images, handling various free-form edits (left) and local edits (right); (b) Compared to the current state-of-the-art SmartEdit, our method achieves a 9.19% performance improvement with 30 × less training data and 13 × fewer model parameters; (c) Our method achieves better overall scores on the human evaluation results, indicating more precise editing capabilities.]({{ '/images/05-2025/SuperEdit:_Rectifying_and_Facilitating_Supervision_for_Instruction-Based_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing methods for instruction-based image editing rely on automatically generated datasets. This process often creates a mismatch between the textual editing instruction and the actual changes in the edited image, resulting in "noisy" supervision signals. Previous works have tried to mitigate this by using more complex models or adding pre-training tasks, but they overlook the fundamental problem of poor-quality supervision data. This paper addresses this gap by focusing on improving the supervision signals themselves to enhance model performance more directly and efficiently.

## 2. Key Ideas and Methodology
The core idea is that improving the quality of supervision is more effective than increasing model complexity. The authors propose a data-oriented solution called SuperEdit with two main components:

1.  **Rectifying Supervision:** The method uses a Vision-Language Model (VLM), GPT-40, to generate more accurate editing instructions that better align with the original-edited image pairs. This rectification process is guided by "diffusion priors"—the principle that different stages of the diffusion process correspond to distinct types of edits (e.g., early stages for global layout, mid-stages for local objects, late stages for details).

2.  **Facilitating Supervision:** To handle ambiguous or complex edits, the paper introduces a contrastive learning scheme. Using the rectified instruction as a positive sample, a VLM generates similar but incorrect instructions as negative samples. The model is then trained with a triplet loss to learn to distinguish between these subtle differences, improving its editing precision.

## 3. Datasets Used / Presented
-   **Training Data:** The authors constructed a new training set of 40,000 samples by extracting and processing image-instruction pairs from three public datasets: InstructPix2Pix, MagicBrush, and Seed-Data-Edit.
-   **Evaluation Benchmark:** The model's performance was evaluated on the **Real-Edit benchmark**, a human-aligned benchmark that uses GPT-40 for automated scoring across three metrics: Following (instruction adherence), Preserving (content preservation), and Quality.

## 4. Main Results
SuperEdit significantly outperforms previous state-of-the-art (SOTA) methods on the Real-Edit benchmark.
-   Compared to the SOTA model SmartEdit, SuperEdit achieves a **9.19% higher overall score (3.91 vs. 3.59)**.
-   This superior performance is achieved using **30x less training data** (40K vs. 1.2M samples) and a **13x smaller model** (1.1B vs. 14.1B parameters).
-   Human evaluations confirm these results, showing that SuperEdit wins against competitors in overall editing capability, instruction following, and image quality.

## 5. Ablation Studies
The authors performed several ablation studies to validate the contributions of their proposed components:

-   **Rectified Instructions:** Training a model with 40K rectified instructions significantly outperformed a baseline trained on 300K original (noisy) instructions. The "Following" accuracy improved from 41% to 62%, and the score increased from 2.45 to 3.40.
-   **Contrastive Instructions:** Adding contrastive supervision on top of rectified instructions further improved performance. The "Following" score increased from 3.40 to 3.59, and the "Preserving" score increased from 4.06 to 4.14.
-   **Data Scaling:** Performance consistently improved as the training dataset size was scaled from 5k to 40k samples, demonstrating the method's effectiveness and potential for further gains with more data. The overall score increased from 3.42 (at 5k) to 3.91 (at 40k).

## 6. Paper Figures
![Figure 3. (a) Existing work primarily uses LLMs and diffusion models to automatically generate edited images. However, current diffusion models often fail to accurately follow text prompts while maintaining the input image’s layout, resulting in mismatches between the original-edited image pairs and the editing instructions. (b) We perform instruction rectification (Step 3) based on the images constructed in Steps 1 and 2. We show VLMs can understand the differences between the images, enabling them to rectify editing instructions to be better aligned with original-edited image pairs.]({{ '/images/05-2025/SuperEdit:_Rectifying_and_Facilitating_Supervision_for_Instruction-Based_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. We show that the editing model follows consistent generation attributes at different sampling stages, independent of the editing instructions. The early, middle, and late sampling stages correspond to global , local , and detail changes, respectively, while style changes occur at all stages. All the generated images here are DDIM 30-step sampled final images. The orange progress bar and the grid progress bar represent the sampling stages with and without the editing instructions, respectively.]({{ '/images/05-2025/SuperEdit:_Rectifying_and_Facilitating_Supervision_for_Instruction-Based_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5. (a) Based on the rectified editing instruction and original-edited image pair, we utilize the Vision-Language Models (VLM) to generate various image-related wrong instructions. These involve random substitutions of quantities, spatial locations, and objects within the rectified editing instructions according to the original-edited images context; (b) During each training iteration, we randomly select one wrong instruction c T neg and input it along with the rectified instruction c T pos into the editing model to obtain predicted noises. The goal is to make the rectified instruction’s predicted noise ϵ pos closer to the sampled training diffusion noise ϵ , while ensuring the noise from incorrect instructions ϵ neg is farther. Best viewed in color.]({{ '/images/05-2025/SuperEdit:_Rectifying_and_Facilitating_Supervision_for_Instruction-Based_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Visual comparison with existing methods and the corresponding human-aligned GPT-4o evaluation scores (Following, Preserving, Quality Scores from left to right). We achieve better results while preserving the layout, quality, and details of the original image. Please note that we do not claim that our editing results are flawless. We provide more visual comparison results in the supplementary material.]({{ '/images/05-2025/SuperEdit:_Rectifying_and_Facilitating_Supervision_for_Instruction-Based_Image_Editing/figure_6.jpg' | relative_url }})
