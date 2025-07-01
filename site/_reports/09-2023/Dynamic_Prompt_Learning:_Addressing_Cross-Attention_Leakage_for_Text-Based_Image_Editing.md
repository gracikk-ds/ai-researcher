---
title: Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing
layout: default
date: 2023-09-27
---
![Figure 1: Compared with other image editing methods, our DPL achieves more consistent layout when modifying one or more objects in the image and keeping other content frozen. And also the desired editing is correctly delivered to the corresponding area. DiffEdit [ 9 ] method thoroughly fails to detect the editing region in multi-object cases. And Null-Text inversion (NTI [ 28 ]) is unable to perfectly distinguish the objects in the given image since the cross-attention maps are suffering background leakage ( yellow circle) and distractor object leakage ( red circle). DPL can more successfully localize the objects in the textual prompts, thus benefits for future editing. Here the 16 × 16 cross-attention maps are interpolated to the image size for better view. (image credits: gettyimages)]({{ '/images/09-2023/Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a critical problem in text-guided image editing with diffusion models: **cross-attention leakage**. When a user modifies a text prompt to edit a specific object in an image, existing methods often cause unintended changes to other regions, such as the background or other "distractor" objects that are semantically or visually related. The paper posits that this failure stems from inaccurate cross-attention maps, which do not correctly associate noun words in the prompt with their corresponding object pixels in the image, especially in complex, multi-object scenes.

## 2. Key Ideas and Methodology
The core idea is **Dynamic Prompt Learning (DPL)**, a method to refine cross-attention maps without fine-tuning the diffusion model itself. Instead of using static text embeddings, DPL treats the embeddings for noun words in the prompt as learnable variables that are optimized at each denoising timestep.

The optimization is guided by three novel loss functions:
1.  **Disjoint Object Attention Loss:** Minimizes the spatial overlap between the attention maps of different nouns, forcing the model to disentangle distinct objects.
2.  **Background Leakage Loss:** Penalizes attention on background regions, which are identified by clustering the model's self-attention maps. This prevents foreground object concepts from "leaking" into the background.
3.  **Attention Balancing Loss:** Encourages each object's attention map to be concentrated and strong, preventing diffuse or weak localization.

By dynamically updating the noun tokens using these losses, DPL generates more precise cross-attention maps, which can then be used by existing editing frameworks like Prompt-to-Prompt (P2P) to achieve cleaner, more accurate edits.

## 3. Datasets Used / Presented
The authors created and used two main datasets for their experiments, both derived from the large-scale LAION-5B dataset:
*   **MO-Set (Multi-Object Set):** A custom collection of 100 real, multi-object images. This set was used for quantitative ablation studies. The authors manually created segmentation masks for these images to serve as ground truth for evaluating the localization accuracy (IoU) of the attention maps.
*   **URS-Set (User-Study Related Set):** A set of 60 multi-object images featuring semantically related objects, used to conduct a forced-choice user study comparing DPL to a baseline method.

## 4. Main Results
DPL demonstrates superior performance both quantitatively and qualitatively. When combined with the P2P editing framework, DPL consistently outperforms the strong baseline (NTI+P2P).

*   **Quantitative Metrics:** In a multi-object editing task (e.g., "cat and dog" → "leopard and tiger"), DPL achieved a higher CLIP-Score (32.23% vs. 31.50%) and a significantly lower Structure-Distortion (0.0312 vs. 0.0800), indicating better alignment with the target prompt while preserving the original image structure.
*   **User Study:** In a head-to-head comparison, evaluators overwhelmingly preferred the editing results from DPL, choosing it over the baseline **87.2%** of the time.

The authors claim that DPL effectively resolves the cross-attention leakage problem, enabling more robust and fine-grained text-based editing, particularly for complex scenes with multiple objects.

## 5. Ablation Studies
The authors performed an ablation study on the MO-Set to validate the contribution of each component of their proposed loss function. They measured the Intersection over Union (IoU) between the generated attention maps and ground-truth object masks.

*   The **Disjoint Object Attention Loss** and **Background Leakage Loss** alone did not provide a significant improvement over the baseline.
*   The **Attention Balancing Loss** on its own offered a noticeable improvement in localization accuracy.
*   The full DPL model, combining all three losses, achieved the highest IoU, demonstrating that all components are necessary and work synergistically to produce the most accurate cross-attention maps.

## 6. Paper Figures
![Figure 2: Dynamic Prompt Learning ( DPL ) first transforms the noun words in the text prompt into dynamic tokens. We register them in the token dictionary and initialize the representations by their original words at time T . Using DDIM inversion, we condition the DM-UNet with the original text condition C to get the diffusion trajectory { z t } T 0 and background mask B . In each denoising step ¯ z t − 1 → ¯ z t , we first update the dynamic token set V t with a background leakage loss, a disjoint object attention loss and an attention balancing loss, in order to ensure high-quality cross-attention maps. Then we apply Null-Text inversion to approximate the diffusion trajectory.]({{ '/images/09-2023/Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: After DDIM inversion, we visualize the average of each component over T timestamps for the input image in Fig. 1 (with the prompt: "a cat and a dog"). From left to right, they are cross-attention (CA) for each noun word, then PCA&clustering of the self-attention (SA), query, key and value representations. Here, the maps are simply resized without any interpolation to demonstrate their original views.]({{ '/images/09-2023/Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Although cross-attention maps produce acceptable results in certain cases (up) with minor leakage, the object masks from self-cross attention matching are not always accurate due to the leakage problem (down). However, as the cross-attention maps tend to concentrate on the foreground objects, the background masks remain reliable.]({{ '/images/09-2023/Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: (a) IoU curves drawn by varying the threshold from 0.0 to 1.0 for MO-Set . (b) We show some images for comparisons between the Null-Text inversion [ 28 ] and our method DPL demonstrated in cross-attention maps.]({{ '/images/09-2023/Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6: Attention refinement and reweighting. In the given text prompt, only one noun word is learnable. The flowers below the cake are playing as distractors which distort the cross-attention maps while Null-Text Inversion [ 28 ] is applied. As a comparison, our method DPL successfully filters the cross-attention by our background leakage loss.]({{ '/images/09-2023/Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing/figure_6.jpg' | relative_url }})
![Figure 7: Word-Swap by only modifying the regions corresponding to the target concept. We list the source prompts on the left with dynamic tokens in the curly brackets. Each line is corresponding to modifying one or multiple concepts with various methods.]({{ '/images/09-2023/Dynamic_Prompt_Learning:_Addressing_Cross-Attention_Leakage_for_Text-Based_Image_Editing/figure_7.jpg' | relative_url }})
