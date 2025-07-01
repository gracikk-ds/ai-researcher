## 1. Motivation of the Paper
The authors address the challenge of applying multiple editing instructions to an image using Diffusion Transformers (DiTs). Current methods are suboptimal: executing instructions sequentially (step-by-step) leads to accumulated errors and degraded image quality, while merging all instructions into a single prompt often results in "instruction conflicts," where the model fails to perform all edits. The paper aims to fill this gap by developing a framework that enables the parallel execution of multiple instructions in a single, efficient denoising process for DiT-based models.

## 2. Key Ideas and Methodology
The core contribution is **Instruction Influence Disentanglement (IID)**, a framework designed to prevent interference between multiple editing instructions. The key idea is to isolate the spatial influence of each instruction and apply them concurrently.

The methodology involves:
1.  **Instruction-Specific Mask Generation:** At a predefined reverse diffusion timestep `S`, the framework analyzes the self-attention maps of a DiT model. To create a mask for a specific instruction, it subtracts the averaged attention map of all other instructions from that instruction's own map. This "head-wise" subtraction effectively isolates the target editing region.
2.  **Adaptive Latent Blending:** The latent representations corresponding to each instruction are blended together using their respective masks. For models sensitive to instruction order, instructions are ranked by an "influence score" to ensure balanced execution.
3.  **Disentangled Attention:** A new, composite attention mask is constructed for the subsequent denoising steps. This mask constrains the attention mechanism, ensuring that tokens related to one instruction do not affect the editing regions of others, thereby mitigating conflicts.

## 3. Datasets Used / Presented
-   **MagicBrush:** The test split, containing 535 editing sessions with up to three instructions each, was used for quantitative evaluation and comparison against baselines.
-   **Custom Dataset:** A set of 50 real-world images with complex, multi-step instructions was collected by the authors and used for a human preference study.

## 4. Main Results
-   **Quantitative Improvement:** On the MagicBrush dataset, IID significantly improved the performance of both the FluxEdit and Omnigen models. For FluxEdit, IID reduced L1 error by 30% (0.1048 → 0.0731) and improved CLIP-I score (image quality) from 0.8487 to 0.8855 compared to the step-by-step baseline. Similar gains were observed for Omnigen.
-   **Qualitative Superiority:** Visual results show that IID produces sharper, more coherent images and achieves better instruction completion than sequential editing, which often introduces blurriness and fails on complex edits.
-   **Human Preference:** In a human study, IID was strongly preferred over the step-by-step method for both instruction alignment and preserving original image details, especially in scenarios with three or more instructions.

The authors claim their framework enables effective, parallelized multi-instruction editing for DiTs, reducing artifacts and improving fidelity.

## 5. Ablation Studies
-   **Pre-defined Step (S) for Blending:** The choice of timestep `S` to start the IID process is critical. For Omnigen, an early step (`S=15`) is necessary to avoid disrupting semantic information. FluxEdit is more robust and performs well with a later step (`S=27`).
-   **Mask Generation Timestep:** The quality of the generated masks improves as the reverse diffusion process advances from its start, stabilizing after a certain number of steps. This confirms the existence of an optimal timestep range for mask extraction.
-   **Layer for Mask Extraction:** The penultimate layer of the DiT was found to be optimal for mask extraction. Lower layers produced dispersed attention, while the final layer was too focused on image reconstruction to yield semantically meaningful masks.