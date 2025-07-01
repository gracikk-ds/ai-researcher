---
title: LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair
layout: default
date: 2024-11-28
---
![Figure 1. Image editing with before-after image pair instructions.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing methods for image editing using language instructions can be ambiguous and fail to capture specific user intentions. While using visual instructions (a before-after image pair) is more precise, current approaches have significant limitations. They typically require large-scale "quad data" (a before-after instruction pair plus a query-target image pair), which is scarce and difficult to collect. This data scarcity limits the models to a narrow range of editing tasks. Furthermore, these methods often fail to explicitly disentangle the editing *instruction* from the image content, which harms the model's interpretability and reusability. The paper aims to solve these problems by creating a generalizable visual instruction editing model that can be trained on more accessible "paired data" (just the before-after pair).

## 2. Key Ideas and Methodology
The core idea is the **LoRA of Change (LoC)** framework, which learns to generate an instruction-specific Low-Rank Adaptation (LoRA) that encodes only the "change" from a before-after image pair.

The methodology has two key components:
1.  **Hypernetwork for LoRA Generation:** A hypernetwork, consisting of a ViT encoder and a transformer decoder, takes a before-after image pair `<A, A'>` as input and dynamically generates a LoRA. This LoRA can then be applied to a frozen, pre-trained image generation model (InstructPix2Pix) to edit any query image `B`. This approach disentangles the editing logic (the LoRA) from the generation model, enhancing interpretability and reusability.
2.  **LoRA Reverse Training:** To overcome the need for quad data, the authors introduce a novel training technique. The model is trained on paired data by using a horizontally flipped version of the instruction pair as the query-target pair. To prevent the model from simply memorizing the appearance of the 'after' image `A'`, a regularization objective is added: if a LoRA `Δ` edits an image from `B` to `B'`, then the reversed LoRA `-Δ` should be able to edit `B'` back to `B`. This forces the network to learn the abstract transformation itself.

## 3. Datasets Used / Presented
*   **SEED-Data-Edit:** A large-scale (3.7M pairs) hybrid dataset used for pre-training the model. It contains synthesized, real-world, and human-annotated image-instruction pairs.
*   **MagicBrush:** A high-quality, manually annotated dataset of 10K image pairs used for fine-tuning the model in a second stage to improve performance on real-world edits.
*   **Evaluation Datasets:** The model was tested on standard benchmarks, including subsets of the InstructPix2Pix dataset, and images from InstructBrush, InstructGIE, and Unsplash.

## 4. Main Results
The LoC framework demonstrates superior performance over state-of-the-art methods for visual instruction-based editing like VISII and Analogist.
*   **Quantitative Metrics:** On the InstructPix2Pix benchmark, LoC achieved the best image quality and fidelity, with an LPIPS of 0.289 (lower is better) and an FID of 46.31 (lower is better). This surpassed competitors while maintaining a fast inference time of just 3 seconds.
*   **Qualitative Results:** The model successfully performs a wide spectrum of edits—including addition, removal, style transfer, and face manipulation—producing high-quality images that are well-aligned with the visual instruction and faithful to the query image.
*   **User Study:** In a human evaluation study, LoC was overwhelmingly preferred, chosen as the best result in 87.4% of cases compared to competing methods.

## 5. Ablation Studies
The authors conducted several ablation studies to validate the core components of their framework:
*   **LoRA Reverse Training:** Removing the reverse training objective caused a critical failure mode called "appearance leakage," where the model would simply copy the appearance of the 'after' instruction image (`A'`) onto the query image, ignoring its original content. Including the reverse objective successfully isolated the "change" and enabled correct editing.
*   **Interpretability and Reusability:** A single LoRA generated from one instruction pair (e.g., "close eyes") was successfully applied to multiple, diverse query images (e.g., a person, a cat), demonstrating that the LoRA effectively encodes a reusable, abstract editing concept.
*   **Random Exchange Consistency:** Randomly swapping the before-after images (`<A, A'>` to `<A', A>`) during training was shown to enforce consistency in the generated LoRAs, leading to edited images with higher fidelity to the query image.
*   **Two-Stage Training:** The second fine-tuning stage on the MagicBrush dataset was shown to be necessary for refinement, improving the model's alignment with visual instructions (Visual CLIP score improved from 0.193 to 0.214).

## 6. Paper Figures
![Figure 2. Information leakage without LoRA Reverse training.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_2.jpg' | relative_url }})
![Figure 3. Comparison of qualitative examples across the 6 editing types between our LoC and two SOTAs.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_3.jpg' | relative_url }})
![Figure 4. Overview of LoRA of Change (LoC) framework. (a) shows that the hypernetwork H generates the instruction-specific LoRA with the before-after image pair < A, A ′ > as inputs. (b) presents the LoRA reverse training. With the generated LoRA ∆ , the red arrows → indicate that the model is trained to reconstruct B ′ taking B as spatial condition while the blue arrows → indicate that the model is trained to reconstruct B taking B ′ as spatial condition. (c) is the inference for image editing. L is the image reconstruction loss.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_4.jpg' | relative_url }})
![Figure 5. Hypernetwork H for LoRA generation. The transformer decoder D consists of M = 6 blocks.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_5.jpg' | relative_url }})
![Figure 6. Ablation on LoRA Reverse training.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_6.jpg' | relative_url }})
![Figure 8. Ablation on interpretability and reusability.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_8.jpg' | relative_url }})
![Figure 9. Ablation on random exchange from < A, A ′ > to < A ′ , A > for LoRA Reverse training.]({{ '/images/11-2024/LoRA_of_Change:_Learning_to_Generate_LoRA_for_the_Editing_Instruction_from_A_Single_Before-After_Image_Pair/figure_9.jpg' | relative_url }})
