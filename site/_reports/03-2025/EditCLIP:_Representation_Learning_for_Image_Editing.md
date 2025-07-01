---
title: EditCLIP:_Representation_Learning_for_Image_Editing
layout: default
date: 2025-03-26
---
![Figure 1. EditCLIP provides a unified representation of image edits by encoding the transformation between an image and its edited counterpart within the CLIP space. We demonstrate the effectiveness of EditCLIP embeddings in exemplar-based image editing and automated evaluation of image editing pipelines, where it achieves better alignment with human assessment.]({{ '/images/03-2025/EditCLIP:_Representation_Learning_for_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address two primary challenges in diffusion-based image editing. First, existing methods that rely on textual instructions struggle to handle complex, artistic, or compound edits that are difficult to describe in words. Second, the automated evaluation of these edits is flawed; current metrics like CLIP score often fail to penalize unwanted structural changes in the edited image, forcing a reliance on costly and time-consuming human studies. The paper aims to solve both problems by creating a unified representation for image edits.

## 2. Key Ideas and Methodology
The core idea is to learn an "edit embedding" that directly represents the transformation between an input image and its edited version. The authors introduce **EditCLIP**, a model that modifies the CLIP architecture to achieve this.

The key methodological steps are:
- **Edit Encoding:** The visual encoder of EditCLIP is trained on a concatenated pair of an input image and its edited counterpart. This forces the model to learn the semantic and visual difference, i.e., the edit itself.
- **Contrastive Pre-training:** This learned edit embedding is aligned with the text embedding of the corresponding edit instruction using a contrastive loss, similar to the original CLIP. The text encoder remains frozen.
- **Exemplar-Based Editing:** The trained EditCLIP encoder can generate an edit embedding from any reference image pair. This embedding is then used as a conditioning signal for a diffusion model (InstructPix2Pix), replacing the need for a text prompt and enabling complex edits by example.
- **Automated Evaluation:** The edit embeddings serve as a basis for new evaluation metrics (`EC2T` and `EC2EC`) that measure the similarity between a generated edit and either a text instruction or a reference edit, providing a more holistic assessment of quality and structural preservation.

## 3. Datasets Used / Presented
- **Instruct-Pix2Pix (IP2P):** A dataset containing approximately 313,000 triplets of an input image, an edited image, and the corresponding text instruction. It was used for pre-training the EditCLIP model and for fine-tuning the exemplar-based editing pipeline.
- **TOP-Bench-X:** An adaptation of the TOP-Bench dataset, used for evaluation. It contains 1,277 samples across various edit types, comprising 257 unique exemplar pairs and 124 unique query images. It was used to benchmark exemplar-based editing performance and validate the proposed evaluation metrics against human judgments.

## 4. Main Results
- **Exemplar-Based Editing:** EditCLIP outperforms state-of-the-art methods in exemplar-based editing. In a two-alternative forced-choice (2AFC) user study, EditCLIP was consistently preferred for both edit quality and preservation of query image details. Quantitatively, it achieves the highest score (0.477) on the proposed `EC2EC` metric and is significantly more efficient, with a runtime of 1.8 seconds compared to competitors like InstaManip (14.9s).
- **Automated Evaluation:** The proposed evaluation metrics show a stronger correlation with human judgment than existing metrics. For text-based editing, `EC2T` aligns best with human ratings for edit quality and preservation. For exemplar-based editing, `EC2EC` achieves a Pearson correlation of 0.372 for edit quality, significantly outperforming the prior `Svisual` metric. This demonstrates that EditCLIP provides a more reliable automated measure of edit success.

## 5. Ablation Studies
- **Conditioning Embedding:** The authors compared their proposed method of concatenating the input and edited images for the visual encoder against simpler strategies (e.g., using only the edited image embedding, or summing/concatenating embeddings from a standard CLIP encoder). The proposed method was qualitatively superior, as alternatives either failed to capture the edit or uncontrollably blended the images.
- **Choice of Embedding Layer:** Using the hidden states from the last transformer layer of the visual encoder as the conditioning signal was found to be more effective than using the final projected embedding. The hidden states contain more detailed visual information, leading to better edit transfer and layout preservation.
- **Input Loss Preservation:** The weight of the LPIPS loss, which encourages preservation of the original image structure, was ablated. A small weight (0.05) was found to provide the best balance between applying the desired edit and maintaining faithfulness to the input image.

## 6. Paper Figures
![Figure 2. An overview of our proposed approach. EditCLIP is pre-trained similarly to CLIP, but the visual encoder processes a concatenated exemplar image pair. After pre-training, EditCLIP can replace the text encoder in InstructPix2Pix [ 4 ] to enable exemplar-based editing.]({{ '/images/03-2025/EditCLIP:_Representation_Learning_for_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3. A visualization of the visual encoder’s attention in EditCLIP compared to the original CLIP. We visualize the attention of the [ CLS ] token from the last attention head. Unlike CLIP, where attention is dispersed across the image, EditCLIP focuses on the differences between the input and edited image, indicating that it effectively captures the edited regions.]({{ '/images/03-2025/EditCLIP:_Representation_Learning_for_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Qualitative comparison for exemplar-based image editing.]({{ '/images/03-2025/EditCLIP:_Representation_Learning_for_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5. EditCLIP can perform complex edits when the exemplars contain multiple edits in a single step.]({{ '/images/03-2025/EditCLIP:_Representation_Learning_for_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Ablation of different conditioning embeddings using the original CLIP visual encoder F θ . EditCLIP embedding greatly outperforms all CLIP variations.]({{ '/images/03-2025/EditCLIP:_Representation_Learning_for_Image_Editing/figure_6.jpg' | relative_url }})
