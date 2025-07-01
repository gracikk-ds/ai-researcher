---
title: Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing
layout: default
date: 2023-11-30
---
![Figure 1. Text-guided Image Editing results via C ontrastive D enoising S core. CDS successfully translates source images with a wellbalanced interplay between maintaining the structural elements of the source image and transforming the content in alignment with the target text prompt.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Existing text-guided image editing methods based on diffusion models, particularly Delta Denoising Score (DDS), often fail to preserve the structural integrity (e.g., pose, layout, background) of the source image. While they excel at modifying content to match a target text prompt, this lack of structural consistency limits their practical use. The authors address this gap by introducing a method to enforce structural correspondence between the source and edited image within the DDS framework.

## 2. Key Ideas and Methodology
The paper proposes **Contrastive Denoising Score (CDS)**, a modification of DDS that integrates a contrastive loss to maintain structural similarity. The core idea is inspired by Contrastive Unpaired Translation (CUT), but adapted for latent diffusion models (LDMs) in a zero-shot, training-free manner.

Instead of training an auxiliary network, CDS leverages the rich spatial information present in the intermediate features of the LDM's U-Net, specifically from the **self-attention layers**. During the DDS optimization process, a patch-wise contrastive loss (PatchNCE) is calculated. This loss maximizes the mutual information between corresponding patches in the self-attention feature maps of the source and target editing branches, while minimizing it for non-corresponding patches. This acts as a regularization term, guiding the edit to preserve the original structure while still transforming the content as directed by the text prompt.

## 3. Datasets Used / Presented
- **LAION 5B:** For quantitative evaluation, the authors collected 250 cat images from this dataset to test object transformation tasks (e.g., cat→dog, cat→cow, cat→pig).
- **Pre-trained NeRF models (TensoRF):** Used to demonstrate the method's applicability to 3D object editing by fine-tuning pre-trained Neural Radiance Fields.
- Various stock images were used for qualitative examples throughout the paper.

## 4. Main Results
- **Quantitative:** In cat-to-dog/cow/pig translation tasks, CDS demonstrated a superior balance between edit accuracy and structural preservation. Compared to vanilla DDS, CDS achieved comparable or higher CLIP accuracy while significantly reducing structural distortion, as measured by lower DINO-ViT structure distance and LPIPS scores. For instance, in the cat→dog task, CDS achieved a DINO-ViT distance of 0.020 versus 0.023 for DDS.
- **Qualitative:** Visual results show that CDS successfully edits objects according to the text prompt while preserving the original pose, composition, and background, unlike baseline methods which often produce severe structural artifacts.
- **User Study:** CDS was rated highest by human evaluators across all criteria: text-match (4.43/5), structural consistency (4.65/5), and overall quality (4.20/5).
- The authors claim that CDS provides a simple yet powerful way to achieve high-fidelity, structure-preserving image editing that is extendable to other domains like NeRF.

## 5. Ablation Studies
- **Effect of Contrastive Loss:** Removing the proposed contrastive loss (`l_con`) reverts the method to vanilla DDS, leading to a noticeable loss of structural details (e.g., animal pose). Including the loss effectively preserves these structures.
- **Feature Extraction Layer:** The authors evaluated applying the contrastive loss to different feature spaces: the final score output, cross-attention layers, and self-attention layers. Applying it to self-attention layers yielded the best performance, confirming that these layers contain disentangled spatial information ideal for enforcing structural consistency.
- **Contrastive Loss Weight:** Varying the weight of the loss allows for a controllable trade-off. Higher weights increase structural preservation at the risk of constraining the edit, while lower weights allow more semantic change at the cost of structure.
- **Patch Size & Number:** Experiments showed that smaller patch sizes (1x1, 2x2) are more effective in the compact latent space, and using a larger number of patches (256) improves the preservation of fine-grained structural details.

## 6. Paper Figures
![Figure 2. Overall pipeline of CDS . We extract the intermediate features of the self-attention layers and calculate ℓ con . This loss enables us to regulate structural consistency and generate reliable images.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3. Comparison with baseline models. CDS demonstrates outstanding performance in effectively regulating structural consistency.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4. Sample results of the cat2dog task from DDS and CDS.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5. Gradient visualization on DDS and CDS.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6. Qualitative results for ablation study on feature extraction location for contrastive loss.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7. Ablation study on weights of contrastive loss.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_7.jpg' | relative_url }})
![Figure 8. Comparison with feature injection method.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_8.jpg' | relative_url }})
![Figure 9. Results on NeRF editing. As an extension of our proposed framework, we applied our method to the NeRF 3D object editing task.]({{ '/images/11-2023/Contrastive_Denoising_Score_for_Text-guided_Latent_Diffusion_Image_Editing/figure_9.jpg' | relative_url }})
