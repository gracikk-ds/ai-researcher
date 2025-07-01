---
title: Beyond_Editing_Pairs:_Fine-Grained_Instructional_Image_Editing_via_Multi-Scale_Learnable_Regions
layout: default
date: 2025-05-25
---
![Figure 1: Framework of the proposed method . Including description text generation, editing feature semantic alignment, learnable edit region prediction, edited image generation and CLIP supervised loss calculation.]({{ '/images/05-2025/Beyond_Editing_Pairs:_Fine-Grained_Instructional_Image_Editing_via_Multi-Scale_Learnable_Regions/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key challenge in text-driven image editing. Current high-precision, instruction-driven methods (e.g., "change the dog into a cat") depend on large-scale "editing pair" datasets, which consist of an original image, an instruction, and a corresponding ground-truth edited image. Creating these datasets is a time-consuming and expensive process that often yields unrealistic results or unwanted artifacts. Conversely, alternative dataset-free approaches often suffer from poor instruction comprehension and lack the ability to perform precise, localized edits. The paper aims to bridge this gap by developing a method that can perform fine-grained, instruction-driven editing without relying on these scarce editing-pair datasets.

## 2. Key Ideas and Methodology
The core idea is to leverage abundant and easily accessible text-image pairs instead of editing pairs. The method achieves this through a novel framework centered on a **multi-scale learnable region**.

-   **High-level Approach:**
    1.  **Automated Data Generation:** The model is trained using standard text-image pairs. For a given image and its caption (`original description`), a Large Language Model (LLM) is prompted to generate a plausible editing instruction and the corresponding `target description`. This synthetically creates the necessary training data without needing an edited image.
    2.  **Learnable Region Prediction:** The model learns to predict a mask for the editing region. It fuses visual features from the source image with textual features from the editing instruction using cross-attention and self-attention mechanisms. An MLP then processes these fused features to predict a spatial mask that localizes the edit.
    3.  **Guided Image Synthesis:** A pre-trained, frozen text-to-image generative model (e.g., Stable Diffusion) performs the final edit. It is conditioned on the original image, the `target description`, and the predicted editing mask. This ensures that modifications are confined to the relevant area and are semantically accurate.

-   **Theoretical Foundation:** The training is supervised by a composite loss function that utilizes CLIP's vision-language alignment. A **Semantic Alignment Loss** ensures the model correctly interprets the instruction to localize the edit region, while a **CLIP Supervision Loss** guides the generative model to produce a high-fidelity output that matches the target description and preserves the structure of unedited regions.

## 3. Datasets Used / Presented
-   **Training Data:** The model is trained on a dataset of **5 million text-image pairs**, randomly sampled from a large-scale public dataset like LAION. This demonstrates the method's ability to learn from general-purpose data instead of specialized editing datasets.
-   **Evaluation Benchmarks:**
    -   **Emu Edit:** A standard benchmark used to evaluate instruction-based editing. It assesses content preservation and the alignment between the edited image and the target text.
    -   **MagicBrush:** A manually annotated dataset for instruction-guided editing. It is used to evaluate editing quality against ground-truth images and captions across single-turn and multi-turn tasks.

## 4. Main Results
The proposed method achieves state-of-the-art or comparable performance against methods trained on specialized editing-pair datasets, demonstrating the viability of its approach.

-   On the **Emu Edit** test set, the model shows strong performance that scales with the amount of training data. The final model (trained on 5M pairs) achieves a CLIP Directional Similarity (CLIPdir) of 0.1088 and a DINO similarity of 0.8337, competitive with leading methods like UltraEdit and MagicBrush.
-   On the **MagicBrush** test set, the method achieves a CLIP-I score of 0.9383 in the single-turn setting, outperforming the MagicBrush baseline (0.9324) and demonstrating its ability to follow semantic instructions accurately.

The authors claim their work introduces a scalable and data-efficient paradigm for instruction-based editing, eliminating the need for costly editing-pair datasets while maintaining high performance and flexibility.

## 5. Ablation Studies
The authors performed ablation studies to validate the contribution of their two main loss components. The editing instruction used was "Remove the pendant from the dog."

-   **Without Semantic Alignment Loss (`LsemAlign`):** The model failed to accurately localize the editing region. The predicted mask was incorrect, especially when multiple potential targets (e.g., similar objects) were present in the image.
-   **Without CLIP Supervision Loss (`LCLIP`):** The predicted learnable region became excessively large and sparse. This resulted in less precise edits that affected larger, unintended areas of the image.

In summary, both loss terms were shown to be critical: `LsemAlign` for accurate region localization and `LCLIP` for generating a well-scaled mask and a high-quality final image.

## 6. Paper Figures
![Figure 2: Multi-Scale Learnable Region. The learnable region adapts to multi-scale editing requirements from different types of editing operations and varying sizes of target objects.]({{ '/images/05-2025/Beyond_Editing_Pairs:_Fine-Grained_Instructional_Image_Editing_via_Multi-Scale_Learnable_Regions/figure_2.jpg' | relative_url }})
![Figure 3: Illustration of user preferences for edited results.]({{ '/images/05-2025/Beyond_Editing_Pairs:_Fine-Grained_Instructional_Image_Editing_via_Multi-Scale_Learnable_Regions/figure_3.jpg' | relative_url }})
![Figure 4: Comparison of editing results produced by different methods .]({{ '/images/05-2025/Beyond_Editing_Pairs:_Fine-Grained_Instructional_Image_Editing_via_Multi-Scale_Learnable_Regions/figure_4.jpg' | relative_url }})
![Add the cat a collar Figure 5: Editing results produced by our method using different generative models . For each example, from left to right: original image, FLUX [19], VAR [39], and MaskGIT [8].]({{ '/images/05-2025/Beyond_Editing_Pairs:_Fine-Grained_Instructional_Image_Editing_via_Multi-Scale_Learnable_Regions/figure_5.jpg' | relative_url }})
![Figure 6: Influence of each loss component. The editing instruction is: "Remove the pendant from the dog." From left to right: original image, result without L semAlign , result without L CLIP , and result using all loss terms. Each result includes both the learnable region and the edited image.]({{ '/images/05-2025/Beyond_Editing_Pairs:_Fine-Grained_Instructional_Image_Editing_via_Multi-Scale_Learnable_Regions/figure_6.jpg' | relative_url }})
