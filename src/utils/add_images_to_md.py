"""Add images and their descriptions to a markdown file."""

import os
from typing import List, Tuple

from loguru import logger

from src.utils.paper_message_template import add_authors_merits


def load_images_and_descriptions(images_dir: str) -> List[Tuple[str, str, str]]:
    """Load images and descriptions from the images directory.

    Args:
        images_dir (str): Path to the directory containing images and .txt descriptions.

    Returns:
        List[Tuple[str, str, str]]: List of tuples containing the base name, image path, and description.
    """
    figures: List[Tuple[str, str, str]] = []
    for fname in sorted(os.listdir(images_dir)):
        if fname.endswith(".jpg"):
            base = fname[:-4]
            txt_path = os.path.join(images_dir, base + ".txt")
            img_path = os.path.join(images_dir, fname)
            if os.path.exists(txt_path):
                with open(txt_path, encoding="utf-8") as description_file:
                    desc = description_file.read().strip()
                figures.append((base, img_path, desc))
    return figures


def img_block(img_path: str, desc: str) -> str:
    """Prepare markdown blocks.

    Args:
        img_path (str): Path to the image.
        desc (str): Description of the image.

    Returns:
        str: Markdown block.
    """
    rel_path = os.path.relpath(img_path).replace("site", "")
    rel_path = f"'{rel_path}' | relative_url"
    rel_path = "{{ " + rel_path + " }}"
    return f"![{desc}]({rel_path})"


def add_images_to_md(md_path: str, images_dir: str, paper_info: dict) -> None:
    """
    Add images and their descriptions from images_dir to a markdown file at md_path.

    Figure 1 is inserted at the top, others are appended at the end.

    Args:
        md_path (str): Path to the markdown file.
        images_dir (str): Path to the directory containing images and .txt descriptions.
        paper_info (dict): The information about the paper.
    """
    paper_name = md_path.split("/")[-1].split(".")[0]
    new_md = f"---\ntitle: {paper_name}\nlayout: default\ndate: {paper_info['published_date']}\n---\n"
    new_md += f"## {paper_info['title']}\n"
    new_md += f"**Authors:**{add_authors_merits(paper_info['authors'])}\n\n"
    new_md += f"**ArXiv URL:** {paper_info['arxiv_url']}\n\n"
    new_md += f"**Citation Count:** {paper_info['citation_count']}\n\n"
    new_md += f"**Published Date:** {paper_info['published_date']}\n\n"

    figures = load_images_and_descriptions(images_dir)
    if not figures:
        logger.warning(f"No figures found in {images_dir}")
        return

    # Separate Figure 1 and the rest
    fig1 = next(
        ((base, img_path, desc) for (base, img_path, desc) in figures if base == "figure_1"),  # noqa: WPS221
        None,
    )
    other_figs = [(base, img_path, desc) for (base, img_path, desc) in figures if base != "figure_1"]

    if fig1 is None:
        fig1 = other_figs[0]
        other_figs = other_figs[1:]

    # Read the original markdown
    with open(md_path, encoding="utf-8") as md_file:
        md_content = md_file.read()

    # Insert Figure 1 at the top
    if fig1:
        _, img_path, desc = fig1
        new_md += img_block(img_path, desc) + "\n"

    new_md += md_content.rstrip()

    if not other_figs:
        logger.warning(f"No other figures found in {images_dir}")
        return
    new_md = new_md + "\n\n"
    new_md = new_md + "## 6. Paper Figures\n"

    # Append other figures
    for _, img_path, desc in other_figs:  # noqa: WPS519,WPS440
        new_md += img_block(img_path, desc) + "\n"

    # Write back to the markdown file
    # md_path_with_images = md_path.replace(".md", "_with_images.md")
    with open(md_path, "w", encoding="utf-8") as md_file:  # noqa: WPS440
        md_file.write(new_md)


def extract_paper_summary(md_path: str) -> str:
    """Extract the summary of the paper from the markdown file.

    Args:
        md_path (str): Path to the markdown file.

    Returns:
        str: The summary of the paper.
    """
    with open(md_path, encoding="utf-8") as md_file:
        md_content = md_file.read()
    motivation_of_the_paper = md_content.split("## 1. Motivation of the Paper")[1].split("##")[0]
    return motivation_of_the_paper.strip()
