"""Get the citation count of an arXiv paper via the Semantic Scholar Academic Graph API."""

import os
import re
import time
from typing import Optional

import requests
from loguru import logger


class CitationCounter:
    """Retrieve the citation count of an arXiv paper using the Semantic Scholar API."""

    api_base: str = "https://api.semanticscholar.org/graph/v1"
    arxiv_re = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{5})(?:v\d+)?", re.I)

    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize the CitationCounter.

        Args:
            api_key (Optional[str]): Semantic Scholar API key. If not provided, will use the
                SEMANTIC_SCHOLAR_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("SEMANTIC_SCHOLAR_API_KEY")

    def _headers(self) -> dict:
        """
        Construct the headers for the API request, including the API key if available.

        Returns:
            dict: Headers for the request.
        """
        if self.api_key:
            return {"x-api-key": self.api_key}
        return {}

    def _extract_arxiv_id(self, url: str) -> Optional[str]:
        """
        Extract the canonical arXiv identifier from a URL.

        Args:
            url (str): The arXiv URL.

        Returns:
            Optional[str]: The arXiv ID if found, else None.
        """
        match = self.arxiv_re.search(url or "")
        if match:
            return match.group(1)
        return None

    def _print_status_error(self, status_code: int, context: str) -> None:  # noqa: WPS231
        """
        Print the error message for the given status code and context.

        Args:
            status_code: The HTTP status code.
            context: A string describing the context (arXiv ID or title).
        """
        if status_code == 400:  # noqa: WPS223
            logger.error(f"[400 Bad Request] Could not understand request for {context}. Check parameters.")
        elif status_code == 401:
            logger.error(f"[401 Unauthorized] Invalid or missing API key for {context}.")
        elif status_code == 403:
            logger.error(f"[403 Forbidden] Access denied for {context}. Check permissions.")
        elif status_code == 404:
            logger.error(f"[404 Not Found] Paper with {context} not found.")
        elif status_code == 429:
            logger.error(f"[429 Too Many Requests] Rate limit exceeded for {context}. Slow down requests.")
        elif status_code == 500:
            logger.error(f"[500 Internal Server Error] Server error for {context}.")
        else:
            logger.error(f"[Error {status_code}] Unexpected error for {context}.")

    def _handle_response(self, response, context: str) -> Optional[int]:  # noqa: WPS212
        """
        Handle the HTTP response for citation count requests.

        Args:
            response: The requests.Response object.
            context: A string describing the context (arXiv ID or title).

        Returns:
            Optional[int]: The citation count if found, else None.
        """
        if response.status_code == 200:
            data = response.json()
            if "citationCount" in data:
                return data["citationCount"]  # noqa: WPS529
            if "data" in data and data["data"]:
                first = data["data"][0]
                if first["title"].strip().lower() == context.strip().lower():
                    return first.get("citationCount")
            return None
        else:
            self._print_status_error(response.status_code, context)
        return None

    def get_citation_count(self, title: str, arxiv_url: str) -> Optional[int]:  # noqa: WPS231
        """
        Return the current citation count for a given paper, or None if not found.

        Args:
            title (str): The title of the paper.
            arxiv_url (str): The arXiv URL of the paper.

        Returns:
            Optional[int]: The citation count, or None if not found.
        """
        headers = self._headers()
        max_retries = 5
        backoff = 1

        # Step 1: Try by arXiv ID (fast, exact)
        arxiv_id = self._extract_arxiv_id(arxiv_url)
        if arxiv_id is not None:
            url = f"{self.api_base}/paper/ARXIV:{arxiv_id}"
            for attempt in range(max_retries):
                response = requests.get(
                    url,
                    params={"fields": "citationCount"},
                    headers=headers,
                    timeout=10,
                )
                if response.status_code == 429:
                    logger.warning(
                        f"[429 Too Many Requests] Retrying arXiv ID {arxiv_id} in {backoff} seconds "  # noqa: WPS237
                        f"(attempt {attempt+1}/{max_retries})...",  # noqa: WPS326
                    )
                    time.sleep(backoff)
                    backoff *= 2
                    continue
                result = self._handle_response(response, f"arXiv ID {arxiv_id}")
                if result is not None:
                    return result

        # Step 2: Fallback to title search
        search_url = f"{self.api_base}/paper/search"
        params = {"query": str(title), "limit": str(1), "fields": "title,citationCount"}
        backoff = 1
        for attempt in range(max_retries):  # noqa: WPS440
            try:
                response = requests.get(search_url, params=params, headers=headers, timeout=10)
            except requests.exceptions.RequestException as exp:
                logger.error(f"Error fetching citation count for {title}: {exp}")
                return None

            if response.status_code == 429:
                logger.warning(
                    f"[429 Too Many Requests] Retrying title '{title}' in {backoff} seconds "  # noqa: WPS237
                    f"(attempt {attempt+1}/{max_retries})...",  # noqa: WPS326
                )
                time.sleep(backoff)
                backoff *= 2
                continue
            return self._handle_response(response, f"title '{title}'")
        return None
