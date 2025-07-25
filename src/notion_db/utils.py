"""Utility functions for working with Notion."""

import os
import re


def resolve_image_path(url: str, project_root: str) -> str:
    """Resolve the path to an image.

    Args:
        url (str): URL of the image.
        project_root (str): Root directory of the project.

    Returns:
        str: Path to the image.
    """
    pattern = r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}"
    match = re.search(pattern, url)
    if match:
        relative_path = match.group(1)
        return os.path.join(project_root, relative_path.lstrip("/"))
    return ""
