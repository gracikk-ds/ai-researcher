"""Upload a Markdown file to a Notion database page."""

import json
import re
from typing import Any, Dict, List

import requests

from src.ai_researcher.google_bucket import GoogleBucket
from src.notion_db.utils import (
    check_for_image,
    extract_image_links,
    resolve_image_path,
)
from src.settings import settings


class MarkdownToNotionUploader:
    """
    Read a Markdown file and upload its content as blocks to a Notion database page.

    Attributes:
        api_token (str): Notion API token.
        database_id (str): Notion database ID.
        base_url (str): Notion API base URL.
        headers (dict): Notion API headers.
    """

    def __init__(self, database_id: str, bucket_prefix: str = "report_images") -> None:
        """Initialize the uploader with the provided database ID.

        Args:
            database_id (str): Notion database ID.
            bucket_prefix (str): Prefix for the Google Bucket.
        """
        self.api_token = settings.notion_token
        self.project_root = settings.site_reports_dir.split("/")[0]
        self.database_id = database_id
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        }
        self.bucket = GoogleBucket(bucket_prefix)

    def _parse_rich_text(self, line: str) -> List[Dict[str, Any]]:
        """
        Parse a line for **bold** markdown and return Notion rich_text objects.

        Args:
            line (str): Line of text to parse.

        Returns:
            List[Dict[str, Any]]: List of Notion rich_text objects.
        """
        segments = []
        pattern = r"\*\*(.+?)\*\*"
        last_end = 0

        for match in re.finditer(pattern, line):
            # Add normal text before the bold
            if match.start() > last_end:
                text = line[last_end : match.start()]
                if text:
                    segments.append(
                        {
                            "type": "text",
                            "text": {"content": text},
                        },
                    )
            # Add bold text
            bold_text = match.group(1)
            segments.append(
                {
                    "type": "text",
                    "text": {"content": bold_text},
                    "annotations": {
                        "bold": True,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default",
                    },
                },
            )
            last_end = match.end()

        # Add the rest of the text after the last match
        if last_end < len(line):
            text = line[last_end:]
            if text:
                segments.append({"type": "text", "text": {"content": text}})
        # If nothing matched, just return the line as normal text
        if not segments:
            segments.append({"type": "text", "text": {"content": line}})
        return segments

    def _parse_heading(self, line: str, blocks: List[Dict[str, Any]]) -> bool:  # noqa: WPS212
        """Parse a heading and add it to the list of blocks.

        Args:
            line (str): Line of text to parse.
            blocks (List[Dict[str, Any]]): List of Notion blocks.

        Returns:
            bool: True if the line is a heading, False otherwise.
        """
        if line.startswith("# "):  # noqa: WPS223
            blocks.append(
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]},
                },
            )
            return True
        elif line.startswith("## "):
            blocks.append(
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {"rich_text": [{"type": "text", "text": {"content": line[3:]}}]},
                },
            )
            return True
        elif line.startswith("### "):
            blocks.append(
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": line[4:]}}]},
                },
            )
            return True
        return False

    def collect_images(self, markdown: str) -> Dict[str, str]:
        """Collect images from the markdown.

        Args:
            markdown (str): Markdown text to check.

        Returns:
            Dict[str, str]: Dictionary mapping original URLs to public URLs.
        """
        image_map = {}

        # Upload images and map their original URLs to public URLs
        for _, url in extract_image_links(markdown):
            local_path = resolve_image_path(url, self.project_root)
            public_url = self.bucket.upload_public_file(local_path)
            image_map[local_path] = public_url
        return image_map

    def markdown_to_blocks(self, markdown: str) -> List[Dict[str, Any]]:  # noqa: WPS231
        """
        Convert basic Markdown text to Notion blocks. Support headings, paragraphs, bullet points.

        Args:
            markdown (str): Markdown text to convert.

        Returns:
            List[Dict[str, Any]]: List of Notion blocks.
        """
        lines = markdown.splitlines()
        blocks = []
        image_map = self.collect_images(markdown)

        for line in lines:
            line = line.rstrip()

            # Parse images
            img_match = check_for_image(line)
            if img_match:
                _, url = img_match.groups()
                public_url = image_map.get(resolve_image_path(url, self.project_root))
                if public_url:
                    blocks.append(
                        {
                            "object": "block",
                            "type": "image",
                            "image": {
                                "type": "external",
                                "external": {"url": public_url},
                            },
                        },
                    )
            if self._parse_heading(line, blocks):
                continue

            if line.startswith("- ") or line.startswith("* "):
                # Bullet list item
                blocks.append(
                    {
                        "object": "block",
                        "type": "bulleted_list_item",
                        "bulleted_list_item": {"rich_text": self._parse_rich_text(line[2:])},
                    },
                )
            else:
                # Paragraph
                blocks.append(
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {"rich_text": self._parse_rich_text(line)},
                    },
                )
        return blocks

    def upload_markdown_file(self, file_path: str, title: str, properties: Dict[str, Any]) -> str:
        """
        Read the markdown file, convert to Notion blocks, and upload as a new page.

        Args:
            file_path (str): Path to the markdown file.
            title (str): Title of the new Notion page.
            properties (Dict[str, Any]): Properties to add to the new Notion page.

        Returns:
            str: URL of the created Notion page.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            markdown = file.read()

        blocks = self.markdown_to_blocks(markdown)
        data = {
            "parent": {"database_id": self.database_id},
            "properties": {"Paper name": {"title": [{"text": {"content": title}}]}, **properties},
            "children": blocks,
        }
        url = f"{self.base_url}/pages"

        response = requests.post(url, headers=self.headers, data=json.dumps(data), timeout=60)  # noqa: WPS221
        response.raise_for_status()
        page = response.json()
        return page.get("url", "")


if __name__ == "__main__":
    DATABASE_ID = "228f6f75bb0b80babf73d46a6254a459"
    FILE_PATH = "site/_reports/01-2024/Diffusion_Model_Compression_for_Image-to-Image_Translation.md"
    TITLE = "Diffusion Model Compression for Image-to-Image Translation"
    properties = {
        "Category": {"multi_select": [{"name": "Image Editing"}]},
        "Status": {"select": {"name": "Inbox"}},
        "Arxiv": {"url": "https://arxiv.org/abs/2406.00000"},
        "Published": {"date": {"start": "2024-01-01"}},
    }

    uploader = MarkdownToNotionUploader(database_id=DATABASE_ID)
    uploader.upload_markdown_file(FILE_PATH, TITLE, properties)
