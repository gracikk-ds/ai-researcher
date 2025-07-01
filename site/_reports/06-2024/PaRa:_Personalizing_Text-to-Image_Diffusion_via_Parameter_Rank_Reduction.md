---
title: PaRa:_Personalizing_Text-to-Image_Diffusion_via_Parameter_Rank_Reduction
layout: default
date: 2024-06-09
---
![Figure 1: Comparison between LoRA [ 7 ] and our propsoed PaRa on T2I personalization for learning a new concept of bear, i . e ., “ [V] ”. For a fair comparison, we set the rank as 4 and adopt the same latent noise for both methods. LoRA scale is set to 1.0.]({{ '/images/06-2024/PaRa:_Personalizing_Text-to-Image_Diffusion_via_Parameter_Rank_Reduction/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of personalizing large-scale Text-to-Image (T2I) diffusion models. The core problem is the trade-off between learning a new visual concept from a few examples (target alignment) and preserving the model's general knowledge and ability to respond to diverse text prompts (text editability). Existing methods often struggle with this balance, either failing to capture the new concept accurately or overfitting to the limited training data, thereby losing creative flexibility.

## 2. Key Ideas and Methodology
The paper introduces **PaRa (Parameter Rank Reduction)**, a novel fine-tuning framework.

- **Core Principle**: The authors hypothesize that personalizing a model for a specific concept (e.g., a particular art style) corresponds to constraining its vast generation space into a smaller, more focused one. They propose that explicitly reducing the rank of the model's parameter matrices is an effective way to achieve this constraint.
- **Methodology**: Instead of adding low-rank updates like the popular LoRA method, PaRa directly reduces the rank of the pre-trained weight matrices. For a given weight matrix `Wo`, a learnable matrix `B` is introduced. Through QR decomposition, `B` yields an orthonormal basis `Q`. The final weight matrix is computed as `W_reduce = Wo - Q * Q^T * Wo`, which effectively removes the components of `Wo` that lie in the learned subspace `Q`. This steers the generation process towards the target concept.
- **Key Features**: This approach is parameter-efficient (requiring half the parameters of LoRA for the same rank), supports combining multiple personalized concepts by sequentially applying rank reductions, and enables stable single-image editing without needing complex noise inversion techniques.

## 3. Datasets Used / Presented
- **Dreambooth Dataset**: This dataset was the primary source for single-subject personalization experiments. The authors used several concepts from it (e.g., `bear_plushie`, `cat`, `ducktoy`) to train and evaluate their method. Each concept consists of a small set of training images (typically 3-5).
- **Stable Diffusion XL (SDXL 1.0)**: This was used as the base pre-trained T2I diffusion model for all personalization experiments.
- **Public LoRA Models**: To demonstrate compatibility, the authors combined PaRa with publicly available, pre-trained LoRA models for stylistic generation, sourced from platforms like Civitai.

## 4. Main Results
- **Superior Image Alignment and Efficiency**: PaRa achieves better alignment with the target concept compared to baseline methods like LoRA and SVDiff, while using 2x fewer learnable parameters than LoRA.
- **Effective Multi-Subject Generation**: PaRa can successfully combine two independently trained concepts into a single coherent image without requiring special training data or techniques. In contrast, LoRA often fails, generating only one of the concepts or creating unrealistic "hybrid" subjects.
- **Stable Single-Image Editing**: PaRa demonstrates high stability in one-shot image editing. When editing a prompt, it preserves the unedited parts of the image much more faithfully than baselines, achieving significantly higher average SSIM scores.
- **Strong User Preference**: In a human evaluation survey with 209 participants, PaRa's generated images were overwhelmingly preferred over LoRA's for both single-subject (e.g., 96% preference for one subject) and multi-subject generation tasks.

## 5. Ablation Studies
- **Effect of Rank Reduction (`r`)**: The authors tested various ranks (`r` from 1 to 16). They found that increasing `r` improves faithfulness to the training concept but reduces the model's editability and diversity. A lower `r` provides more creative control via the text prompt, demonstrating a clear trade-off that can be controlled by this hyperparameter.
- **Tuning Different Parameter Subsets**: Experiments were run on finetuning different subsets of the UNet's parameters (e.g., only attention layers, excluding attention layers). The "Exclude Cross-Attention" (ExCA) subset was found to offer a good balance of performance and parameter efficiency.
- **Order of Combination with LoRA**: The study confirmed that the order of application matters. Applying PaRa first to constrain the space and then applying LoRA to add stylistic details works effectively. The reverse order (LoRA then PaRa) severely degrades performance, as PaRa attempts to cancel out the changes introduced by LoRA.
- **Rank Boundary (`γ`)**: A hyperparameter `γ` was introduced to cap the maximum rank reduction and prevent model collapse, especially when using high ranks or combining multiple models. Empirical results showed that a value around `γ = 1/40` provided stable performance.

## 6. Paper Figures
![Figure 2: Comparing the proposed PaRa with LoRA [ 18 ] and SVDiff [ 15 ] on single-subject generation. Each subject has 5 training images. PaRa includes results with ranks r ranging from 1 to 16. For LoRA, we adopt a rank of 8. We provide more generation results on Dreambooth and Textual Inversion in Appendix F.]({{ '/images/06-2024/PaRa:_Personalizing_Text-to-Image_Diffusion_via_Parameter_Rank_Reduction/figure_2.jpg' | relative_url }})
![Figure 4: Examples of multi-subject generation results. The PaRa results are generated with the reduced rank r 1 = 2 for Concept 1 and r 2 being 8 and 32 for Concept 2. LoRA results are generated with the best rank of 16 for both concepts and the scale value of 1.]({{ '/images/06-2024/PaRa:_Personalizing_Text-to-Image_Diffusion_via_Parameter_Rank_Reduction/figure_4.jpg' | relative_url }})
![Figure 5: Single-image editing results. PaRa allows for image editing through one-shot learning of the original image and performs generation by directly modifying the prompt. We can see that PaRa achieves the expected modifications and preserves the personalized target subject well. In addition, PaRa achieves high consistency with untargeted elements of the initial image under different Gaussian noises.]({{ '/images/06-2024/PaRa:_Personalizing_Text-to-Image_Diffusion_via_Parameter_Rank_Reduction/figure_5.jpg' | relative_url }})
![Figure 6: Generation results of combining PaRa with LoRA. Top: the results of first applying PaRa and then LoRA; Bottom: the results of first applying LoRA and then PaRa.]({{ '/images/06-2024/PaRa:_Personalizing_Text-to-Image_Diffusion_via_Parameter_Rank_Reduction/figure_6.jpg' | relative_url }})
