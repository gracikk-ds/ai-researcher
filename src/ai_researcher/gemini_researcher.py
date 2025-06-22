"""Gemini Api Client."""

import json
import os
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


class GeminiApiClient:
    """Gemini Api Client class."""

    prediction_timeout: int = 120
    location: str = "us-central1"

    def __init__(
        self,
        model_name: str = "gemini-2.5-flash",
        system_prompt: Optional[str] = None,
        temperature: float = 0.3,
    ):
        """Initialize GeminiClient with Vertex AI connection, model, and defaults.

        Args:
            model_name: The model to use.
            system_prompt: The system prompt to use.
            temperature: The temperature to use.
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
        self.bucket = GoogleBucket(bucket_prefix="pdfs")

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
        """Send a prompt to Gemini, with optional system and PDF inputs.

        Args:
            user_prompt (str): The user prompt to send to Gemini.

        Returns:
            The generated text response.
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
                thinking_config=ThinkingConfig(thinking_budget=0),
            ),
        )
        self.total_input_token_count += response.usage_metadata.prompt_token_count  # type: ignore
        self.total_output_token_count += response.usage_metadata.candidates_token_count  # type: ignore
        self.total_requests += 1
        self.info()

        return response.text  # type: ignore

    def __call__(self, user_prompt: str, pdf_local_path: Optional[str] = None) -> str:
        """Send a prompt to Gemini, with optional system and PDF inputs.

        Args:
            user_prompt (str): The user prompt to send to Gemini.
            pdf_local_path (Optional[str]): The local path to the PDF file to attach.

        Returns:
            The generated text response.
        """
        if pdf_local_path is not None:
            pdf_uri = self.bucket.upload_file(pdf_local_path)
            self.attach_pdf(pdf_uri)
        response = self.ask(user_prompt)
        if pdf_local_path is not None:
            self.clear_pdfs()
            self.bucket.remove_file(pdf_uri)
        return response


if __name__ == "__main__":
    client = GeminiApiClient()
    response = client("Make 5 sentence length summary of the following of the paper", pdf_local_path="pdfs/mgie.pdf")
    print(response)
