---
title: In-Context_Learning_Unlocked_for_Diffusion_Models
layout: default
date: 2023-05-01
---
## In-Context Learning Unlocked for Diffusion Models
**Authors:**
- Zhendong Wang
- Mingyuan Zhou, h-index: 44, papers: 169, citations: 6946

**ArXiv URL:** http://arxiv.org/abs/2305.01115v2

**Citation Count:** 78

**Published Date:** 2023-05-01

![Figure 1: Illustration of the in-context learning ability enabled by our proposed Prompt Diffusion for conditioned image generation tasks: With a prompt consisting of a task-specific example pair of images and text guidance , given a new query image that aligns in type with the source image in the example pair, Prompt Diffusion can comprehend the desired task and generate the corresponding output image on both seen (trained) and unseen (new) task types.]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limited application of in-context learning, a paradigm successful in Large Language Models (LLMs), to the field of computer vision. Unlike LLMs that can perform new tasks based on a few examples in a prompt, most large vision models are trained for specific tasks (e.g., segmentation, generation) and lack this flexibility. The paper aims to unlock in-context learning for diffusion-based generative models, enabling them to understand and perform a wide range of vision tasks specified by a prompt containing example image pairs.

## 2. Key Ideas and Methodology
The core of the paper is **Prompt Diffusion**, a framework that enables in-context learning in a diffusion model.

-   **Vision-Language Prompt:** The key idea is a novel prompt structure: `{text-guidance, example: (image1 → image2), image-query: image3}`. The `example` pair demonstrates the desired transformation (e.g., HED map to image), `image-query` is the new input for the task, and `text-guidance` provides semantic control over the output.
-   **Model Architecture:** Prompt Diffusion is built upon the Stable Diffusion and ControlNet architecture. The example pair and query image are processed by dedicated convolutional encoders and fed into the ControlNet branch, which provides conditional control. The text guidance is processed by a standard text encoder and influences generation through the cross-attention layers of the Stable Diffusion branch.
-   **Multi-Task Joint Training:** To acquire the in-context learning ability, the model is not trained on a single task. Instead, it is jointly fine-tuned on six different vision-language tasks (depth/hed/seg-to-image and their inverses) simultaneously. This forces the model to learn the underlying relationship from the example pairs rather than memorizing a single task.

## 3. Datasets Used / Presented
The authors use a public dataset from Brooks et al. (InstructPix2Pix), which contains approximately 310,000 image-caption pairs. They augment this base dataset by generating corresponding conditional maps for each image:
-   **Depth maps:** Generated using Midas.
-   **Segmentation maps:** Generated using Uniformer.
-   **HED maps:** Generated using the HED boundary detector.
These maps, paired with the original images, are used to construct the prompts for training the six "forward" (image-to-map) and "inverse" (map-to-image) tasks. Canny edge and normal maps were also generated for evaluating generalization on unseen tasks.

## 4. Main Results
Prompt Diffusion demonstrates strong performance in both multi-task learning and generalization to new, unseen tasks.

-   **Quantitative Comparison:** Compared to a ControlNet model fine-tuned on each task individually (CN-FT), Prompt Diffusion achieves comparable or superior performance. For inverse tasks (e.g., depth-to-image), it achieves a Fréchet Inception Distance (FID) of 18.60 vs. 19.81 for CN-FT. For forward tasks (e.g., image-to-hed), it achieves a Root Mean Square Error (RMSE) of 0.14 vs. 0.18 for CN-FT.
-   **Author-claimed Impact:** The authors present Prompt Diffusion as the first diffusion-based vision-language foundation model capable of in-context learning. It successfully generalizes to novel tasks like scribble-to-image, style transfer, and Canny-edge-to-image without any task-specific fine-tuning, purely by being provided with a new example pair in the prompt.

## 5. Ablation Studies
An ablation study was conducted to validate the roles of the different components in the vision-language prompt.

-   **Varying the Example Pair:** When the example pair images were changed while keeping the task type the same, the model's output remained consistent, showing it learns the underlying task correlation rather than memorizing specific images.
-   **Varying the Image Query:** Changing the query image resulted in a dramatically different output that was consistent with the new query, confirming its role as the primary structural input.
-   **Varying Text Guidance:** Modifying the text prompt altered the semantic content of the generated image (e.g., changing object colors or styles) while preserving the structure from the query image.
-   **Mismatched Query Type:** Providing a query image of a different type than the source image in the example pair (e.g., a real image query for a depth-to-image task) led to unpredictable and poor-quality results, highlighting the importance of prompt consistency.

## 6. Paper Figures
![Figure 2: Illustration of Prompt Diffusion trained jointly on six different vision-language tasks. Each gray-dashed box represents a task example: prompt → output . The output is a random generation from our trained model given a vision-language prompt, where the query image aligns in type with the source image from the example.]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3: Comparison of the model architectures of ControlNet (Left) and Prompt Diffusion (Right). More details on the network structures of Prompt Diffusion-induced modules can be found in Appendix C.]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4: Qualitative Results of forward tasks and inverse tasks. We show examples of applying our Prompt Diffusion on the six trained tasks (inv-depth/hed/seg and forward-depth/hed/seg).]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5: Generalization to New Tasks. We show Prompt Diffusion has a promising generalization ability to new, unseen tasks, such as Inv-Scribble, Inv-Edge (CannyEdge), and Inv-Normal (Normal map).]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6: We perform Prompt Diffusion on two completely new tasks: style transfer and misaligned input-output example pairs. The first two rows show the style transfer results while the last two rows show the misaligment results.]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_6.jpg' | relative_url }})
![Figure 7: Image Editing Results. We demonstrate that Prompt Diffusion excels in image editing tasks through two strategies: one-step and two-step. One-step: when only the image condition, e.g. , depth/seg/hed maps, is given, our model would edit the condition for generation according to the text descriptions. Two-Step: when the original image is given, we first do forward sampling to sample image conditions and then conduct inverse tasks to edit the condition with text guidance. Two-Step provides more controllable editing.]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_7.jpg' | relative_url }})
![Figure 8: We present some failure cases of Prompt Diffusion when generalizing to new, unseen tasks under ambiguous text guidance.]({{ '/images/05-2023/In-Context_Learning_Unlocked_for_Diffusion_Models/figure_8.jpg' | relative_url }})
