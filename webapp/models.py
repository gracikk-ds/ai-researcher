"""Models for the web application."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Article:
    """Represents a single article or report."""

    id: str  # noqa: WPS111
    title: str
    date: str
    summary: str
    content: str
    path: str
    tags: List[str] = field(default_factory=list)
    likes: int = 0
    dislikes: int = 0
    topic: str = "general"

    @property
    def category(self) -> str:
        """Get the category of the article.

        Returns:
            str: The category of the article.
        """
        if self.dislikes > 0 and self.dislikes >= self.likes:
            return "useless"
        if self.likes > 0:
            return "helpful"
        return "inbox"
