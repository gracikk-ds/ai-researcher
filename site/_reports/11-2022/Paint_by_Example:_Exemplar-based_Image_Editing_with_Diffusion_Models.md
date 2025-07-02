---
title: Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models
layout: default
date: 2022-11-23
---
## Paint by Example: Exemplar-based Image Editing with Diffusion Models
**Authors:**
- Binxin Yang, h-index: 6, papers: 7, citations: 630
- Fang Wen

**ArXiv URL:** http://arxiv.org/abs/2211.13227v1

**Citation Count:** None

**Published Date:** 2022-11-23

![Figure 1. Paint by example. Users are able to edit a scene by painting with a conditional image. Our approach can automatically alter the reference image and merge it into the source image, and achieve a high-quality result.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the limitations of language-guided image editing, which can be ambiguous and lacks the precision needed for fine-grained control. They propose an exemplar-based image editing framework, where a reference image guides the manipulation, allowing for more intuitive and precise control over the final appearance. The core challenge is to semantically transform the object from the exemplar (e.g., altering its pose, size, and lighting) and blend it harmoniously into a source image, rather than simply performing a "copy-paste" operation.

## 2. Key Ideas and Methodology
The core of the method is a diffusion model conditioned on an exemplar image, trained using a self-supervised strategy to overcome the lack of paired training data. To prevent the model from learning a trivial copy-paste solution, the authors introduce several key techniques:
- **Information Bottleneck**: The reference image is represented only by its global CLIP embedding (the class token), discarding spatial information. This forces the model to understand the high-level semantics of the exemplar rather than memorizing its pixel values.
- **Strong Augmentation**: Aggressive data augmentation is applied to the reference image and the editing mask during training. This breaks the direct correspondence between the reference and source, reducing the train-test domain gap and improving generalization.
- **Generative Prior**: The model is initialized from a powerful pretrained text-to-image model (Stable Diffusion) to leverage its ability to generate high-fidelity, plausible images.
- **Classifier-Free Guidance**: This technique is used during inference to control the degree of similarity between the generated content and the reference exemplar.

## 3. Datasets Used / Presented
- **Training**: The model was trained on the **OpenImages** dataset, which contains 1.9 million images with 16 million bounding boxes across 600 object categories. This large-scale dataset was used for self-supervised training.
- **Testing**: The authors created and presented a new benchmark, **COCO Exemplar-based image Editing (COCOEE)**. It consists of 3,500 source images from the MSCOCO validation set, each paired with a manually retrieved, semantically relevant reference image patch from the MSCOCO training set.

## 4. Main Results
The proposed method demonstrated superior performance over several baselines, including text-guided and image-guided variants of Blended Diffusion and Stable Diffusion.
- **Quantitative**: On the COCOEE benchmark, the method achieved the best scores across all metrics: the lowest FID (3.18) for image quality, the highest QS (77.80) for authenticity, and the highest CLIP Score (84.97) for semantic similarity to the reference image.
- **User Study**: In a study with 50 participants, the method's results were ranked highest for overall quality and second for semantic consistency, surpassed in consistency only by a method that directly copies the exemplar.

## 5. Ablation Studies
The authors conducted a series of ablation experiments to validate each component of their approach:
- **Baseline (Naive Solution)**: A model trained without the proposed techniques produced unnatural results with severe copy-paste artifacts (FID: 3.61).
- **+ Image Prior**: Initializing with a pretrained model improved image quality (FID: 3.40) but did not solve the copy-paste issue.
- **+ Augmentation**: Adding strong augmentation partially alleviated artifacts but reduced similarity to the reference (CLIP Score dropped from 88.79 to 81.68).
- **+ Information Bottleneck**: This completely eliminated boundary artifacts by forcing semantic generation, though it slightly decreased raw quality metrics as the task became harder (FID: 3.26).
- **+ Classifier-Free Guidance**: The final addition of classifier-free guidance significantly boosted both image quality and similarity to the reference, leading to the best overall performance (FID: 3.18, CLIP Score: 84.97).

## 6. Paper Figures
![Figure 10. Our framework can synthesize realistic and diverse results from the same source image and exemplar image.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_10.jpg' | relative_url }})
![Figure 2. More visual results. Our approach can handle a wide variety of reference images and source images.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_2.jpg' | relative_url }})
![Figure 3. Illustration of the copy-and-paste artifacts of the naive solution. The generated image is extremely unnatural.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_3.jpg' | relative_url }})
![Figure 4. Our training pipeline.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_4.jpg' | relative_url }})
![Figure 5. Qualitative comparison with other approaches. Our method can generate results that are semantically consistent with the input reference images in high perceptual quality.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_5.jpg' | relative_url }})
![Figure 6. Visual ablation studies of individual components in our approach. We gradually eliminate the boundary artifacts through these techniques and ﬁnally achieve plausible generated results.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_6.jpg' | relative_url }})
![Figure 7. Effect of classiﬁer-free guidance scale λ . A larger λ makes the generated region more similar to the reference.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_7.jpg' | relative_url }})
![Figure 8. Comparison between progressively precise textual description and image as guidance. Using image as condition can maintain more ﬁne-grained details.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_8.jpg' | relative_url }})
![Figure 9. In-the-wild exemplar-based image editing results.]({{ '/images/11-2022/Paint_by_Example:_Exemplar-based_Image_Editing_with_Diffusion_Models/figure_9.jpg' | relative_url }})
