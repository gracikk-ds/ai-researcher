"""Classifier for research papers."""

import os
from typing import Optional, Tuple

from loguru import logger

from src.ai_researcher.gemini_researcher import GeminiApiClient


class Classifier:
    """Classifier for research papers."""

    def __init__(
        self,
        path_to_prompt: str,
        skipped_file_path: str = "data/skipped/skipped_papers_by_classifier.txt",
    ) -> None:
        """Initialize the classifier.

        Args:
            path_to_prompt (str): The path to the prompt file.
            skipped_file_path (str): The path to the file to save the skipped papers to.
        """
        self.gemini_researcher = GeminiApiClient(model_name="gemini-2.5-pro")
        with open(path_to_prompt, "r") as file:
            system_prompt = file.read()
        self.gemini_researcher.system_prompt = system_prompt
        self.skipped_file_path = skipped_file_path

    def classify(self, title: str, summary: str, full_date: str) -> Tuple[bool, Optional[str]]:
        """Classify a research paper.

        Args:
            title (str): The title of the research paper.
            summary (str): The summary of the research paper.
            full_date (str): The full date of the research paper.

        Returns:
            Tuple[bool, Optional[str]]: Whether the paper is about generative image editing.
        """
        prompt = f"Title: {title}\nSummary: {summary}"
        if self.gemini_researcher.ask(prompt).lower() == "yes":
            return False, None
        logger.info(f"Skipping paper {title} because it is not about generative image editing")
        skipped_dir = os.path.dirname(self.skipped_file_path)
        os.makedirs(skipped_dir, exist_ok=True)
        skipped_file_name = os.path.basename(self.skipped_file_path).split(".")[0]
        path_to_save = os.path.join(skipped_dir, f"{skipped_file_name}_{full_date}.txt")
        with open(path_to_save, "a") as file:
            file.write(f"{title}\n")  # noqa: WPS220
        return True, path_to_save


# if __name__ == "__main__":
#     jsonl_path = "data/arxiv_papers/relevant_papers.jsonl"
#     classifier = Classifier("prompts/classifier.txt")

#     with open(jsonl_path, "r", encoding="utf-8") as file:
#         lines = file.readlines()

#         for idx, line in enumerate(lines):
#             data = json.loads(line)
#             answer = classifier.classify(data["title"], data["summary"])
#             if idx % 10 == 0:
#                 classifier.gemini_researcher.info()
#                 print(f"Processed {idx} papers")
#             if not answer:
#                 print(data["title"])
#         classifier.gemini_researcher.info()
