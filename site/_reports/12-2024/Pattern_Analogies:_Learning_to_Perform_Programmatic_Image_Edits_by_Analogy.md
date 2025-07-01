---
title: Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy
layout: default
date: 2024-12-17
---
![Figure 1. Our system performs programmatic edits on pattern images without inferring their underlying programs. (Left) Desired edits, expressed with a pair of patterns ( A, A ′ ) , are executed on a target pattern B by a generative model to produce B ′ . (Right) Parametric changes A → A ′ enabled by our domain-specific pattern language induce corresponding changes to the more complex pattern B .]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of editing visual patterns. Desired edits are often "programmatic," meaning they alter the underlying structural rules of the pattern (e.g., changing tile size or layout). Current methods, like Visual Program Inference (VPI), attempt to solve this by inferring the entire program that generates the pattern. However, this approach struggles with complex real-world patterns and often produces disorganized programs that are difficult for users to edit. The paper aims to enable programmatic edits without the need for explicit program inference, providing a more intuitive and direct editing workflow.

## 2. Key Ideas and Methodology
The core idea is to perform programmatic edits by analogy. A user demonstrates the desired transformation by providing a simple pair of patterns (A, A'), and a generative model applies this transformation to a more complex target pattern B to produce the edited version B'.

To achieve this, the authors introduce:
*   **SPLITWEAVE**: A Domain-Specific Language (DSL) designed for creating and manipulating visual patterns. It is used to generate a large, high-quality synthetic dataset of "analogical quartets" (A, A', B, B'), where the edit from A to A' is programmatically identical to the edit from B to B'.
*   **TRIFUSER**: A Latent Diffusion Model (LDM) architected to execute these analogical edits. It is conditioned on the visual features of the input triplet (A, A', B). To overcome issues like detail loss and ambiguity, TRIFUSER incorporates several key modifications: fusing features from multiple encoder layers to preserve detail, combining features from different encoders (SigLIP and DINOv2) to balance semantic and spatial information, and using 3D positional encodings to distinguish between the input images and their spatial content.

## 3. Datasets Used / Presented
*   **Synthetic Training Dataset**: A dataset of ~1 million analogical quartets (A, A', B, B') generated using the SPLITWEAVE DSL. It covers two primary pattern styles: Motif Tiling Patterns (MTP) and Split-Filling Patterns (SFP). This dataset was used to fine-tune the TRIFUSER model.
*   **Synthetic Test Set**: A set of 1,000 unseen synthetic analogical quartets used for quantitative evaluation of the model against baselines.
*   **Real-World Test Set**: A curated dataset of 50 patterns from Adobe Stock, created by professional artists. It spans seven distinct styles, including some not present in the training data (e.g., Memphis-style, geometric patterns), and was used for human perceptual studies.

## 4. Main Results
In a human preference study on real-world patterns, TRIFUSER's edits were overwhelmingly preferred over those from three leading baseline methods. It was chosen over **Analogist** 89% of the time, over **LatentMod** 81% of the time, and over **Inpainter** 72% of the time.

On the synthetic test set, TRIFUSER consistently outperformed all baselines across perceptual metrics (DSIM, DISTS, LPIPS) and structural similarity (SSIM), demonstrating higher fidelity to the ground truth edit. The authors claim their method faithfully performs the demonstrated edit while generalizing to pattern styles beyond its training distribution.

## 5. Ablation Studies
A subtractive ablation study was performed on the synthetic validation set to measure the impact of TRIFUSER's architectural components.
*   **Removing 3D Positional Encoding**: This caused the most severe performance degradation, as the model struggled to identify which pattern to edit. The LPIPS error metric (lower is better) worsened from 0.304 to 0.383.
*   **Removing Low-Level Feature Fusion**: Performance dropped, with LPIPS worsening to 0.335. This indicates a loss of fine-grained detail.
*   **Removing Multi-Encoder Feature Mixing**: Performance also dropped, with LPIPS worsening to 0.345, showing the value of combining different feature types.
*   **Using a Base Model**: Training a standard Image Variation model without any of the proposed modifications resulted in poor performance (LPIPS of 0.815), underscoring the necessity of the architectural changes for this task.

## 6. Paper Figures
![Figure 2. Overview : To create high-quality visual patterns, we introduce a custom DSL called S PLIT W EAVE . Pairs of S PLIT W EAVE programs ( A, B ) are then jointly edited to create analogical quartets. This synthetic data is then used to train T RI F USER , a neural network for analogical pattern editing.]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_2.jpg' | relative_url }})
![Figure 3. Custom program samplers for two pattern styles. Our samplers produce diverse and high-quality patterns, enabling generalization to real-world patterns.]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_3.jpg' | relative_url }})
![Figure 4. We create synthetic analogical quartets ( A, A ′ , B, B ′ ) with consistent edits between A and B pairs, providing data for training an analogical editing models.]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_4.jpg' | relative_url }})
![Figure 5. (Left) T RI F USER is a latent diffusion model conditioned on patch-wise tokens of the input images ( A, A ′ , B ) to generate the analogically edited pattern B ′ . (Right) To achieve high-quality edits, we enrich these tokens by fusing multi-level features from multiple encoders, followed by a 3D positional encoding: 2D to specify spatial locations and 1D to specify the token’s source ( A , A ′ or B ).]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_5.jpg' | relative_url }})
![Figure 6. Qualitative comparison between patterns generated by our model, T RI F USER , and the baselines. T RI F USER generates higher quality patterns with greater fidelity to the input analogy.]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_6.jpg' | relative_url }})
![Figure 7. T RI F USER effectively edits patterns from novel pattern styles not present in the training dataset. T RI F USER shows a noteworthy ability to generalize beyond its training distribution.]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_7.jpg' | relative_url }})
![Figure 8. Our model helps users mix elements of different realworld patterns together, accelerating design exploration.]({{ '/images/12-2024/Pattern_Analogies:_Learning_to_Perform_Programmatic_Image_Edits_by_Analogy/figure_8.jpg' | relative_url }})
