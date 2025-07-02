---
title: DreamEdit:_Subject-driven_Image_Editing
layout: default
date: 2023-06-22
---
## DreamEdit: Subject-driven Image Editing
**Authors:**
- Tianle Li, h-index: 5, papers: 9, citations: 361
- Wenhu Chen, h-index: 33, papers: 57, citations: 7031

**ArXiv URL:** http://arxiv.org/abs/2306.12624v2

**Citation Count:** None

**Published Date:** 2023-06-22

![Figure 1: The leftmost column is the customized subject, the middle column is the Subject Replacement task, the rightmost column is the Subject Addition task. The output is the generated results by DreamEditor]({{ '/images/06-2023/DreamEdit:_Subject-driven_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a gap between two existing areas of image manipulation: subject-driven generation and text-guided image editing. Current subject-driven generation methods (e.g., DreamBooth) can create images of a specific, personalized subject but lack precise control over the subject's position and the image background. Conversely, text-guided editing methods offer fine-grained control over image layout and background but cannot faithfully synthesize a specific, user-provided subject. This paper aims to bridge this gap by introducing tasks that require both subject fidelity and precise compositional control.

## 2. Key Ideas and Methodology
The paper introduces two novel tasks: **Subject Replacement** (swapping a subject in a source image with a custom one) and **Subject Addition** (placing a custom subject into a designated location in a scene).

The core of their proposed method, **DreamEditor**, is an iterative in-painting process. The high-level approach is as follows:
1.  **Personalization:** A text-to-image diffusion model is fine-tuned using DreamBooth to associate the custom target subject with a unique text token (e.g., `[V]`).
2.  **Initialization:** For Subject Replacement, the source image is used as the starting point. For Subject Addition, a preliminary subject is first inpainted into the target location using a method like GLIGEN to provide a plausible initial pose and context.
3.  **Iterative Refinement:** The model repeatedly performs an in-painting loop. In each iteration, it:
    *   Segments the subject in the current image to create a mask.
    *   Uses DDIM inversion to encode the image into a latent representation.
    *   Denoises the latent representation within the masked region, guided by the personalized text prompt, to regenerate the subject. The background outside the mask is preserved.
    *   The output of one iteration becomes the input for the next. This allows the generated subject to gradually adapt its shape, texture, and lighting to match the target subject while blending realistically with the background.

## 3. Datasets Used / Presented
The authors introduce a new benchmark dataset called **DreamEditBench** to evaluate the proposed tasks.
*   **Domain:** General real-world images.
*   **Content:** It consists of 22 different subject types (e.g., teapots, toys, pets), with a few reference images provided for each custom subject.
*   **Size & Structure:** The benchmark contains a total of 440 source images, split between the two tasks:
    *   **Subject Replacement:** 220 images, each containing a subject of the same class as the custom target.
    *   **Subject Addition:** 220 background images, with manually specified bounding boxes indicating where the custom subject should be added.
*   **Subsets:** The dataset is further divided into "easy" and "hard" subsets to analyze model performance under varying levels of difficulty (e.g., based on the visual dissimilarity between source and target subjects).

## 4. Main Results
The authors evaluate `DreamEditor` against several baselines using both automatic metrics and rigorous human evaluation across three criteria: Subject Consistency, Background Consistency, and Realism.

*   The key finding is that human evaluation results often diverge from automatic metrics, underscoring the necessity of human assessment for these complex editing tasks.
*   In human evaluations for **Subject Replacement**, `DreamEditor` (using 5 iterations) achieves the highest overall score of **0.664**, significantly outperforming the next best baseline, Customized-DiffEdit (0.488).
*   For **Subject Addition**, `DreamEditor` achieves a high Realism score of **0.528**, far surpassing baselines like CopyHarmonize (0.295). This indicates `DreamEditor`'s strength in generating subjects that are contextually aware and realistically integrated into the scene.
*   The authors' takeaway is that the proposed iterative refinement approach enables a gradual and smooth adaptation to the customized subject, leading to superior results in both subject fidelity and realism compared to one-shot methods.

## 5. Ablation Studies
The paper reports several analyses on the components and behavior of `DreamEditor`.

*   **Effect of Iterations:** The performance was analyzed across 1 to 5 iterations for Subject Replacement. As the number of iterations increases, **Subject Consistency** consistently improves (from 0.531 at N=1 to 0.625 at N=5). However, **Background Consistency** and **Realism** tend to fluctuate or decrease after an initial peak. Selecting the best iteration on a per-example basis yields the highest overall score (0.664), demonstrating a trade-off between subject fidelity and image quality that varies with iteration count.
*   **Effect of Initialization Strategy:** For Subject Addition, comparing `DreamEditor` with GLIGEN initialization versus a simpler COPY (copy-paste) initialization shows that the more sophisticated GLIGEN approach leads to better overall performance (0.626 vs. 0.623), primarily by achieving higher realism.
*   **Easy vs. Hard Subsets:** All models, including `DreamEditor`, performed substantially better on the "easy" subset of `DreamEditBench` than the "hard" one. For instance, on Subject Replacement, `DreamEditor` scored **0.702 on the easy set versus 0.567 on the hard set**, confirming the benchmark's difficulty stratification and highlighting the remaining challenges in the field.

## 6. Paper Figures
![Figure 2: The visualization of DreamEditor to iteratively refine the generated target subject.]({{ '/images/06-2023/DreamEdit:_Subject-driven_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: DreamEditor generates the results iteratively. The output of the last iteration will serve as the input for the next. In each iteration, it leverages the dilated mask of subject segmentation and the specialized prompt to guide the DDIM inversion and gradually in-paint a subject more similar to the target one.]({{ '/images/06-2023/DreamEdit:_Subject-driven_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Results on Subject Replacement Task Compared with Baselines]({{ '/images/06-2023/DreamEdit:_Subject-driven_Image_Editing/figure_4.jpg' | relative_url }})
