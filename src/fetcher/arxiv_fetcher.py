"""arXiv paper fetcher (OOP version)."""

import os
from datetime import datetime
from typing import List, Optional

import arxiv
from loguru import logger
from tqdm import tqdm

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
        maximum_results: int = 365,
        page_size: int = 500,
        max_date_difference_days: int = 200,
        save_dir: str = "data/arxiv_papers",
    ):
        """
        Initialize the ArxivFetcher with search parameters.

        Args:
            maximum_results (int): Maximum number of papers to return.
            page_size (int): Number of results per page for the arXiv client.
            max_date_difference_days (int): Maximum number of days between start and end dates.
            save_dir (str): Directory to save the papers to.
        """
        self.maximum_results = maximum_results
        self.page_size = page_size
        self.max_date_difference_days = max_date_difference_days
        self.save_dir = save_dir
        self.authors_fetcher = AuthorInfoFetcher()
        self.citations_counter = CitationCounter()

    def save_papers_to_jsonl(self, papers: List[Paper], filename: str) -> None:
        """
        Save the papers to a JSONL file.

        Args:
            papers (List[Paper]): List of papers to save.
            filename (str): Name of the file to save the papers to.
        """
        with open(os.path.join(self.save_dir, filename), "w") as jsonl_file:
            for paper in papers:
                jsonl_file.write(paper.model_dump_json() + "\n")

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
        if len(result.authors) > 1:
            selected_authors = [result.authors[0], result.authors[-1]]
        else:
            selected_authors = result.authors
        authors: List[Author] = [Author(name=author.name) for author in selected_authors]
        for author in authors:
            author_info = self.authors_fetcher.search_author(author.name, result.title)
            if author_info is not None:
                author.h_index = author_info["hIndex"]
                author.paper_count = author_info["paperCount"]
                author.citation_count = author_info["citationCount"]

        if authors:
            authors_h_index = [author.h_index for author in authors if author.h_index is not None]
            authors_paper_count = [author.paper_count for author in authors if author.paper_count is not None]
            authors_citation_count = [author.citation_count for author in authors if author.citation_count is not None]
            max_h_index = max(authors_h_index) if authors_h_index else None
            max_paper_count = max(authors_paper_count) if authors_paper_count else None
            max_citation_count = max(authors_citation_count) if authors_citation_count else None
            return authors, max_h_index, max_paper_count, max_citation_count
        return authors, None, None, None

    def _filter_papers(self, summary: str, exclude_keywords: Optional[List[str]]) -> bool:
        """
        Filter the papers based on the exclude keywords.

        Args:
            summary (str): The summary of the paper.
            exclude_keywords (Optional[List[str]]): List of keywords to exclude.

        Returns:
            bool: True if the paper should be excluded, False otherwise.
        """
        if exclude_keywords is not None:
            for keyword in exclude_keywords:
                if keyword.lower() in summary.lower().split():
                    return True
        return False

    def fetch_papers(  # noqa: WPS231,WPS210,C901
        self,
        start_date: str,
        end_date: str,
        keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        save_to_jsonl: bool = True,
    ) -> tuple[List[Paper], List[Paper]]:
        """
        Return a list of enriched arXiv paper Pydantic models.

        Args:
            start_date (str): Start date (YYYY-MM-DD) for filtering papers.
            end_date (str): End date (YYYY-MM-DD) for filtering papers.
            keywords (Optional[List[str]]): List of keywords to search for.
            exclude_keywords (Optional[List[str]]): List of keywords to exclude.
            categories (Optional[List[str]]): List of arXiv categories to search in.
            save_to_jsonl (bool): Whether to save the papers to a JSONL file.

        Returns:
            tuple[List[Paper], List[Paper]]:
                - List of highly relevant papers,
                - List of relevant papers.
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
        highly_relevant_papers: List[Paper] = []
        search_results = client.results(search)
        for index, result in tqdm(enumerate(search_results, start=1), desc="Fetching papers"):
            highly_relevant = False
            if index > self.maximum_results:
                break
            summary = " ".join(result.summary.split())
            title = " ".join(result.title.split())
            if self._filter_papers(title, exclude_keywords):
                logger.info(f"Skipping paper {title} because its title contains exclude keywords")
                continue
            if self._filter_papers(summary, exclude_keywords):
                logger.info(f"Skipping paper {title} because its summary contains exclude keywords")
                continue
            if "edit" in title.lower():
                highly_relevant = True
            authors, max_h_index, max_paper_count, max_citation_count = self._fetch_authors_info(result)
            paper = Paper(
                title=title,
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
            )
            if highly_relevant:
                highly_relevant_papers.append(paper)
            else:
                papers.append(paper)

            if save_to_jsonl:
                os.makedirs(self.save_dir, exist_ok=True)
                start_date_str = start_date_obj.strftime("%Y-%m-%d")
                end_date_str = end_date_obj.strftime("%Y-%m-%d")
                if highly_relevant_papers:
                    self.save_papers_to_jsonl(
                        highly_relevant_papers,
                        f"highly_relevant_papers_{start_date_str}_{end_date_str}.jsonl",
                    )
                if papers:
                    self.save_papers_to_jsonl(
                        papers,
                        f"relevant_papers_{start_date_str}_{end_date_str}.jsonl",
                    )
        return highly_relevant_papers, papers


# if __name__ == "__main__":
#     fetcher = ArxivFetcher()
#     papers = fetcher.fetch_papers(start_date="2024-01-01", end_date="2024-02-01")
#     for paper in papers:
#         print(paper)
