---
title: Action-based_image_editing_guided_by_human_instructions
layout: default
date: 2024-12-05
---
## Action-based image editing guided by human instructions
**Authors:**
- Maria Mihaela Trusca
- Marie-Francine Moens, h-index: 16, papers: 118, citations: 1477

**ArXiv URL:** http://arxiv.org/abs/2412.04558v2

**Citation Count:** 1

**Published Date:** 2024-12-05

![Figure 1. Given a text instruction describing an action, we propose EditAction , a method for editing the position and posture of objects in an input image to visually depict the action while preserving the appearance of the objects involved in the action.]({{ '/images/12-2024/Action-based_image_editing_guided_by_human_instructions/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Most text-based image editing models focus on static tasks like adding, removing, or restyling objects. They are generally unable to perform dynamic edits that depict an *action*, such as moving an object or changing its posture according to a command (e.g., "close the cupboard"). This paper addresses this gap by proposing a method to make image editing dynamic, enabling the modification of object positions and postures to visually represent actions described in human instructions, while preserving the visual identity of the objects and the scene's environment.

## 2. Key Ideas and Methodology
The authors introduce **EditAction**, a model that learns to perform action-based edits in a supervised manner. The core idea is to fine-tune a pre-existing static image editing model, **InstructPix2Pix**, to make it sensitive to action-based instructions.

The methodology relies on a multi-part loss function for fine-tuning:
1.  **Contrastive Action Loss (`L_action`)**: The key innovation is a loss that trains the model to differentiate between the correct text instruction and a randomly sampled, incorrect one. This forces the model to accurately interpret and execute the specified action.
2.  **Regularization Loss (`L_reg`)**: To prevent the model from forgetting its prior knowledge and to maintain image quality, a regularization term is added. It minimizes the difference between the fine-tuned model and the original, frozen InstructPix2Pix model.
3.  **Frozen Cross-Attention**: To further preserve the alignment between text and visual concepts learned during pre-training, the cross-attention layers of the underlying U-Net are frozen during fine-tuning.

During inference, the model takes an input image and a text command to generate a new image depicting the final state of the action.

## 3. Datasets Used / Presented
Since no datasets for this task existed, the authors created two new ones by extracting the first (input) and last (ground-truth edited) frames from action clips in video datasets.
*   **LC (Low-Complexity) Dataset**: Created from the MPII-Cooking dataset. It features a fixed camera, meaning the background environment remains consistent between the input and edited images. It contains 13,766 training pairs across 61 actions. A 500-pair subset (`LCtest500`) is used for testing.
*   **HC (High-Complexity) Dataset**: Created from the EPIC-Kitchens dataset. It features a flexible, head-mounted camera, so the viewpoint can change between frames. It contains 37,454 training pairs across 260 actions. A 500-pair subset (`HCtest500`) and a challenging 100-pair subset with long-distance actions (`HCtest100`) are used for testing.

## 4. Main Results
EditAction significantly outperforms existing baselines in both quantitative and qualitative evaluations.
*   **Quantitative Results**: On both the LC and HC test sets, EditAction achieves the highest action recognition accuracy (Acc) as measured by a TimeSformer model (71.4% on LC, 54.4% on HC). It also obtains the best or highly competitive FID scores, indicating that it successfully performs the edit while preserving image fidelity.
*   **Qualitative Results**: Human evaluations confirmed that EditAction is superior at implementing the requested action, preserving the environment, and maintaining object properties compared to baselines.
*   **Author-claimed Impact**: The authors claim that EditAction is an effective model for action-oriented image editing, a dynamic task that prior methods fail to address. It can reason about object movements and even imagine new camera perspectives to depict the outcome of an action.

## 5. Ablation Studies
The authors performed ablation studies to validate the key components of their model architecture and training strategy.
*   **Removing the Action Loss (`L_action`)**: This had the most significant negative impact on performance, causing a substantial drop in action recognition accuracy and an increase in FID score. This confirms the necessity of the contrastive loss for learning to perform actions.
*   **Removing the Regularization Loss (`L_reg`)**: Omitting this term also degraded performance, particularly on the more complex HC dataset. This shows its importance in preventing image quality deterioration and hallucinations.
*   **Unfreezing the Cross-Attention Layers**: Training all layers of the U-Net (instead of freezing the cross-attention) resulted in worse performance. This validates the decision to freeze these layers to preserve the powerful, pre-trained text-image alignments.

## 6. Paper Figures
![Figure 2. Comparison between EditAction and the baselines on the LC and HC datasets. Unlike the baselines, our model can implement actions while preserving the background and the appearance of the objects involved in the action. More examples are presented in Figure 9 (in Appendix).]({{ '/images/12-2024/Action-based_image_editing_guided_by_human_instructions/figure_2.jpg' | relative_url }})
![Figure 3. Left side: HC dataset; Right side: LC dataset. Red indicates the object targeted by the action. Green and blue shows the starting and the ending points of the action.]({{ '/images/12-2024/Action-based_image_editing_guided_by_human_instructions/figure_3.jpg' | relative_url }})
![Figure 4. Training of the U-Net model employed by EditAction. Given an input and an edited image, the model is trained to enhance alignment with the action-based text instruction while preventing hallucinations that may result from fine-tuning on smallscale datasets.]({{ '/images/12-2024/Action-based_image_editing_guided_by_human_instructions/figure_4.jpg' | relative_url }})
![Figure 5. Illustrations of EditAction’s reasoning capabilities, which allow it to extend the scene of the input image based on the action-based text command.]({{ '/images/12-2024/Action-based_image_editing_guided_by_human_instructions/figure_5.jpg' | relative_url }})
![Figure 6. Despite being trained on a limited number of actions, EditAction can implement actions using verbs unseen during the training, such as ”wipe” for the LC dataset and ”place” for the HC dataset.]({{ '/images/12-2024/Action-based_image_editing_guided_by_human_instructions/figure_6.jpg' | relative_url }})
![Figure 7. Limitations of EditAction.]({{ '/images/12-2024/Action-based_image_editing_guided_by_human_instructions/figure_7.jpg' | relative_url }})
