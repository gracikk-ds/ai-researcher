---
title: UIP2P:_Unsupervised_Instruction-based_Image_Editing_via_Cycle_Edit_Consistency
layout: default
date: 2024-12-19
---
![Figure 1. Unsupervised InstructPix2Pix. Our approach achieves more precise and coherent edits while preserving the structure of the scene. UIP2P outperforms state-of-the-art models in both real images (a. and b.) and synthetic images (c. and d.).]({{ '/images/12-2024/UIP2P:_Unsupervised_Instruction-based_Image_Editing_via_Cycle_Edit_Consistency/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the primary limitation of existing instruction-based image editing models: their reliance on supervised learning. These models require large-scale datasets of (input image, edit instruction, ground-truth edited image) triplets. Such datasets are either generated using other models, which introduces systematic biases and limits edit diversity, or are manually annotated by humans, which is prohibitively expensive and not scalable. This dependency on curated triplet datasets hinders the development of more generalizable and versatile editing models that can be trained on vast, unlabeled real-world image collections.

## 2. Key Ideas and Methodology
The paper introduces **UIP2P**, an unsupervised framework for instruction-based image editing. The core of the methodology is a novel principle called **Cycle Edit Consistency (CEC)**. This principle eliminates the need for ground-truth edited images by enforcing that an edit can be reliably reversed.

The high-level approach is as follows:
1.  **Forward Edit:** Given an input image and a forward instruction (e.g., "make the ground forest"), the model generates an edited image.
2.  **Reverse Edit:** The model then takes the edited image and a corresponding reverse instruction (e.g., "make the ground a field") and attempts to reconstruct the original input image.
3.  **Consistency Loss:** A composite loss function enforces consistency throughout this cycle. It includes:
    *   **Reconstruction Loss:** Ensures the final reconstructed image is pixel-wise and semantically similar to the original input.
    *   **CLIP Direction Loss:** Aligns the semantic change in the image space with the change described by the text instructions.
    *   **Attention Map Consistency Loss:** Forces the model to focus on the same image regions during both the forward and reverse edits, ensuring localized changes.

Reverse instructions are generated automatically using Large Language Models (LLMs), making the entire training pipeline unsupervised and scalable to any image-caption dataset.

## 3. Datasets Used / Presented
*   **Training:** The model is trained on both synthetic and real-image datasets.
    *   **InstructPix2Pix (IP2P) Dataset:** A synthetic dataset of image-caption-instruction triplets. The authors augment it by generating reverse instructions using GEMINI Pro.
    *   **CC3M & CC12M:** Large-scale datasets of real images with captions. The authors generate forward instructions, edited captions, and reverse instructions for these datasets using a fine-tuned GEMMA2 model, enabling unsupervised training on real-world data.
*   **Evaluation:**
    *   **IP2P Test Split:** Used for quantitative comparison against the supervised baseline.
    *   **MagicBrush:** A human-annotated benchmark used for zero-shot quantitative evaluation.
    *   **Prolific Platform:** A user study was conducted with 52 participants to gather qualitative human preferences.

## 4. Main Results
UIP2P demonstrates superior performance and generalization compared to supervised methods.
*   **Quantitative:** On the IP2P test set, UIP2P outperforms the baseline InstructPix2Pix on both CLIP image similarity and text-image directional similarity. In zero-shot evaluation on the MagicBrush benchmark, UIP2P is highly competitive with, and sometimes superior to, models specifically fine-tuned on that dataset.
*   **Qualitative:** Visual examples show that UIP2P produces more precise and coherent edits while better preserving the original scene structure compared to state-of-the-art models.
*   **User Study:** In a study comparing six methods, UIP2P received the highest preference scores from users for both matching the instruction and preserving irrelevant image regions.

The authors claim their work is a significant advancement that unblocks the scaling of instruction-based image editing by removing the dependency on ground-truth edited images.

## 5. Ablation Studies
The paper reports two key ablation studies:

1.  **Loss Functions:** The effectiveness of the additional loss components was tested. Starting with a base model (reconstruction and CLIP direction losses), adding the CLIP similarity loss (`L_sim`) improved edit expressiveness. Further adding the attention consistency loss (`L_attn`) provided the most significant performance boost across all metrics, as it improved the model's ability to localize edits to relevant regions. For example, adding `L_attn` reduced the L1 error on the MagicBrush benchmark from 0.089 to 0.062.

2.  **Number of Inference Steps:** The authors analyzed model performance with a varying number of diffusion steps (5, 15, 50). UIP2P was able to produce high-quality, coherent edits with as few as 5 inference steps. In contrast, the baseline InstructPix2Pix struggled at fewer steps and required more to achieve comparable quality, demonstrating that UIP2P is more computationally efficient at inference time.

## 6. Paper Figures
![Figure 2. Examples of biases introduced by Prompt-to-Prompt in the InstructPix2Pix dataset. Each example shows an input image and its corresponding edited image (generated by Prompt-to-Prompt) along with the associated edit instruction. (a) Attribute-entangled edits : modifying the lady’s dress also unintentionally changes the background. (b) Scene-entangled edits: transforming the cottage into a castle affects surrounding elements. (c) Global scene changes: converting the image to black and white alters the entire scene.]({{ '/images/12-2024/UIP2P:_Unsupervised_Instruction-based_Image_Editing_via_Cycle_Edit_Consistency/figure_2.jpg' | relative_url }})
![Figure 3. Overview of the UIP2P training framework. The model learns instruction-based image editing by utilizing forward and reverse instructions. Starting with an input image and a forward instruction, the model generates an edited image using IP2P. A reverse instruction is then applied to reconstruct the original image, enforcing Cycle Edit Consistency (CEC).]({{ '/images/12-2024/UIP2P:_Unsupervised_Instruction-based_Image_Editing_via_Cycle_Edit_Consistency/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative Examples. UIP2P performance is shown across various tasks and datasets, compared to InstructPix2Pix, MagicBrush, HIVE, MGIE, and SmartEdit. Our method demonstrates either comparable or superior results in terms of accurately applying the requested edits while preserving visual consistency.]({{ '/images/12-2024/UIP2P:_Unsupervised_Instruction-based_Image_Editing_via_Cycle_Edit_Consistency/figure_4.jpg' | relative_url }})
![Figure 6. Ablation study on the number of steps. UIP2P achieves high fidelity edits on the input image with fewer steps, whereas IP2P struggles to maintain quality.]({{ '/images/12-2024/UIP2P:_Unsupervised_Instruction-based_Image_Editing_via_Cycle_Edit_Consistency/figure_6.jpg' | relative_url }})
