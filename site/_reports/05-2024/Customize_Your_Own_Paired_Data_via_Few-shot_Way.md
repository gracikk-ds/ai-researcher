---
title: Customize_Your_Own_Paired_Data_via_Few-shot_Way
layout: default
date: 2024-05-21
---
## Customize Your Own Paired Data via Few-shot Way
**Authors:**
- Jinshu Chenpapers: 2, 
- Qian He

**ArXiv URL:** http://arxiv.org/abs/2405.12490v1

**Citation Count:** 0

**Published Date:** 2024-05-21

![Figure 1. Providing only few source-target image pairs, users are allowed to efficiently customize their own image editing models through our framework. Without affecting irrelevant attributes, our proposed method can capture the desired effects precisely. Our model can handle various editing cases, whether the editing targets are commonly known concepts or completely newly defined by users.]({{ '/images/05-2024/Customize_Your_Own_Paired_Data_via_Few-shot_Way/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing image editing methods face a trade-off. Supervised methods produce high-quality results but require large, expensive-to-collect paired datasets, limiting their use for custom tasks. Unsupervised and text-guided methods leverage large pre-trained models but are restricted to the concepts within their training domains, often failing to create novel user-defined effects or perform precise edits without unwanted changes. The authors address this gap by developing a framework that allows users to create high-quality, customized image editing models using only a few (5-50) paired examples.

## 2. Key Ideas and Methodology
The core idea is a novel few-shot learning mechanism called "n-source-to-n-target" training. Instead of learning a direct mapping from a source image to a target image, the model learns the *transformation* between samples within the same domain. For any two source-target pairs `(x_i, y_i)` and `(x_j, y_j)`, the model is trained to predict the transformation from `y_i` to `y_j` given the transformation from `x_i` to `x_j`. This approach exponentially increases the number of learnable training instances from the small set of provided pairs, preventing overfitting.

The methodology is implemented using a diffusion model pipeline with two key modules:
1.  **`Mx` (Transformation Estimator):** Calculates the explicit spatial (optical flow) and color transformations between two source-domain images.
2.  **`My` (Diffusion Editor):** A diffusion model that takes a target-domain image and applies the transformation from `Mx` as a condition to generate the final edited result.

The framework uses a trainable VAE (not frozen) with skip connections and other technical improvements to generate high-quality, detailed images.

## 3. Datasets Used / Presented
The authors did not use standard large-scale benchmarks. Instead, they demonstrated their method's effectiveness on a variety of custom, few-shot paired datasets created for specific editing tasks. The number of pairs for each task was deliberately kept small, ranging from 5 to 50 pairs. Examples of tasks and dataset sizes include:
*   **Face Editing:** Blue eyes (5 pairs), Big smile (10 pairs), Old (25 pairs).
*   **Animal Editing:** Sleepy cats (5 pairs), Painting style dogs (25 pairs).
*   **Scene/Object Editing:** Scenery daytime transfer (50 pairs), Ancient style fonts (50 pairs).

## 4. Main Results
The primary result is that the proposed method can achieve performance comparable to fully supervised methods while using drastically less data. For instance, with only 20 training pairs, the proposed model achieved a Frechet Inception Distance (FID) of 0.0094. This is superior to an improved pix2pix baseline (`pix2pix*`) trained on approximately 10,000 pairs, which scored an FID of 0.0151. When the baseline was trained on the same 20 pairs, its performance was significantly worse (FID of 0.1882), demonstrating the proposed method's superior data efficiency and ability to avoid overfitting. Qualitatively, the model produces high-quality edits that are faithful to the user-defined effect while preserving irrelevant attributes.

## 5. Ablation Studies
The authors performed several ablation studies to validate their design choices:

*   **Data Pairing Mechanism:** Removing the core "n-source-to-n-target" mechanism and reverting to standard one-to-one pair training caused the model to overfit severely, with FID increasing from 0.0094 to 0.9635.
*   **Model Conditions:** Removing either of the two main conditions for the diffusion editor—the transformed source image `xj` or the transformation vector `[F, C]`—destabilized training and made it difficult for the model to converge, significantly degrading performance (FID increased to 0.5502 and 0.6938, respectively).
*   **Technical Improvements:** Removing skip connections, adaptive noise injection, or the frequency-domain loss each resulted in a noticeable drop in image quality, particularly a loss of fine details and high-frequency information. For example, removing skip connections increased FID from 0.0094 to 0.0256.

## 6. Paper Figures
![Figure 2. Instead of training the model on the paired samples themselves, we train the model on the directed transformations among samples from the same domain. In the figure we highlight the training objects in green to show the differences between ours and the existing method. In this way we expand the learnable space to an exponential extent approximately.]({{ '/images/05-2024/Customize_Your_Own_Paired_Data_via_Few-shot_Way/figure_2.jpg' | relative_url }})
![Figure 3. All modules of our framework are trained jointly and endto-end. During training, all samples mentioned in the illustration are selected from the whole training dataset, while x j is provided by users and will be transferred to get y j for the inference time.]({{ '/images/05-2024/Customize_Your_Own_Paired_Data_via_Few-shot_Way/figure_3.jpg' | relative_url }})
![Figure 4. Essentially, our model is trained to find certain manifold where the projections of f x and f y are equal. Horizontal flip is shown on the upper left as a simple example, and normal cases are shown on the lower right.]({{ '/images/05-2024/Customize_Your_Own_Paired_Data_via_Few-shot_Way/figure_4.jpg' | relative_url }})
![Figure 5. Here we show more experimental results of our method. The editing target and the amount of given training pairs are recorded on the top of each result unit, and the relative generated images are displayed below. More visual results are shown in our appendix.]({{ '/images/05-2024/Customize_Your_Own_Paired_Data_via_Few-shot_Way/figure_5.jpg' | relative_url }})
![Figure 6. Comparisons between existing works and our method. Part a) shows comparisons with paired-data methods, while part b) contains results comparing with few/zero-shot methods including methods editing in the latent space and methods relying on the multi-modal information. Note that for the latter methods, we will provide proper instructions which can describe the editing target.]({{ '/images/05-2024/Customize_Your_Own_Paired_Data_via_Few-shot_Way/figure_6.jpg' | relative_url }})
![Figure 7. The qualitative results of the ablation study. Without our “ n -source-ton -target” method, the model overfits easily. Both x j and [ F, C ] ease the difficulties of the training. The improvements we adopt help the model to generate more fine-grained results.]({{ '/images/05-2024/Customize_Your_Own_Paired_Data_via_Few-shot_Way/figure_7.jpg' | relative_url }})
