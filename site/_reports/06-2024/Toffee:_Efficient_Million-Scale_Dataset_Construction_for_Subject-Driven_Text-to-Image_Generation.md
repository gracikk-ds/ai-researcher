---
title: Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation
layout: default
date: 2024-06-13
---
![Figure 1: Subject-driven editing and generation examples from our model, which is trained on our proposed dataset and does not require any fine-tuning at test-time. Editing masks are also presented.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the prohibitive cost of creating large-scale datasets for subject-driven text-to-image generation. Existing high-performing methods, like SuTI and CAFE, rely on synthetic datasets where generating each training pair requires fine-tuning a model on a specific subject. This "per-subject fine-tuning" approach makes dataset construction computationally expensive (tens of thousands of GPU hours), creating a significant barrier for most researchers. The paper aims to bridge this gap by introducing an efficient framework for dataset construction that does not require any subject-level fine-tuning.

## 2. Key Ideas and Methodology
The core idea is to replace per-subject fine-tuning with a one-time pre-training of two specialized generative models, making the dataset construction cost constant (O(1)) regardless of the number of subjects. The proposed method, named **Toffee**, works as follows:

1.  **Initial Generation:** A base diffusion model generates a text-aligned but low-fidelity image of the subject.
2.  **Refiner:** A custom-trained diffusion model refines the subject's identity in the generated image. It uses DINO patch embeddings from the original subject image to identify and enhance corresponding patches in the new image, preserving fine-grained details without losing text alignment.
3.  **View Generator:** A second custom-trained model generates new views of the subject to add pose and viewpoint diversity to the dataset.

Using this pipeline, the authors create a large-scale dataset and train a unified model called **ToffeeNet**. ToffeeNet can perform both subject-driven generation and editing in a zero-shot manner by conditioning on the subject image (via DINO embeddings), a text prompt, and optional inputs like an editing mask and a depth map for pose control.

## 3. Datasets Used / Presented
-   **Toffee-5M (Presented):** The primary contribution is a new large-scale dataset for subject-driven generation and editing. It contains **4.8 million image pairs**, text prompts, and **1.6 million associated editing masks**. The dataset is 5 times larger than previous works and is categorized by changes like style, background, color, and texture.
-   **MVImageNet (Used):** This multi-view image dataset was used to train the *View Generator* component of the data creation pipeline.
-   **DreamBench (Used):** A standard benchmark dataset with 30 subjects, used for quantitative evaluation and comparison of the final ToffeeNet model against other methods.

## 4. Main Results
The primary result is the efficiency of the dataset construction framework. The Toffee pipeline requires less than 3,000 GPU hours, a drastic reduction compared to the estimated 83,000 TPU hours for SuTI or 10,000 GPU hours for CAFE to create a 1-million-subject dataset.

The model trained on this dataset, **ToffeeNet**, achieves state-of-the-art performance among tuning-free methods on the DreamBench benchmark. It scores a DINO similarity of **0.728** (identity preservation) and a CLIP-T score of **0.306** (text alignment), demonstrating that it effectively preserves subject identity while accurately following text prompts. The author-claimed impact is that this efficient framework makes high-quality, large-scale dataset creation for subject-driven generation accessible to the broader research community.

## 5. Ablation Studies
The authors conducted several ablation studies to validate their design choices:
-   **Model Variants:** Models trained only on editing data (`ToffeeNet-E`) or generation data (`ToffeeNet-G`) were compared to the unified `ToffeeNet`. The unified model performed competitively on both tasks, showing the benefit of joint training on a diverse dataset.
-   **Training with Reconstruction:** Forcing the model to perform a reconstruction task (input = target) with a certain probability `p` improved subject similarity (Seg-DINO score increased from 0.803 to 0.818) but at the cost of reduced text alignment (CLIP-T score decreased from 0.306 to 0.286).
-   **Subject Pre-processing:** Using the whole image versus a segmented subject as input to the DINO encoder showed no significant performance difference, simplifying the pipeline.
-   **DINO Embedding Strength:** At inference, scaling the influence of the DINO embedding (λ) allowed for a trade-off: higher λ values preserved subject identity better, while lower values adhered more closely to the text prompt (e.g., making an object more "transparent").

## 6. Paper Figures
![Figure 10: Examples of image generation with ToffeeNet.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_10.jpg' | relative_url }})
![Figure 11: Examples of image editing with ToffeeNet. We can control editing regions by feeding different masks into the model. The identity is well-preserved when the subject is being edited.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_11.jpg' | relative_url }})
![Figure 2: Comparison of resulting dataset size and construction cost.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_2.jpg' | relative_url }})
![Figure 3: The proposed dataset construction framework.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_3.jpg' | relative_url }})
![Figure 4: Illustration of training and inference with our Refiner model.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_4.jpg' | relative_url }})
![Figure 5: Our Refiner can refine the subject details, without the loss of text-alignment.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_5.jpg' | relative_url }})
![Figure 6: Taxonomy of our Toffee-5M.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_6.jpg' | relative_url }})
![Figure 7: Examples of the proposed dataset, including image editing (left) and generation (right) samples. Text prompts are not shown here due to the limited space.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_7.jpg' | relative_url }})
![Figure 8: Illustration of training single ToffeeNet model with both editing and generation pairs.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_8.jpg' | relative_url }})
![Figure 9: We have the flexibility of controlling pose and view change by inputting a depth image. Some interesting examples are provided in Figure 9 for better understanding, from which we can see that the generation follows the provided depth condition.]({{ '/images/06-2024/Toffee:_Efficient_Million-Scale_Dataset_Construction_for_Subject-Driven_Text-to-Image_Generation/figure_9.jpg' | relative_url }})
