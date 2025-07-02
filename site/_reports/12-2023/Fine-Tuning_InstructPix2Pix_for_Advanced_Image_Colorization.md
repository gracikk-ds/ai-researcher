---
title: Fine-Tuning_InstructPix2Pix_for_Advanced_Image_Colorization
layout: default
date: 2023-12-08
---
## Fine-Tuning InstructPix2Pix for Advanced Image Colorization
**Authors:**
- Zifeng An, h-index: 1, papers: 1, citations: 1
- Qi Cao

**ArXiv URL:** http://arxiv.org/abs/2312.04780v1

**Citation Count:** 1

**Published Date:** 2023-12-08

![Figure 1. Example of colorization for human faces from the IMDBWIKI dataset ( Rothe et al. , 2018 ). The task is a pixel-level task that should assign a color to each pixel in the input image. The top row shows the input of the task, a black-and-white image, and the bottom row is the ground truth labels for the input images.]({{ '/images/12-2023/Fine-Tuning_InstructPix2Pix_for_Advanced_Image_Colorization/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The paper addresses the limitations of the general-purpose InstructPix2Pix model when applied to the specific task of image colorization. While InstructPix2Pix excels at various text-guided image edits, its performance is suboptimal for the nuanced domain of adding realistic color to monochrome images, particularly human faces. The authors aim to bridge this gap by fine-tuning the model to specialize its capabilities for high-quality, visually realistic colorization.

## 2. Key Ideas and Methodology
The core idea is to adapt the InstructPix2Pix model for colorization through a targeted fine-tuning strategy. The methodology involves:
- **Selective Component Training**: The authors freeze the model's Variational Auto-Encoder (VAE) and CLIP text encoder, which handle general image representation and text understanding. They exclusively fine-tune the conditional U-Net, which is responsible for the denoising process that generates the final image, thereby focusing the learning process directly on the colorization task.
- **Diverse Prompt Generation**: Inspired by the FLAN-V2 paper, the authors use GPT-4 to generate a set of 30 synonymous prompts based on the instruction "colorize the image." This technique is used during training to enhance the model's robustness and its ability to generalize across different phrasings of the same command.
- **Dual Loss Functions**: The model is trained using the standard noise prediction loss inherent to diffusion models. However, for validation, performance is measured using a pixel-wise Mean Squared Error (MSE) between the generated image and the ground truth in the LAB color space to directly assess color accuracy.

## 3. Datasets Used / Presented
- **IMDB-WIKI Dataset**: The authors used a subset of 766 facial images from this large, publicly available dataset. For training and evaluation, the original color images were used as the ground truth targets, while their corresponding black-and-white versions served as the input to the model.

## 4. Main Results
The fine-tuned model demonstrated significant improvements over the original InstructPix2Pix model both quantitatively and qualitatively.
- **Quantitative**: On the IMDB-WIKI test set, the fine-tuned model outperformed the baseline across all standard image quality metrics. Peak Signal-to-Noise Ratio (PSNR) increased from 19.78 to 19.90, Structural Similarity Index (SSIM) improved substantially from 0.4301 to 0.5348, and Mean Absolute Error (MAE) was reduced from 22.1093 to 21.3045.
- **Author-claimed impact**: The study successfully shows that a focused fine-tuning approach can specialize a general image editing model to achieve enhanced visual realism and superior performance on a specific downstream task like colorization.

## 5. Ablation Studies
The authors conducted several experiments by varying key hyperparameters to find the optimal configuration.
- **Learning Rate**: The model was tested with learning rates of 1e-6, 5e-6, and 1e-5. The rate of 5e-6 was found to be optimal, creating a good balance. A lower rate produced dull, under-colorized images, while a higher rate resulted in overly saturated, high-contrast outputs.
- **Batch Size**: Batch sizes of 2, 4, and 8 were compared. A smaller batch size (4) was found to produce the best results for facial colorization. Larger batch sizes began to show signs of overfitting and "forgetting" the base model's knowledge.
- **Number of Prompts**: The model was trained with a single prompt versus 30 diverse prompts. The authors reported that there was "not much difference" in the qualitative results, theorizing that the CLIP text encoder maps the semantically similar prompts to very close embedding spaces.

## 6. Paper Figures
![Figure 2. Model architecture of InstructPix2Pix. For our finetuning on the task of colorization, we froze the VAE (encoder and decoder) and the CLIP text encoder. The U-Net is not frozen and is finetuned in the process.]({{ '/images/12-2023/Fine-Tuning_InstructPix2Pix_for_Advanced_Image_Colorization/figure_2.jpg' | relative_url }})
![Figure 3. Visual comparison of black-and-white input images (the first row), images colorized by original InstructPix2pix ( Brooks et al. , 2023 ) (the second row) and colorized by our finetuned model (the third row). Our method is able to accomplish visually pleasant colorization and our result is significantly better than the original version.]({{ '/images/12-2023/Fine-Tuning_InstructPix2Pix_for_Advanced_Image_Colorization/figure_3.jpg' | relative_url }})
![Figure 4. The training loss and the validation loss for our finetuned model.]({{ '/images/12-2023/Fine-Tuning_InstructPix2Pix_for_Advanced_Image_Colorization/figure_4.jpg' | relative_url }})
![Figure 5. Comparison of the colorization abilities on a sample image at different training steps of finetuning. The first row shows the input image and the original colorized image, and the second row shows the early, middle, and late stages of finetuning, from left to right respectively.]({{ '/images/12-2023/Fine-Tuning_InstructPix2Pix_for_Advanced_Image_Colorization/figure_5.jpg' | relative_url }})
![Figure 6. This figure shows the results of this sample input image (black-and-white) to our model with different hyperparameters.]({{ '/images/12-2023/Fine-Tuning_InstructPix2Pix_for_Advanced_Image_Colorization/figure_6.jpg' | relative_url }})
