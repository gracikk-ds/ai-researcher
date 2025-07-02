---
title: Delta_Denoising_Score
layout: default
date: 2023-04-14
---
## Delta Denoising Score
**Authors:**
- Amir Hertz, h-index: 15, papers: 22, citations: 4599
- Daniel Cohen-Or

**ArXiv URL:** http://arxiv.org/abs/2304.07090v1

**Citation Count:** None

**Published Date:** 2023-04-14

![Figure 1: Score Distillation Sampling (SDS) vs. Delta Denoising Score (DDS). Top: SDS mechanism optimizes a given image by querying the denoising model on the noisy version of the image and a target text prompt. The resulting image can often be blurry and unfaithful to the target prompt. Bottom: DDS queries an additional reference branch with a matched text-prompt, and generates delta scores that represent the difference between the outputs of the two queries. DDS provides cleaner gradient directions that modify the edited portions of the optimized image, while leaving the other parts unchanged.]({{ '/images/04-2023/Delta_Denoising_Score/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a key limitation in text-based image editing using Score Distillation Sampling (SDS), a technique that leverages large-scale diffusion models. When used for editing, the standard SDS method often produces blurry outputs and makes undesired changes to parts of the image that should remain untouched. The practical problem is the lack of a mechanism to guide the editing process to make minimal, high-quality modifications that are faithful to both the source image and the target text prompt, without introducing noise or artifacts.

## 2. Key Ideas and Methodology
The core idea is that the standard SDS gradient can be decomposed into two parts: a desired, text-aligned component and an undesired, noisy component that causes blurring. The paper introduces **Delta Denoising Score (DDS)** to isolate and remove this noisy component.

The methodology involves a dual-branch approach:
1.  **Target Branch:** Calculates the standard SDS score between the image being optimized and the *target* text prompt (e.g., "a squirrel snowboarding").
2.  **Reference Branch:** Calculates an SDS score between the same image and a *reference* text prompt that describes the original image (e.g., "a panda snowboarding").

The key assumption is that the gradient from the reference branch primarily represents the undesired noisy component. By subtracting the reference gradient from the target gradient, DDS produces a "cleaner" or "distilled" gradient that only reflects the intended edit. This DDS loss can then be used to directly optimize an image (zero-shot editing) or to train a zero-shot image-to-image translation network without requiring paired training data.

## 3. Datasets Used / Presented
*   **InstructPix2Pix Dataset:** A subset of 1000 source/target prompt pairs was used for quantitative evaluation of zero-shot editing methods. Synthetic image pairs from this dataset were also used to validate the DDS correlation assumption.
*   **COCO Dataset:** Used to generate synthetic images for evaluating the properties of SDS gradients. Real images from COCO were also used to test the trained image-to-image translation models.
*   **ILSVRC (ImageNet) & FFHQ:** Real images from these datasets were used to evaluate the performance of the trained image-to-image translation networks on diverse subjects (e.g., cats, people).
*   **Unsplash Dataset:** Used to provide qualitative examples of zero-shot editing on high-quality real-world images.

## 4. Main Results
The paper demonstrates that DDS significantly outperforms existing methods in both direct optimization and trained models.
*   **Zero-Shot Editing:** In quantitative comparisons against methods like SDEdit and Plug-and-Play (PnP), DDS achieves a better trade-off between fidelity to the source image and alignment with the target prompt. It produces results with much lower perceptual distance (LPIPS) to the original image while achieving comparable or higher text-alignment (CLIP score).
*   **Image-to-Image Translation:** A network trained with DDS was compared to InstructPix2Pix. The DDS-trained model was substantially better at preserving the structure of the input image, achieving an LPIPS score of **0.104** versus **0.322** for InstructPix2Pix, while also achieving a higher CLIP score (**0.225** vs. **0.219**).

The authors' main takeaway is that DDS provides cleaner, more stable gradients for text-guided image editing, enabling high-quality modifications that preserve unedited regions.

## 5. Ablation Studies
*   **DDS vs. Standard SDS:** An image translation network was trained using standard SDS instead of DDS. The results were qualitatively worse, struggling to preserve high-frequency details from the input image (e.g., the texture of a hat was lost).
*   **Classifier-Free Guidance (CFG) Warmup:** The authors trained a network without gradually increasing the CFG scale during training. This resulted in mode collapse, where the network learned to produce a similar-looking output (e.g., the same lion in the same pose) regardless of the input image.
*   **Optimizer Selection:** For zero-shot editing, SGD was compared to the Adam optimizer. SGD was found to produce higher-quality results with fewer artifacts, as Adam's adaptive gradient normalization sometimes amplified noise and caused uniform changes across the image.
*   **Regularized SDS as a Baseline:** The authors tested an alternative approach of using standard SDS with an L2 loss to enforce similarity to the input. This method failed to prevent the blurring effect of SDS and created a poor trade-off between text fidelity and image preservation.

## 6. Paper Figures
![Figure 10: Zero shot image editing qualitative comparison. We compare our approach to SDEdit [ 21 ] Plug-andPlay (PnP) [ 41 ] and prompt-to-prompt [ 12 ]. Our method showcases its ability to better apply both structural and color changes described in the target text prompt while simultaneously preserving high ﬁdelity to the input image.]({{ '/images/04-2023/Delta_Denoising_Score/figure_10.jpg' | relative_url }})
![Figure 11: Image-to-Image translation comparison. Our multi-task network was trained to translate cats to different animals (lion, dog, squirrel) using DDS. It was trained on synthetic cat photos and evaluated on a subset of real images from the COCO and Imagenet datasets. Our results (second row) better preserve the structure of the cat in the input image as well as its background.]({{ '/images/04-2023/Delta_Denoising_Score/figure_11.jpg' | relative_url }})
![Figure 12: Limitations. Biases of the diffusion model or limitations in language understanding affect the DDS optimization. Top: we would like to change the color of the curtains in the bedroom, but the color of the pillows is also changed. Bottom: replacing the dog’s reﬂection with a shadow also causes changes in the lighting, weather and background details.]({{ '/images/04-2023/Delta_Denoising_Score/figure_12.jpg' | relative_url }})
![Figure 2: Sampling text-to-image diffusion models. Generation via SDS optimization starting from random noises (left) vs. conventional diffusion-based image generation (right). Both samples are generated with respect to a given text prompt (top). Generating images based on SDS only leads to less diverse results and mode collapse where the main subject in the text appears in front of a blurry background.]({{ '/images/04-2023/Delta_Denoising_Score/figure_2.jpg' | relative_url }})
![Figure 3: Bias in SDS optimization. Left column: an image generated by the prompt “Panda snowboarding”. Top rows show the difference between SDS to DDS optimization when changing the animal in the prompt (“Panda” to “Squirrel”). Bottom row shows SDS optimization applied using the original prompt. Even in this case, the image becomes blurry.]({{ '/images/04-2023/Delta_Denoising_Score/figure_3.jpg' | relative_url }})
![Figure 4: DDS gradients. Top: Visualization of 4 steps in the DDS optimization process, where an image of a “Flamingo rollerskating” (left) gradually transforms into a “Stork rollerskating” (right). Bottom: By subtracting the SDS gradients of the reference image and the source prompt (left) from the SDS gradients of the edited image and the target prompt (middle), we obtain cleaner DDS gradients (right).]({{ '/images/04-2023/Delta_Denoising_Score/figure_4.jpg' | relative_url }})
![Figure 5: DDS optimization results using different values of the classiﬁer-free guidance scale ω . On one hand, using small values of ω leads to slow convergence and low ﬁdelity to the text prompt. On the other hand, using large values of ω results in low ﬁdelity to the input image.]({{ '/images/04-2023/Delta_Denoising_Score/figure_5.jpg' | relative_url }})
![Figure 6: Unsupervised training for multi task image-toimage translation network. Given an input image ˆz (left) and a sampled task embedding (top), our network is trained using the Delta Denoising Score (DDS) and corresponding text embeddings (bottom) that describe the input image and the desired edited image result z . During inference, our network can then translate arbitrary real images based on the speciﬁed task, within a single feedforward pass.]({{ '/images/04-2023/Delta_Denoising_Score/figure_6.jpg' | relative_url }})
![Figure 7: Ablation study. We train a cat-to-lion image translation network under various settings. The ﬁrst and second columns show the input and output results of our full method, respectively. The third row shows the results when training without CFG warmup, and the last column shows the results when training with SDS instead of DDS.]({{ '/images/04-2023/Delta_Denoising_Score/figure_7.jpg' | relative_url }})
