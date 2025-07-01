"""Fetch author information from the Semantic Scholar API."""

import os
import time
from typing import Dict, List, Optional

import requests
from loguru import logger


class AuthorInfoFetcher:
    """Fetch author information from the Semantic Scholar API."""

    api_base: str = "https://api.semanticscholar.org/graph/v1"
    fields = ["authorId", "name", "hIndex", "paperCount", "citationCount"]

    def __init__(self, api_key: Optional[str] = None, verbose: bool = False) -> None:
        """
        Initialize the AuthorInfoFetcher.

        Args:
            api_key (Optional[str]): Semantic Scholar API key. If not provided, will use
                the SEMANTIC_SCHOLAR_API_KEY environment variable.
            verbose (bool): Whether to print verbose output.
        """
        self.api_key = api_key or os.getenv("SEMANTIC_SCHOLAR_API_KEY")
        self.verbose = verbose

    def _headers(self) -> dict:
        if self.api_key:
            return {"x-api-key": self.api_key}
        return {}

    def _print_status_error(self, status_code: int, context: str) -> None:  # noqa: WPS231
        if status_code == 400:  # noqa: WPS223
            logger.error(f"[400 Bad Request] Could not understand request for {context}. Check parameters.")
        elif status_code == 401:
            logger.error(f"[401 Unauthorized] Invalid or missing API key for {context}.")
        elif status_code == 403:
            logger.error(f"[403 Forbidden] Access denied for {context}. Check permissions.")
        elif status_code == 404:
            logger.error(f"[404 Not Found] Author '{context}' not found.")
        elif status_code == 429:
            logger.error(f"[429 Too Many Requests] Rate limit exceeded for {context}. Slow down requests.")
        elif status_code == 500:
            logger.error(f"[500 Internal Server Error] Server error for {context}.")
        else:
            logger.error(f"[Error {status_code}] Unexpected error for {context}.")

    def _handle_response(  # noqa: WPS231,WPS212,C901
        self,
        response,
        context: str,
        is_search: bool = False,
    ) -> Optional[List[Dict]]:
        """
        Handle the response from the Semantic Scholar API.

        Args:
            response: The response from the Semantic Scholar API.
            context: The context of the request.
            is_search: Whether the request is a search request.

        Returns:
            Optional[List[Dict]]: List of author dictionaries, or None if not found.
        """
        if response.status_code == 200:
            data = response.json()
            if is_search:
                authors = data.get("data", [])
                filtred_authors = []
                if authors:
                    for author in authors:
                        if author.get("name") == context:  # noqa: WPS220
                            filtred_authors.append({field: author.get(field) for field in self.fields})  # noqa: WPS220
                if not filtred_authors:
                    if self.verbose:
                        logger.warning(f"No author found for {context}")  # noqa: WPS220
                    return None
                return filtred_authors
            return [{field: data.get(field) for field in self.fields}]
        else:
            self._print_status_error(response.status_code, context)
        return None

    def get_author_papers(self, author_id: str) -> Optional[List[str]]:
        """
        Fetch author papers by author ID.

        Args:
            author_id (str): The Semantic Scholar Author ID.

        Returns:
            Optional[Dict]: Dictionary with author papers, or None if not found.
        """
        max_retries = 3
        backoff = 2
        for attempt in range(max_retries):
            try:
                response = requests.get(
                    f"{self.api_base}/author/{author_id}/papers",
                    params={"fields": "title", "limit": 1000},  # type: ignore
                    headers=self._headers(),
                    timeout=10,
                )
            except requests.exceptions.RequestException as exp:
                logger.error(f"Error fetching author papers for {author_id}: {exp}")
                return None

            if response.status_code == 429:
                if self.verbose:
                    logger.warning(
                        f"[429 Too Many Requests] Retrying author '{author_id}' in {backoff} seconds "  # noqa: WPS237
                        f"(attempt {attempt+1}/{max_retries})...",  # noqa: WPS326
                    )
                time.sleep(backoff)
                backoff *= 2
                continue

            if response.status_code == 200:
                return response.json()["data"]

            self._print_status_error(response.status_code, f"author '{author_id}'")
            time.sleep(backoff)
            backoff *= 2
        return None

    def search_author(self, name: str, author_paper: str) -> Optional[Dict]:  # noqa: WPS231,C901
        """
        Search for an author by name and fetch info for the top match.

        Args:
            name (str): Author's full name.
            author_paper (str): Author's paper title.

        Returns:
            Optional[Dict]: Author info dictionary or None.
        """
        url = f"{self.api_base}/author/search"
        params = {
            "query": name,
            "limit": 25,
            "fields": "authorId,name,hIndex,paperCount,citationCount",
        }
        headers = self._headers()
        max_retries = 3
        backoff = 1

        for attempt in range(max_retries):
            response = requests.get(url, params=params, headers=headers, timeout=10)  # type: ignore
            if response.status_code == 429:
                if self.verbose:
                    logger.warning(
                        f"[429 Too Many Requests] Retrying author search '{name}' in {backoff} seconds "  # noqa: WPS237
                        f"(attempt {attempt+1}/{max_retries})...",  # noqa: WPS326
                    )
                time.sleep(backoff)
                backoff *= 2
                continue
            break
        finded_authors = self._handle_response(response, context=name, is_search=True)

        if finded_authors is not None:
            for author in finded_authors:
                author_papers = self.get_author_papers(author["authorId"])
                if author_papers is not None:
                    author_papers = [paper["title"].lower() for paper in author_papers]  # type: ignore
                if author_papers is not None and author_paper.lower() in author_papers:
                    return author  # noqa: WPS220
        return None
