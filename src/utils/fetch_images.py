"""Extract images from a PDF file into an output folder."""

import os
import re
from io import BytesIO
from pathlib import Path
from typing import List, Tuple

import fitz
from loguru import logger
from PIL import Image

MIN_IMAGE_SIZE: int = 50
MAX_IMAGE_HEIGHT: int = 416


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


def extract_image_bytes_and_path(
    blk: dict,
    figure_number: str,
    output_folder: str,
) -> Tuple[bytes, str]:
    """Extract the image bytes and metadata.

    Args:
        blk (dict): The block object
        figure_number (str): The figure number
        output_folder (str): The folder to save the image

    Returns:
        Tuple[bytes, str]: The image bytes and the path to the image
    """
    image_bytes = blk["image"]
    image_ext = blk["ext"]
    image_name = f"figure_{figure_number}.{image_ext}"  # noqa: WPS237
    image_path = os.path.join(output_folder, image_name)
    return image_bytes, image_path


def save_image(image_bytes: bytes, image_path: str) -> None:
    """Resize  if needed and save the image to the specified path.

    Args:
        image_bytes (bytes): The image bytes
        image_path (str): The path to save the image
    """
    img = Image.open(BytesIO(image_bytes))
    if img.height > MAX_IMAGE_HEIGHT:
        new_width = int(img.width * MAX_IMAGE_HEIGHT / img.height)
        img = img.resize((new_width, MAX_IMAGE_HEIGHT))
    img.save(image_path)


def first_text_after(blocks: List[dict], start_idx: int) -> str:
    """Given a list of page blocks, return the first text appearing after start_idx.

    Args:
        blocks (List[dict]): The list of page blocks
        start_idx (int): The index of the block to start searching from

    Returns:
        str: The first text appearing after start_idx
    """
    for blk in blocks[start_idx:]:
        if blk["type"] == 0:  # text
            description = " ".join(
                span["text"] for line in blk["lines"] for span in line["spans"]  # noqa: WPS221
            ).strip()
            description = re.sub(r"\s+", " ", description)
            description = re.sub(r"\n", " ", description)
            return re.sub(r"- ", "", description)  # noqa: WPS360
    return ""


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
    return ""


def extract_images(pdf_path: str, output_folder: str = "images") -> None:  # noqa: WPS210,WPS231,C901
    """Extract images from a PDF file into an output folder.

    Args:
        pdf_path: Path to the input PDF file
        output_folder: Folder to save extracted images
    """
    doc = fitz.open(pdf_path)
    pdf_stem = Path(pdf_path).stem
    output_folder = os.path.join(output_folder, pdf_stem)
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each page
    for page_index, page in enumerate(doc, start=1):
        # Reading-order blocks of this page
        blocks = page.get_text("dict")["blocks"]
        for blk_idx, blk in enumerate(blocks, start=1):
            if blk["type"] != 1:
                continue
            if filter_images_by_size(blk, blk_idx, page_index):
                continue
            description = first_text_after(blocks, blk_idx)
            if "Figure" not in description:
                continue
            figure_number = extract_figure_number(description)
            image_bytes, image_path = extract_image_bytes_and_path(blk, figure_number, output_folder)
            save_image(image_bytes, image_path)
            with open(os.path.join(output_folder, f"figure_{figure_number}.txt"), "w") as description_file:
                description_file.write(f"{description}")
    logger.info(f"\nCompleted extraction of images from '{pdf_path}'")


if __name__ == "__main__":
    extract_images("pdfs/mgie.pdf", "site/images")
