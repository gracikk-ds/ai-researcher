---
title: Learning_Action_and_Reasoning-Centric_Image_Editing_from_Videos_and_Simulations
layout: default
date: 2024-07-03
---
![model architectures which handle different editing subtasks [Couairon et al., 2023, Zhang et al., 2023a]. However, neither of these approaches includes edits requiring more holistic visual understanding of how humans and objects interact or how events unfold , such as ‘make the cook cut the apple in half’ or ‘make the dog jump in the air’ (see Fig. 1). These more action-centric edits are severely understudied in the space of instruction-tuned image editing models [Brooks et al., 2023, Huang et al., 2024]; when they are considered, it is done in isolation, ignoring other image edit subtasks and rigorous semantic evaluation [Souˇcek et al., 2023, Black et al., 2024]. In Sec. 2 we describe a typology of these edit types and how existing datasets currently fail to address them all.]({{ '/images/07-2024/Learning_Action_and_Reasoning-Centric_Image_Editing_from_Videos_and_Simulations/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address a significant gap in instruction-guided image editing: current models excel at simple object or attribute changes but fail at complex "action and reasoning-centric" edits. These edits, such as "make the person walk away" or "move the cup to the right of the table," require understanding physical dynamics, temporality, and spatial relationships. The paper argues that this failure stems from a lack of high-quality training data. Existing datasets are either synthetically generated and noisy or focus on static, localized changes, leaving models unable to learn more holistic and dynamic transformations.

## 2. Key Ideas and Methodology
The core hypothesis is that training on a diverse dataset of "truly minimal" edit examples can teach models to perform complex action and reasoning edits. A "truly minimal" example is a source image, target image, and prompt triplet where the visual change between the images is singular and precisely described by the prompt.

The methodology involves three main contributions:
1.  **Dataset Curation:** The authors create the **AURORA** dataset, a large-scale collection of high-quality, minimal-change edit examples. It is meticulously curated from videos (capturing actions) and simulation engines (for precise control over spatial reasoning).
2.  **Holistic Evaluation:** They introduce **AURORA-BENCH**, an expert-curated benchmark with 8 diverse editing tasks to evaluate models beyond simple object edits. They rely primarily on human judgment for evaluation, arguing that existing automatic metrics are flawed as they mainly reward faithfulness to the source image rather than edit accuracy.
3.  **New Discriminative Metric:** They propose **DiscEdit**, a novel automatic metric that evaluates a model's understanding by testing its ability to distinguish between a prompt that requires a significant change and a minimally different prompt that requires no change.

## 3. Datasets Used / Presented
-   **AURORA (Action-Reasoning-Object-Attribute) Dataset (Presented):** A new training dataset with 289K examples. It is composed of four sub-datasets:
    -   **Action-Genome-Edit (11K):** Curated from video frames with crowd-sourced minimal edit instructions.
    -   **Something-Something-Edit (119K):** Created from the first and last frames of short action clips in the Something-Something video dataset.
    -   **Kubric-Edit (150K):** Generated using the Kubric simulator to teach spatial, geometric, and count-based reasoning.
    -   **MagicBrush (9K):** An existing high-quality dataset for object-centric edits, included for diversity.

-   **AURORA-BENCH (Presented):** A new evaluation benchmark of 400 expert-curated image-prompt pairs covering 8 distinct editing skills (object/attribute, global, action, and reasoning) from both in-distribution and out-of-distribution sources.

## 4. Main Results
The authors finetune an InstructPix2Pix model on their AURORA dataset and evaluate it against strong baselines on AURORA-BENCH.

-   **Human Judgment:** The AURORA-finetuned model significantly outperforms all baselines. It achieves a balanced overall success score of **41.3** (out of 100), compared to the strongest baseline (MagicBrush) which scores **32.6**. The improvements are most pronounced on the challenging reasoning tasks (e.g., a score of **59.6** vs. 9.3 on Kubric) and action tasks (e.g., **35.6** vs. 16.3 on Action-Genome).
-   **Discriminative Evaluation:** On the proposed DiscEdit metric, the AURORA model demonstrates a superior ability to understand instructions, scoring above random chance on most tasks, while the MagicBrush baseline performs at or below random chance.

The key takeaway is that high-quality, minimal-change data sourced from videos and simulations is crucial for advancing image editing models beyond simple edits to handle complex actions and reasoning.

## 5. Ablation Studies
-   **Quantifying Sim2Real Transfer:** To measure the impact of simulated data on real-world reasoning, the authors trained a model on AURORA *without* the simulated Kubric-Edit data. When evaluated on the real-world spatial reasoning task (WhatsUp), the full AURORA model had a **46% win-rate** against the ablated model. The ablated model only won a single example (2%), demonstrating that the simulated data provides a significant and transferable benefit for reasoning on real images.
-   **Qualitative Impact of Kubric Data:** The authors qualitatively observed that training on the "truly minimal" Kubric examples helps "stabilize" the model, reducing the frequency of hallucinations and un-needed changes (e.g., adding artifacts or people) during generation.

## 6. Paper Figures
![Figure 2: Our A U RO R A dataset covers action, reasoning and object-centric edits via 4 sub-datasets.]({{ '/images/07-2024/Learning_Action_and_Reasoning-Centric_Image_Editing_from_Videos_and_Simulations/figure_2.jpg' | relative_url }})
![Figure 3: Common failure mode of previous models trained on noisy image pairs (e.g. InstructPix2Pix and GenHowTo): Their outputs are rarely faithful to the source image due to its noisy training pairs.]({{ '/images/07-2024/Learning_Action_and_Reasoning-Centric_Image_Editing_from_Videos_and_Simulations/figure_3.jpg' | relative_url }})
![Figure 5: Prompt: Put the white porcelain ramekin on the right hand of the brown shoe. We show attention maps for three levels of U-Net layers: Down, Middle, Upper.]({{ '/images/07-2024/Learning_Action_and_Reasoning-Centric_Image_Editing_from_Videos_and_Simulations/figure_5.jpg' | relative_url }})
