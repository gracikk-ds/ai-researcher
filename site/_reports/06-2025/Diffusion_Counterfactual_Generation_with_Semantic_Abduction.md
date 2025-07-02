---
title: Diffusion_Counterfactual_Generation_with_Semantic_Abduction
layout: default
date: 2025-06-09
---
## Diffusion Counterfactual Generation with Semantic Abduction
**Authors:**
- Rajat Rasal, h-index: 2, papers: 3, citations: 16
- Ben Glocker, h-index: 2, papers: 9, citations: 10

**ArXiv URL:** http://arxiv.org/abs/2506.07883v1

**Citation Count:** 0

**Published Date:** 2025-06-09

![Figure 2. Morpho-MNIST ( 28 × 28 ) counterfactuals generated using an amortised, anti-causally guided semantic mechanism ( p ∅ = 0 . 1 , ω = 1 . 5 ) based on the DSCM shown in (a). (b) illustrates counterfactual soundness (Obs: Observation, Comp: Composition, Cf: Counterfactual, Rev: Reversibility). (c) depicts image counterfactuals: interventions are shown above the top row and the bottom row visualises total causal effects (red: increase, blue: decrease), refer to (Appendix A.2 ) for details.]({{ '/images/06-2025/Diffusion_Counterfactual_Generation_with_Semantic_Abduction/figure_2.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address the challenge of generating high-fidelity counterfactual images that are faithful to an underlying causal model. Existing methods based on autoencoders often struggle with image quality and scalability. While diffusion models produce state-of-the-art visuals, they typically lack a controllable semantic representation space, which is crucial for performing causal interventions and preserving the subject's core identity during edits. This gap limits their use in applications requiring principled causal reasoning, such as personalized medicine or fair AI.

## 2. Key Ideas and Methodology
The paper proposes a framework to integrate Pearlian causality into diffusion models for counterfactual image generation. The core methodology is built around three key ideas:

*   **Spatial vs. Semantic Abduction:** The authors first define a "spatial mechanism" that uses standard DDIM inversion to abduct (infer) the initial noise map, which encodes low-level structure. They then introduce their primary contribution, a "semantic mechanism," which decomposes the exogenous noise into two parts: the low-level spatial noise and a high-level semantic latent code `z` inferred by a separate encoder. This explicit separation allows for better preservation of high-level semantic attributes.
*   **Amortised Anti-Causal Guidance:** To ensure faithfulness to interventions, the framework incorporates classifier-free guidance. This is framed as an "anti-causal" predictor that steers the generation process toward the desired counterfactual outcome.
*   **Dynamic Semantic Abduction:** To mitigate the identity degradation caused by strong guidance, the authors propose Counterfactual Trajectory Alignment (CTA). This is a test-time optimization that fine-tunes guidance tokens at each step of the reverse diffusion process to better align the guided and unguided generation paths, improving the preservation of backgrounds and fine-grained features.

## 3. Datasets Used / Presented
*   **Morpho-MNIST:** A synthetic dataset of 28x28 digit images with known causal relationships between attributes like digit class, slant, thickness, and intensity. Used for controlled quantitative evaluation. A colorized version was also created.
*   **CelebA-HQ:** A dataset of 64x64 high-quality celebrity face images. Used to model causal relationships between facial attributes (e.g., "Smiling" causes "Mouth Open") and evaluate identity preservation in a real-world scenario.
*   **EMBED:** A real-world medical imaging dataset of 192x192 mammograms. Used to demonstrate a practical application: removing spurious artifacts (triangular and circular skin markers) via counterfactual intervention.

## 4. Main Results
The main finding is that the proposed semantic mechanisms significantly outperform baseline methods (VAE, HVAE, VCI) and the authors' own spatial mechanisms in preserving identity while maintaining high effectiveness (faithfulness to the causal intervention).

*   On Morpho-MNIST, semantic mechanisms achieve better identity preservation (lower composition/reversibility error) than spatial ones for the same guidance strength, with only a minor drop in effectiveness.
*   On CelebA-HQ, the semantic mechanism consistently achieves superior identity preservation (e.g., LPIPS of 0.096 vs. 0.171 for the spatial model under one condition) and better preserves complex features like hairstyle and background.
*   The authors claim their work is the first to systematically enable principled trade-offs between causal control and identity preservation for diffusion-based counterfactuals.

## 5. Ablation Studies
*   **Spatial vs. Semantic Mechanism:** Comparing the two mechanisms shows that explicitly modeling a semantic latent space (`z`) leads to substantially better identity preservation (lower L1 and LPIPS scores) across all experiments, demonstrating the core value of semantic abduction.
*   **Effect of Guidance Scale (ω):** Increasing the guidance scale `ω` consistently improves effectiveness (e.g., F1-score on CelebA-HQ) but degrades identity preservation (higher composition/reversibility error). This highlights the fundamental trade-off between causal faithfulness and identity.
*   **Effect of Guidance Dropout (pØ):** Training with a lower dropout probability `pØ` (i.e., more conditional training) improves effectiveness but harms identity preservation, similar to the effect of increasing `ω`.
*   **Effect of Dynamic Abduction (CTA):** Adding dynamic abduction to the guided semantic mechanism qualitatively and quantitatively improves identity preservation, especially for preserving backgrounds, skin tones, and other intricate details that are often distorted by strong guidance.

## 6. Paper Figures
![Figure 3. CelebA-HQ ( 64 × 64 ) counterfactuals generated using amortised, anti-causally guided semantic mechanisms. (a) DSCM with spatial ( u ), semantic ( z ) and dynamic ( ∅ ∗ 1: T ) exogenous noise terms for x . (b) shows counterfactual soundness using semantic abduction with p ∅ = 0 . 1 and ω = 2 . (c) shows that semantic mechanisms improve identity preservation, and dynamic abduction further improves backgrounds, hairstyle, skin colour and facial structure. Here, the choice of η is fine-tuned for each observation.]({{ '/images/06-2025/Diffusion_Counterfactual_Generation_with_Semantic_Abduction/figure_3.jpg' | relative_url }})
![Figure 4. CelebA-HQ: Effect of guidance scale ( ω ), depicted by the number on each dot, on composition, model identity preservation (IDP) and effectiveness of amortised anti-causally guided mechanisms trained with p ∅ = 0 . 1 .]({{ '/images/06-2025/Diffusion_Counterfactual_Generation_with_Semantic_Abduction/figure_4.jpg' | relative_url }})
![Figure 5. CelebA-HQ: Effect of step size ( η ) and guidance scale ( ω ) on model identity preservation (IDP) when using dynamic abduction with amortised anti-causally guided semantic mechanism ( p ∅ = 0 . 1 ) on 200 randomly chosen images from the val. set.]({{ '/images/06-2025/Diffusion_Counterfactual_Generation_with_Semantic_Abduction/figure_5.jpg' | relative_url }})
![Figure 6. Skin marker removal on EMBED (192 × 192) using an amortised, anti-causally guided semantic mechanism with and without dynamic abduction; (orange: circle, green: triangle).]({{ '/images/06-2025/Diffusion_Counterfactual_Generation_with_Semantic_Abduction/figure_6.jpg' | relative_url }})
