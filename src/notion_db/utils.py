"""Utility functions for working with Notion."""

import os
import re
from typing import List, Match, Optional, Tuple


def extract_image_links(markdown: str) -> List[Tuple[str, str]]:
    """Extract image links from Markdown text.

    Args:
        markdown (str): Markdown text to extract image links from.

    Returns:
        List[Tuple[str, str]]: List of tuples containing the alt text and URL of the image.
    """
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    return re.findall(pattern, markdown)


def check_for_image(line: str) -> Optional[Match[str]]:
    """Check if the line contains an image.

    Args:
        line (str): Line of text to check.

    Returns:
        bool: True if the line contains an image, False otherwise.
    """
    return re.match(r"!\[([^\]]*)\]\(([^)]+)\)", line)


def resolve_image_path(url: str, project_root: str) -> str:
    """Resolve the path to an image.

    Args:
        url (str): URL of the image.
        project_root (str): Root directory of the project.

    Returns:
        str: Path to the image.
    """
    match = re.match(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", url)
    if match:
        relative_path = match.group(1)
        return os.path.join(project_root, relative_path.lstrip("/"))
    return os.path.join(project_root, url.lstrip("/"))
