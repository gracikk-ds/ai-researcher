---
title: Custom-Edit:_Text-Guided_Image_Editing_with_Customized_Diffusion_Models
layout: default
date: 2023-05-25
---
![Figure 1. Our Custom-Edit allows high-fidelity text-guided editing, given a few references. Edited images with BLIP2 [ 13 ] captions show the limitation of textual guidance in capturing the finegrained appearance of the reference.]({{ '/images/05-2023/Custom-Edit:_Text-Guided_Image_Editing_with_Customized_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Standard text-to-image diffusion models support text-guided editing, but they often fail to capture the precise, fine-grained appearance of a user's unique concept, especially if it was not well-represented in the original training data. The authors address this limitation by proposing a method that allows a user to define a custom visual concept using a few reference images and then use that concept to perform high-fidelity image editing.

## 2. Key Ideas and Methodology
The paper introduces **Custom-Edit**, a two-step framework for personalized image editing.

-   **Core Principle:** The key discovery is that for the task of editing, fine-tuning only the *language-relevant parameters* of a diffusion model is highly effective. This includes the key and value projection matrices in the cross-attention layers and a new token embedding for the custom concept. This approach preserves the model's general knowledge while effectively learning the new concept's appearance.
-   **Methodology:**
    1.  **Customization:** The user provides 4-5 reference images of a concept (e.g., a specific "V* patterned teapot"). The model is then fine-tuned on these images using augmented text prompts like `"a photo of a V* patterned teapot"`. A prior preservation loss is used with a larger set of class-generic images (e.g., general teapots) to prevent the model from forgetting the general class concept.
    2.  **Editing:** The customized model is used to edit a source image with a text prompt. The authors leverage the **Prompt-to-Prompt (P2P)** editing framework, which preserves the source image's structure by injecting its attention maps during the generation of the edited image. They also utilize **Null-Text Inversion** to ensure faithful reconstruction of the source image.

## 3. Datasets Used / Presented
-   **Reference Concepts:** The authors evaluate their method on 8 custom concepts collected from prior works, including objects (wooden pot, patterned teapot), pets (cat, dog), and artwork (pencil drawing). Each concept is defined by a small set of reference images.
-   **Prior Preservation Dataset:** To prevent overfitting during customization, 200 images per concept are retrieved from the **LAION** dataset using CLIP-retrieval. These images correspond to the general class of the custom object (e.g., "photo of a teapot").
-   **Source Images:** For evaluation, source images were collected from various text-to-image model papers, including Imagen, eDiff-I, and Imagic. On average, five source images were used for each reference concept.

## 4. Main Results
The primary finding is that Custom-Edit achieves a superior trade-off between preserving the source image's structure and transferring the reference concept's appearance compared to other customization methods.

-   **Quantitative Results:** In plots measuring source similarity vs. reference similarity (using CLIP), the proposed method (based on Custom-Diffusion) consistently yields a better trade-off curve than **Dreambooth** and **Textual Inversion**. Dreambooth shows high source similarity but low reference similarity (failing to edit effectively), while Textual Inversion fails to capture the detailed appearance of the reference.
-   **Author-claimed Impact:** Custom-Edit enables high-fidelity, text-guided editing that incorporates fine-grained visual details from a few reference images, significantly improving faithfulness to the user's intended concept while maintaining structural consistency with the source image.

## 5. Ablation Studies
The paper validates its design choices through several comparative experiments rather than a formal ablation section.

-   **Comparison of Customization Methods:** The core comparison is between their method (tuning only language-relevant parameters), Dreambooth (tuning the full U-Net), and Textual Inversion (tuning only a token embedding). The results show that tuning only the language-relevant parameters is the most effective strategy for the editing task, providing the best balance of source preservation and reference fidelity.
-   **Analysis of Editing "Strength":** The authors analyze the effect of the P2P and SDEdit "strength" parameter, which controls the trade-off between source and reference similarity. They show how varying this parameter impacts the output and identify optimal ranges (e.g., a strength of 0.4-0.6 for P2P) to achieve good results.
-   **Choice of P2P Operations:** The paper proposes a specific recipe for using P2P (using prompt refinement and a source-only attention mask), which they found works better for customized concepts than the default P2P settings.

## 6. Paper Figures
![Figure 2. Our Custom-Edit consists of two processes: the customization process and the editing process. (a) Customization. We customize a diffusion model by optimizing only language-relevant parameters (i.e., custom embedding V* and attention weights) on a given set of reference images. We also apply the prior preservation loss to alleviate the language drift. (b) Editing. We then transform the source image to the output using the customized word. We leverage the P2P and Null-text inversion methods [ 7 , 16 ] for this process.]({{ '/images/05-2023/Custom-Edit:_Text-Guided_Image_Editing_with_Customized_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3. Custom-Edit results. Our method transfers the reference’s appearance to the source image with unprecedented fidelity. The structures of the source are well preserved. We obtain source prompts using BLIP2 [ 13 ]. Except for the pencil drawing example, we use local editing of P2P with automatically generated masks.]({{ '/images/05-2023/Custom-Edit:_Text-Guided_Image_Editing_with_Customized_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4. Source-Reference Trade-Off. Custom-Diffusion shows the best trade-off, indicating the effectiveness of training only language-relevant parameters. We exhibit qualitative comparisons and samples with various strengths in Sec. A.2 .]({{ '/images/05-2023/Custom-Edit:_Text-Guided_Image_Editing_with_Customized_Diffusion_Models/figure_4.jpg' | relative_url }})
