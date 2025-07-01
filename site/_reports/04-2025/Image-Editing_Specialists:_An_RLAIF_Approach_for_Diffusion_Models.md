---
title: Image-Editing_Specialists:_An_RLAIF_Approach_for_Diffusion_Models
layout: default
date: 2025-04-17
---
![Figure 1. Representative results showcasing our method’s ability to perform precise and realistic edits. The input image is displayed alongside four diverse edits, highlighting our approach’s capacity to align with user intentions while preserving structural coherence.]({{ '/images/04-2025/Image-Editing_Specialists:_An_RLAIF_Approach_for_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing instruction-based image editing models often struggle with two key challenges: 1) **Structural Preservation**, where edits inadvertently alter unrelated parts of the image, and 2) **Semantic Alignment**, where the model fails to precisely follow the user's textual and visual intent. Current methods either require complex architectural changes, are computationally expensive, or depend on large, potentially biased, curated datasets. This paper addresses the gap by proposing a method to train specialized, precise, and structurally coherent editing models without relying on extensive human annotation or large-scale datasets.

## 2. Key Ideas and Methodology
The core of the paper is a novel framework for training "Image-Editing Specialists" using **Reinforcement Learning from AI Feedback (RLAIF)**. Instead of relying on human-annotated preferences, this approach uses AI-generated feedback to fine-tune a diffusion model.

The methodology has three key components:
*   **Online RLAIF Framework:** The model is fine-tuned in an online manner, learning from preference rankings of its own generated samples. This avoids the need for a pre-collected dataset and allows for rapid specialization (e.g., after just 10 training steps). The preference learning is based on the Direct Preference Optimization (DPO) algorithm, which directly optimizes the policy without a separate reward model.
*   **Multi-Objective Reward:** To generate preference labels, the AI feedback is structured as a composite score. A **Structural Score** uses monocular depth estimation to ensure the edited image's structure matches the input. A **Semantic Score** uses a pretrained vision encoder (DreamSim) to measure alignment with both the text instruction and a visual prompt (style image) within a segmented region of interest.
*   **Visual and Textual Prompting:** The model is conditioned on an input image, a simple text instruction (e.g., "add snow"), and a visual prompt (e.g., an image of sparse snow). This allows for nuanced control over the edit's style that is difficult to describe with text alone, requiring only about 5 reference images to learn a new concept.

## 3. Datasets Used / Presented
The method was evaluated on diverse editing tasks using the following datasets:
*   **Oxford RobotCar Dataset:** Used to train and evaluate models on 7 types of realistic edits (e.g., adding snow, rain, sand) across 2,500 images per edit type.
*   **Places Dataset:** Used for 6 types of stylistic edits (e.g., changing water to gold, a building to steel) across 2,000 images per edit type.
*   **Google Robot Environment:** Used for a sim-to-real application, where simulated scenes of a robot manipulating a drawer were edited to appear more realistic.

## 4. Main Results
The proposed method demonstrates superior performance over state-of-the-art baselines like InstructPix2Pix, HIVE, MagicBrush, and HQ-Edit.
*   **Quantitative Metrics:** The model achieves the best balance between edit fidelity and structural preservation. It scored lowest on depth map error (20.76 vs. 28.50 for the next best, HIVE), indicating better structure preservation. It also scored highest on visual prompt similarity (0.240) and text-image alignment (0.241), indicating better semantic alignment.
*   **Human Preference Scores:** The model's outputs were preferred by automated human preference predictors (ImageReward, PickScore, HPSv2) over all baselines.
*   **Sim-to-Real Transfer:** In robotics simulations, policies evaluated on the method's edited images showed a much stronger correlation with real-world performance (Pearson r of 0.966) than prior methods.

The authors claim their approach enables precise, realistic, and structurally consistent edits that better align with user intent, with practical utility in domains like robotics.

## 5. Ablation Studies
Two main ablation studies were performed:
1.  **Encoder Choice for Semantic Score:** The authors compared DINOv2, CLIP, and DreamSim as the encoder for the semantic score. Qualitatively, DreamSim produced the most realistic and faithful edits, avoiding the grainy textures of DINOv2 and the color tints and vagueness of CLIP.
2.  **Classifier-Free Guidance (CFG) Scale:** The guidance scale for the visual prompt was varied. Increasing the scale improved alignment with the visual prompt but reduced faithfulness to the original input image's structure. A scale of 3 was found to provide an optimal trade-off for quantitative evaluations.

## 6. Paper Figures
![Figure 2. Qualitative comparison. Our method outperforms its counterparts by significantly editing the image while sharply preserving the structure of regions unrelated to the instruction. We exclude the conditioning style image from the visualization since it is not applicable to the other methods. Additional samples are shown in Appendix 6 .]({{ '/images/04-2025/Image-Editing_Specialists:_An_RLAIF_Approach_for_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 4. Visualization of the impact of the visual prompt (displayed in dashed lines contour) on generated samples when provided the text instruction “add snow on the road”. Our method effectively captures semantic nuances beyond that described in the text prompt. We present further applications of such nuanced control for materials in Fig. 10 , demonstrating how our method can effectively handle diverse visual styles and attributes, such as varying colors, while maintaining structural coherence.]({{ '/images/04-2025/Image-Editing_Specialists:_An_RLAIF_Approach_for_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5. Examples of a simulated scene edited by our method, showcasing enhanced realism compared to the original image across various styles. See Appendix 6.4 for more variants.]({{ '/images/04-2025/Image-Editing_Specialists:_An_RLAIF_Approach_for_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6. We plot the trade-off between consistency with the input image (Y-axis) and consistency with the visual prompt (X-axis). For both metrics, higher is better. We fix the same parameters as in [ 12 ] and vary the s I sty ∈ [1 . 0 , 6 . 0]]({{ '/images/04-2025/Image-Editing_Specialists:_An_RLAIF_Approach_for_Diffusion_Models/figure_6.jpg' | relative_url }})
![Figure 7. Qualitative comparison of the reproduction of the visual prompt induced by different encoders. Best viewed zoomed-in.]({{ '/images/04-2025/Image-Editing_Specialists:_An_RLAIF_Approach_for_Diffusion_Models/figure_7.jpg' | relative_url }})
