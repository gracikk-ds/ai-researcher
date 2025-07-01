"""Utility to download PDFs from a JSONL file containing 'pdf_url' fields into a specified directory."""

import json
import os
from pathlib import Path

import requests
from loguru import logger
from tqdm import tqdm


def download_pdf(pdf_url: str, pdf_path: Path) -> None:
    """
    Download a single PDF from a URL to the specified path.

    Args:
        pdf_url (str): The URL of the PDF to download.
        pdf_path (Path): The local file path to save the downloaded PDF.
    """
    file_dir = pdf_path.parent
    os.makedirs(file_dir, exist_ok=True)
    response = requests.get(pdf_url, stream=True, timeout=60)  # noqa: WPS432
    response.raise_for_status()
    with open(pdf_path, "wb") as pdf_file:
        for chunk in response.iter_content(chunk_size=8192):  # noqa: WPS432
            if chunk:
                pdf_file.write(chunk)


def download_pdfs_from_jsonl(jsonl_path: str, output_dir: str) -> None:
    """
    Download PDFs from URLs listed in a JSONL file and save them to the specified directory.

    Args:
        jsonl_path (str): Path to the JSONL file containing 'pdf_url' fields.
        output_dir (str): Directory to save the downloaded PDFs.
    """
    os.makedirs(output_dir, exist_ok=True)
    with open(jsonl_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for entry in tqdm(lines, desc="Downloading PDFs", total=len(lines)):
        data = json.loads(entry)
        pdf_url = data.get("pdf_url")
        title = data.get("title", "Unknown")
        if not pdf_url:
            logger.warning(f"No PDF URL found for {title}")
            continue
        pdf_name = f"{title.replace(' ', '_')}.pdf"
        pdf_path = Path(output_dir) / pdf_name
        try:
            if pdf_path.exists():
                continue
            download_pdf(pdf_url, pdf_path)
        except Exception as exp:
            logger.error(f"Failed to download from {pdf_url}: {exp}")


# if __name__ == "__main__":
#     download_pdfs_from_jsonl(
#         jsonl_path="data/arxiv_papers/relevant_papers.jsonl",
#         output_dir="data/arxiv_papers/pdfs",
#     )
