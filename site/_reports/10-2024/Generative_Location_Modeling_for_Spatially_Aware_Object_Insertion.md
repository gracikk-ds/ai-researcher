---
title: Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion
layout: default
date: 2024-10-17
---
## Generative Location Modeling for Spatially Aware Object Insertion
**Authors:**
- Jooyeol Yun, h-index: 5, papers: 14, citations: 81
- Auke Wiggers

**ArXiv URL:** http://arxiv.org/abs/2410.13564v1

**Citation Count:** None

**Published Date:** 2024-10-17

![Figure 1: Our proposed pipeline for object insertion (b), in contrast to instruction-tuned methods (a). We use a pretrained inpainting model and provide it with plausible locations for object insertion.]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current generative models for object insertion often lack spatial awareness, leading them to place objects in unrealistic locations or scales. Instruction-tuned models, which learn to determine placement (where) and appearance (what) simultaneously, struggle with this joint task. This often results in distorted backgrounds, replacement of existing objects, or other unintended scene changes. The authors identify a gap in explicitly modeling plausible object locations, which is critical for achieving visually coherent and realistic image edits.

## 2. Key Ideas and Methodology
The paper proposes a two-stage pipeline that decouples object insertion into two distinct problems: location modeling and inpainting.

*   **Core Idea:** First, a dedicated "location model" identifies a plausible bounding box for a new object. Second, a pre-trained inpainting model generates the object within that specified location. This factorization allows each model to specialize, improving overall quality.
*   **Methodology:** The location model is an autoregressive transformer (GPT-2 based) that generatively predicts bounding box coordinates. It is conditioned on the background image (encoded by a ViT) and the desired object class (encoded by a CLIP text encoder). This generative formulation effectively handles sparsely annotated datasets, as it only requires positive examples of plausible locations for training.
*   **Refinement with DPO:** To further improve accuracy, the model leverages negative (implausible) location labels using Direct Preference Optimization (DPO). This fine-tunes the model to prefer generating plausible locations over implausible ones, treating the labels as preference data.

## 3. Datasets Used / Presented
*   **PIPE Dataset:** A large-scale dataset with over 888,000 image pairs showing scenes before and after object removal. It was used to pre-train the location model on a wide variety of objects and scenes. Positive bounding boxes were extracted by differencing the image pairs.
*   **OPA Dataset:** A smaller, richly annotated dataset with human-labeled plausible (positive) and implausible (negative) locations for objects in COCO images. It was used for fine-tuning the location model and for the DPO training stage, leveraging both positive and negative labels. It was also the primary dataset for evaluation.

## 4. Main Results
The proposed two-stage approach significantly outperforms state-of-the-art instruction-tuned models in object insertion tasks.

*   **Quantitative Results:** On the OPA dataset, the proposed method achieves superior background preservation (Background SSIM of ~0.78) while generating high-quality objects (Foreground CLIP of ~0.28). In contrast, top-performing instruction-tuned models either degrade the background significantly (e.g., InstructPix2Pix SSIM of ~0.55) or fail to generate convincing objects.
*   **User Study:** Human evaluators showed a strong preference for the results from the proposed method over all baselines. For instance, edits from the proposed model were preferred over InstructPix2Pix 86.3% of the time.
*   **Author Takeaway:** Separating the problem of *where* to place an object from *what* the object looks like is a more reliable and effective strategy for object insertion than end-to-end approaches.

## 5. Ablation Studies
*   **DPO Training:** The authors compared their full model (trained with DPO) to a version trained only on positive locations. The DPO-trained model achieved a higher True Positive Rate (TPR) for a given False Positive Rate (FPR), demonstrating that explicitly leveraging negative labels improves the model's ability to identify plausible locations.
*   **Alternative Inpainting Methods:** The authors swapped the PowerPaint inpainting model with an older one (GLIGEN). The results showed a comparable object quality (Foreground CLIP score), confirming that the location model is not tied to a specific inpainter and can benefit from general advancements in inpainting technology.

## 6. Paper Figures
![Figure 10: Example failure case observed when inpainting large areas, for instruction “add a horse”.]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_10.jpg' | relative_url }})
![Figure 2: Training scheme during pretraining (left) and direct preference optimization (right).]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_2.jpg' | relative_url }})
![Figure 3: Annotation format for the PIPE dataset (left) and OPA dataset (right). The PIPE dataset has one groundtruth location per image, whereas OPA provides multiple positive and negative locations.]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_3.jpg' | relative_url }})
![Figure 6: (Left) Example evaluation scenario. Predicted boxes are counted only if a positive or negative ground-truth box meets an IoU above the threshold. (Right) TPR-FPR curves. Each line is constructed by increasing the number of sampled locations from { 10 , 20 , . . . , 100 } . Higher and to the left is better.]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_6.jpg' | relative_url }})
![Figure 7: Comparison between our method + powerpaint, and instruction-guided image editing models on the OPA dataset. Best viewed electronically.]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_7.jpg' | relative_url }})
![Figure 8: Comparison between our method + powerpaint, and instruction-guided image editing models on the PIPE dataset. Additional results are available in Section F . Best viewed electronically.]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_8.jpg' | relative_url }})
![Figure 9: Controlled location sampling for positional instructions, achieved by restricting the allowed sampling region. Instruction-tuned models often fail to follow positional instructions.]({{ '/images/10-2024/Generative_Location_Modeling_for_Spatially_Aware_Object_Insertion/figure_9.jpg' | relative_url }})
