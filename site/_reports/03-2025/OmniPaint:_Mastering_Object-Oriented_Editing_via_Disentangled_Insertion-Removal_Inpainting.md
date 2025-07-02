---
title: OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting
layout: default
date: 2025-03-11
---
## OmniPaint: Mastering Object-Oriented Editing via Disentangled Insertion-Removal Inpainting
**Authors:**
- Yongsheng Yu
- Jiebo Luo

**ArXiv URL:** http://arxiv.org/abs/2503.08677v2

**Citation Count:** None

**Published Date:** 2025-03-11

![Realistic Object Removal Generative Object Insertion Figure 1. Illustration of OmniPaint for object-oriented editing, including realistic object removal (left) and generative object insertion (right). Masked regions are shown as semi-transparent overlays. In removal cases, the × marks the target object and its physical effects, such as reflections, with the right column showing the results. In insertion cases, the reference object (inset) is placed into the scene, indicated by a green arrow. Note that for model input, masked regions are fully removed rather than semi-transparent.]({{ '/images/03-2025/OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address key challenges in diffusion-based object-oriented image editing. Current methods for object removal and insertion often struggle with the intricate interplay of physical effects like shadows and reflections. Furthermore, they typically rely on large-scale paired training datasets, which are difficult to acquire, or treat removal and insertion as separate, isolated tasks. This separation is inefficient and fails to leverage the inherent relationship between the two processes, leading to suboptimal results like object hallucination or poor integration of new objects.

## 2. Key Ideas and Methodology
The paper introduces **OmniPaint**, a unified framework that reconceptualizes object removal and insertion as interdependent, inverse processes. The core idea is to leverage a pre-trained diffusion model (FLUX) and a progressive training pipeline that reduces dependency on paired data.

The methodology consists of three main stages:
1.  **Inpainting Pretext Training:** The model is first fine-tuned for general inpainting capabilities.
2.  **Paired Warmup:** The model is then trained separately for removal and insertion tasks using a small, custom-collected paired dataset (3,300 samples).
3.  **CycleFlow Unpaired Post-Training:** To improve insertion quality without requiring extensive paired data, the authors introduce **CycleFlow**. This mechanism uses the well-trained removal model to pre-process unpaired images (by removing object effects like shadows). The insertion model is then trained on this processed data, enforcing a cycle consistency loss that ensures an object removed and then re-inserted remains faithful to the original.

Additionally, the paper proposes a novel, reference-free evaluation metric, the **Context-Aware Feature Deviation (CFD) score**, to better assess object removal quality by specifically penalizing object hallucinations and contextual inconsistencies.

## 3. Datasets Used / Presented
*   **Training Data:**
    *   A custom-collected dataset of **3,300 real-world paired samples** for object removal, where each sample includes the original image, the image with the object physically removed, and the object mask.
    *   Large-scale unpaired segmentation datasets (**COCO-Stuff** and **HQSeg**) were used for the CycleFlow post-training phase.
*   **Evaluation Data:**
    *   **Removal:** A custom 300-sample test set and the public **RORD** dataset (1,000 samples).
    *   **Insertion:** A benchmark of **565 samples**, combining the test set from the IMPRINT paper with custom-captured real-world cases.

## 4. Main Results
OmniPaint demonstrated superior performance over existing state-of-the-art methods in both object removal and insertion tasks.
*   **Object Removal:** On the RORD dataset, OmniPaint achieved the best scores across multiple metrics, including the lowest (best) FID, CMMD, and LPIPS. Crucially, it obtained a significantly lower (better) CFD score of 0.3682, indicating fewer hallucinations and better context blending compared to all baselines.
*   **Object Insertion:** OmniPaint achieved the highest scores on all object identity preservation metrics (CLIP-I, DINOv2, CUTE, DreamSim) and overall image quality metrics (MUSIQ, MANIQA), indicating it generates more realistic and seamlessly integrated objects that better match the reference.

Qualitatively, OmniPaint excels at handling complex physical effects, successfully removing objects along with their corresponding reflections and shadows, and inserting objects with natural lighting and geometric alignment.

## 5. Ablation Studies
The authors performed several ablation studies to validate their design choices:

*   **Cycle Loss Weight (γ):** This experiment analyzed the impact of the CycleFlow mechanism. Without it (γ=0), the model failed to synthesize realistic physical effects for inserted objects, resulting in a "copy-paste" appearance. The default weight (γ=1.5) provided the best balance, effectively learning from unpaired data. A higher weight (γ=3.0) caused exaggerated and unnatural effects.
*   **Neural Function Evaluation (NFE) / Inference Steps:** The impact of the number of inference steps was analyzed. For removal, as few as 18 steps were sufficient to cleanly remove objects. For both tasks, quality improved with more steps, with diminishing returns after 28 steps, which was set as the default for optimal visual quality.

## 6. Paper Figures
![Figure 2. Visualization of CFD metric assessment for object removal. The segmentation results are obtained using SAM [ 17 ] with refinement, with purple masks for background, orange masks for segments fully within the original mask, and unmasked for those extending beyond the original mask. Note that the orange masked regions correspond to hallucinated objects. A higher ReMOVE [ 4 ] score is better, while a lower CFD score is preferable. In these cases, ReMOVE scores are too similar to indicate removal success, while CFD score offers a clearer distinction.]({{ '/images/03-2025/OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting/figure_2.jpg' | relative_url }})
![Figure 3. Illustration of the proposed CFD metric for evaluating object removal quality. Left: We apply SAM to segment the inpainted image into object masks and classify them into nested ( Ω M n ) and overlapping ( Ω M o ) masks. Middle: The context coherence term measures the feature deviation between the inpainted region ( Ω M ) and its surrounding background ( Ω B \ M ) in the DINOv2 feature space. Right: The hallucination penalty is computed by comparing deep features of detected nested objects ( Ω M n ) with their adjacent overlapping masks ( Ω M o ) to assess whether unwanted object-like structures have emerged.]({{ '/images/03-2025/OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting/figure_3.jpg' | relative_url }})
![Figure 4. Illustration of CycleFlow. The mapping F removes the object, predicting an estimated target z ′ 1 , while G reinserts the object, generating estimated target z 1 . Cycle consistency is enforced by ensuring G reconstructs the original latent z 1 from the effect removal output. Dashed arrows indicate the cycle loss supervision.]({{ '/images/03-2025/OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting/figure_4.jpg' | relative_url }})
![Figure 5. Qualitative comparison on object insertion. Given masked images and reference object images (top row), we compare results from AnyDoor [ 5 ], IMPRINT [ 34 ], and OmniPaint.]({{ '/images/03-2025/OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting/figure_5.jpg' | relative_url }})
![Figure 6. Qualitative comparison of object removal in challenging scenarios. Top: Simultaneous removal of objects and glass reflections. Middle: Shadow-free removal under real-world lighting. Bottom: Occlusion-robust inpainting, reconstructing background objects without distortion. The compared methods include FreeCompose [ 6 ], PowerPaint [ 58 ], CLIPAway [ 7 ], and FLUX-Inpainting [ 37 ].]({{ '/images/03-2025/OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting/figure_6.jpg' | relative_url }})
![Figure 7. Impact of inference steps and cycle loss weights. (a) Removal (top) and insertion (bottom) results across different neural function evaluations (NFE). (b) Insertion results with varying cycle loss weights γ , with OmniPaint defaulting to γ = 1 . 5 .]({{ '/images/03-2025/OmniPaint:_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting/figure_7.jpg' | relative_url }})
