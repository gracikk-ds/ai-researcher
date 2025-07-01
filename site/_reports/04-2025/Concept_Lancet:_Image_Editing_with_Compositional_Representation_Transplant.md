---
title: Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant
layout: default
date: 2024-04-01
---
![Figure 1. Given a source image and the editing task, our proposed CoLan generates a concept dictionary and performs sparse decomposition in the latent space to precisely transplant the target concept.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_1.png' | relative_url }})

*Figure 1. Given a source image and the editing task, our proposed CoLan generates a concept dictionary and performs sparse decomposition in the latent space to precisely transplant the target concept.*


## 1. Motivation of the Paper
Existing diffusion-based image editing methods struggle to determine the appropriate "editing strength" for a given image. Manually setting this value is difficult; overestimating it harms visual consistency by corrupting the image, while underestimating it fails to execute the desired edit. This trial-and-error process is inefficient and image-dependent. The authors address this gap by proposing a method to automatically estimate and apply the correct edit magnitude for each specific image.

## 2. Key Ideas and Methodology
The paper introduces **Concept Lancet (CoLan)**, a framework for principled representation manipulation. The core idea is that by quantifying the presence of a concept in a source image, one can perform a more precise edit.

The methodology involves two main steps:
1.  **Concept Dictionary Synthesis:** The authors first curate a large-scale dataset of visual concepts and their textual descriptions (stimuli). From these, they extract representative "concept vectors" in the latent space of a diffusion model to form a comprehensive dictionary.
2.  **Concept Transplant:** At inference time, CoLan decomposes the source image's latent vector into a sparse linear combination of vectors from a task-specific dictionary. The resulting coefficients represent the magnitude of each concept in the image. To perform an edit (e.g., 'cat' → 'dog'), CoLan "transplants" the target concept vector ('dog') into the decomposition, replacing the source vector ('cat') but keeping its original coefficient. This ensures the edit is applied with a magnitude appropriate for the source image, preserving other visual elements.

## 3. Datasets Used / Presented
- **CoLan-150K:** A new dataset created by the authors, containing 152,971 textual stimuli for 5,078 diverse visual concepts. It is used to build the dictionary of concept vectors.
- **PIE-Bench:** An existing benchmark used for the quantitative evaluation of image editing methods.

## 4. Main Results
CoLan significantly improves the performance of existing editing backbones. When integrated with the P2P-Zero backbone, CoLan improved consistency preservation metrics, reducing the perceptual distance (LPIPS) by nearly 50% and increasing PSNR by approximately 10%. Simultaneously, it improved edit effectiveness (CLIP similarity). The authors claim that CoLan achieves state-of-the-art performance by enabling accurate edits that maintain high visual consistency, eliminating the need for manual parameter tuning.

## 5. Ablation Studies
- **Dictionary Size:** The editing performance was evaluated with different dictionary sizes (N=5, 10, 20, 30). Results showed that performance generally improved with a larger dictionary, as a richer set of concepts allows for a more accurate decomposition of the source image.
- **Editing Strength:** The authors visually compared images edited with a range of fixed strength values against those edited using the strength estimated by CoLan. The results demonstrated that CoLan's approach provides a better balance, avoiding the under-editing and over-editing artifacts produced by fixed-strength methods.
- **Concept Grounding:** To verify that the extracted concept vectors were meaningful, they were added to various source images. The CLIP similarity between the edited image and the corresponding concept text (e.g., "watercolor") consistently increased, confirming that the vectors effectively impose the intended visual semantics.

## 6. Paper Figures
![Figure 10. Visualizations of edited images with increasing strength of the concept [green] extracted from our CoLan-150K dataset. The values on top correspond to the coefficient w green for adding the concept vector d green . CoLan solves w ∗ green of 0 . 586 for the apple and 0 . 695 for the rose.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_10.png' | relative_url }})

*Figure 10. Visualizations of edited images with increasing strength of the concept [green] extracted from our CoLan-150K dataset. The values on top correspond to the coefficient w green for adding the concept vector d green . CoLan solves w ∗ green of 0 . 586 for the apple and 0 . 695 for the rose.*


![Figure 2. Representation manipulation in diffusion models involves adding an accurate magnitude of edit direction (e.g., Image (3) by CoLan) to the latent source representation. Figure 5 and Figure 7 show more examples.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_2.png' | relative_url }})

*Figure 2. Representation manipulation in diffusion models involves adding an accurate magnitude of edit direction (e.g., Image (3) by CoLan) to the latent source representation. Figure 5 and Figure 7 show more examples.*


![Figure 3. The CoLan framework. Starting with a source image and prompt, a vision-language model extracts visual concepts (e.g., cat, grass, sitting) to construct a concept dictionary. The source representation is then decomposed along this dictionary, and the target concept (dog) is transplanted to replace the corresponding atom to achieve precise edits. Finally, the image editing backbone generates an edited image where the desired target concept is incorporated without disrupting other visual elements.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_3.png' | relative_url }})

*Figure 3. The CoLan framework. Starting with a source image and prompt, a vision-language model extracts visual concepts (e.g., cat, grass, sitting) to construct a concept dictionary. The source representation is then decomposed along this dictionary, and the target concept (dog) is transplanted to replace the corresponding atom to achieve precise edits. Finally, the image editing backbone generates an edited image where the desired target concept is incorporated without disrupting other visual elements.*


![Figure 5. Visual comparisons of CoLan in the text embedding space of P2P-Zero. Texts in gray are the original captions of the source images from PIE-Bench, and texts in blue are the corresponding edit task (replace, add, remove). [x] represents the concepts of interest, and [] represents the null concept.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_5.png' | relative_url }})

*Figure 5. Visual comparisons of CoLan in the text embedding space of P2P-Zero. Texts in gray are the original captions of the source images from PIE-Bench, and texts in blue are the corresponding edit task (replace, add, remove). [x] represents the concepts of interest, and [] represents the null concept.*


![Figure 6. The histograms of solved magnitudes of the concept atoms in CoLan decomposition (text embedding space). As there are tens of concepts in a single dictionary, the histogram includes the concepts whose CoLan coefficients have the top 10 largest magnitudes.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_6.png' | relative_url }})

*Figure 6. The histograms of solved magnitudes of the concept atoms in CoLan decomposition (text embedding space). As there are tens of concepts in a single dictionary, the histogram includes the concepts whose CoLan coefficients have the top 10 largest magnitudes.*


![Figure 7. Visual comparisons of CoLan in the score space (first row) and text embedding space (second row) of InfEdit. Texts in gray are the original captions of the source images from PIE-Bench, and texts in blue are the corresponding edit task (replace, add, remove).]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_7.png' | relative_url }})

*Figure 7. Visual comparisons of CoLan in the score space (first row) and text embedding space (second row) of InfEdit. Texts in gray are the original captions of the source images from PIE-Bench, and texts in blue are the corresponding edit task (replace, add, remove).*


![Figure 8. The histograms of solved magnitudes of the concept atoms in CoLan decomposition (score space). The histogram includes the concepts whose CoLan coefficients have the top 10 largest magnitudes.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_8.png' | relative_url }})

*Figure 8. The histograms of solved magnitudes of the concept atoms in CoLan decomposition (score space). The histogram includes the concepts whose CoLan coefficients have the top 10 largest magnitudes.*


![Figure 9. Visualizations of edited images with decreasing strength of the concept [fresh] extracted from our CoLan-150K dataset. The values on top correspond to the coefficient w fresh for removing the concept d fresh . CoLan solves w ∗ fresh of − 0 . 977 for the apple and − 1 . 16 for the lotus.]({{ '/images/04-2025/Concept_Lancet:_Image_Editing_with_Compositional_Representation_Transplant/figure_9.png' | relative_url }})

*Figure 9. Visualizations of edited images with decreasing strength of the concept [fresh] extracted from our CoLan-150K dataset. The values on top correspond to the coefficient w fresh for removing the concept d fresh . CoLan solves w ∗ fresh of − 0 . 977 for the apple and − 1 . 16 for the lotus.*
