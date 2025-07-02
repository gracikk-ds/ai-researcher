---
title: MoEController:_Instruction-based_Arbitrary_Image_Manipulation_with_Mixture-of-Expert_Controllers
layout: default
date: 2023-09-08
---
## MoEController: Instruction-based Arbitrary Image Manipulation with Mixture-of-Expert Controllers
**Authors:**
- Sijia Li
- Haonan Lu

**ArXiv URL:** http://arxiv.org/abs/2309.04372v2

**Citation Count:** 10

**Published Date:** 2023-09-08

![Fig. 1 : Arbitrary instruction-guided image global and local manipulation visualizations.]({{ '/images/09-2023/MoEController:_Instruction-based_Arbitrary_Image_Manipulation_with_Mixture-of-Expert_Controllers/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of creating a single, unified model for arbitrary instruction-based image manipulation. Existing diffusion-model-based methods are often specialized for either global manipulations (like style transfer) or local editing (like changing an object's attribute). For instance, Instruction-pix2pix (IP2P) excels at local edits but performs poorly on global tasks. The paper aims to bridge this gap by developing a model with zero-shot capabilities for both types of edits, guided by natural language instructions.

## 2. Key Ideas and Methodology
The core idea is to use a Mixture-of-Expert (MoE) architecture to dynamically handle the diverse nature of image manipulation instructions.

- **Methodology:** The authors propose **MoEController**, a conditional diffusion model equipped with an MoE module.
    1.  **Global Dataset Generation:** To address the lack of data for global manipulations, the authors first generate a large-scale dataset. They use ChatGPT to create target text captions from source captions based on stylistic instructions (e.g., "turn it into a watercolor painting"). Then, ControlNet is used to synthesize the corresponding image pairs.
    2.  **MoE Controller:** This controller is placed between the text encoder and the diffusion model. It consists of a **Fusion Module** that integrates text and image features, a set of **Expert Models** (three in this work, specializing in global, local, and fine-grained edits), and a **Gating Network**. The gating network analyzes the instruction and assigns weights to each expert, creating a blended output tailored to the specific task.
    3.  **Reconstruction Loss:** To ensure that unedited parts of the image remain consistent, a reconstruction loss term is added during training, penalizing deviations from the original image content where no changes are instructed.

## 3. Datasets Used / Presented
- **Custom Global Manipulation Dataset:** The authors created a new large-scale dataset for global image transfer. It was generated using a portion of the **LAION-5B** dataset as a source, with **ChatGPT** generating new text prompts and **ControlNet** generating the target images.
- **Instruction-pix2pix (IP2P) Dataset:** The model was also trained on this existing dataset, which contains examples of instruction-guided local image editing.

## 4. Main Results
The proposed MoEController was evaluated against state-of-the-art (SOTA) methods like IP2P, PNP, Clipstyler, and SDEdit on both global and local manipulation tasks.

- **Quantitative Results:** On global manipulation tasks, MoEController achieved the highest scores on both text-image similarity (CLIP-T: 0.1548) and directional consistency (CLIP-D: 0.2817). For local editing, it achieved the top CLIP-D score (0.2687) and a competitive CLIP-T score, demonstrating strong all-around performance.
- **User Study:** In a study with 10 participants, MoEController's results were ranked as the top choice 33.5% of the time, outperforming all other compared methods.
- **Author-claimed Impact:** The approach successfully endows a diffusion model with comprehensive capabilities for both global and local image editing from arbitrary human instructions, achieving superior performance over existing specialized models.

## 5. Ablation Studies
- **Mixture-of-Expert Model:** The authors compared their full model ("w/ MOE") to a version trained on both datasets but without the MoE architecture ("w/o MOE"). The "w/o MOE" model showed a clear performance trade-off, where training for global tasks degraded its local editing ability. The full "w/ MOE" model significantly outperformed this baseline on both task types, confirming that the MoE component is crucial for successfully balancing and executing diverse manipulations.
- **Reconstruction Loss:** The impact of the reconstruction loss weight (`w`) was analyzed. A weight of `w=0` (no loss) resulted in distorted images, while `w=1.0` preserved too much of the original image, hindering the desired edit. A weight of `w=0.5` was found to provide the best balance between image fidelity and effective transformation, and was used for the final model.

## 6. Paper Figures
![Fig. 2 : Cross-attention heat map of the core words and generated image of different methods.]({{ '/images/09-2023/MoEController:_Instruction-based_Arbitrary_Image_Manipulation_with_Mixture-of-Expert_Controllers/figure_2.jpg' | relative_url }})
![Fig. 3 : An overview of our approach. Left : pipeline of dataset construction. Right : MOE controller structure.]({{ '/images/09-2023/MoEController:_Instruction-based_Arbitrary_Image_Manipulation_with_Mixture-of-Expert_Controllers/figure_3.jpg' | relative_url }})
![Fig. 4 : Comparison of image global and local manipulation tasks with and without mixture-of-experts.]({{ '/images/09-2023/MoEController:_Instruction-based_Arbitrary_Image_Manipulation_with_Mixture-of-Expert_Controllers/figure_4.jpg' | relative_url }})
![Fig. 5 : The effect of image style transfer with different w.]({{ '/images/09-2023/MoEController:_Instruction-based_Arbitrary_Image_Manipulation_with_Mixture-of-Expert_Controllers/figure_5.jpg' | relative_url }})
![Fig. 6 : Global and local image manipulation qualitative comparison experimental results.]({{ '/images/09-2023/MoEController:_Instruction-based_Arbitrary_Image_Manipulation_with_Mixture-of-Expert_Controllers/figure_6.jpg' | relative_url }})
