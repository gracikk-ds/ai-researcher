from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Article:
    """Represents a single article or report."""

    id: str
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
        if self.dislikes > 0 and self.dislikes >= self.likes:
            return "useless"
        if self.likes > 0:
            return "helpful"
        return "inbox"
