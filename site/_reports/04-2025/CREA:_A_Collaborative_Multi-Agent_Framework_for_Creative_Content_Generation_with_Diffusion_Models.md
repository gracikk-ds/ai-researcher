---
title: CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models
layout: default
date: 2024-04-02
---
![Figure 1. We introduce CREA, an agentic framework that emulates the human creative process for creative image editing and generation. Our approach is driven by collaborative interactions between specialized agents, such as a Creative Director and an Art Critic , who communicate to refine and enhance creative output. Moreover, our approach can be extended to video domain for creative video generation. Our framework can also be integrated with personalization techniques to further enrich and expand creative workflows.]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_1.png' | relative_url }})

*Figure 1. We introduce CREA, an agentic framework that emulates the human creative process for creative image editing and generation. Our approach is driven by collaborative interactions between specialized agents, such as a Creative Director and an Art Critic , who communicate to refine and enhance creative output. Moreover, our approach can be extended to video domain for creative video generation. Our framework can also be integrated with personalization techniques to further enrich and expand creative workflows.*


## 1. Motivation of the Paper
Current generative AI models, while capable of producing high-quality visuals, often lack true originality and artistic depth. They typically rely on a direct prompt-to-image paradigm that requires significant user effort through tedious prompt refinement and manual editing to infuse creativity. The authors address this gap by introducing the task of "creative image editing," where the goal is to autonomously transform images into novel, expressive, and artistically rich compositions with minimal user intervention, effectively turning the AI into a creative partner rather than just a tool.

## 2. Key Ideas and Methodology
The paper introduces **CREA (Creative Collaborative Agentic Framework)**, a multi-agent system designed to emulate the human creative process. The core idea is to structure creativity as a dynamic, iterative collaboration between specialized AI agents.

*   **Multi-Agent Collaboration:** The framework consists of five distinct agents:
    1.  **Creative Director:** The main decision-maker that interprets concepts and defines a "creativity blueprint."
    2.  **Prompt Architect:** Translates the blueprint into structured, high-creativity prompts using contrastive prompting and Chain-of-Thought fusion.
    3.  **Generative Executor:** Interfaces with diffusion models (e.g., Flux, ControlNet) to generate or edit the image.
    4.  **Art Critic:** Evaluates the generated image using a multimodal LLM, assigning scores based on six creativity principles.
    5.  **Refinement Strategist:** Translates the critic's feedback into actionable refinements for the next iteration.

*   **Iterative Refinement Process:** The workflow involves four stages:
    1.  **Pre-Generation Planning:** Agents collaborate to create a high-creativity prompt.
    2.  **Image Synthesis/Editing:** The Generative Executor creates an initial image.
    3.  **Post-Generation Evaluation:** The Art Critic assesses the image against a **Creativity Index (CI)**.
    4.  **Self-Enhancement:** If the CI is below a threshold, the agents iteratively refine the prompt and image for a set number of rounds. This loop can also incorporate optional user guidance.

*   **Theoretical Foundation:** The framework's evaluation is grounded in six established creativity principles derived from cognitive psychology and aesthetics: Originality, Expressiveness, Aesthetic Appeal, Technical Execution, Unexpected Associations, and Interpretability & Depth.

## 3. Datasets Used / Presented
The authors created a custom evaluation set for their experiments. This set was used for both the creative editing and generation tasks. It consists of:
*   **24 different object concepts** (e.g., "couch," "car," "monster").
*   **25 distinct prompts** for each object, used for either editing an existing image or generating a new one.
*   This resulted in a total evaluation set of **600 images per task**.

## 4. Main Results
CREA significantly outperforms state-of-the-art methods in both creative image editing and generation across quantitative metrics, LLM-based judging, and human user studies.

*   **Quantitative Metrics:**
    *   **Editing:** CREA surpassed baselines like SDEdit and InstructPix2Pix on all metrics, achieving higher CLIP scores (0.417), VENDI diversity scores (3.70), and transformative LPIPS scores (0.414).
    *   **Generation:** Compared to models like SDXL and ConceptLab, CREA produced the most diverse results, achieving the highest VENDI (10.44) and LPIPS (0.709) scores.

*   **LLM-as-a-Judge & User Studies:** In subjective evaluations, CREA's outputs were consistently rated as more creative, original, expressive, and aesthetically appealing than those from all baseline methods. For example, in the user study for generation, CREA achieved a novelty score of 4.16, compared to 3.56 for SDXL and 3.18 for ConceptLab.

The authors claim that by structuring creativity as a collaborative, agentic process, CREA redefines the intersection of AI and art, enabling more autonomous and profound artistic exploration.

## 5. Ablation Studies
The paper presents several ablation studies to validate the design choices of the CREA framework.

