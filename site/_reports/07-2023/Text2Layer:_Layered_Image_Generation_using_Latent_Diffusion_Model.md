---
title: Text2Layer:_Layered_Image_Generation_using_Latent_Diffusion_Model
layout: default
date: 2023-07-19
---
![Fig. 1. Examples of two-layer images. Prompts are displayed on the top of images. Each example includes foreground (fg), background (bg), and mask component to compose a two-layer image. From left to right of each example: fg, bg, mask, and composed image.]({{ '/images/07-2023/Text2Layer:_Layered_Image_Generation_using_Latent_Diffusion_Model/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-to-image editing models often lack fine-grained control, modifying more pixels than desired and struggling with edits that are difficult to describe in text. A common workaround is to generate an image and then use a separate segmentation tool, but this often results in low-quality masks and artifacts. The authors address this practical problem by proposing a new paradigm: generating images as distinct, editable layers (foreground, background, and mask) directly from a text prompt. This approach aims to provide users with high-quality, layered assets for more flexible and precise compositing workflows.

## 2. Key Ideas and Methodology
The core idea is to reframe text-to-image synthesis as a layered image generation task. Instead of producing a single flat image, the model simultaneously generates a foreground layer (F), a background layer (B), a layer mask (m), and the final composed image.

The methodology is built upon a latent diffusion model. The key innovation is a novel **Composition-Aware Two-Layer Autoencoder (CaT2I-AE)**, which is specifically designed to handle layered image data.
-   The autoencoder learns a latent representation of the layered image (F, B, m).
-   Its decoder uses three separate prediction heads to reconstruct the foreground, background, and mask independently, which is more effective than a single-head decoder.
-   An auxiliary supervision branch is added to the decoder to also reconstruct the final composed image, which was found to improve overall generation quality.

After this autoencoder is trained, a standard conditional diffusion model (UNet) is trained on its latent space to generate layered images from text prompts.

## 3. Datasets Used / Presented
The authors introduce a new large-scale dataset, **LAION-L2I**, because no suitable dataset for layered image generation existed.
-   **Creation:** Starting with the LAION-Aesthetics dataset (~600M images), they automatically generated layered data. For each image, a salient object detection model (ICON) extracted a foreground mask, and a diffusion-based inpainting model generated the corresponding background.
-   **Filtering:** Since this automated process is imperfect, they trained two classifiers on 5,000 manually labeled examples to filter out low-quality masks and inpainting results.
-   **Size and Domain:** The final LAION-L2I dataset contains **57.02 million** high-quality, text-paired layered images (foreground, background, mask) derived from general-domain web images. It was used to train and evaluate their models.

## 4. Main Results
The proposed method, **CaT2I-AE-SD**, demonstrates superior performance compared to several baselines based on Stable Diffusion.
-   **Image Quality:** The model achieves a significantly better Fréchet Inception Distance (FID) of 10.51 on the test set, compared to a baseline that uses a standard autoencoder (FID of 18.53), indicating higher-quality and more realistic composed images.
-   **Mask Quality:** The generated masks are more accurate. The model achieves an Intersection-over-Union (IOU) of 0.799 against human-annotated masks, outperforming the baseline's IOU of 0.766.
-   **Text Relevance:** The model shows better alignment with input text prompts, achieving a higher CLIP score (0.251) than the baselines (0.219).

The authors claim their method successfully generates high-quality layered images and establishes a strong benchmark for future research in this area.

## 5. Ablation Studies
-   **Autoencoder Design:** Comparing the custom `CaT2I-AE` to using a standard Stable Diffusion autoencoder (`SD-AE`) showed that the specialized architecture is critical. The `CaT2I-AE` model drastically outperformed the `SD-AE` baseline across all metrics (e.g., FID of 10.51 vs. 18.53), proving the necessity of an autoencoder designed for layered data.
-   **Auxiliary Supervision:** A version of the model was trained without the auxiliary branch for reconstructing the composed image (`no-sup`). The full model achieved better image quality (FID of 10.51 vs. 13.84) and text relevance (CLIP score of 0.251 vs. 0.241), confirming that this additional supervision is beneficial.
-   **Data Filtering:** The model was trained on both the final filtered LAION-L2I dataset and an unfiltered version. The model trained on the filtered data showed substantial improvements in image quality (FID of 10.51 vs. 13.82), mask accuracy (IOU of 0.799 vs. 0.736), and text relevance, validating the effectiveness of their data curation pipeline.

## 6. Paper Figures
![Fig. 2. Layer mask examples. The scale, location, and number of objects vary largely.]({{ '/images/07-2023/Text2Layer:_Layered_Image_Generation_using_Latent_Diffusion_Model/figure_2.jpg' | relative_url }})
![Fig. 3. Failure cases of salient object segmentation (left) and inpainting (middle and right). The red shaded regions indicate the object to be removed.]({{ '/images/07-2023/Text2Layer:_Layered_Image_Generation_using_Latent_Diffusion_Model/figure_3.jpg' | relative_url }})
![(d) Predicted “good” inpaintings Fig. 4. Predicted good and bad salient masks and inpaintings]({{ '/images/07-2023/Text2Layer:_Layered_Image_Generation_using_Latent_Diffusion_Model/figure_4.jpg' | relative_url }})
![(d) SD-AE-UNet (ft) Fig. 5. Composited samples from CaT 2 I-AE-SD and baseline models for 256 × 256 resolution. The prompts are (1) Dogs at the entrance of Arco Iris Boutique and (2) Haunted Mansion Holiday at Disneyland Park . Each 2 × 2 block displays the composited images and masks m of the corresponding models. Find more in the supplement.]({{ '/images/07-2023/Text2Layer:_Layered_Image_Generation_using_Latent_Diffusion_Model/figure_5.jpg' | relative_url }})
![Fig. 6. F, B, m components and composed images for two-layer images sampled from CaT 2 I-AE-SD (512). Prompts are omitted. From top to down: F , b , and m . For more samples cf. the supplement.]({{ '/images/07-2023/Text2Layer:_Layered_Image_Generation_using_Latent_Diffusion_Model/figure_6.jpg' | relative_url }})
