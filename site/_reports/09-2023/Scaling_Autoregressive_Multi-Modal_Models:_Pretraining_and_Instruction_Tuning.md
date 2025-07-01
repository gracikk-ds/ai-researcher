---
title: Scaling_Autoregressive_Multi-Modal_Models:_Pretraining_and_Instruction_Tuning
layout: default
date: 2023-09-05
---
![Figure 1: Showcase of CM3Leon zero-shot generations (no-retrieval augmentation). Refer to § A for a complete list of prompts. CM3Leon can generate complex compositional objects, tail entities (Khachkar–Armenian crosses carved from stone), and historically hard entities such as hands and text.]({{ '/images/09-2023/Scaling_Autoregressive_Multi-Modal_Models:_Pretraining_and_Instruction_Tuning/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the perception that autoregressive (AR) models for image generation, while powerful, are significantly more computationally expensive and less performant than diffusion models. The paper aims to "flip this narrative" by demonstrating that AR models can be made highly efficient and achieve state-of-the-art results. They do this by adapting a modern training recipe from text-only large language models (LLMs) to the multi-modal domain, creating a single, general-purpose model for a wide range of text and image tasks.

## 2. Key Ideas and Methodology
The core of the paper is **CM3Leon** (pronounced "Chameleon"), a decoder-only, token-based multi-modal model. Its methodology is centered around a two-stage training process:

1.  **Retrieval-Augmented Pretraining:** The model is first pretrained on a large dataset of image-text pairs. Crucially, for each training instance, the model's context is augmented with several relevant image-text examples retrieved from a memory bank. This retrieval mechanism, based on a CLIP bi-encoder, is key to the model's training efficiency and its ability to learn about a wide range of concepts, especially rare or "tail" entities.

2.  **Multi-task Supervised Fine-Tuning (SFT):** After pretraining, the model undergoes instruction tuning on a diverse mixture of tasks. These tasks, ranging from text-guided image editing and conditional generation (e.g., from pose or segmentation maps) to visual question answering (VQA) and image captioning, are formatted into unified sequences of interleaved text and image tokens. This SFT stage significantly enhances the model's controllability and its ability to follow user instructions.

The paper also introduces **Contrastive Decoding TopK (CD-K)**, a novel decoding strategy that improves generation quality by contrasting text-conditioned and unconditional model outputs.

## 3. Datasets Used / Presented
- **Pretraining:** The model was pretrained on a large-scale, licensed dataset of **340 million image-text pairs from Shutterstock**.
- **Supervised Fine-Tuning (SFT):** A wide array of datasets were used for instruction tuning, including:
    - **Image-Focused Tasks:** Data derived from **InstructPix2Pix** (127k examples) for editing, **ControlNet** processing on Shutterstock for conditional generation from poses, edges, etc. (~7M examples), and object detection datasets like **MS-COCO** and **OpenImages** for spatially grounded generation (3M examples).
    - **Text-Focused Tasks:** Standard vision-language datasets such as **MS-COCO Captions** (591k), **Flickr30k** (144k), **VQA2** (1.3M), **VizWiz** (92k), and **ScienceQA** (6k).

## 4. Main Results
- **State-of-the-Art Text-to-Image Generation:** The 7-billion parameter CM3Leon model achieves a new state-of-the-art zero-shot Fréchet Inception Distance (FID) of **4.88** on the MS-COCO benchmark. The authors highlight that this was achieved using **5 times less training compute** than comparable SOTA models like PARTI.
- **Strong Vision-Language Performance:** After SFT, the model shows strong zero-shot performance on various VQA and captioning tasks. Notably, it outperforms the much larger Flamingo-9B model on the VizWiz VQA benchmark (37.6 vs. 28.8 accuracy), despite being pretrained on over 30x less text data.
- **Author Takeaway:** The results strongly suggest that autoregressive models, when combined with a retrieval-augmented pretraining and SFT recipe, are a highly efficient and powerful architecture for multi-modal AI.

## 5. Ablation Studies
- **Impact of Retrieval:** The importance of retrieval augmentation at inference time was ablated. The FID score on MS-COCO improved dramatically as more retrieved examples were provided: **10.82** (with 0 examples), **5.78** (with 1 example), and **4.88** (with 2 examples). This confirms that retrieval is critical to the model's top performance.
- **Decoding Strategies:** The paper compared different decoding methods. It found that the proposed **Contrastive Decoding (CD-K)** was competitive with standard Classifier-Free Guidance (CFG) and that combining CD-K with Top-P sampling yielded complementary benefits, resulting in a lower (better) FID score than either method used alone.

## 6. Paper Figures
![Figure 5: We perform fine-tuning on the CM3Leon model using a vast assortment of combined image and text tasks. Our retrieval augmented pretraining allows us to fine-tune the model effectively on a mixture of interleaved texts and images, as well as text-to-image and image-to-text tasks. We present some common model inputs for various tasks on the left, with the corresponding model outputs displayed on the right. Throughout the training process, we concatenate the model input and output and train them using the same objective that was utilized during the pretraining stage.]({{ '/images/09-2023/Scaling_Autoregressive_Multi-Modal_Models:_Pretraining_and_Instruction_Tuning/figure_5.jpg' | relative_url }})
![Figure 6: Qualitative examples of finetuned CM3Leon-7B model.]({{ '/images/09-2023/Scaling_Autoregressive_Multi-Modal_Models:_Pretraining_and_Instruction_Tuning/figure_6.jpg' | relative_url }})
![Figure 7: Qualitative examples showing our SFT-CM3Leon-7B model’s generations for various long form generation tasks.]({{ '/images/09-2023/Scaling_Autoregressive_Multi-Modal_Models:_Pretraining_and_Instruction_Tuning/figure_7.jpg' | relative_url }})
