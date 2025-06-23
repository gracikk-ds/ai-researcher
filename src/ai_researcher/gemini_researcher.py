"""Gemini Api Client."""

import json
import os
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv
from google import genai
from google.cloud import aiplatform
from google.genai.types import (
    Content,
    FileData,
    GenerateContentConfig,
    HttpOptions,
    Part,
    ThinkingConfig,
)
from loguru import logger

from src.ai_researcher.google_bucket import GoogleBucket
from src.utils.price_caculation import calculate_inference_price

load_dotenv()


class GeminiApiClient:  # noqa: WPS230,WPS214
    """Gemini Api Client class."""

    prediction_timeout: int = 120
    location: str = "us-central1"

    def __init__(
        self,
        model_name: str = "gemini-2.5-pro",
        system_prompt: Optional[str] = None,
        temperature: float = 0.3,
        thinking_budget: Optional[int] = None,
        site_reports_dir: str = "site/_reports",
    ):
        """Initialize GeminiClient with Vertex AI connection, model, and defaults.

        Args:
            model_name: The model to use.
            system_prompt: The system prompt to use.
            temperature: The temperature to use.
            thinking_budget: The thinking budget to use.
            site_reports_dir: The directory to save the reports to.
        """
        self._load_project_id_from_creds()
        self.model_name = model_name
        aiplatform.init(project=self.project, location=self.location)
        self.client = genai.Client(
            vertexai=True,
            project=self.project,
            location=self.location,
            http_options=HttpOptions(timeout=self.prediction_timeout * 1000),
        )
        self.temperature = temperature
        self.thinking_budget = thinking_budget if thinking_budget is not None else -1
        self.bucket = GoogleBucket(bucket_prefix="pdfs")
        self.site_reports_dir = site_reports_dir
        self._system_prompt = system_prompt
        self.file_uris: List[str] = []
        self.total_input_token_count: int = 0
        self.total_output_token_count: int = 0
        self.total_requests: int = 0

    def _load_project_id_from_creds(self) -> None:
        """Load the project id from the credentials.

        Raises:
            ValueError: If the project id cannot be loaded.
        """
        creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if creds_path is None:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set")
        with open(creds_path, "r") as creds_file:
            creds = json.load(creds_file)
        self.project = creds["project_id"]  # type: ignore

    @property
    def system_prompt(self) -> str:
        """Get the system prompt.

        Returns:
            The system prompt.
        """
        if self._system_prompt is None:
            return "You are a helpful senior research assistant."
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, prompt: str) -> None:
        """Set or update the system prompt.

        Args:
            prompt (str): The system prompt to use.

        Raises:
            ValueError: If the system prompt is not a string.
        """
        if not isinstance(prompt, str):
            raise ValueError("`system_prompt` must be a string.")
        self._system_prompt = prompt

    def info(self) -> None:
        """Print the info about the client."""
        inference_price = calculate_inference_price(
            model_name=self.model_name,
            total_input_token_count=self.total_input_token_count,
            total_output_token_count=self.total_output_token_count,
        )
        logger.info(
            f"Total processed: {self.total_requests}. Spent: {inference_price:.4f}$",
        )

    def attach_pdf(self, gcs_uri: str) -> None:
        """Attach a PDF (or text file) for native processing.

        Args:
            gcs_uri (str): The URI of the PDF file to attach.
        """
        self.file_uris.append(gcs_uri)

    def clear_pdfs(self) -> None:
        """Clear all attached document URIs."""
        self.file_uris = []

    def ask(self, user_prompt: str) -> str:
        """Send a prompt to Gemini, with optional system, PDF, and image inputs.

        Args:
            user_prompt (str): The user prompt to send to Gemini.

        Returns:
            str: The generated text response.
        """
        contents: List[Content] = []

        # System instruction
        contents.append(Content(role="model", parts=[Part(text=self.system_prompt)]))

        # Attached PDF files if any
        for uri in self.file_uris:
            contents.append(
                Content(
                    role="user",
                    parts=[Part(file_data=FileData(file_uri=uri, mime_type="application/pdf"))],
                ),
            )

        # User message
        contents.append(Content(role="user", parts=[Part(text=user_prompt)]))

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=contents,  # type: ignore
            config=GenerateContentConfig(
                temperature=self.temperature,
                thinking_config=ThinkingConfig(thinking_budget=self.thinking_budget),
            ),
        )
        self.total_input_token_count += getattr(response.usage_metadata, "prompt_token_count", 0)
        self.total_output_token_count += getattr(response.usage_metadata, "candidates_token_count", 0)
        self.total_output_token_count += getattr(response.usage_metadata, "thoughts_token_count", 0)
        self.total_requests += 1
        self.info()

        return response.text  # type: ignore

    def save_response(self, response: str, pdf_local_path: Optional[str] = None) -> None:
        """Save the response to a markdown file.

        Args:
            response (str): The response to save.
            pdf_local_path (Optional[str]): The local path to the PDF file to attach.
        """
        pdf_stem = Path(pdf_local_path).stem if pdf_local_path is not None else None
        if pdf_stem is not None:
            md_path = os.path.join(self.site_reports_dir, f"response_{pdf_stem}_{self.model_name}.md")  # noqa: WPS221
            with open(md_path, "w", encoding="utf-8") as response_file:  # noqa: WPS221
                response_file.write(response)

    def __call__(  # noqa: C901
        self,
        user_prompt: str,
        pdf_local_path: Optional[str] = None,
        save_to_file: bool = True,
    ) -> str:
        """Send a prompt to Gemini, with optional system, PDF, and image inputs.

        Args:
            user_prompt (str): The user prompt to send to Gemini.
            pdf_local_path (Optional[str]): The local path to the PDF file to attach.
            save_to_file (bool): Whether to save the response to a markdown file.

        Returns:
            str: The generated text response.
        """
        # Attach the PDF file if provided
        if pdf_local_path is not None:
            pdf_uri = self.bucket.upload_file(pdf_local_path)
            self.attach_pdf(pdf_uri)

        # Send the prompt to Gemini
        response = self.ask(user_prompt)

        # Remove the PDF file from the bucket
        if pdf_local_path is not None:
            self.clear_pdfs()
            self.bucket.remove_file(pdf_uri)

        # Save the response to a markdown file
        if save_to_file:
            self.save_response(response, pdf_local_path)

        return response


if __name__ == "__main__":
    client = GeminiApiClient()
    with open("prompts/summarizer.txt", "r", encoding="utf-8") as summary_file:
        summary_prompt = summary_file.read()
    response = client(summary_prompt, pdf_local_path="pdfs/mgie.pdf")
