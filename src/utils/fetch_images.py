"""Extract images from a PDF file into an output folder."""

import io
import os
import re

import fitz
from loguru import logger
from PIL import Image

MIN_IMAGE_SIZE: int = 10


def filter_images_by_size(blk: dict, img_index: int, page_index: int) -> bool:
    """Filter images by size.

    Args:
        blk (dict): Block object
        img_index (int): Index of the image
        page_index (int): Index of the page

    Returns:
        bool: True if image is large enough, False otherwise
    """
    blk_width = blk["bbox"][2] - blk["bbox"][0]
    blk_height = blk["bbox"][3] - blk["bbox"][1]
    if blk_width <= MIN_IMAGE_SIZE and blk_height <= MIN_IMAGE_SIZE:
        logger.info(f"Skipping image {img_index} on page {page_index} because it's too small.")
        return True
    return False


def get_block_description(block: dict) -> str:
    """Given a page block, return the text appearing in the block.

    Args:
        block (dict): Page block

    Returns:
        str: The text appearing in the block
    """
    description = " ".join(span["text"] for line in block["lines"] for span in line["spans"]).strip()  # noqa: WPS221
    if "Figure" not in description and "Fig." not in description:
        return ""
    description = re.sub(r"\s+", " ", description)
    description = re.sub(r"\n", " ", description)
    return re.sub(r"- ", "", description)


def extract_figure_number(description: str) -> str:
    """Extract the figure number from the description.

    Args:
        description (str): The description of the figure

    Returns:
        str: The figure number
    """
    match = re.search(r"Figure (\d+)", description)
    if match:
        return match.group(1)
    match = re.search(r"Fig\. (\d+)", description)
    if match:
        return match.group(1)
    return ""


def extract_images(pdf_path: str, output_folder: str = "images") -> None:  # noqa: WPS210,WPS231,C901
    """Extract images from a PDF file into an output folder.

    Args:
        pdf_path: Path to the input PDF file
        output_folder: Folder to save extracted images
    """
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each page
    max_pages: int = 10
    max_images: int = 10
    img_num = 0
    for page_index, page in enumerate(doc, start=1):
        if page_index > max_pages:
            break
        # Reading-order blocks of this page
        blocks = page.get_text("dict")["blocks"]
        is_inside_picture = False
        coords = None
        for blk_idx, blk in enumerate(blocks, start=1):
            if blk["type"] != 1 and not is_inside_picture:
                continue

            if blk["type"] == 1:
                if filter_images_by_size(blk, blk_idx, page_index):
                    continue
                is_inside_picture = True

            if coords is None:
                coords = blk["bbox"]
            else:
                coords = (
                    min(coords[0], blk["bbox"][0]),
                    min(coords[1], blk["bbox"][1]),
                    max(coords[2], blk["bbox"][2]),
                    max(coords[3], blk["bbox"][3]),
                )

            if blk["type"] != 1:
                description = get_block_description(blk)
                figure_number = extract_figure_number(description)
                if figure_number == "":
                    continue
            else:
                continue
            image_name = f"figure_{figure_number}.jpg"  # noqa: WPS237
            image_path = os.path.join(output_folder, image_name)
            rect = fitz.Rect(coords[0] - 10, coords[1] - 10, coords[2] + 10, coords[3] + 10)
            pix = page.get_pixmap(dpi=300, clip=rect, alpha=False)
            img_bytes = pix.tobytes("ppm")  # Get image as PPM bytes
            image = Image.open(io.BytesIO(img_bytes))
            image = image.convert("RGB")  # Ensure no alpha channel for JPEG
            image.save(image_path, "JPEG", quality=70)
            # pix.save(image_path, quality=70)
            with open(os.path.join(output_folder, f"figure_{figure_number}.txt"), "w") as description_file:
                description_file.write(f"{description}")
            is_inside_picture = False
            coords = None
            img_num += 1
        if img_num >= max_images:
            break
    logger.info(f"\nCompleted extraction of images from '{pdf_path}'")


# if __name__ == "__main__":
#     extract_images(
#         "data/pdfs/01-2024/Unified_Diffusion-Based_Rigid_and_Non-Rigid_Editing_with_Text_and_Image_Guidance.pdf",
#         "site/images/01-2024/",
#     )
