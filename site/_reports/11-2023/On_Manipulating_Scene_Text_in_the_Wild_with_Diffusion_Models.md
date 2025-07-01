---
title: On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models
layout: default
date: 2023-11-01
---
![Figure 1. Top: Comparison between state-of-the-art methods and our method from given input image and target text on scene text manipulation. Bottom: Comparison between baseline text-toimage Latent Diffusion Model (LDM) [ 30 ] represented with blue box and our method represented with red box on scene text domain from given random noise and text condition as an input.]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of scene text manipulation, where the goal is to replace text within an image while preserving the original visual style (e.g., font, color, size, and background). They observe that state-of-the-art diffusion models, while powerful for general image editing, perform poorly on this task. These models often deteriorate image details or misinterpret text prompts, generating objects related to the words rather than rendering the text itself. This gap limits practical applications like real-time sign translation or data augmentation for OCR models.

## 2. Key Ideas and Methodology
The paper introduces the **Diffusion-BasEd Scene Text manipulation Network (DBEST)**, which adapts a pre-trained Latent Diffusion Model (LDM) for high-fidelity scene text editing. The core of the methodology is a two-stage optimization process applied for each editing task:

1.  **One-Shot Style Adaptation:** To preserve the unique style of the source image, the diffusion model's weights are fine-tuned on the single input image. This forces the model to learn the specific font, color, and background characteristics, ensuring the edited text integrates seamlessly.
2.  **Text Recognition Guidance:** To ensure the generated text is legible and accurate, the target text embedding is optimized. The model generates a candidate image, which is fed to an external OCR model. The cross-entropy loss from the OCR model is then used to guide the text embedding, effectively correcting character-level errors in the output.

## 3. Datasets Used / Presented
-   **Synthetic Training Dataset:** The authors generated a dataset of 100,000 training images using the **SynText** generator. This dataset was used to fine-tune the base LDM for the scene text domain.
-   **Synthetic Evaluation Dataset:** A test set of 600 synthesized images was created for quantitative evaluation.
-   **In-the-Wild Datasets:** Standard benchmarks were used for evaluation, including **COCO-Text** (100 images) and **ICDAR2013** (100 images). Qualitative results were also shown on ICDAR2015, IIIT5K, SVT, and HierText datasets.

## 4. Main Results
The proposed DBEST method significantly outperforms existing GAN-based and diffusion-based approaches in terms of generated text quality, measured by OCR accuracy.

-   On the synthetic SynText dataset, DBEST achieves a word-level OCR accuracy of **84.83%**, a 13% absolute improvement over the previous best-performing method, SRNet.
-   On the challenging in-the-wild datasets, DBEST demonstrates robust performance, achieving **83.00%** word-level accuracy on COCO-Text and **98.12%** character-level accuracy on ICDAR2013.

The authors claim their method is the first to effectively leverage diffusion models for high-quality scene text manipulation while preserving crucial stylistic details.

## 5. Ablation Studies
The authors conducted several ablation studies to validate the contribution of each component of their method.

-   **Effect of SynText Pre-training:** Without fine-tuning the base LDM on the SynText dataset, the model fails to generate coherent scene text, with word-level OCR accuracy dropping from 84.83% to just 11.50%. This highlights the need to adapt the model to the scene text domain.
-   **Effect of One-Shot Style Adaptation:** Removing this step leads to generated text that does not match the style (font, color, geometry) of the source image. This component is crucial for preserving the original appearance.
-   **Effect of Text Recognition Guidance:** Disabling this guidance module causes a significant drop in word-level OCR accuracy on the SynText dataset from 84.83% to 60.16%. This shows its importance in correcting character errors and improving the final text's readability.

## 6. Paper Figures
![Figure 2. The pipeline of our proposed method. The process is divided into 2 steps. One-shot style adaptation for fine-tuning the diffusion model and text recognition guidance for optimizing the target embedding.]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3. Qualitative comparison on COCO-Text [ 39 ] and ICDAR2013 [ 16 ] datasets. DBEST (ours) achieves superior qualitative results compared to SRNet [ 40 ], STEFFAN [ 32 ], SDEdit [ 20 ], Imagic [ 17 ], Null-Inv [ 22 ]+p2p [ 12 ], Text2Img LDM [ 30 ], Text2Live [ 3 ].]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4. Result of text scene manipulation on row 1: ICDAR2015 [ 15 ], row 2: IIIT5K [ 21 ], and row 3: SVT [ 27 ]. The input image is represented by green box and the edited version by red box .]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5. Given a single word green box from in-the-wild images and the desired text, our method successfully to edit the text with the desired text in the image red box .]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6. Result from a single image with different target texts. The input image is represented by green box , the edited image without one-shot diffusion model is shown by blue box and the final edited version by red box .]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_6.jpg' | relative_url }})
![Figure 7. Ablation result of our method on Syntext dataset. The label ’SynText’ and ’Text’ denote a utilization of SynText dataset and text recognition guidance, respectively.]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_7.jpg' | relative_url }})
![Figure 8. ‘MAIN’, ‘STOP’ −→ ‘NIPS’, ‘ICML’. The input image is represented by green box , the result by ’Imagic with SynText’ is shown by blue box and ours by red box .]({{ '/images/11-2023/On_Manipulating_Scene_Text_in_the_Wild_with_Diffusion_Models/figure_8.jpg' | relative_url }})
