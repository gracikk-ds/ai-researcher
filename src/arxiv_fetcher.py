"""arXiv paper fetcher."""

from typing import List, Optional

import arxiv
from loguru import logger

ARXIV_DELAY_SECONDS: int = 3


def _build_arxiv_query(keywords: List[str], categories: List[str]) -> str:
    """
    Build a boolean query string that conforms to the arXiv API grammar.

    Each multi-word keyword is wrapped in double quotes and searched in `all:`.
    Keywords are combined with AND; categories with OR.

    Parameters:
        keywords (List[str]): List of keywords to search for.
        categories (List[str]): List of arXiv categories to search in.

    Returns:
        str: The constructed arXiv query string.
    """
    keyword_clauses = [f'all:"{kw}"' for kw in keywords]  # noqa: WPS111
    category_clauses = [f"cat:{cat}" for cat in categories]
    return f"({' AND '.join(keyword_clauses)}) AND ({' OR '.join(category_clauses)})"  # noqa: WPS237


def fetch_arxiv_papers(
    *,
    keywords: List[str],
    categories: List[str],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    maximum_results: int = 100,
    page_size: int = 100,
) -> List[dict]:
    """
    Return a list of enriched arXiv paper dictionaries.

    Parameters:
        keywords (List[str]): List of keywords to search for.
        categories (List[str]): List of arXiv categories to search in.
        start_date (Optional[str]): Start date (YYYY-MM-DD) for filtering papers.
        end_date (Optional[str]): End date (YYYY-MM-DD) for filtering papers.
        maximum_results (int): Maximum number of papers to return.
        page_size (int): Number of results per page for the arXiv client.

    Returns:
        List[dict]: List of dictionaries, each representing an arXiv paper with metadata and citation count.
    """
    query_string = _build_arxiv_query(keywords, categories)
    logger.info(f"arXiv query: {query_string}")

    client = arxiv.Client(page_size=page_size, delay_seconds=ARXIV_DELAY_SECONDS)
    search = arxiv.Search(
        query=query_string,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    papers: List[dict] = []
    for index, result in enumerate(client.results(search), start=1):
        if index > maximum_results:
            break

        published_date = result.published.strftime("%Y-%m-%d")
        if start_date and published_date < start_date:
            continue
        if end_date and published_date > end_date:
            continue

        papers.append(
            {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "summary": result.summary,
                "published": published_date,
                "arxiv_url": result.entry_id,
                "categories": result.categories,
            },
        )

    return papers
