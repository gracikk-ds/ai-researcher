"""arXiv paper fetcher (OOP version)."""

from datetime import datetime
from typing import List, Optional

import arxiv
from loguru import logger

from src.fetcher.authors_info_fetcher import AuthorInfoFetcher
from src.fetcher.citations_count import CitationCounter
from src.utils.schemas import Author, Paper


class ArxivFetcher:
    """Class to fetch and filter arXiv papers based on keywords, categories, and date range."""

    arxiv_delay_seconds: int = 3
    predefined_keywords: List[str] = ["image editing", "image edit"]
    predefined_categories: List[str] = ["cs.CV", "cs.LG", "cs.CL", "cs.AI", "cs.MM"]

    def __init__(
        self,
        maximum_results: int = 100,
        page_size: int = 100,
        max_date_difference_days: int = 180,
    ):
        """
        Initialize the ArxivFetcher with search parameters.

        Args:
            maximum_results (int): Maximum number of papers to return.
            page_size (int): Number of results per page for the arXiv client.
            max_date_difference_days (int): Maximum number of days between start and end dates.
        """
        self.maximum_results = maximum_results
        self.page_size = page_size
        self.max_date_difference_days = max_date_difference_days
        self.authors_fetcher = AuthorInfoFetcher()
        self.citations_counter = CitationCounter()

    def _build_arxiv_query(
        self,
        keywords: List[str],
        categories: List[str],
        start_date: datetime,
        end_date: datetime,
    ) -> str:
        """
        Build a boolean query string that conforms to the arXiv API grammar.

        Args:
            keywords (List[str]): List of keywords to search for.
            categories (List[str]): List of arXiv categories to search in.
            start_date (datetime): Start date for filtering papers.
            end_date (datetime): End date for filtering papers.

        Returns:
            str: The constructed arXiv query string.
        """
        keyword_clauses = [f'all:"{kw}"' for kw in keywords]  # noqa: WPS111
        category_clauses = [f"cat:{cat}" for cat in categories]
        query = f"({' OR '.join(keyword_clauses)}) AND ({' OR '.join(category_clauses)})"  # noqa: WPS237,WPS221

        start = start_date.strftime("%Y%m%d%H%M")
        end = end_date.strftime("%Y%m%d%H%M")
        date_clause = f" AND submittedDate:[{start} TO {end}]"
        return f"{query}{date_clause}"

    def check_start_end_dates_diff(self, start_date: str, end_date: str) -> tuple[datetime, datetime]:
        """
        Check if the start and end dates are valid.

        Args:
            start_date (str): Start date (YYYY-MM-DD) for filtering papers.
            end_date (str): End date (YYYY-MM-DD) for filtering papers.

        Raises:
            ValueError: The difference between the dates is greater than the maximum allowed difference.

        Returns:
            tuple[datetime, datetime]: The start and end dates as datetime objects.
        """
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        if start_date_obj > end_date_obj:
            raise ValueError("Start date must be before end date.")

        if (end_date_obj - start_date_obj).days > self.max_date_difference_days:
            raise ValueError(
                f"The difference between start and end dates must be less than {self.max_date_difference_days} days.",
            )

        return start_date_obj, end_date_obj

    def _fetch_authors_info(
        self,
        result: arxiv.Result,
    ) -> tuple[List[Author], Optional[int], Optional[int], Optional[int]]:
        """
        Fetch author information from the Semantic Scholar API.

        Args:
            result (arxiv.Result): The result of the arXiv search.

        Returns:
            tuple[List[Author], Optional[int], Optional[int], Optional[int]]:
                - The list of authors with their information,
                - The maximum h-index,
                - The maximum paper count,
                - The maximum citation count.
        """
        authors: List[Author] = [Author(name=author.name) for author in result.authors]
        for author in authors:
            author_info = self.authors_fetcher.search_author(author.name, result.title)
            if author_info is not None:
                author.h_index = author_info["hIndex"]
                author.paper_count = author_info["paperCount"]
                author.citation_count = author_info["citationCount"]

        if authors:
            max_h_index = max(author.h_index for author in authors if author.h_index is not None)
            max_paper_count = max(author.paper_count for author in authors if author.paper_count is not None)
            max_citation_count = max(author.citation_count for author in authors if author.citation_count is not None)
            return authors, max_h_index, max_paper_count, max_citation_count
        return authors, None, None, None

    def fetch_papers(  # noqa: WPS231,WPS210
        self,
        start_date: str,
        end_date: str,
        keywords: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
    ) -> List[Paper]:
        """
        Return a list of enriched arXiv paper Pydantic models.

        Args:
            start_date (str): Start date (YYYY-MM-DD) for filtering papers.
            end_date (str): End date (YYYY-MM-DD) for filtering papers.
            keywords (Optional[List[str]]): List of keywords to search for.
            categories (Optional[List[str]]): List of arXiv categories to search in.

        Returns:
            List[Paper]: List of Paper models, each representing an arXiv paper with metadata.
        """
        if keywords is None:
            keywords = self.predefined_keywords
        if categories is None:
            categories = self.predefined_categories

        start_date_obj, end_date_obj = self.check_start_end_dates_diff(start_date, end_date)
        query_string = self._build_arxiv_query(keywords, categories, start_date_obj, end_date_obj)
        logger.info(f"arXiv query: {query_string}")

        client = arxiv.Client(page_size=self.page_size, delay_seconds=self.arxiv_delay_seconds)
        search = arxiv.Search(
            query=query_string,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        papers: List[Paper] = []
        for index, result in enumerate(client.results(search), start=1):
            if index > self.maximum_results:
                break
            authors, max_h_index, max_paper_count, max_citation_count = self._fetch_authors_info(result)
            summary = " ".join(result.summary.split())
            papers.append(
                Paper(
                    title=result.title,
                    authors=authors,
                    max_authors_h_index=max_h_index,
                    max_authors_paper_count=max_paper_count,
                    max_authors_citation_count=max_citation_count,
                    summary=summary,
                    published=result.published.strftime("%Y-%m-%d"),
                    arxiv_url=result.entry_id,
                    pdf_url=result.pdf_url,
                    categories=result.categories,
                    citation_count=self.citations_counter.get_citation_count(result.title, result.entry_id),
                ),
            )
            break

        return papers


# if __name__ == "__main__":
#     fetcher = ArxivFetcher()
#     papers = fetcher.fetch_papers(start_date="2024-01-01", end_date="2024-02-01")
#     for paper in papers:
#         print(paper)
