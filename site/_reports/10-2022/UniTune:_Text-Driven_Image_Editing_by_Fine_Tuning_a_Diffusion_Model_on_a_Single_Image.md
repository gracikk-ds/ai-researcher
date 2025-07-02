---
title: UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image
layout: default
date: 2022-10-17
---
## UniTune: Text-Driven Image Editing by Fine Tuning a Diffusion Model on a Single Image
**Authors:**
- Dani Valevski, h-index: 6, papers: 6, citations: 516
- Yaniv Leviathan, h-index: 8, papers: 10, citations: 1268

**ArXiv URL:** http://arxiv.org/abs/2210.09477v4

**Citation Count:** None

**Published Date:** 2022-10-17

![Fig. 1. UniTune edits preserving visual and semantic fidelity to the user supplied image.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of existing text-driven image editing methods. These methods often require user-provided masks, struggle to perform edits that involve significant visual changes (e.g., altering an object's pose or style), and fail to preserve important semantic and visual details from the original image. The paper aims to create a more powerful and flexible editing tool that works on arbitrary images and can perform a wide range of expressive edits with high fidelity, without needing additional inputs like masks.

## 2. Key Ideas and Methodology
- **Core hypothesis or principle introduced:** The central idea is that a large, pre-trained text-to-image diffusion model can be repurposed for high-fidelity editing of a *specific* image by fine-tuning it on that single image. This process biases the model's output distribution towards the input image without causing catastrophic forgetting of its vast, pre-existing knowledge.

- **High-level approach (UniTune):** The method consists of two stages:
    1.  **Fine-tuning:** The diffusion model is fine-tuned for a small number of steps (e.g., 64-128) on the user's input image, which is paired with a unique, rare text identifier. This creates a specialized model checkpoint for that image.
    2.  **Modified Sampling:** To perform an edit, the fine-tuned model is used with a new text prompt. The sampling process is modified to balance fidelity and expressiveness by (a) using a high weight for Classifier-Free Guidance (CFG) to enforce the edit, and (b) initializing the diffusion process with a noised version of the original image to preserve its structure and content.

- **Key assumptions or theoretical foundations:** The method relies on the robustness of large diffusion models to limited fine-tuning. It assumes that the model's learned semantic space is rich enough that a slight bias towards one image still allows for meaningful, guided manipulation through text prompts and CFG.

## 3. Datasets Used / Presented
The authors did not use a standard benchmark. For quantitative evaluation against the SDEdit baseline, they created a custom dataset of 93 pairs, each consisting of a base image and a textual edit prompt.
- **Domain:** The images cover diverse categories including animals, people, objects, food, and scenery.
- **Usage:** The dataset was designed so that approximately half of the edits required significant pixel-level changes (termed "unaligned" edits, e.g., moving objects or changing style), while the other half required smaller, localized changes ("aligned" edits). This was used for a human preference study.

## 4. Main Results
- **Main quantitative insights and metrics:** In a human preference study comparing UniTune to SDEdit, UniTune was chosen as the superior method in 72% of cases overall.
    - For "unaligned" edits that require significant changes, UniTune's preference rate rose to 83%.
    - For "aligned" (more local) edits, UniTune was still preferred 60% of the time.
    - On a 1-5 rating scale, users scored UniTune's best outputs higher than SDEdit's on quality (4.14 vs 3.90), fidelity to the original image (3.87 vs 3.54), and alignment with the text prompt (4.21 vs 3.89).

- **Author-claimed impact or takeaway sentence:** The paper demonstrates that fine-tuning a diffusion model on a single image is a simple yet powerful technique for high-fidelity, text-driven image editing, enabling a surprisingly wide range of expressive operations that were previously impossible.

## 5. Ablation Studies
The authors performed a comprehensive ablation study by analyzing the effects of the two key hyperparameters: the number of fine-tuning (FT) iterations and the initial sampling step (`t₀`).

- **Experiment 1: Role of Fine-Tuning:** By keeping `t₀` fixed and varying the number of FT steps, they showed that without fine-tuning (FT=0, equivalent to SDEdit), the model struggles to maintain the identity of subjects during major edits. Increasing FT steps progressively improves fidelity to the original image's content and style.

- **Experiment 2: Role of Noisy Initialization:** By keeping FT steps fixed and varying `t₀`, they demonstrated that without noisy initialization (`t₀=1.0`, i.e., starting from pure noise), the model loses the original image's layout and composition. Decreasing `t₀` (initializing with a noised version of the input) is crucial for preserving the overall structure.

The study concludes that the combination of both fine-tuning and noisy initialization is essential for achieving the best balance between fidelity to the source image and the expressiveness of the edit.

## 6. Paper Figures
![Fig. 10. Comparison of UniTune and Text2LIVE. The original images and Text2LIVE edits are taken from the Text2LIVE paper [Bar-Tal et al . 2022]. We observe comparable results for the types of edits Text2LIVE supports. We have not compared UniTune to Text2LIVE for complex edits, like adding new objects or deviating from the original layout, as Text2LIVE does not support these kinds of edits. To generate UniTune examples we manually selected the best result out of 64 variations generated with different UniTune configurations. The edit prompts for the last two examples were slightly changed from the original paper to mention ’coffee cup’ and ’cigar’.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_10.jpg' | relative_url }})
![Fig. 2. UniTune maintains high visual fidelity in unaffected areas of the image when making localized edits (e.g. the faces when adding a train to the background), and high semantic fidelity when making global edits (e.g. when changing the style of the entire image).]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_2.jpg' | relative_url }})
![Fig. 3. The images generated by the model conditioned on the tokens it was trained on after different number of fine tuning iterations. It takes around 64 iterations for the model to be able to faithfully reproduce the original image. Input source: Unsplash.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_3.jpg' | relative_url }})
![Fig. 4. Images for the prompt "minion" after fine-tuning on the image on the left, with various degrees of Classifier Free Guidance weights. With standard conditioned sampling (second from the left), the model is biased towards the image it was fine-tuned on. Using Classifier Free Guidance (right) we observe that the knowledge of what a "minion" is, is preserved within the model’s weights.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_4.jpg' | relative_url }})
![Fig. 5. An example showing the benefit of interpolation to quality.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_5.jpg' | relative_url }})
![Fig. 6. Examples of UniTune performing local edits (adding objects) without masks.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_6.jpg' | relative_url }})
![Fig. 7. UniTune works in multiple domains and can carry out a combination of local and global manipulations. Input source: Unsplash.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_7.jpg' | relative_url }})
![Fig. 8. UniTune shows comparable editing capabilities to models trained on a single domain like portrait photos.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_8.jpg' | relative_url }})
![Fig. 9. More UniTune examples. The bottom two rows demonstrate visual and semantic fidelity. See the appendix for the full edit prompts and parameter settings used to generate the images in this figure. Input source: Unsplash.]({{ '/images/10-2022/UniTune:_Text-Driven_Image_Editing_by_Fine_Tuning_a_Diffusion_Model_on_a_Single_Image/figure_9.jpg' | relative_url }})
