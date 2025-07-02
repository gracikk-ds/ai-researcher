---
title: MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis
layout: default
date: 2024-12-03
---
## MetaShadow: Object-Centered Shadow Detection, Removal, and Synthesis
**Authors:**
- Tianyu Wang
- Soo Ye Kim, h-index: 5, papers: 11, citations: 102

**ArXiv URL:** http://arxiv.org/abs/2412.02635v1

**Citation Count:** 2

**Published Date:** 2024-12-03

![Figure 1. MetaShadow is a versatile three-in-one framework designed for shadow-related tasks, enabling shadow manipulation in various object-centered image editing operations such as: [I] Object Relocation: Our model can detect and remove the shadow of an existing object, then synthesize the shadow in the new location consistent with the original shadow. [II] Remove an object and its shadow: (1) Based on the mask of the unwanted object, our model can directly remove its shadow (2). After removing the object (3), we can eliminate any remaining shadows for a cleaner background (4) if we do not specify which shadow to remove. [III] Insert an object and synthesize its shadow: When inserting the person in (b) to another image (a) with similar lighting, our model can generate a realistic shadow, enhancing the final compositing quality.]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing image editing applications often neglect or improperly handle shadows during object manipulation tasks like removal, relocation, or insertion. This oversight significantly reduces the realism and visual coherence of the final edited image. Furthermore, current research methods typically address shadow detection, removal, and synthesis as separate, isolated problems. This prevents them from sharing learned knowledge, leading to inconsistent and suboptimal results when used together in a pipeline. The authors identify a need for a unified, object-centered framework that can jointly and cohesively manage all three shadow-related tasks to enable high-quality, realistic image editing.

## 2. Key Ideas and Methodology
The paper introduces **MetaShadow**, a versatile three-in-one framework designed for object-centered shadow manipulation. The core idea is to synergistically combine two cooperative components and enable knowledge sharing between them.

*   **Shadow Analyzer**: A GAN-based model that takes an image and an object mask as input. It is trained to perform object-centered shadow detection and removal simultaneously. It identifies the specific shadow cast by the designated object and removes it, producing a clean background.
*   **Shadow Synthesizer**: A reference-based diffusion model that generates a realistic shadow for a newly placed or moved object.
*   **Shadow Knowledge Transfer**: This is the key methodological innovation. Instead of using generic text or image encoders for conditioning, the Shadow Synthesizer is guided by multi-scale intermediate features extracted directly from the Shadow Analyzer. These features encapsulate rich, task-specific information about the scene's lighting (e.g., shadow color, softness, direction), allowing the diffusion model to synthesize new shadows that are contextually consistent and realistic.

## 3. Datasets Used / Presented
The authors introduce three new datasets to facilitate training and evaluation for object-centered shadow editing:
*   **Moving Object with Shadow (MOS) Dataset**: A large-scale synthetic training dataset of 8,000 image pairs generated using Blender, featuring diverse scenes with object relocations.
*   **Moving DESOBA**: A real-world test set created by repositioning objects in images from the existing DESOBA dataset.
*   **Video DESOBA**: A real-world video test set with 12 clips of moving objects casting dynamic shadows on static backgrounds.

For training, MetaShadow also leverages several existing datasets, including **DESOBA**, **Shadow-AR**, **ISTD+**, and **SRD**. For evaluation, it is benchmarked on **SOBA**, **DESOBA**, and the newly presented datasets.

## 4. Main Results
MetaShadow demonstrates state-of-the-art performance across all three targeted tasks on multiple benchmarks.
*   **Shadow Detection**: On the SOBA dataset, MetaShadow significantly improves the mean Intersection over Union (mIoU) from 55.8% (previous SOTA) to 71.0%.
*   **Shadow Removal**: On the DESOBA test set, the model achieves superior removal quality, improving the Bbox PSNR from 70.17 to 96.49 compared to a fine-tuned baseline.
*   **Shadow Synthesis**: On the Video DESOBA dataset, MetaShadow achieves more realistic synthesis, reducing the Local Root Mean Squared Error (RMSE) from 51.73 to 36.54.

The authors claim that MetaShadow is the first framework to jointly handle these three tasks in an object-centered manner, pushing the boundaries of realistic image editing.

## 5. Ablation Studies
The authors performed an ablation study to validate the effectiveness of their proposed **Shadow Knowledge Transfer** mechanism for the Shadow Synthesizer. They compared their method against two baselines:
1.  A model conditioned on text embeddings ("shadow") from a T5 encoder.
2.  A model conditioned on image embeddings from a fine-tuned CLIP encoder.

The results on the DESOBA test set showed that the proposed method, which transfers features from the Shadow Analyzer, outperformed both baselines. It achieved a lower Global RMSE (2.93 vs. 3.36 for text and 4.51 for CLIP) and a higher Bbox PSNR (30.73 vs. 29.80 for text and 29.72 for CLIP). This confirms that using a task-specific encoder for shadow feature extraction is more effective than relying on general-purpose text or image encoders for conditioning the synthesis process.

## 6. Paper Figures
![Figure 2. We construct one training set, i.e ., MOS Dataset, and two real-world evaluation sets, i.e ., Moving DESOBA Dataset (without ground truths) and Video DESOBA Dataset (with ground truths), to train and evaluate the effectiveness of MetaShadow.]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_2.jpg' | relative_url }})
![Figure 3. The schematic illustration of our MetaShadow framework. In Stage I, the Shadow Analyzer takes the input image with object mask (left player) to perform object-centered shadow detection and removal. After that, the selected player, together with the detected shadow region, will be moved to a new location. Our Stage II then takes these as input and synthesizes a shadow for this object. To achieve realistic shadow synthesis, we transfer the shadow knowledge extracted from the Shadow Analyzer to Shadow Synthesizer as reference. Note that s represents the global style code, w denotes the intermediate latent space, and ”K Q V” stand for key, query, and value in UNet’s cross attention layer.]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_3.jpg' | relative_url }})
![Figure 4. Respective limitations of GAN-based and diffusion-based methods on shadow synthesis. For more discussion, please see Sec. 5.2 .]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_4.jpg' | relative_url }})
![Figure 5. Visual comparison for object-centered shadow detection and removal tasks on the DESOBA test set. † means fine-tuned on our multi-source dataset strategy. Zoom in to see the details. For more results, please refer to the supplementary materials.]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_5.jpg' | relative_url }})
![Figure 6. Visual comparison for object-centered shadow synthesis on the DESOBA test set [ 13 ], our Moving DESOBA test set, and Video DESOBA. Zoom in to see the details. For more results, please refer to the supplementary materials.]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_6.jpg' | relative_url }})
![Figure 7. Visual comparison on different random seeds reveals a critical issue with the previous diffusion-based method [ 28 ]: inconsistent shadow generation across various sampled noises. Empirically, our model does not exhibit this weakness.]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_7.jpg' | relative_url }})
![Figure 8. Visualization of the intermediate multi-scale feature maps of our Shadow Analyzer. Given an object mask, Shadow Analyzer detects and removes the shadow for specific objects. Thus, the feature maps effectively capture the shadow knowledge, especially in the target shadow regions.]({{ '/images/12-2024/MetaShadow:_Object-Centered_Shadow_Detection,_Removal,_and_Synthesis/figure_8.jpg' | relative_url }})
