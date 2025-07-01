---
title: PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing
layout: default
date: 2025-06-09
---
![Figure 1: Editing results of PairEdit trained on three image pairs (1st-2nd rows) or a single image pair (3rd row). Our method effectively captures semantic variations between source and target images.]({{ '/images/06-2025/PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of existing image editing methods. Text-guided editing struggles to precisely specify complex or nuanced semantic changes that are difficult to describe with words. While exemplar-based editing (using source-target image pairs) is a practical alternative, current methods often still rely on textual descriptions of the change, or they fail to learn complex transformations while maintaining high fidelity to the original image's content and identity. The paper aims to solve this by creating a method that can learn intricate semantic edits directly from a very small number of example pairs—or even a single pair—without any text guidance.

## 2. Key Ideas and Methodology
The core principle of PairEdit is to model the semantic variation between a source and target image as an explicit "guidance direction," analogous to the mechanism in Classifier-Free Guidance (CFG).

The methodology is built on three key ideas:
1.  **Disentangled LoRA Modules**: The method jointly optimizes two distinct Low-Rank Adaptation (LoRA) modules on a pre-trained diffusion model (FLUX). A **Content LoRA** is trained to faithfully reconstruct the source image, while a **Semantic LoRA** is trained to capture the desired transformation. This separation disentangles content preservation from semantic change.
2.  **Guidance-Based Semantic Learning**: The semantic LoRA is not trained with a simple reconstruction loss. Instead, its objective is to provide a guidance direction. The combined prediction from both LoRAs is guided towards a target noise vector that represents the edit. This direction is explicitly derived from the difference between the source and target images, effectively teaching the model `edit = target - source`.
3.  **Content-Preserving Noise Schedule**: The authors introduce a novel noising schedule (`xt = x0 + tβε`) that adds noise to the original image instead of interpolating towards pure noise. This ensures that essential content information is preserved even at high noise levels, which stabilizes training and allows the model to learn a more meaningful and consistent semantic difference.

## 3. Datasets Used / Presented
The authors did not use a standard, pre-existing benchmark. They created their own datasets of paired images for training and evaluation.
-   **Creation Process**: The source-target image pairs were generated in several ways: some were sourced from the web or previous work, while others were created by applying existing editing techniques (like SDEdit) to a source image and then manually transferring the edited regions to generate a clean target image.
-   **Usage**: The method is designed for few-shot learning. For each semantic concept (e.g., "age progression," "stylization," "adding glasses"), the model was trained using either three image pairs or, in some cases, just a single image pair.

## 4. Main Results
PairEdit demonstrated superior performance in both quantitative and qualitative evaluations compared to several state-of-the-art exemplar-based and text-based editing methods.
-   **Quantitative Insights**: In evaluations measuring identity preservation (LPIPS, lower is better) and edit magnitude (CLIP similarity, higher is better), PairEdit significantly outperformed baselines. For example, when editing for "chubbiness," PairEdit achieved an LPIPS of **0.0815**, while baselines ranged from 0.1423 to 0.2173, indicating much better identity preservation for a comparable semantic change.
-   **User Study**: The method was overwhelmingly preferred by human evaluators. When asked to choose the better edit based on quality and identity preservation, users preferred PairEdit's results over 93% of the time against baselines like VISII, Analogist, and Concept Slider.
-   **Author-claimed Impact**: PairEdit successfully learns complex, intricate semantics from a very limited number of examples, achieving high-quality, continuous edits while significantly improving content consistency and identity preservation compared to previous methods.

## 5. Ablation Studies
The authors conducted a thorough ablation study to validate the contribution of each of their proposed components.
1.  **Semantic Loss**: When their guidance-based semantic loss was replaced with the visual concept loss from a baseline method (Concept Slider), the model's ability to capture complex editing semantics was significantly diminished.
2.  **Content LoRA**: Removing the dedicated content LoRA and relying only on the semantic LoRA resulted in inconsistent edits with unintended changes to image content, such as altered fur color on an animal or different hairstyles on a person.
3.  **Content-Preserving Noise Schedule**: Replacing their custom noise schedule with a standard one negatively impacted the generalization capability of the semantic LoRA, leading to lower-quality results with artifacts like blurry glasses and inconsistent colors.

Each ablation confirmed that all three components are crucial for achieving the method's high performance in both semantic fidelity and identity preservation.

## 6. Paper Figures
![Figure 2: Overview of PairEdit. (Left) Given a pair of source and target images, we jointly train two LoRAs: a content LoRA, which reconstructs the source image using the standard diffusion loss (Eq. 3), and a semantic LoRA, which captures the semantic difference between the paired images using the proposed semantic loss (Eq. 10). (Right) During inference, when applying the learned semantic LoRA, the original image is edited towards the target semantic.]({{ '/images/06-2025/PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Qualitative comparison. We present exemplar-based image editing results of our method and three baseline methods, including VISII [ 39 ], Analogist [ 20 ], and Slider [ 17 ]. Our method demonstrates superior performance in accurately editing the original image while preserving its content.]({{ '/images/06-2025/PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Examples of continuous editing by our method. By adjusting the scaling factor of the learned LoRA, our method enables a high-fidelity and fine-grained control over the semantic from exemplar images.]({{ '/images/06-2025/PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Real image editing . The reconstructed image is obtained by optimizing a LoRA over the real image. We apply the learned semantic LoRAs to the reconstructed image by merging the LoRAs during inference.]({{ '/images/06-2025/PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Composing sequential edits. Our method effectively composes different edits while preserving the original identity. Multiple semantic LoRAs are merged using the strategy illustrated in Eq. 12.]({{ '/images/06-2025/PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7: Ablation study. We evaluate three variants of our model: (A) replacing the semantic loss with the visual concept loss proposed in [ 17 ], (B) removing the content LoRA, and (C) replacing the content-preserving noise schedule with a standard noise schedule.]({{ '/images/06-2025/PairEdit:_Learning_Semantic_Variations_for_Exemplar-based_Image_Editing/figure_7.jpg' | relative_url }})
