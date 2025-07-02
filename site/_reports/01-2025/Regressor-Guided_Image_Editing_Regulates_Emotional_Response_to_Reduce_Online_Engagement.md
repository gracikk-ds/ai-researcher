---
title: Regressor-Guided_Image_Editing_Regulates_Emotional_Response_to_Reduce_Online_Engagement
layout: default
date: 2025-01-21
---
## Regressor-Guided Image Editing Regulates Emotional Response to Reduce Online Engagement
**Authors:**
- Christoph Gebhardt, h-index: 4, papers: 8, citations: 52
- Christian Holz, h-index: 4, papers: 9, citations: 35

**ArXiv URL:** http://arxiv.org/abs/2501.12289v1

**Citation Count:** 0

**Published Date:** 2025-01-21

![Fig. 1. We propose three regressor-guided image editing approaches aimed at reducing the emotional intensity evoked by images. These methods take the original image (b) as input and modify it using distinct strategies. The first two approaches adjust low-level properties, such as brightness, saturation, color, and sharpness, by optimizing either the style latent space of a generative adversarial network (a) or the parameters of global image transformations (c). The third approach uses score guidance and classifier-free guidance with a diffusion model to modify the image content (d). These semantic changes include adding extra layers of clothing, simplifying backgrounds, or aging the appearance of subjects. Experimental results show that the adapted images produced by the diffusion-model-based approach effectively influence viewers’ emotional responses compared to their original counterparts and, unlike greyscale images, maintain a high perceived image quality.]({{ '/images/01-2025/Regressor-Guided_Image_Editing_Regulates_Emotional_Response_to_Reduce_Online_Engagement/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the problem of excessive online engagement, which is often driven by emotionally intense content and can lead to negative outcomes like social media addiction and poor mental health. Existing digital self-control tools are frequently too restrictive, causing users to circumvent them. The paper proposes a less intrusive solution: automatically editing images to regulate their emotional impact (i.e., neutralize valence and lower arousal), thereby potentially reducing users' online engagement without degrading the user experience as severely as simple filters like greyscale.

## 2. Key Ideas and Methodology
The core idea is to use a trained emotion regressor, which predicts the valence and arousal an image will evoke, to guide generative models in editing images toward a more neutral emotional state. The authors propose and compare three distinct methods:
1.  **Parametric Optimization**: Optimizes the parameters of global, differentiable image transformations (e.g., brightness, contrast, saturation) to minimize the difference between the edited image's predicted emotion and the neutral target, while a CLIP loss preserves content.
2.  **Latent Style Optimization**: Employs a MUNIT GAN to disentangle an image into content and style vectors. It then optimizes the style vector to meet the emotional target while keeping the content vector fixed to preserve the image's subject matter.
3.  **Inverse Diffusion with Score-Guided Resampling (CG & CFG)**: This is the most complex and effective method. It uses a pre-trained diffusion model (SDXL) to perform semantic edits. An input image is first inverted into a latent noise vector. This vector is then resampled (denoised) under dual guidance: (a) **classifier-free guidance (CFG)** uses the original image's caption to ensure the output remains semantically similar, and (b) **classifier guidance (CG)** uses a dedicated emotion regressor to steer the generation process toward the target of neutral valence and low arousal.

## 3. Datasets Used / Presented
- **Emotion Regressor Training**: A custom dataset of 20,460 images was created by aggregating 10 public emotional databases (including NAPS, IAPS, OASIS, and GAPED). This was used to fine-tune a ResNet50 model to predict valence and arousal.
- **Technical Evaluation**: The COCO validation set was used to quantitatively assess the methods' ability to alter predicted emotions while maintaining image quality (FID/KID) and fidelity.
- **Qualitative & Bidirectional Evaluation**: A random subset of 500 images from the Instagram Influencer Dataset was used for qualitative analysis and to test if the methods could steer images toward various emotional targets, not just neutrality.
- **Behavioral Study**: 12 emotionally evocative images from the Nencki Affective Picture System (NAPS) were used as stimuli in a human study to measure the actual change in perceived valence, arousal, and image quality.

## 4. Main Results
The main findings come from a behavioral study with 56 participants, which validated the technical results with human perception.
- Only the **diffusion-based (CG & CFG)** approach successfully and significantly altered viewers' emotional responses as intended. It shifted valence ratings closer to the neutral reference point (mean 5.23 vs. 4.43 for original images on a 9-point scale) and significantly lowered perceived arousal.
- The parametric and style optimization methods failed to produce a significant emotional shift in human viewers.
- The diffusion-based approach was the only method that **maintained perceived image quality** comparable to the original images. In contrast, the parametric, style, and greyscale methods all resulted in significantly lower perceived quality.
- The authors' key takeaway is that the diffusion-based approach effectively regulates emotional response by introducing semantic changes (e.g., aging a subject, adding clothing, simplifying a background) rather than just low-level color and brightness adjustments.

## 5. Ablation Studies
The authors conducted an ablation study on their diffusion-based model to isolate the contributions of its guidance mechanisms.
- **CG Only (Classifier Guidance Only)**: Using only the emotion regressor for guidance without text conditioning successfully reduced predicted valence and arousal but introduced more visual artifacts and had worse quality scores (FID/KID) than the full model.
- **NTO-instruct (Text-Conditioned Only)**: Using only text guidance (by appending a phrase like "the image should elicit low arousal..." to the caption) without a regressor was inconsistent and failed to adequately reduce valence and arousal.
- **NTO-edit (Caption Refinement)**: Using a manually refined, more neutral text caption for guidance also failed to achieve the desired emotional shift.
- The results demonstrate that the combination of regressor-based classifier guidance (for emotional control) and text-based classifier-free guidance (for content preservation) is essential for the method's success.

## 6. Paper Figures
![Fig. 2. Parametric optimization: To adapt an input image 𝐼 , the parameters 𝑝 of the differentiable image transformations 𝑇 are optimized to produce a similar image that elicits a reduced emotional response, represented by ˆ 𝐼 = 𝑇 ( 𝐼, 𝑝 ) . The optimization minimizes the distance between the predicted valence and arousal of the adapted image, [ ˆ 𝑣, ˆ 𝑎 ] = 𝑅 ( ˆ 𝐼 ) , and the emotional reference , [ 𝑣 ′ ,𝑎 ′ ] . It further ensures a high cosine similarity between the CLIP-space embeddings of the input image 𝑐 = 𝐶𝐿𝐼𝑃 ( 𝐼 ) and the transformed image ˆ 𝑐 = 𝐶𝐿𝐼𝑃 ( ˆ 𝐼 ) .]({{ '/images/01-2025/Regressor-Guided_Image_Editing_Regulates_Emotional_Response_to_Reduce_Online_Engagement/figure_2.jpg' | relative_url }})
![Fig. 3. Latent style optimization: To adapt an input image 𝐼 , its latent style vector 𝑠 is optimized to generate a similar image that elicits a reduced emotional response when decoded with 𝐼 ’s latent content 𝑐 0 = 𝐸 𝑐 ( 𝐼 ) , resulting in ˆ 𝐼 = 𝐷 ( 𝑐 0 ,𝑠 ) . The optimization process minimizes the distance between the predicted valence and arousal of the adapted image, [ ˆ 𝑣, ˆ 𝑎 ] = 𝑅 ( ˆ 𝐼 ) , and the target values specified by emotional reference , [ 𝑣 ′ ,𝑎 ′ ] . Additionally, the optimization incorporates a term to ensure content consistency by minimizing the L1 loss between the encoded latent content of the generated image, ˆ 𝑐 = 𝐸 𝑐 ( ˆ 𝐼 ) , and 𝑐 0 . The style vector 𝑠 is initialized as the encoded style vector of the input image, 𝑠 0 = 𝐸 𝑠 ( 𝐼 ) .]({{ '/images/01-2025/Regressor-Guided_Image_Editing_Regulates_Emotional_Response_to_Reduce_Online_Engagement/figure_3.jpg' | relative_url }})
![Fig. 4. Inverse diffusion with classifier-guided resampling: To adapt an input image 𝐼 , it is first encoded into a latent vector 𝑧 0 = 𝐸 ( 𝐼 ) and then inverted to its corresponding noise vector 𝑧 𝑇 = 𝐷𝐷𝐼𝑀 inv ( 𝑧 0 ,𝑡, C , 𝛽 ) , while generating unconditional text embeddings for each timestep {∅ 𝑡 } 𝑇 𝑡 = 1 = 𝑁𝑇𝑂 ([ 𝑧 𝑇 , . . . ,𝑧 0 ] , C) . At each step of the denoising process, ˆ 𝑧 𝑡 is updated by blending the predicted unconditional and conditional noise 𝜖 𝜃 , further refined by a score ∇ 𝑧 𝑡 that quantifies alignment with the emotional reference . With the resulting noise vector ˜ 𝜖 𝜃 , ˆ 𝑧 𝑡 − 1 can be obtained. The final latent vector ˆ 𝑧 0 is decoded into the image ˆ 𝐼 = 𝐷 ( ˆ 𝑧 0 ) , which closely resembles 𝐼 while modulating the emotional response.]({{ '/images/01-2025/Regressor-Guided_Image_Editing_Regulates_Emotional_Response_to_Reduce_Online_Engagement/figure_4.jpg' | relative_url }})
