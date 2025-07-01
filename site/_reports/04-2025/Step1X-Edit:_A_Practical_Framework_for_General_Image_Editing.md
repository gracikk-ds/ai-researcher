---
title: Step1X-Edit:_A_Practical_Framework_for_General_Image_Editing
layout: default
date: 2025-04-24
---
![Figure 1: Overview of Step1X-Edit . Step1X-Edit is an open-source general editing model that achieves proprietary-level performance with comprehensive editing capabilities.]({{ '/images/04-2025/Step1X-Edit:_A_Practical_Framework_for_General_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the significant performance gap between open-source image editing models and leading proprietary, closed-source systems like GPT-4o and Gemini. Existing open-source methods often lack generalization, struggle with edit accuracy, and produce lower-quality images. Furthermore, the authors argue that available training datasets are insufficient in quality and diversity to train models that can compete with their closed-source counterparts. The primary goal is to narrow this performance gap by introducing a practical, high-performing, open-source framework and the high-quality data required to train it.

## 2. Key Ideas and Methodology
The core of the work is **Step1X-Edit**, a unified framework that integrates the semantic reasoning of a Multimodal Large Language Model (MLLM) with the generative power of a Diffusion in Transformer (DiT) architecture.

-   **Architecture:** The model consists of three main components: an MLLM (e.g., Qwen-VL), a lightweight connector module, and a DiT-based image decoder.
-   **Methodology:** An input image and a natural language instruction are fed into the MLLM, which processes them to generate token embeddings that capture the editing intent. These embeddings are then passed to a connector module that refines and restructures them into a compact multimodal feature. This feature is concatenated with the noisy latent representation of the source image and used to condition the DiT decoder, which generates the final edited image.
-   **Training:** The connector and DiT are trained jointly, optimizing only a standard diffusion loss. This approach avoids the need for auxiliary losses (e.g., mask loss) and ensures stable training.

## 3. Datasets Used / Presented
The paper introduces a new data generation pipeline and a new evaluation benchmark.

-   **Step1X-Edit Dataset (Training):** The authors developed a scalable data pipeline covering 11 distinct editing categories (e.g., subject removal, style transfer, text modification). This pipeline generated over 20 million image-instruction-edit triplets, which were filtered down to a high-quality training set of over 1 million examples.
-   **GEdit-Bench (Evaluation):** A novel benchmark created to evaluate models on practical, real-world scenarios. It consists of 606 test cases sourced from real user requests on the internet (e.g., Reddit). The benchmark includes a diverse set of 11 editing tasks and features a careful de-identification protocol to protect user privacy while preserving the original editing intent.

## 4. Main Results
Step1X-Edit demonstrates a significant improvement over existing open-source models and achieves performance comparable to leading proprietary systems.

-   **Quantitative Results:** On the English GEdit-Bench (full set), Step1X-Edit achieved an overall GPT-4.1-evaluated score (G_O) of 6.444. This substantially outperforms other open-source models like OmniGen (5.005) and is competitive with closed-source models like Gemini (6.509) and Doubao (6.983).
-   **User Study:** In a blind user preference study with 55 participants, Step1X-Edit's results were rated competitively against those from GPT-4o and Gemini, confirming its ability to produce visually pleasing and user-preferred edits.
-   **Impact:** The authors claim that Step1X-Edit successfully narrows the performance gap between open-source and closed-source systems, providing a strong, publicly available baseline for future research in general-purpose image editing.

## 5. Ablation Studies
Not performed. The paper compares its architectural choices (e.g., token concatenation, no mask loss) to alternatives used in other models but does not present formal ablation experiments that isolate the impact of its own components.

## 6. Paper Figures
![Figure 3: Data Construction Pipeline and Sub-Task Distribution .]({{ '/images/04-2025/Step1X-Edit:_A_Practical_Framework_for_General_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Framework of Step1X-Edit . Step1X-Edit leverages the image understanding capabilities of MLLMs to parse editing instructions and generate editing tokens, which are then decoded into images using a DiT-based network.]({{ '/images/04-2025/Step1X-Edit:_A_Practical_Framework_for_General_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: DiT module details.]({{ '/images/04-2025/Step1X-Edit:_A_Practical_Framework_for_General_Image_Editing/figure_5.jpg' | relative_url }})
![Figure 6: De-Identification Process .]({{ '/images/04-2025/Step1X-Edit:_A_Practical_Framework_for_General_Image_Editing/figure_6.jpg' | relative_url }})
