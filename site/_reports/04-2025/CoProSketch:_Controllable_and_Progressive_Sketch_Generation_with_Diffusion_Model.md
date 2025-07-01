---
title: CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model
layout: default
date: 2025-04-11
---
![Figure 1. Demonstrations of the proposed pipeline. Left : The proposed pipeline takes a text prompt and an expected layout, represented by a bounding box, as input and generates sketches progressively, from rough to detailed. If the results are unsatisfactory, the user can make timely edits during the rough stage at a low cost. Right : one application is layer-based composition, where the layers (i.e., instance masks) and the sketches are both the output from the proposed pipeline.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the gap between advanced generative models and the practical needs of artists, particularly in sketch creation. While sketches are fundamental to artistic workflows due to their intuitive editability, automatic sketch generation remains under-explored. Existing generative models for RGB images lack the precise control over layout and structure that artists require, and editing the final RGB output is often cumbersome. The paper aims to create a framework for sketch generation that is both highly controllable and progressive, allowing users to iteratively refine a sketch from a rough concept to a detailed drawing, integrating user feedback seamlessly into the process.

## 2. Key Ideas and Methodology
The core idea of the paper is to enable controllable and progressive sketch generation by representing sketches not as binary images, but as continuous Unsigned Distance Fields (UDFs). This representation is more suitable for diffusion models, which struggle with the sharp, sparse nature of binary sketch data.

The proposed framework, CoProSketch, operates in a multi-stage process:
1.  **Rough Sketch Generation:** A user provides a text prompt and a bounding box. A modified SDXL-based diffusion model, conditioned on the bounding box mask and a "rough stage" indicator, generates an initial rough UDF.
2.  **User Editing & Refinement:** The rough UDF is decoded into a sketch, which the user can manually edit.
3.  **Detailed Sketch Generation:** The edited sketch is re-encoded into a UDF. An instance mask is generated from this UDF, which, along with the original text prompt and a "detailed stage" indicator, is fed back into the same diffusion model to produce a refined, detailed UDF.
4.  **Final Output:** A lightweight decoder network (UDF2Sketch) converts the final UDF into a clean, high-quality sketch.

This progressive workflow leverages the inherent editability of sketches and provides fine-grained control over the final output.

## 3. Datasets Used / Presented
The authors curate a new, large-scale text-sketch paired dataset containing approximately 100,000 samples. This dataset was constructed to train the various modules of their pipeline.

*   **Source Datasets:** The data was aggregated from three existing datasets: COCO2017, the Anime Colorization dataset, and SOD-Data (a composite of several salient object detection datasets).
*   **Construction Process:** For each source image, the authors used Gemini AI to generate detailed text descriptions. They then applied a combination of salient object detection (UDASODUPL) and segmentation (SAM2) to extract object masks and bounding boxes. Detailed sketches were generated from the RGB images using the InformativeDrawing model.
*   **Final Dataset Content:** Each sample in the final dataset includes a text description, the original RGB image, an instance mask, a bounding box, an object contour, and a detailed sketch.

## 4. Main Results
The proposed method, CoProSketch, demonstrates superior performance over baseline methods in both quantitative metrics and user studies.

*   **Quantitative Metrics:** Compared to several text-to-image-to-sketch pipelines and the DiffSketcher model, CoProSketch achieved the highest scores in both aesthetic quality and semantic alignment. It obtained an Aesthetic Score (AES) of 4.256 and a CLIP Score of 0.245, outperforming all other configurations.
*   **User Study:** In a study with 33 volunteers, CoProSketch was overwhelmingly preferred for its positional control and semantic accuracy, receiving the highest voting rates of 72.1% and 64.2%, respectively. It also achieved a competitive aesthetic quality rating (37.6%), second only to a pipeline that used the ground-truth generation tool (InformativeDrawings).

The authors claim their method strikes an effective balance between robust layout control and high-quality sketch generation, making it a practical tool for creative applications.

## 5. Ablation Studies
The authors performed ablation studies on three key components of their pipeline to validate their design choices.

*   **UDF Representation:** When the model was trained directly on binary sketch images instead of UDFs, the quality of the generated sketches dropped significantly. The results featured large, undesirable color blocks, and the semantic consistency with the text prompt was reduced (CLIP score dropped from 0.245 to 0.219).
*   **UDF2Mask Module:** Removing the module that generates a clean instance mask for the detailed generation stage harmed positional control. Without it, the generated sketches were more likely to exceed the boundaries of the input bounding box.
*   **UDF2Sketch Module:** Replacing the learned UDF-to-sketch decoder with traditional methods like thresholding or marching squares resulted in visually inferior sketches. These methods produced fragmented lines and lacked the aesthetic appeal of the sketches generated by the trained network.

## 6. Paper Figures
![Figure 2. (a) : The proposed pipeline begins by taking a text prompt and a rough mask (derived from a bounding box) as input to generate a rough UDF representation. If users find the results unsatisfactory, they have the option to edit the rough result. The rough result, which is the sketch decoded from the UDF, is re-encoded back into the UDF after editing. The edited result is then converted into a instance mask, which is fed back into the same model, guided by a different stage indicator, to produce the refined output. (b) : Details of our modified U-Net: The conditional mask is concatenated with the noisy latent. The stage indicator is first converted into an embedding and then added to the time embedding. All other components remain unchanged.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_2.jpg' | relative_url }})
![Figure 3. Details of UDF representation. Given a binarized sketch, we compute its UDF representation and transform it by f ( u ) to adapt it for training networks.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_3.jpg' | relative_url }})
![Figure 4. Dataset construction process.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_4.jpg' | relative_url }})
![Figure 5. Dataset sample. (a) : Rough sketches. (b) : Detailed sketches.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_5.jpg' | relative_url }})
![Figure 6. Comparison with baselines. (a c) represent the box mask input, our results and diffsketcher. (d)(h) represent the RGB images generated by SDXL + ControlNet and SD15+HiCo, and (e g)(i k) represent the sketches generated by canny, InformativeDrawings and Photo-Sketching.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_6.jpg' | relative_url }})
![Figure 7. Ablation study. (a c): bounding box, full pipeline UDF and sketch. (d): Without UDF representation. (e): Without UDF2Mask. (f): Without UDF2Sketch, use marching squares to extract sketch from UDF. (g): Without UDF2Sketch, use thresholding to extract sketch from UDF.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_7.jpg' | relative_url }})
![Figure 8. Comparison between editing in text-to-RGB pipeline(baseline) and text-rough-detailed-RGB pipeline(ours). Our pipeline shows better editing performance.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_8.jpg' | relative_url }})
![Figure 9. Application of composing multiple objects into one sketch.]({{ '/images/04-2025/CoProSketch:_Controllable_and_Progressive_Sketch_Generation_with_Diffusion_Model/figure_9.jpg' | relative_url }})
