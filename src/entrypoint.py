"""Entrypoint for the application."""

from datetime import datetime, timedelta
from typing import List, Optional

from loguru import logger

from src.ai_researcher.gemini_researcher import GeminiApiClient
from src.fetcher.arxiv_fetcher import ArxivFetcher, Paper


class Entrypoint:
    """Entrypoint for the application."""

    def __init__(self) -> None:
        """Initialize the entrypoint."""
        self.gemini_researcher = GeminiApiClient(model_name="gemini-2.5-flash")
        self.arxiv_fetcher = ArxivFetcher()

    def extract_key_words_by_user_intention(self, user_intention: str) -> List[str]:  # noqa: WPS118
        """Extract key words for arxiv search by user research intention.

        Args:
            user_intention (str): The user research intention.

        Returns:
            List[str]: The key words for arxiv search.
        """
        with open("prompts/key_words_extractor.txt", "r") as file:
            system_prompt = file.read()
        self.gemini_researcher.system_prompt = system_prompt
        response = self.gemini_researcher.ask(user_intention, thinking_budget=0)
        self.gemini_researcher.system_prompt = "You are a helpful senior research assistant."
        return response.split(", ")

    def start_research(
        self,
        start_date: str,
        end_date: str,
        keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        research_intention: Optional[str] = None,
        categories: Optional[List[str]] = None,
    ) -> tuple[List[Paper], List[Paper]]:
        """Start the research.

        Args:
            start_date (str): Start date (YYYY-MM-DD) for filtering papers.
            end_date (str): End date (YYYY-MM-DD) for filtering papers.
            keywords (Optional[List[str]]): The keywords for arxiv search.
            exclude_keywords (Optional[List[str]]): The keywords to exclude from the search.
            research_intention (Optional[str]): The research intention.
            categories (Optional[List[str]]): The categories for arxiv search.

        Raises:
            ValueError: If neither keywords nor research intention is provided.

        Returns:
            tuple[List[Paper], List[Paper]]:
                - List of highly relevant papers,
                - List of relevant papers.
        """
        if keywords is None and research_intention is None:
            raise ValueError("Either keywords or research intention must be provided.")

        if keywords is None:
            logger.warning("No keywords provided, trying to extract keywords from user intention.")
            logger.warning("This behavior is not recommended, as it may not be accurate.")
            keywords = self.extract_key_words_by_user_intention(research_intention)  # type: ignore
            logger.info(f"Extracted keywords: {keywords}")

        if categories is None:
            categories = self.arxiv_fetcher.predefined_categories

        highly_relevant_papers, papers = self.arxiv_fetcher.fetch_papers(
            start_date,
            end_date,
            keywords,
            exclude_keywords,
            categories,
        )
        return highly_relevant_papers, papers


if __name__ == "__main__":
    entrypoint = Entrypoint()
    start_date = "2023-01-01"
    days_in_period = 180
    number_of_periods = 6
    for _ in range(number_of_periods):
        end_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=days_in_period)).strftime("%Y-%m-%d")
        logger.info(f"Fetching papers from {start_date} to {end_date}")
        entrypoint.start_research(
            keywords=["image editing", "image edit", "edit image"],
            exclude_keywords=[
                "gan",
                "training-free",
                "training free",
                "tuning-free",
                "tuning free",
                "2d",
                "3d",
                "4d",
                "radiance fields",
                "sam",
                "segmentation",
                "detection",
                "coco",
                "matting",
                "cnn",
                "harmonization",
                "video",
                "attention control",
                "inversion",
                "fashion",
                "face",
                "bounding box",
                "mask",
                "masking",
                "medical",
                "watermark",
            ],
            start_date=start_date,
            end_date=end_date,
        )
        start_date = end_date
