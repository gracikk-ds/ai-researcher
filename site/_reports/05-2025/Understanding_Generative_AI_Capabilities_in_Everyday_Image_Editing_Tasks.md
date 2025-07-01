---
title: Understanding_Generative_AI_Capabilities_in_Everyday_Image_Editing_Tasks
layout: default
date: 2025-05-22
---
![Figure 1: We propose PSR, the largest dataset of realworld image-editing requests and human-made edits. PSR enables the community (and our work) to identify types of requests that can be automated using existing AIs and those that need improvement. PSR is the first dataset to tag all requests with WordNet subjects, realworld editing actions, and creativity levels.]({{ '/images/05-2025/Understanding_Generative_AI_Capabilities_in_Everyday_Image_Editing_Tasks/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the gap between the promise of generative AI for image editing and its practical utility for everyday users. They argue that existing benchmarks often rely on synthetic or contrived editing requests, which do not accurately represent the diversity, ambiguity, and specific needs found in real-world scenarios. This work aims to understand what users actually request, evaluate how well current state-of-the-art (SOTA) AI editors can fulfill these requests compared to skilled humans, identify key areas for AI improvement, and assess whether Vision Language Models (VLMs) can serve as reliable judges for edit quality.

## 2. Key Ideas and Methodology
The core idea is to perform a large-scale, systematic study of real-world image editing tasks to benchmark generative AI capabilities. The methodology involves several key steps:
- **Data Collection:** The authors created **PSR**, a new dataset of 83k real-world image editing requests and their 305k corresponding human-made edits, sourced from the `/r/PhotoshopRequest` Reddit community.
- **Taxonomy and Annotation:** They developed a novel taxonomy to classify each request by its `subject` (mapped to WordNet), `editing action` (a set of 15 verbs like *delete*, *add*, *adjust*), and `creativity level` (low, medium, or high). This annotation was performed using large language models.
- **Comparative Evaluation:** They generated edits for a subset of requests using 49 different AI models (including GPT-40, Gemini-2.0-Flash, and SeedEdit).
- **Human Study:** A pairwise comparison study was conducted where 122 human raters judged which edit—the AI's or a human's—better fulfilled the original request.
- **VLM as Judge:** The study also evaluated three SOTA VLMs as judges to compare their preferences against human ratings.

## 3. Datasets Used / Presented
- **PSR (PhotoshopRequest) Dataset:** The primary dataset presented, containing 83,000 real-world requests and 305,000 human-created edits collected over 12 years. It is the largest dataset of its kind and is annotated with a detailed taxonomy of subjects, actions, and creativity levels.
- **PSR-328:** A curated test subset of 328 requests from PSR, balanced across low, medium, and high creativity levels. This subset was used for the intensive human and VLM evaluation, comprising 1,644 human edits and 2,296 AI-generated edits.

## 4. Main Results
- **AI editors can satisfactorily handle about one-third (33.4%) of real-world requests.** Human-made edits are still preferred by human judges in 66% of cases.
- **AI performance is context-dependent.** AIs perform better on open-ended, high-creativity tasks (e.g., "make this magical") but struggle with low-creativity tasks that demand high precision (e.g., precise object removal).
- **Key AI weaknesses include a failure to preserve subject identity** (especially for people and animals), introducing unwanted artifacts, and misinterpreting user instructions. However, AIs often improve the general aesthetics of an image, even when not explicitly asked to.
- **VLMs are poor proxies for human judgment.** They exhibit strong biases (e.g., heavily favoring edits from specific models like GPT-40) and achieve low agreement (Cohen's κ < 0.23) with human raters, often failing to notice critical details or identity changes.

## 5. Ablation Studies
The paper presents several detailed breakdown analyses instead of traditional ablation studies:
- **Performance by AI Model:** A comparison of 49 AI models showed that SeedEdit had the highest win rate against human editors (winning or tying in 46.5% of its matchups), followed by GPT-40 (38.5%).
- **Performance by Creativity Level:** The performance gap between humans and AI narrows as creativity requirements increase. For low-creativity tasks, AI wins/ties in only 29.9% of cases, which rises to 39.1% for high-creativity tasks.
- **Performance by Editing Action:** AIs are most successful at `clone` (48% win+tie rate) and `apply` (39.6%) actions but perform poorly on `zoom` (14.7%) and `crop` (18.6%).
- **Impact of Aesthetic Improvement:** AIs are more likely to be preferred when their edits result in a larger increase in aesthetic score (measured by LAION Aesthetics) compared to the human edit. An AI's win rate increases from 18.7% to 30.3% when its aesthetic improvement surpasses the human's.

## 6. Paper Figures
![Figure 2: Example cases from PSR dataset where PSR wizard edits were preferred by human raters over the AI edits (a-c) and samples where AI edits was preferred (d-f). (a) : The human edit completes the request, but the AI]({{ '/images/05-2025/Understanding_Generative_AI_Capabilities_in_Everyday_Image_Editing_Tasks/figure_2.jpg' | relative_url }})
![Figure 4: AIs can significantly alter both a person’s identity and the overall image quality through iterative imageediting requests. GPT4o was repeatedly instructed to modify the shirt color, with each step’s output serving as the input for the next iteration. Over iterations, facial identity, body shape, and the background shift away from the original person (more details in Appendix G ).]({{ '/images/05-2025/Understanding_Generative_AI_Capabilities_in_Everyday_Image_Editing_Tasks/figure_4.jpg' | relative_url }})
![Figure 5: o 1 judge occasionally fails to notice details in edited images, here, overlooking the position of the hand and the configuration of the fingers.]({{ '/images/05-2025/Understanding_Generative_AI_Capabilities_in_Everyday_Image_Editing_Tasks/figure_5.jpg' | relative_url }})
![Figure 6: AI models tend to increase overall image aesthetics. While both requests (a) and (b) ask for changes in the background, AI editors tend to enhance the subject’s facial features. SeedEdit]({{ '/images/05-2025/Understanding_Generative_AI_Capabilities_in_Everyday_Image_Editing_Tasks/figure_6.jpg' | relative_url }})
