---
title: Emu_Edit:_Precise_Image_Editing_via_Recognition_and_Generation_Tasks
layout: default
date: 2023-11-16
---
![Figure 1. Emu Edit is a multi-tasking model that combines various editing (left, middle) and vision (right) tasks for precise image editing.]({{ '/images/11-2023/Emu_Edit:_Precise_Image_Editing_via_Recognition_and_Generation_Tasks/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of existing instruction-based image editing models. These models often struggle to accurately interpret and execute user commands, especially for tasks that deviate from their training data. This results in a performance gap where models fail to produce precise edits while preserving the original image's fidelity, limiting their practical utility for a wide range of editing operations.

## 2. Key Ideas and Methodology
The core idea is that training a model on a diverse combination of recognition, generation, and editing tasks enhances its ability to perform precise, instruction-guided image editing. The authors formulate all tasks, including computer vision tasks like object detection and segmentation, as generative problems.

The key methodological contributions are:
*   **Multi-Task Learning:** The model, Emu Edit, is a diffusion model trained on an unprecedented variety of 16 distinct tasks, spanning region-based editing, free-form editing, and computer vision.
*   **Learned Task Embeddings:** To handle the diverse task set, the model learns a unique embedding for each task. This embedding is provided as an additional condition during generation, steering the model toward the correct edit type (e.g., local, global, style) and resolving ambiguity in user instructions.
*   **Task Inversion for Few-Shot Learning:** The model can adapt to new, unseen tasks with only a few examples by freezing the main model weights and learning a new task embedding.

## 3. Datasets Used / Presented
*   **Emu Edit Training Dataset:** The authors constructed a new large-scale dataset of 10 million examples. It covers 16 tasks, including local edits, background changes, text editing, detection, segmentation, and image-to-image translation. Data was generated using a combination of LLMs (Llama 2) for instruction creation and specialized image generation pipelines for each task.
*   **Emu Edit Benchmark:** A new, challenging benchmark was created and publicly released to facilitate more rigorous evaluation. It contains human-annotated instructions for seven distinct editing operations on images from the MagicBrush benchmark, along with corresponding input and output captions.

## 4. Main Results
Emu Edit sets a new state-of-the-art in instruction-based image editing, outperforming previous models like InstructPix2Pix and MagicBrush on both the existing MagicBrush benchmark and the new Emu Edit benchmark.
*   **Quantitative Metrics:** On the MagicBrush test set, Emu Edit achieves superior scores in text-image directional similarity (CLIPdir 0.135 vs. 0.123 for MagicBrush) and image fidelity (DINO 0.879 vs. 0.871).
*   **Human Evaluation:** Human raters showed a strong preference for Emu Edit's results over all baselines. For example, when compared to MagicBrush on its own benchmark, human raters preferred Emu Edit for text alignment 59.5% of the time and for image faithfulness 60.4% of the time.
*   **Author Takeaway:** The authors conclude that combining recognition and generation tasks is essential for building more capable and precise image editing models.

## 5. Ablation Studies
*   **Contribution of Vision Tasks:** The authors ablated the inclusion of computer vision tasks. Removing detection and segmentation tasks degraded performance on region-based edits (human preference for the full model was ~60%). Similarly, removing image-to-image translation tasks hurt performance on free-form edits (human preference for the full model was ~59%). This shows that vision tasks directly improve editing capabilities.
*   **Contribution of Learned Task Embeddings:** A model trained without task embeddings performed worse (CLIPdir of 0.104 vs. 0.117 with embeddings). Qualitatively, the model without embeddings often confused edit types, for instance, performing a global style change when a local texture edit was requested.
*   **Multi-Task vs. Expert Models:** The single multi-task Emu Edit model was compared against "expert" models, each trained on only one specific editing task. The multi-task model outperformed every expert model on its own specialized task, demonstrating the benefit of learning from a diverse task mixture.

## 6. Paper Figures
![Figure 2. Multi-turn image editing. Each subsequent image is derived from the prior one, using its associated caption. The initial image is based on a zeroed reference.]({{ '/images/11-2023/Emu_Edit:_Precise_Image_Editing_via_Recognition_and_Generation_Tasks/figure_2.jpg' | relative_url }})
![Figure 3. Failure cases of baseline instruction-based image editing models. 2]({{ '/images/11-2023/Emu_Edit:_Precise_Image_Editing_via_Recognition_and_Generation_Tasks/figure_3.jpg' | relative_url }})
![Figure 4. Task embeddings. Model trained without task embeddings may get confused about the edit type when the instructions are complicated or there is ambiguity regarding the edit type: (1) Global edit (instead of Texture), (2) Segmentation (instead of Global), (3) Style edit (instead of Local). errors, which translate to noticeable artifacts. To mitigate this, we add a per-pixel thresholding step after each editturn. At each step s , we use the pixel value in the output image, c s +1 I , only if its alteration surpasses a specific threshold. Otherwise, we keep the pixel value from the input image, c s I . Specifically, given an edit turn s , we compute the absolute difference image d = ∥ c s +1 I − c s I ∥ 1 over the RGB channel, and apply the following thresholding:]({{ '/images/11-2023/Emu_Edit:_Precise_Image_Editing_via_Recognition_and_Generation_Tasks/figure_4.jpg' | relative_url }})
![Figure 5. Generations on unseen tasks with task inversion. (i) composition of add and detect tasks, (ii) object contour detection.]({{ '/images/11-2023/Emu_Edit:_Precise_Image_Editing_via_Recognition_and_Generation_Tasks/figure_5.jpg' | relative_url }})
