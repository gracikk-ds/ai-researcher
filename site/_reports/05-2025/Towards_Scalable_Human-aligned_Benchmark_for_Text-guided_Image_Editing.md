---
title: Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing
layout: default
date: 2025-05-01
---
![Figure 1. An example highlighting the importance of consistency in image editing. (a) Original image (b) Edited images for a prompt “Make her smile”. The left result is more consistent with the input than the right one, better preserving her identity.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the critical lack of a standardized, objective, and scalable evaluation methodology for text-guided image editing models. The subjective nature of the task, where multiple "correct" edited outputs can exist for a single instruction, makes simple pixel-level or ground-truth comparisons ineffective. Consequently, researchers have relied on small-scale, non-reproducible manual user studies, which hinders robust and consistent progress in the field. The paper aims to fill this gap by creating an automated benchmark that can comprehensively assess model performance in a way that aligns with human perception.

## 2. Key Ideas and Methodology
The core contribution is **HATIE (Human-Aligned benchmark for Text-guided Image Editing)**, a framework for automated and comprehensive evaluation.

-   **Core Principle**: A good edit must be evaluated on multiple facets: fidelity to the instruction, consistency of unedited parts, and overall image quality. HATIE formalizes this by breaking down evaluation into five criteria: **Image Quality (IQ)**, **Object Fidelity (OF)**, **Background Fidelity (BF)**, **Object Consistency (OC)**, and **Background Consistency (BC)**.
-   **High-level Approach**:
    1.  **Dataset & Query Curation**: A large-scale dataset with diverse images and editing queries is constructed. Queries cover a wide range of tasks like object addition/replacement, attribute change, and style transfer.
    2.  **Automated Metric Pipeline**: An instance segmentation model is used to isolate target objects from the background. A suite of established metrics (e.g., CLIP for semantic similarity, LPIPS/DINO for perceptual similarity, FID for quality) are then applied to the relevant image regions to calculate scores for the five criteria.
    3.  **Human Alignment**: The authors conduct a large-scale user study to gather human preferences on edited images. The weights used to combine the individual metrics into the final five scores (and a single "Total Score") are optimized to maximize the correlation with these human judgments, ensuring the benchmark's evaluations are human-aligned.

## 3. Datasets Used / Presented
-   **Base Dataset**: The **GQA dataset** was used as a starting point due to its rich annotations of objects, attributes, and relationships, which is crucial for generating feasible and context-aware editing queries.
-   **HATIE Benchmark (Presented)**: The authors present a new, curated benchmark derived from GQA. It contains:
    -   **18,226 images** with **19,933 editable objects** across 76 classes.
    -   **49,840 editing queries** covering 7 distinct edit types, automatically generated using templates and LLMs. The queries are available in both description-based (e.g., "a photo of a red car") and instruction-based (e.g., "change the car to red") formats to support different model types.

## 4. Main Results
-   **Strong Human Alignment**: HATIE's evaluation scores showed a very strong Pearson correlation (r > 0.8) with human judgments on a held-out test set. This significantly outperforms conventional single metrics like raw CLIP alignment (r = -0.34) or FID (r = 0.51), proving the effectiveness of its multi-faceted, calibrated approach.
-   **Comprehensive Model Benchmarking**: The paper provides benchmark results for 9 state-of-the-art models. Among description-based models, **Prompt-to-Prompt (P2P)** was the best all-around performer. For instruction-based models, **MagicBrush** achieved the highest total score.
-   **Author-claimed Impact**: HATIE enables robust, reproducible, and nuanced evaluation of image editing models, revealing specific strengths and weaknesses (e.g., fidelity vs. consistency trade-offs) that were previously difficult to quantify, thereby paving the way for more guided progress in the field.

## 5. Ablation Studies
-   **Varied Edit Intensity**: The authors tested models by varying hyperparameters that control edit strength (e.g., guidance scale). HATIE's metrics successfully captured the expected trade-off: as edit intensity increased, fidelity scores improved while consistency scores degraded. The final "Total Score" correctly identified an optimal balance point, demonstrating the benchmark's sensitivity and utility for hyperparameter tuning.
-   **Metric Combination vs. Single Metrics**: The study demonstrated that the full HATIE framework, which combines multiple metrics with human-calibrated weights, correlates far better with user preferences (r > 0.8) than any of its constituent metrics used in isolation. For instance, LPIPS alone had a correlation of r=0.55, and detection rate had r=0.43. This result validates the necessity of the paper's complex, multi-faceted evaluation pipeline over simpler, conventional metrics.

## 6. Paper Figures
![Figure 2. Overview of our HATIE Benchmark. HATIE consists of an image and query dataset for editing, along with an automated evaluation pipeline for assessing editing performance. We curate a large-scale comprehensive dataset with images and corresponding editing queries, on which a model would perform text-guided image editing. Then, HATIE evaluates the edited images from 5 different aspects: Object Fidelity, Background Fidelity, Object Consistency, Background Consistency, and Image Quality . Finally, these scores are aggregated by a weight fitted to human feedback through our user study, producing the final Total Score.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3. Object Class Distribution in Our Dataset. HATIE evaluates fairly by providing evenly distributed dataset.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Query Set Distribution. (a) Distribution of edit types in our query set, (b) Distribution of the object classes designated as the target in object-centric queries.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5. Evaluation Workflow Specific to Each Editing Task. See Appendix C.1 for more details.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Aggregated HATIE scores with Varied Editing Intensity for Prompt-to-Prompt. Larger τ means a weaker edit.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7. Demonstration of Our Evaluation Metrics for sample images for each criteria. Tested model is InstructPix2Pix with s T ∈{ 2 . 5 , 5 . 0 , 7 . 5 , 10 . 0 , 12 . 5 } . Higher s T means stronger edit.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_7.jpg' | relative_url }})
![Figure 8. Relation between winning rates by users and HATIE, measured on the user study test set. The least square linear fit (red line) and Pearson’s correlation coefficient ( r ) are reported. The cross mark in object fidelity figure exhibits an outlier which has been excluded from correlation calculation.]({{ '/images/05-2025/Towards_Scalable_Human-aligned_Benchmark_for_Text-guided_Image_Editing/figure_8.jpg' | relative_url }})
