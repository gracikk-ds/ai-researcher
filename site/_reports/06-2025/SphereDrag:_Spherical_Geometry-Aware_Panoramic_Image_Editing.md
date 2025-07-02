---
title: SphereDrag:_Spherical_Geometry-Aware_Panoramic_Image_Editing
layout: default
date: 2025-06-13
---
## SphereDrag: Spherical Geometry-Aware Panoramic Image Editing
**Authors:**
- Zhiao Feng
- Xi Li

**ArXiv URL:** http://arxiv.org/abs/2506.11863v1

**Citation Count:** None

**Published Date:** 2025-06-13

![Figure 1: Illustration of challenges in panoramic image editing. (Upper right) The panoramic image may divide movement trajectory into two parts, located near the left and right boundaries, respectively. (Middle right) Straight lines in the panoramic image do not correspond to great-circle paths on the sphere, leading to trajectory deviations. (Lower right) The same region in the panoramic image corresponds to unequal solid angles at different latitudes, causing non-uniform tracking across the sphere.]({{ '/images/06-2025/SphereDrag:_Spherical_Geometry-Aware_Panoramic_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenges of interactive, point-based editing for panoramic images. Unlike standard planar images, panoramic images possess a unique spherical geometry that causes three key problems when using existing editing methods:
1.  **Boundary Discontinuity:** Editing trajectories that cross the image's left and right edges become split and distorted.
2.  **Trajectory Deformation:** A straight-line drag in the 2D image plane does not correspond to the shortest path (a great circle) on the sphere, leading to inaccurate object movement.
3.  **Uneven Pixel Density:** The equirectangular projection distorts pixels, especially near the poles, causing inconsistent tracking and editing effects across different latitudes.

## 2. Key Ideas and Methodology
The paper proposes **SphereDrag**, a framework that incorporates spherical geometry knowledge into a diffusion-based point-editing pipeline to solve the aforementioned problems. The core methodology consists of three components:

1.  **Adaptive Reprojection (AR):** To handle boundary discontinuity, the framework first rotates the panoramic sphere to place the midpoint of the user's drag path at the center of the 2D image. This ensures the entire editing operation occurs in a continuous region, avoiding seam-crossing artifacts.
2.  **Great-Circle Trajectory Adjustment (GCTA):** Instead of calculating motion as a straight line in the 2D plane, GCTA computes the movement vector along the great-circle path on the sphere between the current handle point and the target point. This ensures the edited object follows a geometrically correct trajectory.
3.  **Spherical Search Region Tracking (SSRT):** To counteract projection distortion, the point-tracking search window is adaptively scaled. The vertical size of the search region is adjusted by a factor of `1/cos(φ)` (where φ is the latitude), ensuring the search area corresponds to a consistent physical size on the sphere, improving tracking accuracy at high latitudes.

## 3. Datasets Used / Presented
The authors introduce **PanoBench**, a new benchmark specifically for evaluating panoramic image editing.
*   **Content:** It consists of 81 high-resolution (1024×512) panoramic images depicting diverse scenes (e.g., interiors, landscapes).
*   **Annotations:** Each image is accompanied by masks, handle points, and target points designed for drag-based editing tasks.
*   **Usage:** It is used to provide a standardized framework for quantitatively and qualitatively comparing SphereDrag against other state-of-the-art editing methods.

## 4. Main Results
SphereDrag demonstrates significant improvements over existing methods like DragDiffusion, DragNoise, and StableDrag.
*   **Quantitative:** When evaluated on perspective views with a 30° Field of View (FOV), SphereDrag achieves an Image Fidelity (IF) score of 0.7364, outperforming the baseline's 0.6666. This represents a 10.5% relative improvement. It also achieves lower (better) FID and sFID scores across all tested FOVs (30°, 60°, 90°), indicating superior image quality and geometric consistency.
*   **Author-claimed impact:** The results show that explicitly modeling spherical geometry is crucial for high-quality panoramic image editing, and SphereDrag provides an effective framework for achieving accurate and controllable results.

## 5. Ablation Studies
The authors conducted ablation studies to validate the contribution of each proposed component (AR, GCTA, and SSRT), using the IF metric for evaluation.
*   **Adaptive Reprojection (AR):** Adding only AR to the baseline model improved performance significantly by resolving boundary artifacts. For example, at 30° FOV, IF increased from 0.6666 to 0.7060.
*   **Great-Circle Trajectory Adjustment (GCTA):** Adding GCTA on top of AR provided a further, albeit smaller, improvement by ensuring correct motion paths (IF increased to 0.7081 at 30° FOV).
*   **Spherical Search Region Tracking (SSRT):** Incorporating all three components (AR + GCTA + SSRT) yielded the best performance across all FOVs, demonstrating that each module contributes effectively to the final result (IF reached 0.7364 at 30° FOV).

## 6. Paper Figures
![Figure 2: Classic point-interactive image editing pipeline]({{ '/images/06-2025/SphereDrag:_Spherical_Geometry-Aware_Panoramic_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Overview of SphereDrag. Using DragDiffusion as our baseline, we introduce our three parts: adaptive reprojection (AR), great-circle trajectory adjustment (GCTA), and spherical search region tracking (SSRT). AR: It applies spherical rotation to transform input panoramic images into a suitable representation. GCTA: It handles the points P tar , P k , and P han using the great-circle distance d gc in a spherical manner. The underlying planar feature maps visualize the corresponding trajectory. SSRT: It highlights the current (blue) and future (red) search regions, which have equal sizes on the sphere. However, their projected areas differ on the feature maps due to spherical distortion.]({{ '/images/06-2025/SphereDrag:_Spherical_Geometry-Aware_Panoramic_Image_Editing/figure_3.jpg' | relative_url }})
