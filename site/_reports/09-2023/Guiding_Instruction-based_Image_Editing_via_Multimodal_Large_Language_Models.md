---
title: Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models
layout: default
date: 2023-09-29
---
![Figure 1: We introduce MLLM-Guided Image Editing (MGIE) to improve instruction-based image editing for various editing aspects. The top is the input instruction, and the right is the jointly derived expressive instruction by MGIE.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current instruction-based image editing models struggle to follow human commands that are often brief and ambiguous. For example, an instruction like "make it more healthy" lacks the specific details needed for a model to perform a precise edit. This gap exists because existing methods, which typically use static text encoders like CLIP, are not designed to understand the visual context of an image and infer the user's underlying intent. The authors address this by proposing a method that can derive more detailed and explicit guidance from simple instructions by reasoning about the image content.

## 2. Key Ideas and Methodology
The paper introduces **MLLM-Guided Image Editing (MGIE)**, a framework that leverages a Multimodal Large Language Model (MLLM) to enhance instruction-based editing.

-   **Core Idea:** The central hypothesis is that an MLLM can interpret a brief user instruction in the context of an input image to generate a more detailed, "expressive instruction." This expressive instruction serves as explicit guidance for the editing model, bridging the gap between the user's concise command and the model's need for detailed direction. For instance, given an image of a pizza and the instruction "make it more healthy," the MLLM might generate "add vegetable toppings, such as tomatoes and herbs."

-   **Methodology:** MGIE consists of two main components trained end-to-end:
    1.  **A Multimodal Large Language Model (MLLM):** This model takes the input image and user instruction to autoregressively generate the expressive instruction. To make this guidance concise, the authors first generate a detailed explanation and then use a summarizer to create the final expressive instruction.
    2.  **A Latent Diffusion Model:** This model performs the actual image edit. It is guided by the latent "visual imagination" derived from the MLLM's output, which is passed through a dedicated "edit head" to be transformed into visual guidance. This joint training allows the MLLM to learn to produce guidance that is most effective for the diffusion model.

## 3. Datasets Used / Presented
-   **IPr2Pr:** A large-scale dataset with 1 million synthetic image-instruction-goal triplets, used for pre-training the models.
-   **EVR:** Contains 5.7K triplets from Photoshop forums, used for evaluating Photoshop-style modifications.
-   **GIER:** A larger dataset with 29.9K triplets from online forums, used for evaluating global photo optimization.
-   **MA5k:** Consists of 24.8K triplets focused on global attribute changes like brightness, contrast, and saturation.
-   **MagicBrush:** A manually annotated dataset with 10.5K triplets for evaluating various local and global editing tasks.

## 4. Main Results
MGIE demonstrates significant improvements over existing methods across various editing tasks in both zero-shot and fine-tuned settings.

-   **Quantitative Results:** In fine-tuned experiments on the MagicBrush dataset, MGIE achieved superior performance on key metrics, such as a DINO score of 90.65 and a CVS score of 95.28, compared to the baseline InstructPix2Pix (87.99 DINO, 93.83 CVS). Similar gains were observed across all other evaluation datasets (EVR, GIER, MA5k).
-   **Qualitative Results:** Visual comparisons show that MGIE produces more plausible and instruction-aligned edits. For example, when asked to "let the donuts have strawberry glaze on them," MGIE correctly applies the glaze only to the donuts, whereas baselines incorrectly alter the entire image.
-   **Author's Takeaway:** The authors conclude that expressive instructions derived with visual awareness are crucial for high-quality instruction-based image editing, and MGIE effectively provides this guidance, leading to notable performance improvements while maintaining competitive inference efficiency.

## 5. Ablation Studies
The paper includes several ablation studies to validate the design choices of MGIE.

-   **Training Strategy:** The authors compared three strategies for using expressive instructions:
    1.  **FZ (Frozen):** Using expressive instructions with a frozen baseline model. This yielded minimal to no improvement.
    2.  **FT (Fine-tuning):** Fine-tuning the baseline on expressive instructions. This showed moderate improvement.
    3.  **E2E (End-to-End):** The proposed joint training of the MLLM and diffusion model. This achieved the best performance, demonstrating the importance of co-adapting the guidance generation and editing modules.
-   **Role of Visual Perception:** A variant named LGIE, which uses a text-only LLM (without image input) to generate expressive instructions, was consistently outperformed by MGIE. This highlights that visual perception is critical for generating relevant and effective editing guidance.
-   **Instruction Loss:** Removing the loss for training the MLLM to generate concise instructions (`L_ins`) caused a significant drop in performance. This confirms the necessity of explicitly training the MLLM to produce succinct and relevant guidance.

## 6. Paper Figures
![Figure 2: Overview of MLLM-Guided Image Editing ( MGIE ), which leverages MLLMs to enhance instruction-based image editing. MGIE learns to derive concise expressive instructions and provides explicit visual-related guidance for the intended goal. The diffusion model jointly trains and achieves image editing with the latent imagination through the edit head in an end-to-end manner.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_2.jpg' | relative_url }})
![Figure 3: Trade-off curve for image editing . We set α X as 7.5 and vary α V in [1 . 0 , 2 . 2] . For both edit (X-axis) and input consistency (Yaxis), higher is better.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_3.jpg' | relative_url }})
![Figure 4: CLIP-S across images (input / goal) and expressive instructions.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_4.jpg' | relative_url }})
![Figure 5: Human eval of expressive instructions quality.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_5.jpg' | relative_url }})
![Figure 6: Human eval of image editing results in terms of instruction following, ground-truth relevance, and overall quality.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_6.jpg' | relative_url }})
![Figure 7: Qualitative comparison between InsPix2Pix, LGIE, and our MGIE. For the 1st example, MGIE can showcase the clear “ lightning ” in the sky and its reflection on the water. For the 2nd one, although LGIE accurately targets the Christmas tree, only MGIE removes it in the background. For photo optimization (the 3rd example), InsPix2Pix fails to adjust the brightness, and LGIE makes the whole photo white and obviously distinct. In contrast, MGIE follows the instruction to brighten as well as sharpen it. Moreover, in the 4th one, MGIE puts the “ glaze ” only on the donuts, but baselines even draw the entire image in strawberry pink.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_7.jpg' | relative_url }})
![Figure 8: Qualitative comparison of expressive instructions by LGIE and our MGIE. Due to the limitation of the single modality, LGIE can only have language-based insight but may derive irrelevant or even wrong explanations for image editing ( e.g. , “ two people still in the foreground ” for GIER). With access to images, MGIE provides explicit visual imagination after the editing such as “ baby on the beach with a shark ” or “ bring out details of leaves and trunk ”. More surprisingly, we can link “ lightsaber or spaceship ” from Star Wars and describe “ chewing on the stick ” for the dog, which is aligned with the intended goal.]({{ '/images/09-2023/Guiding_Instruction-based_Image_Editing_via_Multimodal_Large_Language_Models/figure_8.jpg' | relative_url }})
