---
title: ChartReformer:_Natural_Language-Driven_Chart_Image_Editing
layout: default
date: 2024-03-01
---
## ChartReformer: Natural Language-Driven Chart Image Editing
**Authors:**
- Pengyu Yan
- David Doermann, h-index: 6, papers: 9, citations: 65

**ArXiv URL:** http://arxiv.org/abs/2403.00209v2

**Citation Count:** None

**Published Date:** 2024-03-01

![Fig. 1: Examples of chart editing results from our methods. In total, our methods define and cover four types of chart editing: style, layout, format and data-centric edit.]({{ '/images/03-2024/ChartReformer:_Natural_Language-Driven_Chart_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
- **What gap or practical problem are the authors addressing?**
Most chart visualizations exist as static images, disconnected from their underlying data tables. This makes it difficult to alter their appearance, format, or the data they represent for different applications, such as highlighting specific insights or improving accessibility for colorblind readers. Existing methods for chart editing often require access to the original data and plotting software or do not support a comprehensive range of modifications, particularly data-centric edits. The paper aims to solve this by enabling direct, natural language-driven editing of chart images without any prior information.

## 2. Key Ideas and Methodology
- **Core hypothesis or principle introduced.**
The core idea is that instead of directly predicting plotting code (which is brittle and prone to failure), a more robust approach is to decompose the chart editing task. The model first comprehends the input chart image and the natural language prompt, then generates an intermediate representation consisting of the modified underlying data table and a set of explicit visual attributes (e.g., colors, fonts, chart type).

- **High-level approach (e.g., model architecture, algorithmic trick, experimental design).**
The proposed system, **ChartReformer**, is a visual-language encoder-decoder model. The workflow is:
1.  **Decomposition:** The model takes a chart image and an edit instruction (e.g., "change the line chart to a bar chart") as input.
2.  **Prediction:** It predicts the new data table and a JSON object containing all visual attributes for the desired edited chart.
3.  **Replotting:** A separate, deterministic replotter module uses the predicted data and attributes to render the final edited chart image.
This process is trained in two stages: pre-training to de-render charts into data/attributes, and fine-tuning to perform edits based on text prompts.

- **Key assumptions or theoretical foundations.**
The key assumption is that any chart can be fully described by its underlying data table and a finite set of visual styling parameters. By manipulating this structured representation instead of generating free-form code, the model can achieve more precise and reliable edits.

## 3. Datasets Used / Presented
- **Name, size, domain of each dataset, and how it was used.**
The authors introduce a new dataset called **ChartCraft**.
*   **Size:** It contains ~110,000 pairs of original and edited chart images.
*   **Domain:** It covers line charts, grouped bar charts, and stacked bar charts, with data derived from real-world sources like the World Bank. The edits are categorized into four types: style, layout, format, and data-centric.
*   **Usage:** Each sample includes the original and edited images, their corresponding data tables, visual attributes (in JSON format), and multiple natural language prompts describing the edit. The dataset was used to pre-train and fine-tune the ChartReformer model.

## 4. Main Results
- **Main quantitative insights and metrics in human-readable format.**
ChartReformer demonstrated high effectiveness across all edit categories. On a test set, it achieved an overall F1-score of 86.3% for predicting visual attributes (VAES) and 89.3% for data table accuracy (RMS). The generated images showed high fidelity to the ground truth, with an average Structural Similarity Index (SSIM) of 83.7% and a near-perfect image generation success rate of 99.9%.

- **Author-claimed impact or takeaway sentence.**
In a direct comparison with the ChartLlama baseline, ChartReformer was significantly more robust, achieving a 100% success rate in generating an output image, while ChartLlama only succeeded on 17% of the test samples. The authors conclude that their decomposition-based approach enables precise and stable natural language-driven chart editing, outperforming methods that generate plotting code.

## 5. Ablation Studies  *(If none are reported, write “Not performed”)*
Not performed. The paper's evaluation focuses on comparing the overall performance of ChartReformer against an external baseline (ChartLlama) and analyzing its performance across different predefined edit categories. It does not include ablation experiments where components of the ChartReformer model or its training process are systematically removed to measure their impact.

## 6. Paper Figures
![Fig. 2: A Chart Image and edit-prompt are taken as input by the ChartReformer model, which predicts visual attributes and data for the corresponding edited chart. A Replotter software takes in these predicted parameters and generates the edited chart-image]({{ '/images/03-2024/ChartReformer:_Natural_Language-Driven_Chart_Image_Editing/figure_2.jpg' | relative_url }})
![Fig. 3: Distribution of Samples for Style Edits across Chart Categories]({{ '/images/03-2024/ChartReformer:_Natural_Language-Driven_Chart_Image_Editing/figure_3.jpg' | relative_url }})
