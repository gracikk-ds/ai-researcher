---
title: An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control
layout: default
date: 2024-03-07
---
![Figure 1: The editing pipeline of using D-Edit. The user first uploads an image which is segmented into several items. After finetuning DPMs, the user can do various types of control, including (a) replacing the model with another using a text prompt; (b) refining imperfect details caused by segmentation; (c) moving bags to the ground; (d) replacing the handbag with another one from a reference image; (e) reshaping handbag; (f) resizing the model and handbag; (g) removing background.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_1.jpg' | relative_url }})
## 1. Motivation of the Paper
The authors address two primary challenges in prompt-based image editing with diffusion models. First, directly modifying a global text prompt often results in unintended, widespread changes to the entire image, failing to preserve the unedited regions. Second, existing methods that use masks to protect unedited areas often produce disharmonious results because the diffusion model's attention mechanism can disregard these spatial constraints, leading to unnatural transitions and artifacts. The paper aims to create a versatile editing framework that provides precise, localized control over individual objects within an image while maintaining overall coherence.

## 2. Key Ideas and Methodology
The core idea of the paper, named **D-Edit**, is to disentangle the global image-prompt interaction into multiple, independent **item-prompt interactions**. This is achieved by segmenting an image into distinct "items" (objects and background) and associating each with a unique, learnable prompt.

The methodology consists of three main components:
1.  **Grouped Cross-Attention:** The standard cross-attention mechanism in diffusion models is modified. Instead of allowing every image patch (query) to attend to the entire text prompt (key/value), the attention is restricted. The queries from a specific image item are only allowed to attend to the key/value pairs generated from that item's unique prompt. This enforces disentangled control, ensuring that editing one item's prompt does not affect other items.
2.  **Item-Prompt Association via Two-Step Finetuning:** To establish a strong link between each visual item and its new prompt, a two-step optimization process is performed on the diffusion model for a given image:
    *   **Prompt Injection:** New, randomly initialized tokens are added to the text encoder's vocabulary to serve as the unique prompt for each item. Only the embeddings of these new tokens are optimized to reconstruct the original image.
    *   **Model Finetuning:** The UNet's cross-attention layer weights are then finetuned to perfect the reconstruction of the original image using the learned item prompts.
3.  **Versatile Editing Operations:** Once finetuned, the model can perform various edits by manipulating the item-prompt associations. This includes text-based editing (swapping a learned prompt for text), image-based editing (swapping learned prompts between two images), mask-based editing (moving, resizing, or reshaping an item's mask), and item removal (deleting an item's prompt-mask pair).

## 3. Datasets Used / Presented
The authors introduce two new benchmarks for quantitative evaluation:
*   **D-Item(Text):** A benchmark of 100 manually selected multi-item images. Each image is segmented into 3-8 items. For evaluation, 2 items per image are chosen and paired with 5 different target text prompts, creating a total of 1,000 item-prompt editing pairs. It is used to evaluate text-guided editing.
*   **D-Item(Image):** Constructed from the same 100 images as D-Item(Text). Each selected item is paired with two different reference items from other images, resulting in 400 item-item pairs for evaluating image-guided editing (item replacement).

## 4. Main Results
D-Edit demonstrates state-of-the-art performance across multiple editing tasks by providing superior image preservation and target guidance fidelity.
*   **Text-Guided Editing:** On the D-Item(Text) benchmark, D-Edit achieves a significantly better LPIPS score of **0.179** (lower is better for image preservation) compared to P2P (0.401) and SDEdit (0.432). It also shows stronger semantic alignment with a CLIP-T score of **42.0** (higher is better) compared to P2P (39.5).
*   **Image-Guided Editing:** On D-Item(Image), D-Edit shows strong preservation of the original image (LPIPS of **0.340**) and high fidelity to the reference item (CLIP-I score of **66.4**), outperforming methods like Anydoor.
*   **Item Removal:** In a user study, D-Edit's results for removing an object were rated higher in both quality (**4.01/5**) and fidelity (**4.44/5**) compared to a standard SDXL-inpaint baseline (3.26/5 and 2.42/5, respectively).

The authors claim that D-Edit is the first unified framework capable of performing mask-based editing and combining text- and image-based editing on specific items simultaneously.

## 5. Ablation Studies
Two main ablation studies were performed to validate the core components of the D-Edit framework.
1.  **Effect of Cross-Attention Disentanglement:** The authors compared text-guided editing results with and without the proposed grouped cross-attention. Without disentanglement, editing a target item (e.g., a handbag) caused the edit to "bleed" into surrounding regions (e.g., the hand holding it), altering their appearance. With disentanglement, the edit was precisely confined to the target item, preserving the rest of the image and producing a more controllable and higher-quality result.
2.  **Influence of Token Number:** The study investigated how many new tokens should be used to represent each item. Experiments were run with 1, 2, 5, and 10 tokens. The results showed that using 1-5 tokens yielded good performance, with **5 tokens** providing the best balance of image preservation (LPIPS 0.179) and text alignment (CLIP-T 42.0). Using 10 tokens complicated the training and degraded performance.

## 6. Paper Figures
![Figure 10: Post-editing refinement can be performed when obtaining imperfect results due to imperfect segmentation.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_10.jpg' | relative_url }})
![Figure 11: Removing items one by one from the image.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_11.jpg' | relative_url }})
![Figure 12: Qualitative comparison of textual-guided editing with and without cross-attention disentanglement]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_12.jpg' | relative_url }})
![Figure 2: Comparison of conventional full cross-attention and grouped cross-attention. Query, key, and value are shown as one-dimensional vectors. For grouped cross-attention, each item (corresponding to certain pixels/patches) only attends to the text prompt (two tokens) assigned to it.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_2.jpg' | relative_url }})
![D c Figure 3: Embedding layer in the text encoder. New tokens are inserted with random initialization.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_3.jpg' | relative_url }})
![Figure 5: Text-guided editing. D-Edit enables selection of any item segmentation and edit using text prompt.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_5.jpg' | relative_url }})
![Figure 6: The learned prompt (denoted as [v]) can be combined with words to achieve refinement/editing of the target item. (a) Augment an item prompt with words while keeping other prompts unchanged for editing. (b) Generate the entire image with certain item prompt(s) augmented with text words for personalization.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_6.jpg' | relative_url }})
![Figure 7: Qualitative comparison of image-guided editing. D-Edit is compared with Anydoor, Paint-by-Example, and TF-ICON, on item replacement and face swapping.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_7.jpg' | relative_url }})
![Figure 8: Image-guided editing: Any item in the image can be replaced by another item from the same or different images.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_8.jpg' | relative_url }})
![Figure 9: Different types of mask-based editing: (a) Moving/swapping items; (b) reshaping an item; (c) Resizing an item.]({{ '/images/03-2024/An_Item_is_Worth_a_Prompt:_Versatile_Image_Editing_with_Disentangled_Control/figure_9.jpg' | relative_url }})
