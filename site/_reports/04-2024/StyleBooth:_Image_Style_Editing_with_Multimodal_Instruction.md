---
title: StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction
layout: default
date: 2024-04-18
---
![Figure 1: Edited images by StyleBooth . Based on multimodal instructions, StyleBooth supports 3 types of image style editing. Following the same instruction template: "Let this image be in the style of <style>/<image>", we conduct (a) text-based style editing and (b) exemplar-based style editing (c) compositional style editing. "<style>" or "<image>" is the identifier of textual style name and visual exemplar images. The style name is placed under the result image and exemplar is shown at the left-bottom corner. In (c), the style name and identifier "<image>" are marked in different color fading levels. The degree of fading represents the proportion of the corresponding style in the result images. Tuned by our elegantly designed style editing data, StyleBooth is capable of generating high-quality output images in diverse styles.]({{ '/images/04-2024/StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address two primary challenges in diffusion-based image editing. First, existing methods typically accept instructions in only a single modality, either text or an exemplar image, but not both simultaneously. This limits creative flexibility. Second, there is a significant scarcity of high-quality training data for image style editing, specifically lacking large-scale, content-consistent triplets of source images, target stylized images, and corresponding multimodal instructions.

## 2. Key Ideas and Methodology
The core idea of the paper is **StyleBooth**, a framework that unifies text and image exemplars into a single multimodal instruction for style editing.

The methodology involves:
*   **Multimodal Instruction:** The model uses special tokens (`<style>` for text, `<image>` for exemplars) within a text prompt. An exemplar image is encoded using a CLIP image encoder, and its features are mapped into the text embedding space via a trainable convolutional alignment layer. This creates a unified conditioning vector for the diffusion model.
*   **Model Architecture:** StyleBooth is built upon a pre-trained latent diffusion model (similar to InstructPix2Pix). It takes the original image (as a latent code) and the unified multimodal instruction as inputs to guide the denoising process, generating the edited image.
*   **Compositional Control:** A "Scale Weighting Mechanism" is introduced to adjust the influence of multiple text or image styles during inference, enabling style interpolation and composition by applying different weights to their respective feature embeddings.

## 3. Datasets Used / Presented
The authors introduce a new high-quality dataset for style editing, which they also name **StyleBooth**.

*   **Name:** StyleBooth Dataset
*   **Description:** This dataset was created through a novel "Iterative Style-Destyle Tuning and Editing" pipeline. The process starts with T2I-generated stylized and plain images. It then iteratively fine-tunes specialized "Style Tuners" and "De-style Tuners" (LoRA models) and uses them to generate and refine stylized/plain image pairs. A CLIP-based filtering step is applied after each iteration to discard low-quality or content-inconsistent pairs.
*   **Size and Domain:** The final dataset contains high-quality, content-preserved image pairs across 63 different artistic styles.

## 4. Main Results
StyleBooth was evaluated against state-of-the-art text-based editing models (InstructPix2Pix, MagicBrush, Emu Edit) on the style editing subset of the Emu Edit benchmark.

*   **Quantitative Results:** StyleBooth achieved the highest instruction-following success rate (SRins) of 77.65% and the highest user preference rate (UPR) of 58.85% when compared against all baselines. While its content preservation score (SRcont) of 94.47% was slightly below Emu Edit's 97.12%, qualitative results show Emu Edit often fails to apply the style sufficiently, whereas StyleBooth strikes a better balance.
*   **Author-claimed Impact:** The results demonstrate that the quality and diversity of the training data significantly enhance the model's ability to preserve content and accurately apply styles, leading to superior editing quality, especially in zero-shot scenarios with novel styles and instruction formats.

## 5. Ablation Studies
The paper demonstrates the effectiveness of its data generation pipeline through an iterative improvement analysis.

*   **Experiment:** The authors compared the "usability rate" of the generated image pairs before and after their iterative tuning-and-editing process. The usability rate is the percentage of image pairs that pass a CLIP-score-based filter, indicating sufficient style change and content preservation.
*   **Impact:** The iterative process dramatically improved the quality of the dataset. The average usability rate of the generated pairs increased from **38.11%** after a single vanilla de-styling step to **79.91%** after the full iterative pipeline. This highlights the critical role of the proposed data generation strategy in creating a high-quality dataset.

## 6. Paper Figures
![Figure 2: Overview of StyleBooth method. We propose Multimodal Instruction, mapping the text input and exemplar image input into a same hidden space through a trainable matrix W , which unifies vision and text instructions. The textual instruction templates are carefully designed, introducing undetermined identifiers like "<style>" and "<image>" to support multimodal inputs. To balance every style for compositional style editing, we conduct Scale Weights Mechanism α i on the hidden space embeddings. Editing is conditioned by multimodal features following the composed instructions from different modalities at the same time.]({{ '/images/04-2024/StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction/figure_2.jpg' | relative_url }})
![Figure 3: Iterative Style-Destyle Tuning and Editing pipeline. Following a de-style editing, filtering, style tuning, stylize editing, filtering and de-style tuning steps, Iterative Style-Destyle Tuning and Editing leverages the image quality and usability.]({{ '/images/04-2024/StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction/figure_3.jpg' | relative_url }})
![Figure 4: Generated samples of the intermediate and final image pairs during Iterative StyleDestyle Tuning and Editing. During iterations, image quality gets higher while key style features are gradually wiped off in the de-styled images. We show the style images and de-style results generated in 1st and 2nd de-styled phase and a plain image and results generated in 1st stylize phase.]({{ '/images/04-2024/StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction/figure_4.jpg' | relative_url }})
![Figure 5: Comparisons with instruction-based style editing baselines in Emu Edit benchmark. We show editing results of StyleBooth and 3 baselines. The results of StyleBooth are the most accurate in both style conveying and content preservation comparing to others, though some of the styles and instruction syntax are not contained in our tuning dataset.]({{ '/images/04-2024/StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction/figure_5.jpg' | relative_url }})
![Figure 6: Exemplar-based style editing comparisons The inputs include a style exemplar and an original image displayed on the left-bottom corner of exemplar images. StyleBooth achieves both accurate style extraction and transformation and identical content preservation.]({{ '/images/04-2024/StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction/figure_6.jpg' | relative_url }})
![Figure 7: StyleBooth compositional style editing and style interpolation. StyleBooth unifies textual and visual exemplar by mapping them into a same hidden space making it possible to adjust the proportion of different styles in different modalities.]({{ '/images/04-2024/StyleBooth:_Image_Style_Editing_with_Multimodal_Instruction/figure_7.jpg' | relative_url }})
