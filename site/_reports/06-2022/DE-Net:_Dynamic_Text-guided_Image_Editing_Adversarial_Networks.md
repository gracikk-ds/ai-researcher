---
title: DE-Net:_Dynamic_Text-guided_Image_Editing_Adversarial_Networks
layout: default
date: 2022-06-02
---
## DE-Net: Dynamic Text-guided Image Editing Adversarial Networks
Authors:
- Ming Tao
- Qi Tian

ArXiv URL: http://arxiv.org/abs/2206.01160v2

Citation Count: 15

Published Date: 2022-06-02

![Figure 1. Beneﬁting from dynamic editing design, our DE-Net can deal with various editing tasks (e.g., color changing, content editing). Furthermore, the text-adaptive convolution in DCBlock enables more accurate manipulations.]({{ '/images/06-2022/DE-Net:_Dynamic_Text-guided_Image_Editing_Adversarial_Networks/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current text-guided image editing models face two primary limitations. First, they apply fixed manipulation modules for all types of edits (e.g., color, texture, content changes), which often results in either over-editing or insufficient editing because different tasks require different manipulation strategies. Second, these models struggle to clearly distinguish between image regions that are relevant to the text description and those that are not, leading to inaccurate edits that incorrectly alter background or other preserved content.

## 2. Key Ideas and Methodology
The paper proposes DE-Net, a Dynamic text-guided Image Editing adversarial Network, to address these issues. The core idea is to create an adaptive editing framework that can dynamically compose suitable editing processes and precisely locate target regions.

The methodology is centered around three novel components integrated into a GAN architecture:
1.  **Composition Predictor (Comp-Pred):** This module analyzes the source image and target text to predict composition weights.
2.  **Dynamic Editing Block (DEBlock):** This block uses the weights from the Comp-Pred to dynamically combine two types of manipulations: a channel-wise affine transformation (for style/color edits) and a spatial-wise affine transformation (for content/shape edits). This allows the model to adapt its editing strategy for each specific input pair.
3.  **Dynamic text-adaptive Convolution Block (DCBlock):** To improve editing precision, this block uses text-conditioned dynamic convolutions that act like a query mechanism. It learns to attend to text-relevant image regions for editing while ignoring text-irrelevant parts. A semantic decoder provides this block with rich global-local features, enhancing its localization accuracy.

## 3. Datasets Used / Presented
The experiments were conducted on two standard public datasets:
*   **CUB bird:** Contains 11,788 images of 200 bird species, with 10 text descriptions per image. It is used to evaluate performance on fine-grained object manipulation.
*   **COCO:** A large-scale dataset with 80k training and 40k testing images of complex scenes, with 5 descriptions per image. It is used to test the model's ability to handle diverse and challenging editing tasks.

## 4. Main Results
DE-Net significantly outperformed existing state-of-the-art models (ManiGAN, Lightweight GAN, ManiTrans) across all evaluation metrics on both datasets.
*   **Quantitative:** On the COCO dataset, DE-Net achieved the highest Inception Score (25.81), CLIP-score (0.192), and Manipulation Precision (0.189), while also recording the lowest L2-error (0.015), indicating superior image quality, text-image alignment, and preservation of irrelevant content.
*   **Author-claimed impact:** The authors state that DE-Net can manipulate source images more correctly and accurately by adaptively composing editing modules and distinguishing between text-required and text-irrelevant parts, enabling it to handle a wider variety of editing tasks effectively.

## 5. Ablation Studies
A series of ablation studies on the COCO dataset validated the contribution of each key component of DE-Net:
*   **Effect of DEBlock:** Removing the full Dynamic Editing Block and using only fixed spatial or channel-wise editing resulted in significantly lower performance, confirming the benefit of the dynamic composition strategy.
*   **Effect of Comp-Pred:** Removing the Composition Predictor caused a notable performance drop, demonstrating its crucial role in generating the adaptive weights for the DEBlock.
*   **Effect of DCBlock:** Replacing the Dynamic text-adaptive Convolution Block with a standard convolution layer decreased manipulation accuracy, highlighting the importance of text-adaptive kernels for precise editing.
*   **Effect of Semantic Decoder:** Removing the Semantic Decoder, which feeds rich contextual features to the DCBlock, also degraded performance, proving that providing global-local semantic information is vital for accurate manipulation.

## 6. Paper Figures
![Figure 2. The architecture of the proposed DE-Net. The DE-Net comprises a source image encoder, a target image decoder, a semantic decoder, a Composition Predictor (Comp-Pred), and a pretrained text encoder [ 31 ]. The DEBlock and DCBlock are introduced in the target image decoder to enable effective and accurate manipulations, respectively.]({{ '/images/06-2022/DE-Net:_Dynamic_Text-guided_Image_Editing_Adversarial_Networks/figure_2.jpg' | relative_url }})
![Figure 3. Illustration of the proposed Comp-Pred and DCBlock. (a) The Comp-Pred predicts the combination weights for DEBlock. (b) The DEBlock composes suitable editing processes for each input pair according to the combined weights of C-Afﬁne and S-Afﬁne.]({{ '/images/06-2022/DE-Net:_Dynamic_Text-guided_Image_Editing_Adversarial_Networks/figure_3.jpg' | relative_url }})
![Figure 4. Illustration of the DCBlock. The text-attended features are predicted by the text-conditioned convolution layer.]({{ '/images/06-2022/DE-Net:_Dynamic_Text-guided_Image_Editing_Adversarial_Networks/figure_4.jpg' | relative_url }})
![Figure 5. Qualitative comparison between different methods on the test set of CUB and COCO.]({{ '/images/06-2022/DE-Net:_Dynamic_Text-guided_Image_Editing_Adversarial_Networks/figure_5.jpg' | relative_url }})
![Figure 6. Visualization of the queried results by different textadaptive convolution kernels.]({{ '/images/06-2022/DE-Net:_Dynamic_Text-guided_Image_Editing_Adversarial_Networks/figure_6.jpg' | relative_url }})
