---
title: SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models
layout: default
date: 2022-12-08
---
## SINE: SINgle Image Editing with Text-to-Image Diffusion Models
**Authors:**
- Zhixing Zhang
- Jian Ren

**ArXiv URL:** http://arxiv.org/abs/2212.04489v2

**Citation Count:** 160

**Published Date:** 2022-12-08

![Figure 1. With only one real image, i.e. , Source Image, our method is able to manipulate and generate the content in various ways, such as changing style, adding context, modifying the object, and enlarging the resolution, through guidance from the text prompt.]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of editing a single real-world image using large-scale text-to-image diffusion models. Existing methods, such as DreamBooth, require multiple images of a subject to avoid overfitting. When fine-tuned on just one image (e.g., a unique painting like *Girl with a Pearl Earring*), these models suffer from severe overfitting and "language drift." This causes two main problems: 1) the model loses its general knowledge and fails to generate creative edits based on new text prompts, and 2) it learns a fixed spatial layout, leading to artifacts like object repetition when generating images at resolutions different from the training image.

## 2. Key Ideas and Methodology
The core idea of the paper, named SINE (SINgle Image Editing), is to leverage an overfitted model as a guide for a general pre-trained diffusion model, rather than using it directly for generation. This approach combines the specific content and structure from the single source image with the vast generative capabilities of the original model.

The methodology consists of two key components:
*   **Model-based Classifier-Free Guidance:** The authors introduce a novel guidance technique that extends standard classifier-free guidance. During the initial steps of the denoising process, the noise prediction is a linear combination of outputs from both the general pre-trained model and the specialized model fine-tuned on the single image. The fine-tuned model acts as a "content seed," injecting the identity of the source object. After a set number of steps (`K`), the process relies solely on the pre-trained model to complete the generation, ensuring high-quality and creative results aligned with the target text prompt.
*   **Patch-based Fine-tuning:** To enable arbitrary-resolution generation, the model is fine-tuned on random patches of the source image instead of the entire image. Each patch is coupled with its positional coordinates, which are passed to the model using Fourier embeddings. This teaches the model the correlation between content and its spatial position, allowing it to generate coherent images at any resolution or aspect ratio without geometric artifacts.

The method is built upon the Latent Diffusion Model (LDM) framework, specifically Stable Diffusion.

## 3. Datasets Used / Presented
*   **LAION:** The authors use a pre-trained Stable Diffusion model, which was originally trained on the LAION dataset.
*   **Flickr and Unsplash:** For experiments, the authors collect a variety of individual, free-to-use, high-resolution images from these platforms. These images span diverse domains (e.g., animals, architecture, art) and are used as single-image inputs to demonstrate the method's editing capabilities. No new large-scale dataset is created; the focus is on case studies with single images.

## 4. Main Results
The paper's results are primarily qualitative, demonstrating superior performance over concurrent methods.
*   SINE successfully performs a wide range of edits—including style transfer, content addition, and object manipulation—while preserving the identity and key features of the source image (Figure 3).
*   Crucially, the patch-based fine-tuning allows SINE to generate high-fidelity images at arbitrary resolutions (e.g., 512x1024) without the duplication or stretching artifacts that plague other methods (Figure 4, 5).
*   In direct comparisons with DreamBooth and Textual-Inversion, SINE shows better structural integrity and fidelity to the source subject, especially when editing at higher resolutions (Figure 5).
*   The authors claim their method effectively distills knowledge from a specialized, overfitted model into a general pre-trained model, enabling high-fidelity, arbitrary-resolution editing from a single image.

## 5. Ablation Studies
The authors conduct several ablation studies to validate their design choices:
*   **Patch-based Fine-tuning:** Removing the patch-based mechanism (`w/o pos`) and fine-tuning on the whole image results in severe geometric artifacts (object duplication, stretching) when generating at a different resolution. The proposed method (`w/ pos`) correctly preserves the image structure (Figure 5).
*   **Model-based Guidance:** Sampling directly from the fine-tuned model without the proposed guidance (`w/o guidance`) fails to produce edits corresponding to the text prompt due to overfitting. In contrast, the proposed guidance (`w/ guidance`) successfully synthesizes the desired changes (Figure 6).
*   **Guidance Step (`K`):** The number of steps where the fine-tuned model provides guidance is analyzed. A low `K` preserves more of the source image but results in weaker edits. A high `K` produces stronger edits but with less fidelity to the original. A value of `K=400` (out of 1000 steps) is chosen as a good trade-off (Figure 7, 8a).
*   **Guidance Weight (`v`):** The weight balancing the fine-tuned and pre-trained models is studied. A low `v` relies too heavily on the overfitted model, causing artifacts, while a high `v` makes the output too generic. A value of `v=0.7` is found to be an effective balance between fidelity and creativity (Figure 9, 8b).

## 6. Paper Figures
![Figure 10. In-the-wild human face manipulation. We conduct various editing on human face photos, locally or globally. The models are trained and edited at a resolution of 512 × 512 .]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_10.jpg' | relative_url }})
![Figure 11. More applications. We show how our approach can be applied to various tasks in image editing, such as content removal (a), style generation (b), and style transfer (c).]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_11.jpg' | relative_url }})
![Figure 2. Overview of our method. (a) Given a source image, we first randomly crop it into patches and get the corresponding latent code z with the pre-trained encoder. At fine-tune time, the denoising model, ϵ θ , takes three inputs: noisy latent z T , language condition c , and positional embedding for the area where the noisy latent is obtained. (b) During sampling, we give additional language guidance about the target domain to edit the image. Also, we sample a noisy latent code z T with the dimension corresponding to the desired output resolution. Language conditioning for ϵ θ and c are given by pre-trained language encoder τ θ with the target language guidance. While for the fine-tuned diffusion model, ˆ ϵ θ , in addition to the language conditioning ˆc , we also input the positional embedding for the whole image. We employ a linear combination between the score calculated by each model for the first K steps and inference only on pre-trained ϵ θ after.]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3. Editing on single source image from various domains. We employ our method on various images and edit them with two target prompts at 512 × 512 resolution. We show the wide range of edits our approach can be used, including but not limited to style transfer, content add-on, posture change, breed change, etc .]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4. Arbitrary resolution editing. Our method achieves higher-resolution image editing without artifacts like duplicates, even on ones that change the height-width ratio drastically.]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5. Comparisons of various methods. We compare our method to DreamBooth [ 33 ] and Textual-Inversion [ 9 ]. On the left part of the figure, we edit at the resolution same as training time. On the right part, we edit the source image at a higher resolution. Our work successfully edits the image as required while preserving the details of the source images. We also compare our method without and with the patch-based fine-tuning mechanism (w/o pos vs. w/ pos). When editing at a fixed resolution, two settings perform equally, while at a higher resolution, the patch-based fine-tuning method successfully prevents artifacts.]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6. Analysis of model-based classifier-free guidance. Directly sampling with target text using the fine-tuned model (w/o guidance) fails to generate images corresponding to the text prompt. In contrast, the model-based classifier-free guidance (w/ guidance) can synthesize high-fidelity images.]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_6.jpg' | relative_url }})
![Figure 7. Analysis on guidance step K . Varying K , we can decide the steps where the model-based guidance is applied, which controls the details from the source image and edits to be applied.]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_7.jpg' | relative_url }})
![Figure 9. Analysis of score interpolation. Varying v with the same random seed gets editing results with various qualities.]({{ '/images/12-2022/SINE:_SINgle_Image_Editing_with_Text-to-Image_Diffusion_Models/figure_9.jpg' | relative_url }})
