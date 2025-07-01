## 1. Motivation of the Paper
Existing unified Multimodal Large Language Models (MLLMs) struggle to simultaneously excel at visual understanding, image generation, and fine-grained editing. Current models often compromise on one capability to enhance another; for instance, some achieve strong understanding but lack the texture preservation needed for high-quality editing, while others have decoupled architectures that limit their ability to perform interleaved, multi-turn tasks. The authors address this gap by developing a truly unified architecture that seamlessly integrates all three core functionalities without sacrificing performance.

## 2. Key Ideas and Methodology
The authors propose ILLUME+, a unified MLLM built on three key ideas:
- **Dual Vision Tokenizer (DualViTok):** A novel tokenizer with two parallel branches. A semantic branch uses a pre-trained text-aligned encoder to capture high-level meaning, while a pixel branch preserves fine-grained texture details. This dual representation is designed to balance understanding and reconstruction quality.
- **Unified MLLM with Coarse-to-Fine Generation:** The model uses a continuous-input, discrete-output scheme. It takes continuous visual features as input to avoid information loss during quantization and autoregressively generates discrete tokens in a coarse-to-fine manner (semantic tokens first, then pixel tokens) using a single language model head.
- **Diffusion Decoder:** An optional diffusion model is used as a decoder to refine the generated tokens into high-fidelity images and enable efficient super-resolution, enhancing the final output quality.

The entire system is trained progressively, gradually increasing image resolution and task complexity to ensure stability and performance.

## 3. Datasets Used / Presented
The model was trained on a large-scale, diverse dataset mixture across several stages:
- **Tokenizer & Diffusion Training:** 63M images from public datasets like COYO and Wukong, plus in-house data, were used to train the DualViTok and diffusion decoder.
- **MLLM Training:** A 70M sample pre-training dataset and a 9.7M sample supervised fine-tuning (SFT) dataset were used. These combined various tasks and data sources, including image captioning (LLaVA), instruction-following editing (UltraEdit, AnyEdit), and text-to-text reasoning (OpenOrca).
- **Evaluation:** The model was evaluated on a wide range of benchmarks for understanding (MMBench, DocVQA, OCRBench), generation (MJHQ-30K, GenEval), and editing (Emu Edit).

## 4. Main Results
Despite its relatively small size (3B parameters), ILLUME+ demonstrates competitive or state-of-the-art performance across all three capabilities.
- **Understanding:** It achieves strong results, particularly on document-oriented tasks where many unified models falter, outperforming larger competitors.
- **Generation:** It obtains a state-of-the-art FID score of 6.00 on the MJHQ-30K benchmark among unified models and achieves the highest score on the advanced portion of GenAI-bench, indicating high-quality and context-aware image generation.
- **Editing:** It excels on the Emu Edit benchmark, showing a superior ability to follow editing instructions while preserving unchanged image parts.
The authors claim ILLUME+ provides an effective and scalable foundation for building powerful, truly unified multimodal models.

## 5. Ablation Studies
- **Tokenizer Design:** The dual-branch (semantic + pixel) tokenizer significantly outperformed single-branch alternatives in both reconstruction quality and downstream understanding tasks.
- **Input Representation:** Using continuous visual features as input for the MLLM proved crucial for understanding, substantially outperforming the use of discrete tokens as input across all benchmarks.
- **Tokenizer Components:** Experiments validated design choices like using DC blocks for sampling, a larger pixel codebook, and noise injection during training, which collectively improved reconstruction rFID from a baseline of 1.83 to 1.33.
- **Quantization Method:** The SimVQ method was shown to be superior to vanilla VQ, improving reconstruction quality (rFID of 1.83 vs. 2.24) and achieving 100% codebook utilization.