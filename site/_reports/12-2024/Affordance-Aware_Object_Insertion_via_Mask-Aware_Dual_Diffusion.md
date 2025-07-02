---
title: Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion
layout: default
date: 2024-12-19
---
## Affordance-Aware Object Insertion via Mask-Aware Dual Diffusion
**Authors:**
- Jixuan He, h-index: 2, papers: 3, citations: 19
- Hanspeter Pfister, h-index: 8, papers: 36, citations: 339

**ArXiv URL:** http://arxiv.org/abs/2412.14462v2

**Citation Count:** 4

**Published Date:** 2024-12-19

![Figure 1. Given a foreground-background object-scene pair, our model can perform affordance-aware object insertion conditioning on different position prompts, including points, bounding boxes, masks, and even null prompts.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the problem of unrealistic object placement in image composition tasks. Existing generative models often fail to respect "affordance"—the common-sense, physical, and semantic rules that govern how an object should interact with a scene (e.g., a boat should be on water, not land; a bottle needs a surface for support). The paper aims to generalize this concept from human-centric tasks to any object in any scene, tackling the dual challenges of modeling these complex relationships and the lack of large-scale, diverse training data for this purpose.

## 2. Key Ideas and Methodology
The core idea is to explicitly teach the model affordance by having it predict not just the final image but also the object's insertion mask. The paper introduces **Mask-Aware Dual Diffusion (MADD)**, a model built on a latent diffusion framework. Its key feature is a dual-stream UNet architecture that simultaneously denoises two separate inputs: the latent features of the RGB image and the binary mask indicating the object's final position and shape. This forces the model to reason about plausible placement. The model is conditioned on a foreground object image (encoded with DINOv2 for fine-grained details), the background scene, and a flexible position prompt (point, bounding box, mask, or even no prompt).

## 3. Datasets Used / Presented
The authors construct and present a new large-scale dataset named **SAM-FB**. It is derived from the SA-1B (Segment Anything) dataset and is specifically designed for affordance-aware insertion. It contains over **3.2 million** high-quality foreground-background pairs across more than **3,400 object categories**. The creation pipeline involves:
1.  Generating object masks with SAM.
2.  Applying rigorous rule-based and learning-based filters to ensure foreground quality.
3.  Using the LAMA inpainting model to remove the object from the background, which forces the model to learn affordance instead of relying on simple hole-filling cues.

## 4. Main Results
MADD significantly outperforms existing state-of-the-art methods on the SAM-FB benchmark.
- **Quantitative:** Compared to methods like Stable Diffusion, PBE, and GLI-GEN, MADD achieves the best image quality (average FID score of **13.69**) and the highest semantic similarity to the reference object (average CLIP score of **0.85**).
- **Qualitative:** The model generates visually coherent compositions, correctly adjusting object scale, orientation, and position based on scene context, even for ambiguous or null prompts.
The authors claim MADD serves as a strong and generalizable baseline for affordance-aware object insertion.

## 5. Ablation Studies
Ablation studies were performed to validate the key components of the MADD architecture.
- **Baseline:** A strong insertion model using a standard diffusion setup achieved an FID of 18.32.
- **+ Dual Diffusion:** Introducing the simultaneous diffusion of the image and mask within a fully shared UNet improved the FID to 14.43, showing the benefit of the dual-task approach.
- **+ Expert Branch:** Adding separate, specialized input/output blocks for the image and mask streams (the full MADD model) further improved the FID to **13.69**. This confirms that both the dual-stream design and the expert branches are critical for achieving the best performance.

## 6. Paper Figures
![Figure 2. Dataset construction pipeline for SAM-FB. The pipeline automatically converts any input image into a tetrad output through four stages, ensuring high-quality foreground and background retention via a rigorous data quality control process.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_2.jpg' | relative_url }})
![Figure 3. Mask-aware Dual Diffusion Model (MADD). The RGB image feature z and object mask m are jointly denoised, conditioning on the embeddings of the foreground object f , background object b , and the prompt p . (green: reverse process t → t − 1 )]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative results of MADD on the SAM-FB test set. Each row corresponds to one type of prompt, i.e ., point, bounding box, mask, and null, respectively. Our MADD simultaneously predicts the RGB image and the object mask.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_4.jpg' | relative_url }})
![Figure 5. We test ambiguous prompts (points and blank) on in-the-wild images. With point prompts, our model adjusts foreground properties for affordance-aware insertion, while it autonomously finds suitable positions when no prompt is given.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_5.jpg' | relative_url }})
![Figure 6. MADD can work on images of higher resolution, generating sharper edges, clearer reflections, improved texture details.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_6.jpg' | relative_url }})
![Figure 7. MADD can give different feasible solutions for ambiguous prompts such as point and blank.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_7.jpg' | relative_url }})
![Figure 8. Rank distribution for different methods. Our method has the most proportion of rank 1 and least proportion of rank 5.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_8.jpg' | relative_url }})
![Figure 9. More in-the-wild affordance-insertion examples. The model can generate an affordance-feasible solution to insert the foreground objects according to the background scene.]({{ '/images/12-2024/Affordance-Aware_Object_Insertion_via_Mask-Aware_Dual_Diffusion/figure_9.jpg' | relative_url }})
