"""Auxiliary functions."""

from typing import List


def get_skipped_titles(exculded_by_keywords_paths: List[str], exculded_by_classifier_paths: List[str]) -> List[str]:
    """Get the titles of the skipped papers.

    Args:
        exculded_by_keywords_paths (List[str]): The paths to the files where papers were excluded by keywords.
        exculded_by_classifier_paths (List[str]): The paths to the files where papers were excluded by classifier.

    Returns:
        List[str]: The titles of the skipped papers.
    """
    skipped_titles = []
    for path in exculded_by_keywords_paths:
        with open(path, "r", encoding="utf-8") as file:
            skipped_titles.extend(file.readlines())

    for path in exculded_by_classifier_paths:  # noqa: WPS440
        with open(path, "r", encoding="utf-8") as file:  # noqa: WPS440
            skipped_titles.extend(file.readlines())
    return skipped_titles
