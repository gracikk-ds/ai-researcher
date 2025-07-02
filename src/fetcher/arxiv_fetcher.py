"""arXiv paper fetcher (OOP version)."""

import os
from datetime import datetime
from typing import List, Optional, Tuple

import arxiv
from loguru import logger

from src.ai_researcher.classifier import Classifier
from src.fetcher.authors_info_fetcher import AuthorInfoFetcher
from src.fetcher.citations_count import CitationCounter
from src.fetcher.lists_of_keywords import EXCLUDE_KEYWORDS, PREDEFINED_KEYWORDS
from src.utils.schemas import Author, Paper


class ArxivFetcher:
    """Class to fetch and filter arXiv papers based on keywords, categories, and date range."""

    arxiv_delay_seconds: int = 3
    predefined_keywords: List[str] = PREDEFINED_KEYWORDS
    exclude_keywords: List[str] = EXCLUDE_KEYWORDS
    predefined_categories: List[str] = ["cs.CV", "cs.LG", "cs.CL", "cs.AI", "cs.MM"]

    def __init__(
        self,
        page_size: int = 500,
        path_to_prompt: str = "prompts/classifier.txt",
        save_dir: str = "data/arxiv_papers",
        skipped_file_path: str = "data/skipped/skipped_papers_by_keywords.txt",
    ):
        """
        Initialize the ArxivFetcher with search parameters.

        Args:
            page_size (int): Number of results per page for the arXiv client.
            path_to_prompt (str): Path to the prompt file for the classifier.
            save_dir (str): Directory to save the papers to.
            skipped_file_path (str): Path to the file to save the skipped papers to.
        """
        self.page_size = page_size
        self.save_dir = save_dir
        self.skipped_file_path = skipped_file_path
        self.classifier = Classifier(path_to_prompt)
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
            ValueError: The start date is after the end date.

        Returns:
            tuple[datetime, datetime]: The start and end dates as datetime objects.
        """
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        if start_date_obj > end_date_obj:
            raise ValueError("Start date must be before end date.")
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

    def _filter_papers(
        self,
        title: str,
        summary: str,
        exclude_keywords: Optional[List[str]],
        full_date: str,
    ) -> Tuple[bool, Optional[str]]:
        """
        Filter the papers based on the exclude keywords.

        Args:
            title (str): The title of the paper.
            summary (str): The summary of the paper.
            exclude_keywords (Optional[List[str]]): List of keywords to exclude.
            full_date (str): The full date of the paper.

        Returns:
            tuple[bool, Optional[str]]: True if the paper should be excluded, False otherwise.
        """
        if exclude_keywords is not None:
            for keyword in exclude_keywords:
                exclude_by_title = keyword.lower() in title.lower().split()
                exclude_by_summary = keyword.lower() in summary.lower().split()
                if exclude_by_title or exclude_by_summary:
                    logger.info(f"Skipping paper {title} because its title or summary contains exclude keywords")
                    skipped_dir = os.path.dirname(self.skipped_file_path)
                    os.makedirs(skipped_dir, exist_ok=True)
                    skipped_file_name = os.path.basename(self.skipped_file_path).split(".")[0]
                    path_to_save = os.path.join(skipped_dir, f"{skipped_file_name}_{full_date}.txt")
                    with open(path_to_save, "a") as file:
                        file.write(f"{title}\n")  # noqa: WPS220
                    return True, path_to_save
        return False, None

    def _save_papers(
        self,
        papers: List[Paper],
        start_date_obj: datetime,
        end_date_obj: datetime,
        save_to_jsonl: bool,
    ) -> None:
        if save_to_jsonl:
            os.makedirs(self.save_dir, exist_ok=True)
            if papers:
                start_date_str = start_date_obj.strftime("%m-%Y")
                end_date_str = end_date_obj.strftime("%m-%Y")
                self.save_papers_to_jsonl(
                    papers,
                    f"relevant_papers_{start_date_str}_{end_date_str}.jsonl",
                )

    def fetch_papers(  # noqa: WPS231,WPS210,C901
        self,
        start_date: str,
        end_date: str,
        keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        save_to_jsonl: bool = True,
    ) -> Tuple[List[Paper], List[str], List[str]]:
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
            Tuple[List[Paper], List[str], List[str]]:
                - List of relevant papers.
                - List of paths to the files where papers were excluded by keywords.
                - List of paths to the files where papers were excluded by classifier.
            """
        if keywords is None:
            keywords = self.predefined_keywords
        if categories is None:
            categories = self.predefined_categories
        if exclude_keywords is None:
            exclude_keywords = self.exclude_keywords

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
        exculded_by_keywords_paths: List[str] = []
        exculded_by_classifier_paths: List[str] = []
        search_results = client.results(search)
        search_month_and_year = end_date_obj.strftime("%m-%Y")
        for result in search_results:
            summary = " ".join(result.summary.split())
            title = " ".join(result.title.split())
            full_date = result.published.strftime("%d-%m-%Y")

            if search_month_and_year != result.published.strftime("%m-%Y"):
                logger.info(f"Looking for papers in {search_month_and_year}...")
                search_month_and_year = result.published.strftime("%m-%Y")

            # Filter papers by exclude keywords
            is_skipped, exculded_by_keywords_path = self._filter_papers(title, summary, exclude_keywords, full_date)
            if is_skipped:
                exculded_by_keywords_paths.append(exculded_by_keywords_path)  # type: ignore
                continue

            # Classify paper
            is_skipped, exculded_by_classifier_path = self.classifier.classify(title, summary, full_date)
            if is_skipped:
                exculded_by_classifier_paths.append(exculded_by_classifier_path)  # type: ignore
                continue

            authors, max_h_index, max_paper_count, max_citation_count = self._fetch_authors_info(result)
            citation_count = self.citations_counter.get_citation_count(result.title, result.entry_id)
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
                citation_count=citation_count,
            )
            papers.append(paper)

            # Save papers to JSONL file
            self._save_papers(papers, start_date_obj, end_date_obj, save_to_jsonl)
        self.classifier.gemini_researcher.info()
        return papers, exculded_by_keywords_paths, exculded_by_classifier_paths


# if __name__ == "__main__":
#     fetcher = ArxivFetcher()
#     papers = fetcher.fetch_papers(start_date="2024-01-01", end_date="2024-02-01")
#     for paper in papers:
#         print(paper)
