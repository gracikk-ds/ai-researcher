"""Schemas for the papers."""

from typing import Optional

from pydantic import BaseModel


class Author(BaseModel):
    """Pydantic model representing an arXiv author."""

    name: str
    h_index: Optional[int] = None
    paper_count: Optional[int] = None
    citation_count: Optional[int] = None


class Paper(BaseModel):
    """Pydantic model representing an arXiv paper."""

    title: str
    authors: list[Author]
    max_authors_h_index: Optional[int] = None
    max_authors_paper_count: Optional[int] = None
    max_authors_citation_count: Optional[int] = None
    summary: str
    published: str
    arxiv_url: str
    pdf_url: str
    categories: list[str]
    citation_count: Optional[int] = None
    md_path: Optional[str] = None