*   **Component Ablation:** The effectiveness of each core component was tested by removing it from the pipeline. The full framework (Base + Principles + Contrastive Prompting + Self-Enhancement) achieved the highest performance. For instance, the full model achieved a LPIPS diversity score of 0.414, significantly outperforming the base model (0.302) and demonstrating that each component adds value.
*   **Iterative Refinement:** The study showed that the multi-iteration self-enhancement process progressively improves the creative quality of the output, with the Creativity Index increasing with each refinement step.
*   **Model Generalization:** The CREA framework was successfully applied to different backbone generative models, including SDXL and DALL-E, demonstrating its versatility and model-agnostic nature.
*   **Prompt Variations:** The authors explored alternative prompting strategies, such as using negative prompts (e.g., "a normal couch") to steer the model away from conventional outputs, confirming the framework's flexibility.

## 6. Paper Figures
![Figure 2. CREA Framework . We introduce a collaborative multi-agent framework for creative image editing and generation. Our framework consists of four stages, 1.a Pre-Generation Planning, 1.b Creative Image Generation/Editing, 2. Post-Generation Evaluation and 3. Self-Enhancement. Here, K is the number of maximum iterations.]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_2.png' | relative_url }})

*Figure 2. CREA Framework . We introduce a collaborative multi-agent framework for creative image editing and generation. Our framework consists of four stages, 1.a Pre-Generation Planning, 1.b Creative Image Generation/Editing, 2. Post-Generation Evaluation and 3. Self-Enhancement. Here, K is the number of maximum iterations.*


![Figure 3. Qualitative Results for Creative Image Editing and Generation Tasks. (a) Qualitative results illustrating CREA’s disentangled creative edits. (b) Generation results across diverse objects and domains, demonstrating CREA’s ability to produce a wide range of creative variations. For more results, please visit Supplementary Material.]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_3.png' | relative_url }})

*Figure 3. Qualitative Results for Creative Image Editing and Generation Tasks. (a) Qualitative results illustrating CREA’s disentangled creative edits. (b) Generation results across diverse objects and domains, demonstrating CREA’s ability to produce a wide range of creative variations. For more results, please visit Supplementary Material.*


![Figure 4. Qualitative Comparison of Creative Image Editing Task. We compare CREA with state-of-the-art editing methods. As shown, CREA successfully reimagines objects into creative variants in a disentangled manner, whereas other approaches either fail to produce distinctly creative edits or introduce unintended alterations.]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_4.png' | relative_url }})

*Figure 4. Qualitative Comparison of Creative Image Editing Task. We compare CREA with state-of-the-art editing methods. As shown, CREA successfully reimagines objects into creative variants in a disentangled manner, whereas other approaches either fail to produce distinctly creative edits or introduce unintended alterations.*


![Figure 5. Qualitative Comparison of Creative Image Generation Task. We compare CREA with ConceptLab, SDXL and Flux. CREA consistently produces diverse and creative generations across multiple domains.]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_5.png' | relative_url }})

*Figure 5. Qualitative Comparison of Creative Image Generation Task. We compare CREA with ConceptLab, SDXL and Flux. CREA consistently produces diverse and creative generations across multiple domains.*


![Figure 6. Creative applications of our method beyond image generation and editing. (a) Users can steer the creative process with additional conditions such as ‘Monster’. (b) CREA-generated images can be leveraged for personalization in creative domains.]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_6.png' | relative_url }})

*Figure 6. Creative applications of our method beyond image generation and editing. (a) Users can steer the creative process with additional conditions such as ‘Monster’. (b) CREA-generated images can be leveraged for personalization in creative domains.*


![Figure 7. Ablation Study. We perform comprehensive ablation studies to analyze the design choices of CREA: (a) Model Generalization: Our method extends effectively to different generative models, such as SDXL and DALL-E. (b) Parameter Sensitivity: We ablate CFG values for Flux and the conditioning scale for ControlNet to evaluate their impact. (c) Iterative Refinement: We demonstrate the benefits of our method’s refinement process over multiple iterations. (d) Prompt Variations: We explore alternative prompts beyond ‘a creative <obj> ’. For additional ablation results, please refer to Table 3 .]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_7.png' | relative_url }})

*Figure 7. Ablation Study. We perform comprehensive ablation studies to analyze the design choices of CREA: (a) Model Generalization: Our method extends effectively to different generative models, such as SDXL and DALL-E. (b) Parameter Sensitivity: We ablate CFG values for Flux and the conditioning scale for ControlNet to evaluate their impact. (c) Iterative Refinement: We demonstrate the benefits of our method’s refinement process over multiple iterations. (d) Prompt Variations: We explore alternative prompts beyond ‘a creative <obj> ’. For additional ablation results, please refer to Table 3 .*


![Figure 8. Video Generation . Comparison between baseline generations from CogVideoX and outputs generated using our creative agentic pipeline. Our method enables the creation of visually diverse and creative video scenes.]({{ '/images/04-2025/CREA:_A_Collaborative_Multi-Agent_Framework_for_Creative_Content_Generation_with_Diffusion_Models/figure_8.png' | relative_url }})

*Figure 8. Video Generation . Comparison between baseline generations from CogVideoX and outputs generated using our creative agentic pipeline. Our method enables the creation of visually diverse and creative video scenes.*
