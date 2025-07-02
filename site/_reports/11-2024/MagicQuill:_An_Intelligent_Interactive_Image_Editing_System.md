---
title: MagicQuill:_An_Intelligent_Interactive_Image_Editing_System
layout: default
date: 2024-11-14
---
## MagicQuill: An Intelligent Interactive Image Editing System
**Authors:**
- Zichen Liu, h-index: 2, papers: 3, citations: 15
- Yujun Shen, h-index: 7, papers: 14, citations: 259

**ArXiv URL:** http://arxiv.org/abs/2411.09703v2

**Citation Count:** None

**Published Date:** 2024-11-14

![Figure 1. MagicQuill is an intelligent and interactive image editing system built upon diffusion models. Users seamlessly edit images using three intuitive brushstrokes: add, subtract, and color (A). A MLLM dynamically predicts user intentions from their brush strokes and suggests contextual prompts (B1-B4). The examples demonstrate diverse editing operations: to generate a jacket from clothing contour (B1), add a flower crown from head sketches (B2), remove background (B3), and apply color changes to the hair and flowers (B4).]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current image editing tools, even those based on powerful diffusion models, struggle with performing precise and nuanced modifications. They often lack intuitive interfaces, forcing users to write complex text prompts and offering poor fine-grained control over the shape, position, and color of edits. The authors address this gap by developing a system that allows users to express complex editing ideas through simple, direct interactions like brushstrokes, making high-quality, controlled editing accessible and efficient without requiring prompt engineering expertise.

## 2. Key Ideas and Methodology
The paper introduces **MagicQuill**, an integrated system built on three core components:
1.  **Idea Collector:** A streamlined user interface with three intuitive brush tools (`add`, `subtract`, `color`) that allow users to visually specify their edits by drawing directly on the image.
2.  **Painting Assistor:** A Multimodal Large Language Model (MLLM) that observes the user's brushstrokes and image context in real-time. It performs a novel "Draw&Guess" task to predict the user's intent and automatically generates a corresponding text prompt, eliminating the need for manual text input.
3.  **Editing Processor:** A diffusion-based inpainting model enhanced with a dual-branch control architecture. One branch provides content-aware guidance for the masked region, while a second "control" branch uses the user's strokes to enforce precise adherence to desired edge structures and color schemes. This plug-in module ensures the final output is both high-quality and faithful to the user's input.

## 3. Datasets Used / Presented
-   **Custom "Draw&Guess" Dataset:** The authors constructed a new dataset to train the Painting Assistor. Using the **Densely Captioned Images (DCI)** dataset as a source, they simulated user editing sessions by generating edge maps, selecting object masks, inpainting them, and overlaying the edges to create sketch-like inputs. This process yielded 24,315 image-label pairs for fine-tuning the MLLM.
-   **LAION-Aesthetics:** Used to fine-tune the control branch of the Editing Processor.
-   **MagicBrush Benchmark:** Used for quantitative and qualitative evaluation against other state-of-the-art instruction-based editing methods.

## 4. Main Results
-   **Controllable Generation:** The Editing Processor outperformed baselines like SmartEdit and BrushNet, achieving state-of-the-art results in controllable generation with an LPIPS score of 0.0667 (lower is better) and a PSNR of 27.282 (higher is better).
-   **Intent Prediction:** The Painting Assistor's MLLM was more accurate at interpreting user drawings than general-purpose models like LLaVA and GPT-4O, achieving a GPT-4 similarity score of 2.712 (vs. 1.976 for the next best).
-   **User Study:** In a 30-participant study, MagicQuill was rated as significantly more user-friendly, efficient, and satisfying than a baseline interface. The Painting Assistor was shown to reduce editing time by up to 25%.
-   The authors claim MagicQuill is the first robust, open-source system that makes precise image editing easy and efficient by intelligently interpreting simple brushstrokes.

## 5. Ablation Studies
-   **Scribble-Prompt Trade-Off:** The authors analyzed the impact of edge control strength. A high strength (0.6) strictly follows the user's sketch, which can appear unnatural if the sketch is abstract. Reducing the strength (0.2) produces a more realistic and harmonious image that better aligns with the text prompt, trading sketch fidelity for generation quality.
-   **Colorization-Details Trade-Off:** The system's reliance on downsampled color blocks for color control was examined. Applying color with full opacity (alpha=1.0) achieves perfect colorization but can obscure fine details. Reducing the opacity (alpha=0.8) blends the new color with the original texture, preserving more structural detail at the cost of slightly less vibrant color.

## 6. Paper Figures
![Figure 2. System framework consisting of three integrated components: an Editing Processor with dual-branch architecture for controllable image inpainting, a Painting Assistor for real-time intent prediction, and an Idea Collector offering versatile brush tools. This design enables intuitive and precise image editing through brushstroke-based interactions.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_2.jpg' | relative_url }})
![Figure 3. Data processing pipeline. The input image undergoes edge extraction via CNN and color simplification through downscaling. Three editing conditions are then generated based on brush signals: editing mask, edge condition, and color condition, which together provide control for image editing.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_3.jpg' | relative_url }})
![Figure 4. Overview of our Editing Processor. The proposed architecture extends the latent diffusion UNet with two specialized branches: an inpainting branch for content-aware per-pixel inpainting guidance and a control branch for structural guidance, enabling precise brush-based image editing.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_4.jpg' | relative_url }})
![Figure 5. Illustration of dataset construction process. (a) Original images from the DCI dataset; (b) Edge maps extracted from original images; (c) Selected masks (highlighted in purple) with highest edge density; (d) Results after BrushNet inpainting on augmented masked regions; (e) Final results with edge map overlay on selected areas. By overlaying edge maps on inpainted results, we simulate scenarios where users edit images with brush strokes, as the edge maps resemble hand-drawn sketches. The bounding box coordinates of the mask and labels are inherited from the DCI dataset.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_5.jpg' | relative_url }})
![Figure 6. Visual result comparison. The first two columns present the edge and color conditions for editing, while the last column shows the ground truth image that the models aim to recreate. SmartEdit [ 25 ] utilizes natural language for guidance, but lacks precision in controlling shape and color, often affecting non-target regions. SketchEdit [ 79 ], a GAN-based approach [ 20 ], struggles with open-domain image generation, falling short compared to models with diffusion-based generative priors. Although BrushNet [ 28 ] delivers seamless image inpainting, it struggles to align edges and colors simultaneously, even with ControlNet [ 81 ] enhancement. In contrast, our Editing Processor strictly adheres to both edge and color conditions, achieving high-fidelity conditional image editing.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_6.jpg' | relative_url }})
![Figure 7. Visual comparison with stroke-based editing baselines.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_7.jpg' | relative_url }})
![Figure 8. User ratings for the Painting Assistor, focusing on its prediction accuracy and efficiency enhancement capabilities.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_8.jpg' | relative_url }})
![Figure 9. Comparative user ratings between our system and the baseline, with standard deviation shown as error bars.]({{ '/images/11-2024/MagicQuill:_An_Intelligent_Interactive_Image_Editing_System/figure_9.jpg' | relative_url }})
