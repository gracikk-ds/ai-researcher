---
title: An_image_speaks_a_thousand_words,_but_can_everyone_listen?_On_image_transcreation_for_cultural_relevance
layout: default
date: 2024-04-01
---
## An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance
**Authors:**
- Simran Khanuja, h-index: 13, papers: 28, citations: 1168
- Graham Neubig, h-index: 16, papers: 49, citations: 1147

**ArXiv URL:** http://arxiv.org/abs/2404.01247v3

**Citation Count:** None

**Published Date:** 2024-04-01

![Figure 1: Image transcreation as done in various applications today: a) Audiovisual (AV) media : where several changes were made to adapt Doraemon to the US context like adding crosses and Fs in grade sheets, or in Inside Out, where broccoli is replaced with bell peppers in Japan as a vegetable that children don’t like; b) Education : where the same concepts are taught differently in different countries, using local currencies or celebration-themed worksheets; c) Advertisements : where the same product is packaged and marketed differently, like in Ferrero Rocher taking the shape of a lunar festival kite in China, and that of a Christmas tree elsewhere.]({{ '/images/04-2024/An_image_speaks_a_thousand_words,_but_can_everyone_listen?_On_image_transcreation_for_cultural_relevance/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The paper addresses a gap in machine translation, which has historically focused on text and speech, by introducing the task of **image transcreation**. This involves culturally adapting visual content to be more relevant and meaningful to a target audience. This capability is crucial for modern multimedia applications in education, marketing, and entertainment, where images must be as culturally resonant as the accompanying text.

## 2. Key Ideas and Methodology
The core idea is that modular systems leveraging the cultural knowledge of Large Language Models (LLMs) can outperform monolithic, end-to-end image editors. The authors propose and compare three pipelines to achieve image transcreation:
1.  **`e2e-instruct`**: A baseline that directly uses an instruction-based image editor (InstructPix2Pix) to edit the image based on a simple text prompt.
2.  **`cap-edit`**: A modular pipeline that first generates a caption for the source image, uses an LLM (GPT-3.5) to edit the caption for cultural relevance, and then uses an image editor to apply this new description to the original image.
3.  **`cap-retrieve`**: Similar to `cap-edit`, but the final step involves retrieving a new, natural image from a country-specific database (a subset of LAION) using the culturally-edited caption, instead of editing the original image.

## 3. Datasets Used / Presented
The authors created a new, two-part evaluation dataset to benchmark the task:
*   **Concept Dataset**: A set of approximately 600 images designed as a research prototype. It focuses on single, concrete concepts (e.g., food, clothing) across 7 diverse countries (Brazil, India, Japan, Nigeria, Portugal, Turkey, US). The data was collected and verified by native speakers to ensure cultural salience.
*   **Application Dataset**: A more challenging set of 100 images curated from real-world applications. It includes educational worksheets and children's storybooks, which feature complex scenes, multiple objects, and application-specific constraints.

## 4. Main Results
Human evaluation revealed that existing end-to-end models (`e2e-instruct`) largely fail at the task, often making meaningless or stereotypical edits (e.g., superimposing flag colors). The modular pipelines that leverage LLMs (`cap-edit` and `cap-retrieve`) performed significantly better. `cap-retrieve` was found to produce the most culturally relevant and natural-looking images. However, the authors conclude that the task remains extremely challenging; even the best pipeline successfully transcreated only 5% of images for Nigeria and 30% for Japan in the simpler `concept` dataset, and no pipeline was successful for some countries in the harder `application` dataset.

## 5. Ablation Studies
The paper's primary analysis is a comparative study of its three proposed pipelines, which functions as an ablation on the system's components:
*   **`e2e-instruct` (Baseline vs. others)**: This pipeline performed the worst, confirming that instruction-based image editors alone lack the necessary cultural context for meaningful transcreation.
*   **`cap-edit` (Adding LLM intelligence)**: Introducing a captioning and LLM-editing module significantly improved the semantic meaningfulness of the edits compared to the baseline. This approach was most effective at preserving the original image's structure and semantic category.
*   **`cap-retrieve` (Retrieval vs. Editing)**: Replacing the final image-editing step with image retrieval led to the highest scores for cultural relevance and naturalness. This highlights a key trade-off: retrieval yields more authentic results but may deviate further from the source image's content and layout.

## 6. Paper Figures
![Figure 2: Pipelines to transcreate images: e2e-instruct takes as input the original image and a natural language instruction; cap-edit first captions the image, uses a LLM to edit the caption for cultural relevance, and edits the original image using the LLM-edit as instruction; and cap-retrieve uses this LLM-edit to retrieve a natural image from a country-specific image dataset. Given the unprecedented nature of this task, we create pipelines using pre-existing SOTA models, and benchmark them on our newly created test set.]({{ '/images/04-2024/An_image_speaks_a_thousand_words,_but_can_everyone_listen?_On_image_transcreation_for_cultural_relevance/figure_2.jpg' | relative_url }})
![Figure 3: Concept dataset: We select seven geographically diverse countries and universal categories that are cross-culturally comprehensive. Annotators native to selected countries give us 5 concepts and associated images that are culturally salient for the speaking population of their country.]({{ '/images/04-2024/An_image_speaks_a_thousand_words,_but_can_everyone_listen?_On_image_transcreation_for_cultural_relevance/figure_3.jpg' | relative_url }})
![Figure 5: Story text: My mom bought rice.]({{ '/images/04-2024/An_image_speaks_a_thousand_words,_but_can_everyone_listen?_On_image_transcreation_for_cultural_relevance/figure_5.jpg' | relative_url }})
![Figure 6: Human ratings for the concept dataset : Our primary goal is to test whether the edited image belongs to the same universal category as the original image ( C1 ) and whether it increases cultural relevance ( C3 ). We plot the count of images that can do both above ( C1+C3 ), and observe that the best pipeline’s performance ranges between 5% (Nigeria) to 30% (Japan).]({{ '/images/04-2024/An_image_speaks_a_thousand_words,_but_can_everyone_listen?_On_image_transcreation_for_cultural_relevance/figure_6.jpg' | relative_url }})
![Figure 7: Application: Education; Target: Japan — Task : count the number of cherries. cap-edit is a successful transcreation despite the semantic drift from a fruit to a flower, because the final image can be used to teach counting to children.]({{ '/images/04-2024/An_image_speaks_a_thousand_words,_but_can_everyone_listen?_On_image_transcreation_for_cultural_relevance/figure_7.jpg' | relative_url }})
