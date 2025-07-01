---
title: FunEditor:_Achieving_Complex_Image_Edits_via_Function_Aggregation_with_Diffusion_Models
layout: default
date: 2024-08-16
---
![Figure 1: (a) Results of applying the two basic functions —Edge Enhancement (center) and Object Removal (right)—using their respective masks on the input image Best viewed when enlarged. (b) Demonstration of function aggregation using the proposed method. By simultaneously applying Object Removal and Edge Enhancement on different masks, complex edits such as object shrinking (middle) and object movement (right) can be achieved. A represents the operation of function aggregation.]({{ '/images/08-2024/FunEditor:_Achieving_Complex_Image_Edits_via_Function_Aggregation_with_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address two key limitations in existing diffusion-based image editing models. First, these models struggle to apply multiple, complex edits simultaneously, forcing them into an inefficient sequential process that can accumulate errors. Second, relying on purely textual instructions to define the edit region often leads to unintended alterations in other parts of the image. The paper aims to create a method that can perform complex edits (like object movement) efficiently in a single step while maintaining high fidelity and localization.

## 2. Key Ideas and Methodology
The core idea is **function aggregation**, where complex edits are decomposed into and performed by combining simpler, "atomic" functions. The proposed model, **FunEditor**, learns these atomic functions (e.g., object removal, edge enhancement, harmonization) individually during training.

-   **Methodology:** Each atomic function is represented by a unique, learnable **task token** (e.g., `<Task_OR>`) added to the text encoder's vocabulary. During inference, a complex task is executed by providing a combination of these learned tokens as a prompt.
-   **Localization:** To ensure edits are applied only to specific regions, the model uses a **cross-attention (CA) masking** technique. This modifies the attention maps to restrict each task token's influence to its corresponding user-provided mask, preventing unwanted changes to the background.
-   **Efficiency:** The framework is compatible with few-step inference techniques like Latent Consistency Models (LCM), enabling high-quality edits in just 4 steps.

## 3. Datasets Used / Presented
-   **Evaluation Datasets:** The model's performance on complex tasks was evaluated using two main datasets:
    -   **COCOEE:** A benchmark of 100 images with masks and vectors for the object movement task.
    -   **ReS dataset:** Contains 100 pairs of real-world images with challenging object movement scenarios.
-   **Training Datasets:** The model was trained by fine-tuning an InstructPix2Pix (IP2P) backbone on various datasets for atomic tasks like object removal and harmonization. The paper notes that data for these simple tasks is abundant or easy to collect.

## 4. Main Results
FunEditor significantly outperforms existing training-based and optimization-based methods in both efficiency and quality.

-   **Efficiency:** For the object movement task, FunEditor requires only 4 inference steps and takes ~1 second, making it 5-24x faster than baselines like DiffEditor (24 seconds) and AnyDoor (12 seconds).
-   **Quality:** On the COCOEE dataset, FunEditor achieved superior object consistency (LPIPS score of 0.017 vs. >0.034 for all baselines) and better background preservation (LPIPS of 0.066 vs. >0.089). Similar gains were observed on the ReS dataset.
-   **Author's Takeaway:** By aggregating simple, well-learned functions, FunEditor can achieve superior results on complex editing tasks more efficiently than models designed specifically for those tasks.

## 5. Ablation Studies
The paper presents a qualitative ablation study on the effect of **cross-attention (CA) masking**.

-   **Experiment:** An image harmonization task was performed with and without the CA masking technique.
-   **Impact:** Without CA masking, the harmonization edit "leaked" and affected the entire image, causing undesired global changes. With CA masking enabled, the edit was correctly confined to the specified masked region, demonstrating that this component is crucial for achieving precise, localized control.

## 6. Paper Figures
![Figure 2: Our approach is capable of composing multiple editing functions and applying them simultaneously. This enables it to perform complex edit functions such as object movement, object resizing, and object pasting in 4 steps . f OR , f EE , and f HR refer to object removal, edge enhancement, and harmonization functions, respectively. Each function is applied only to the specified mask region. To save space, source image I is omitted from the function arguments.]({{ '/images/08-2024/FunEditor:_Achieving_Complex_Image_Edits_via_Function_Aggregation_with_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3: Overview of our proposed training and inference pipeline. During the basic task training phase (a) the diffusion model learns to perform various simple tasks based on the provided task tokens and masks. During inference (b), we could implement complex edit functions by combining multiple task masks and tokens.]({{ '/images/08-2024/FunEditor:_Achieving_Complex_Image_Edits_via_Function_Aggregation_with_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4: Harmonization without cross-attention masking affects the entire image (a). While with masking, edits are confined to the masked region, (b), preventing changes to unmasked areas. Mask is indicated by the top right minifigure.]({{ '/images/08-2024/FunEditor:_Achieving_Complex_Image_Edits_via_Function_Aggregation_with_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative comparison between our approach and baseline methods for object repositioning within an image, demonstrating the superior performance of our method. To move an object, FunEditor composes object removal and edge enhancement functions.]({{ '/images/08-2024/FunEditor:_Achieving_Complex_Image_Edits_via_Function_Aggregation_with_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6: Visual comparison between our method and baseline methods for object pasting from a reference image into a target image. FunEditor applies harmonization and edge enhancement functions to seamlessly paste an object into another image.]({{ '/images/08-2024/FunEditor:_Achieving_Complex_Image_Edits_via_Function_Aggregation_with_Diffusion_Models/figure_6.jpg' | relative_url }})
