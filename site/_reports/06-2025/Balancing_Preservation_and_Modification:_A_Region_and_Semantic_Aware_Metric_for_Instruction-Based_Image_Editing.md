---
title: Balancing_Preservation_and_Modification:_A_Region_and_Semantic_Aware_Metric_for_Instruction-Based_Image_Editing
layout: default
date: 2025-06-15
---
![Figure 1: (a) The scores rated by existing metrics LPIPS, CLIPScore and DINOScore all witness a contradict trends with human evaluation, while our proposed BPM aligns with human evaluation. (b) Previous metrics favor excessively preserved or modified result, while our BPM favor the well-edited image.]({{ '/images/06-2025/Balancing_Preservation_and_Modification:_A_Region_and_Semantic_Aware_Metric_for_Instruction-Based_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the lack of a comprehensive and reliable automatic metric for instruction-based image editing. Existing metrics suffer from two primary issues: 1) they are often adapted from other tasks (like image generation) and fail to simultaneously evaluate both the successful modification of the target region and the crucial preservation of irrelevant content; 2) they evaluate the image as a whole, ignoring the distinct requirements for different regions. This leads to biased and untrustworthy scores that frequently contradict human judgment, hindering the objective assessment and development of editing models.

## 2. Key Ideas and Methodology
The paper introduces a new metric, **Balancing Preservation Modification (BPM)**, built on the core principle of disentangling the image into editing-relevant and irrelevant regions for separate evaluation.

The methodology follows a multi-step process:
1.  **Instruction Parsing**: A Large Language Model (LLM) first analyzes the text instruction to identify the source and target objects, as well as the required changes in their size and position.
2.  **Region Localization**: Object detection and segmentation models are then used to generate masks and bounding boxes for the identified objects in both the original and edited images.
3.  **Two-Tier Evaluation**: The metric then performs a two-part assessment:
    *   **Region-Aware Judge**: This tier verifies if the geometric properties (position and size) of the edited region align with the parsed instruction, yielding a `S_region` score.
    *   **Semantic-Aware Judge**: This tier evaluates the content. It uses directional CLIP similarity to measure semantic compliance within the modified region (`S_modify`) and L2 distance to measure content preservation in the unmodified, irrelevant regions (`S_preserve`).
4.  The final BPM score is a weighted combination of the region-aware and semantic-aware scores, providing a balanced and interpretable assessment.

## 3. Datasets Used / Presented
*   **MagicBrush**: A manually annotated dataset for instruction-guided image editing. The authors sampled image-instruction pairs from it to evaluate performance on **local edits**.
*   **PIE-Bench**: A benchmark for prompt-based image editing. The authors used its global edits subset to evaluate performance on **global edits**.
*   **Generated Data**: To conduct experiments, the authors used several state-of-the-art editing models (IP2P, MGIE, DALLE-2, FTIP2P) to generate edited images based on the prompts from the above datasets.
*   **Human Annotations**: A total of **960** edited image results were collected and rated by human evaluators across five criteria to create a ground-truth benchmark for the "Human Alignment Test".

## 4. Main Results
*   **Human Alignment**: BPM demonstrated the highest alignment with human preferences compared to all existing metrics. In pairwise comparisons, BPM's ranking agreed with human evaluators **80%** of the time for local edits and **83%** for global edits, significantly outperforming metrics like LPIPS, CLIPScore, and even the VLM-based GPT-4O.
*   **Bias Reduction**: In a "Ground Truth Test" with triplets of (excessively preserved, excessively modified, well-edited) images, BPM correctly favored the well-edited ground truth image **87%** of the time. This shows it is significantly less biased than preservation metrics (e.g., LPIPS, which favored preserved images 100% of the time) and modification metrics (e.g., CLIPScore, which favored modified images 83% of the time).
*   **Author Takeaway**: By explicitly disentangling and separately evaluating modification and preservation, BPM provides a more trustworthy, comprehensive, and interpretable metric that better reflects human perception of editing quality.

## 5. Ablation Studies
*   **Component Score Effectiveness**: The individual component scores of BPM (`S_preserve`, `S_modify`, `S_position`, `S_size`) were evaluated against human judgments for their specific tasks. Each component significantly outperformed its corresponding baseline metric (e.g., `S_modify` vs. CLIPScore), validating the effectiveness of the disentangled evaluation design.
*   **Balancing Factor (α)**: The authors tested different weights for combining the semantic and region scores. A weight of **α=0.7** for the semantic score achieved the highest alignment with human evaluation, suggesting that while semantic correctness is paramount, geometric accuracy is also a critical component.
*   **LLM Choice**: The performance of different LLMs for the instruction parsing task was compared. The results showed that the smaller, open-source `gemma-9b` model achieved performance on par with `GPT-4O`, demonstrating the method's practicality and accessibility.
*   **Application as Editing Guidance**: The region localization component of BPM was used to create a mask to guide existing editing models. This enhancement led to steady improvements in both preservation and modification scores across three different models, with a user study confirming that the enhanced results were preferred in the vast majority of cases.

## 6. Paper Figures
![Figure 2: Overall Pipeline of BPM . Firstly, LLM is utilized to parse and analyze editing instruction, generates responses to identify the source and target object, as well as the object size and position changing state requirement during editing. Then we conduct Region-Aware Judge to verify editing follows the instruction for region size and position, yielding region-aware score S region . For Semantic-Aware Judge , we utilize detection and segmentation tools to locate and segment the edited object, subsequently apart the origin and edited images into edited regions and irrelevant regions, separately evaluating the semantical instruction compliance in edited regions and content preservation in irrelevant regions, yielding semantic-aware score S semantic .]({{ '/images/06-2025/Balancing_Preservation_and_Modification:_A_Region_and_Semantic_Aware_Metric_for_Instruction-Based_Image_Editing/figure_2.jpg' | relative_url }})
![Figure 3: Evaluation functions for region-aware judge.]({{ '/images/06-2025/Balancing_Preservation_and_Modification:_A_Region_and_Semantic_Aware_Metric_for_Instruction-Based_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 4: Visualized example of evaluation metrics comparison.]({{ '/images/06-2025/Balancing_Preservation_and_Modification:_A_Region_and_Semantic_Aware_Metric_for_Instruction-Based_Image_Editing/figure_4.jpg' | relative_url }})
![Figure 5: Visualized example of image editing mask guidance.]({{ '/images/06-2025/Balancing_Preservation_and_Modification:_A_Region_and_Semantic_Aware_Metric_for_Instruction-Based_Image_Editing/figure_5.jpg' | relative_url }})
