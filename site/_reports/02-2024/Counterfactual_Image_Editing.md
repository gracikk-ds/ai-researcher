---
title: Counterfactual_Image_Editing
layout: default
date: 2024-02-07
---
![Figure 1: (Left) A causal graph depicting the causal relationships among features. (Right) Image editing results are displayed, with the first row showing edits incorporating causal relations, and the second row without them. Each column represents a unique counterfactual query, altering the age, gender, and gray hair of the individuals. These instances provide preliminary evidence that the causal approach introduced in this paper ensures the preservation of the relevant causal invariances for the query across both factual and counterfactual images.]({{ '/images/02-2024/Counterfactual_Image_Editing/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
Current generative models for image editing often produce unrealistic or biased results because they rely on spurious correlations in the data rather than true causal relationships. For example, when asked to make a person in an image look older, a model might incorrectly change their gender simply because the training data contains more images of older men than older women. This paper addresses the problem of performing counterfactual image edits that are faithful to the underlying causal mechanisms of the real world, ensuring that changes to one attribute propagate logically to others while leaving causally independent attributes unchanged.

## 2. Key Ideas and Methodology
The authors' core idea is to formalize counterfactual image editing using causal inference principles. They introduce a new model class, **Augmented Structural Causal Models (ASCMs)**, to represent the causal relationships between image attributes (generative factors) and the final image.

The key contributions and methodology are:
- **Non-Identifiability Proof**: They formally prove that image counterfactuals are not uniquely identifiable from observational data alone, even when the causal graph between attributes is known. This means a single "correct" edited image cannot be determined.
- **Ctf-Consistent Estimation**: To overcome non-identifiability, they propose a relaxed criterion. Instead of a single point estimate, they derive theoretical "optimal bounds" for a counterfactual query. A model is deemed **Ctf-consistent** if its generated images produce attribute changes that fall within these bounds.
- **ANCM Algorithm**: They develop an efficient algorithm, the **Augmented Neural Causal Model (ANCM)**, to generate Ctf-consistent images. ANCM is a deep generative model that encodes the known causal diagram as a structural constraint, ensuring that its outputs adhere to the derived theoretical guarantees.

## 3. Datasets Used / Presented
- **Modified Colored MNIST with Bars**: A synthetic dataset where the causal ground truth is known and can be controlled. It features digits with attributes for color and the presence of a bar. The authors create two settings, "Backdoor" and "Frontdoor," each with a unique underlying causal graph to test the model's ability to handle different causal structures (e.g., confounding, mediation).
- **CelebA-HQ**: A high-resolution dataset of celebrity faces used to demonstrate the method's effectiveness on complex, real-world images. Plausible causal graphs based on common knowledge (e.g., age affects hair color; smiling affects mouth shape) are used as an inductive bias.

## 4. Main Results
The proposed ANCM method consistently outperformed baselines by generating causally plausible image edits.
- On the synthetic MNIST dataset, the quantitative results from ANCM for counterfactual queries fell within the theoretically derived optimal bounds, while baselines like CVAE, CGN, and DEAR did not.
- On CelebA-HQ, when editing a person's age to be older, ANCM correctly preserved their gender while increasing the likelihood of gray hair. In contrast, baseline methods often changed the person's gender, demonstrating their reliance on spurious dataset correlations.
The authors claim this is the first framework to provide formal causal guarantees for counterfactual image editing.

## 5. Ablation Studies
While the paper does not contain a formal ablation section, the experimental comparison against several baselines serves a similar purpose by testing the importance of the core components of the proposed causal framework. Each baseline represents an ablation of a key assumption:
- **CVAE**: Represents a model with no causal knowledge, relying only on statistical correlations. It frequently failed to preserve causally independent attributes.
- **CGN**: Assumes independent causal mechanisms between attributes, which is a restrictive assumption. It failed to model indirect causal effects present in the data.
- **DEAR**: Assumes a Markovian causal graph (i.e., no unobserved confounders). It failed in scenarios with confounding, which ANCM is designed to handle.
The superior performance of ANCM across all scenarios demonstrates that modeling general, semi-Markovian causal structures is crucial for robust and realistic counterfactual image editing.

## 6. Paper Figures
![(b) Figure 3: (a) The proxy generator c M is compatible with the same observational distributions with the unobserved true model but is not guaranteed to induce the same image counterfactual distributions. (b) Two different image counterfactual distributions in Example 3.2 . Each sample from a P ( I , I Y =0 ) has an initial image i and a counterfactual image i ′ Y =0 . Sampling from the red part of distributions, counterfactual images do not contain gray hair. Sampling from the blue part of distributions, counterfactual images have gray hair.]({{ '/images/02-2024/Counterfactual_Image_Editing/figure_3.jpg' | relative_url }})
![Figure 6: The causal diagram G B and samples for "Backdoor" setting. There are more red larger digits and green smaller digits; larger digits are less likely to have a bar on top; red digits are less likely to have a bar on top.]({{ '/images/02-2024/Counterfactual_Image_Editing/figure_6.jpg' | relative_url }})
