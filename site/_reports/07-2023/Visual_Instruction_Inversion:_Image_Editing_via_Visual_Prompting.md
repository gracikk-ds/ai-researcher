---
title: Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting
layout: default
date: 2023-07-26
---
## Visual Instruction Inversion: Image Editing via Visual Prompting
**Authors:**
- Thao Nguyen
- Yong Jae Lee

**ArXiv URL:** http://arxiv.org/abs/2307.14331v1

**Citation Count:** None

**Published Date:** 2023-07-26

![Figure 1: Image editing via visual prompting. Given a pair of before-and-after images of an edit, our approach (bottom) can learn and apply that edit along with the user’s text prompt to enable a more accurate and intuitive image editing process compared to text-only conditioned approaches (top).]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Text-based image editing can be powerful, but language is often ambiguous or insufficient for describing specific, nuanced visual transformations, such as a particular artistic style. It is often more intuitive and precise for a user to provide a "before" and "after" image pair to demonstrate the desired edit. This paper addresses the problem of how to leverage such visual prompts to guide modern text-to-image diffusion models, which typically rely on textual instructions.

## 2. Key Ideas and Methodology
The paper introduces **Visual Instruction Inversion (VISII)**, a framework to learn a text-based editing instruction from a visual example. The core hypothesis is that the rich instruction space of a pre-trained editing model can be inverted to find a latent text instruction that represents a visual transformation.

The methodology is as follows:
- It uses a frozen, pre-trained text-conditioned image editing model (InstructPix2Pix).
- Given a single "before" (`x`) and "after" (`y`) image pair, the goal is to optimize a latent text instruction (`c_T`).
- The optimization is guided by a two-part loss function:
    1.  **Image Reconstruction Loss (`L_mse`)**: Encourages the model to reconstruct the "after" image `y` when conditioned on the "before" image `x` and the learned instruction `c_T`.
    2.  **CLIP Direction Loss (`L_clip`)**: Aligns the learned instruction `c_T` with the editing direction vector calculated as the difference between the CLIP embeddings of the "after" and "before" images.
- Once learned, this instruction can be applied to new test images. It can also be concatenated with natural language prompts to create "hybrid instructions" for more complex edits.

## 3. Datasets Used / Presented
- **Clean-InstructPix2Pix dataset**: A dataset of over 450,000 synthetic before-after image pairs with corresponding ground-truth text instructions. The authors randomly sampled from this set to create their training and evaluation examples.
- **Real Image Pairs**: For further evaluation, the authors downloaded real photos and used other models (e.g., [51]) with manual text prompts to generate corresponding "after" images, creating new test pairs.

## 4. Main Results
- Qualitatively, the method successfully learns specific and nuanced editing styles from a single example pair. It produces edited images that are visually closer to the target style compared to state-of-the-art text-only methods like InstructPix2Pix and SDEdit, which can misinterpret ambiguous text prompts.
- Quantitatively, the approach is competitive with these baselines. It achieves the highest **Image CLIP Similarity**, indicating superior faithfulness to the input image's content. It performs comparably on **Directional CLIP Similarity** and the authors' proposed **Visual CLIP Similarity**, showing it effectively learns the intended transformation.
- The main takeaway is that the method achieves competitive results with state-of-the-art frameworks, even when learning from just one example pair.

## 5. Ablation Studies
- **Loss Function**: Adding the `L_clip` loss to the `L_mse` loss was critical. It significantly improved the Directional and Visual CLIP Similarity scores, confirming that it helps the model learn the correct *edit direction* rather than just memorizing the target image.
- **Instruction Initialization**: Initializing the instruction vector using a generated caption of the "after" image proved more effective than using a ground-truth text prompt, leading to better overall performance.
- **Noise Schedule**: Using a fixed noise sequence (i.e., reusing the same noise for inference that was sampled during optimization) led to a more balanced result, improving the trade-off between applying the edit and preserving the original image content compared to using random noise at test time.
- **Number of Examples**: Performance modestly improved as the number of example pairs increased from one to four, but strong results were already achievable with a single pair.

## 6. Paper Figures
![Figure 2: Image editing with visual prompting. (a) Text-conditioned scheme (Prior work): Model takes an input image and a text prompt to perform the desired edit. (b) Visual prompting scheme (Ours): Given a pair of before-after images of an edit, our goal is to learn an implicit text-based editing instruction, and then apply it to new images.]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_2.jpg' | relative_url }})
![Figure 3: Our framework . (a) Given an example before-and-after image pair, we optimize the latent text instruction that converts the “before” image to the “after” image using a frozen image editing diffusion model. (b) We leverage the CLIP embedding space to help learn the editing direction. (c) Once learned, the instruction can be applied to a new image to achieve the same edit. Optionally, the user can also combine the learned instruction with a natural text prompt to create a hybrid instruction.]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_3.jpg' | relative_url }})
![Figure 4: Instruction details . (a) Instruction Optimization: We only optimize a part of the instruction embedding c T , called <ins> . (b) Instruction Concatenation: During test time, we can add extra information into the learned instruction c T to further guide the edit.]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_4.jpg' | relative_url }})
![Figure 5: Qualitative comparisons. Our method learns edits from example pairs and thus can produce visually closer edited images to the target example than other state-of-the-art baselines.]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_5.jpg' | relative_url }})
![Figure 6: A variety of edits can be performed for “Turn it into a drawing/ painting” (Zoom in for details).]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_6.jpg' | relative_url }})
![Figure 8: Fixed noise leads to more balanced results . Different noises can lead to large variations in the output. Using the same training noises yields a balanced trade-off between editing manipulation and image reconstruction.]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_8.jpg' | relative_url }})
![Figure 9: Hybrid instruction . We can concatenate extra information into the learned instruction c T to navigate the edit. (Zoom in for details.)]({{ '/images/07-2023/Visual_Instruction_Inversion:_Image_Editing_via_Visual_Prompting/figure_9.jpg' | relative_url }})
