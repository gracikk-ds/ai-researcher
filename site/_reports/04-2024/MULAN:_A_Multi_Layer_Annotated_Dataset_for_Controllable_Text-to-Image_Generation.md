---
title: MULAN:_A_Multi_Layer_Annotated_Dataset_for_Controllable_Text-to-Image_Generation
layout: default
date: 2024-04-03
---
## MULAN: A Multi Layer Annotated Dataset for Controllable Text-to-Image Generation
**Authors:**
- Petru-Daniel Tudosiu, h-index: 5, papers: 10, citations: 132
- Sarah Parisot, h-index: 2, papers: 5, citations: 15

**ArXiv URL:** http://arxiv.org/abs/2404.02790v1

**Citation Count:** 12

**Published Date:** 2024-04-03

![Figure 1. Example annotations from our MuLAn dataset. We decompose an image into a multi-layer RGBA stack, where each layer comprises an instance image with transparent alpha layer (green overlays) and background image. For each scene, the second row shows iterative addition of RGBA instance layers.]({{ '/images/04-2024/MULAN:_A_Multi_Layer_Annotated_Dataset_for_Controllable_Text-to-Image_Generation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
State-of-the-art text-to-image models struggle with precise spatial control, prompt fidelity, and compositional editing. A key reason for this limitation is that these models are trained on "flat" rasterized RGB images, which do not inherently represent the compositional, instance-level nature of scenes. The authors identify a critical gap: the lack of a large-scale, photorealistic dataset with multi-layer annotations that could enable the development of generative models capable of layer-wise image creation and editing.

## 2. Key Ideas and Methodology
The paper introduces a novel, training-free pipeline to decompose a single monocular RGB image into a multi-layer stack of instance-wise RGBA images. This approach leverages a sequence of pre-trained, general-purpose models to achieve this decomposition without requiring any new model training.

The core methodology consists of three main modules:
1.  **Image Decomposition:** Discovers and extracts object instances using an open-vocabulary detector (`detCLIPv2`), a segmentation model (`SAM`), and a depth estimator (`MiDaS`). It establishes an instance ordering based on depth and occlusion graphs (`InstaDepthNet`).
2.  **Instance Completion:** Iteratively reconstructs the occluded parts of each extracted instance and the background. It uses a diffusion-based inpainting model guided by automatically generated captions. The pre-determined instance order (from furthest to closest) is crucial for providing the correct context for inpainting.
3.  **Image Re-assembly:** Assembles the completed instances and background into a final, ordered RGBA stack, generating occlusion-aware alpha channels to ensure the flattened stack reconstructs the original image.

## 3. Datasets Used / Presented
The authors use their pipeline to create **MuLAn (MUlti-Layer ANnotations)**, a new dataset for controllable generation research. MuLAn is built by processing images from two widely-used datasets:
*   **COCO:** All 58K images were processed, resulting in 16,034 high-quality decompositions (**MuLAn-COCO**).
*   **LAION Aesthetics V2 6.5:** A subset of 100K images was processed, resulting in 28,826 high-quality decompositions (**MuLAn-LAION**).

The final MuLAn dataset contains over **44,800 images** with multi-layer RGBA annotations, comprising over **101,000 individual instance images**.

## 4. Main Results
The primary result is the creation and release of the MuLAn dataset, the first of its kind to provide photorealistic instance decomposition and occlusion information for a large and diverse set of images.

The authors demonstrate the utility of MuLAn through two applications:
1.  **RGBA Image Generation:** A Stable Diffusion model fine-tuned on MuLAn's instance images generated significantly higher-quality RGBA images with better transparency handling compared to a model fine-tuned on standard matting datasets.
2.  **Instance Addition:** An InstructPix2Pix model fine-tuned on MuLAn's layered structure demonstrated superior performance in adding objects to scenes. It achieved better background preservation and suffered from less "attribute bleeding" (e.g., color smearing) than the original editing model.

## 5. Ablation Studies
The authors performed an ablation study on their instance ordering and re-assembly strategy to validate its design. They measured image reconstruction quality (LPIPS, SSIM, PSNR) by comparing different ordering methods for composing the final RGBA stack.
*   **Experiment:** They started with a simple `Depth Based` ordering and incrementally added their proposed refinements.
*   **Steps:**
    1.  Adding `Occlusion Resolution` (using an occlusion graph) improved all metrics.
    2.  Further adding `Mutual-Occlusion Resolution` provided another performance boost.
    3.  Finally, adding `Occlusion Altered Alpha` (making mutually occluded areas transparent) yielded the best reconstruction quality.
*   **Impact:** Each component of the ordering algorithm was shown to be beneficial, with the full method outperforming all simpler baselines, confirming the effectiveness of their carefully designed re-assembly process.

## 6. Paper Figures
![Figure 11. Instance addition. Qualitative examples.]({{ '/images/04-2024/MULAN:_A_Multi_Layer_Annotated_Dataset_for_Controllable_Text-to-Image_Generation/figure_11.jpg' | relative_url }})
![Figure 12. Visualisation of 3 decompositions from MuLAn-COCO (top) and MuLAn-LAION (bottom 2). From left to right: original image, instance RGBA image with green alpha overlay (top row); reconstructed images by adding layers one by one (bottom row).]({{ '/images/04-2024/MULAN:_A_Multi_Layer_Annotated_Dataset_for_Controllable_Text-to-Image_Generation/figure_12.jpg' | relative_url }})
![Figure 2. Illustration of our RGBA decomposition objective.]({{ '/images/04-2024/MULAN:_A_Multi_Layer_Annotated_Dataset_for_Controllable_Text-to-Image_Generation/figure_2.jpg' | relative_url }})
![Figure 3. Illustration of the inpainting procedure for a given instance.]({{ '/images/04-2024/MULAN:_A_Multi_Layer_Annotated_Dataset_for_Controllable_Text-to-Image_Generation/figure_3.jpg' | relative_url }})
![Figure 9. RGBA generation results. Captions: “a train is approaching“, “a red suitcase“, “a pair of running shoes“, “a cartoon car is parked“. For StableDiffusion, “on a black background“ was added.]({{ '/images/04-2024/MULAN:_A_Multi_Layer_Annotated_Dataset_for_Controllable_Text-to-Image_Generation/figure_9.jpg' | relative_url }})
