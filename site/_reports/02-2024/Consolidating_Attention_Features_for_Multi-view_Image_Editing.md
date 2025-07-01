---
title: Consolidating_Attention_Features_for_Multi-view_Image_Editing
layout: default
date: 2024-02-22
---
![Figure 1. Given an object-centric multi-view image set (center), we edit all images simultaneously (left and right), using 3D geometric control, such as changing the body skeleton. To promote consistency across different views, we leverage an image diffusion model and introduce QNeRF, a query feature space neural radiance field, to progressively consolidate attention features during the generation process.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the problem of 3D inconsistency when applying modern diffusion-based image editing techniques to a set of multi-view images depicting a single scene. While these methods are powerful for single images, applying them naively to multiple views results in edits that are not geometrically coherent (e.g., a person's edited pose differs from one camera angle to the next). Existing multi-view editing methods often struggle with large geometric changes like articulations, as they tend to produce visual artifacts.

## 2. Key Ideas and Methodology
The core idea is that the `query` features in the self-attention layers of a diffusion model significantly influence the geometric structure of the generated image. The authors propose to enforce 3D consistency by consolidating these query features across all views.

The methodology introduces **QNeRF**, a Neural Radiance Field (NeRF) trained on the internal `query` features extracted from the diffusion model during the editing process. The workflow is as follows:
1.  During the denoising process for all views, `query` features are extracted.
2.  A QNeRF is trained on these features to learn a 3D-consistent representation of the queries.
3.  This QNeRF is then used to render consolidated, 3D-consistent queries for each view.
4.  These rendered queries are softly injected back into the diffusion model to guide the generation, improving multi-view consistency.

This process is performed progressively and iteratively, interleaving consolidation steps with standard denoising steps. This allows the image features to evolve naturally while ensuring they do not drift too far apart before being re-consolidated.

## 3. Datasets Used / Presented
The method was evaluated on 7 object-centric multi-view datasets, most of which were collected by the authors. The datasets include:
*   **Person:** 350 images
*   **Spiderman:** 348 images
*   **Statue:** 291 images
*   **Alligator-toy:** 493 images
*   **Sofa:** 333 images
*   **Lamp:** 305 images
*   **Boot:** 281 images

These datasets were used to perform and evaluate geometric edits, such as changing a character's pose or modifying an object's shape.

## 4. Main Results
The proposed method demonstrated superior performance compared to three baseline techniques (IN2N-CN, CSD-CN, TokenFlow) in both visual fidelity and 3D consistency.
*   **Image Fidelity:** The method achieved the best (lowest) Kernel Inception Distance (KID) of **0.072** and Fréchet Inception Distance (FID) of **73**, indicating that its edits are more faithful to the original scene's appearance and have fewer artifacts.
*   **3D Consistency (User Study):** In a user study where participants ranked the quality and geometric alignment of 3D NeRFs reconstructed from the edited images, the proposed method was preferred most often. It achieved the best average rank of **1.90** (lower is better) and a win-rate of **50.83%**, significantly outperforming the next-best method (34.16%).

The authors conclude that their method achieves better multi-view consistency and higher fidelity, enabling the creation of NeRFs with fewer artifacts that are better aligned with the target geometry.

## 5. Ablation Studies
The authors performed ablation studies to validate the core components of their method:
1.  **Without Consolidation:** Editing images independently with MasaCtrl (the base editor) resulted in geometrically inconsistent outputs, such as objects being in different positions across views.
2.  **Without Soft-Injection:** Directly replacing the model's queries with the rendered QNeRF queries (instead of using soft guidance) made the images consistent but caused them to diverge significantly from the original appearance, leading to major artifacts like cut-off limbs.
3.  **Without Progressive Consolidation:** Training the QNeRF only once on queries from independently edited images, rather than iteratively, also produced more visual artifacts (e.g., a missing leg), showing that progressive consolidation is crucial for high-quality results.

## 6. Paper Figures
![Figure 10. Qualitative results of our method. Here we edit the images with a skeleton and show a sample of three different views for each example.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_10.jpg' | relative_url }})
![Figure 11. Qualitative results of our method. Here we edit the images with a loose depth map [ 4 ], and show a sample of three different views for each example.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_11.jpg' | relative_url }})
![Figure 2. Editing multi-view images of a boot, with a loose depth map [ 4 ]. We show a sample of three images from the set.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3. The first and third rows show images captured from different viewpoints. When these are individually edited using ControlNet [ 59 ] and MasaCtrl [ 8 ], inconsistencies arise. Note the shape of the lamp (top) or the distance of the foot from the wall (bottom). Images were edited using 2D controls projected from a shared 3D model (skeleton, box). The leftmost column shows controls corresponding to view 1.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. We simultaneously generate multi-view edited images with a diffusion model. To consolidate the images, along the denoising process we (1) extract self-attention queries from the network, (2) train a NeRF (termed QNeRF) on the extracted queries and render consolidated queries, and (3) softly inject the rendered queries back to the network for each view. We repeat these steps throughout the denoising process.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 6. In each multi-view denoising interval we have query-guided steps, followed by steps without guidance. In query-guided steps, we alter the noisy latent code with an objective of proximity between the self-attention queries generated by the latent code, and queries rendered from the QNeRF. At the last step of the interval, we extract the generated queries and use them to train the QNeRF that provides guidance for the next interval. Query guidance consolidates the geometry across the different views. In addition, we inject the keys and values of self-attention layers from the original images to preserve the appearance.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7. Our progressive denoising process is analogous to a zipper mechanism. Each step of a zipper relies on the closure of all preceding parts, and benefits from the fact that they got closer together. The dotted red curves (left) illustrate the queries generated along the diffusion process of two views. The zipper represents the QNeRF that consolidates the red dots, and projects them to form the orange dots (left) which sit along closer trajectories. After a few steps, we repeat this process with the orange and green curves (right), progressively consolidating the generated queries.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_7.jpg' | relative_url }})
![Figure 8. Ablation study results. Our full method creates more consistent images, while accurately preserving the original scene.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_8.jpg' | relative_url }})
![Input Input Target IN2N-CN CSD-CN TokenFlow Ours Control Image Control Figure 9. Qualitative comparison of our approach with baseline methods. Techniques relying on “dataset update”, such as IN2N-CN and CSD-CN, struggle to alter the geometry. This can be seen in the noisy depth of the statue’s right arm when using IN2N-CN, and the ghostly right arm of the statue with CSD-CN. TokenFlow struggles to preserve the appearance of the original image, and tends to produce noisy geometry, suggesting a lack of consistency between the edited frames. Our method preserves the appearance of the original images while changing the geometry consistently.]({{ '/images/02-2024/Consolidating_Attention_Features_for_Multi-view_Image_Editing/figure_9.jpg' | relative_url }})
