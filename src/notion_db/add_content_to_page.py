"""Upload a Markdown file to a Notion database page."""

import json
import os
import re
from typing import Any, Dict, List

import requests

from src.notion_db.s3_loader import S3Uploader
from src.notion_db.utils import resolve_image_path
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

    def __init__(self, database_id: str = "228f6f75bb0b80babf73d46a6254a459") -> None:
        """Initialize the uploader with the provided database ID.

        Args:
            database_id (str): Notion database ID. Default is "228f6f75bb0b80babf73d46a6254a459"
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
        self.bucket = S3Uploader()

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

    def _remove_meta_lines(self, line: str, lines_to_remove: bool) -> tuple[bool, bool]:  # noqa: WPS212
        """Check whether the line is a meta line.

        Args:
            line (str): Line of text to parse.
            lines_to_remove (bool): True if we in the meta lines block, False otherwise.

        Returns:
            tuple[bool, bool]: Should we skip the line, and whether we are in the meta lines block.
        """
        if line.startswith("---") and lines_to_remove:  # end of meta lines block
            lines_to_remove = False
            return True, lines_to_remove  # skip the line and end the meta lines block

        if line.startswith("---"):  # start of meta lines block
            lines_to_remove = True
            return True, lines_to_remove  # skip the line and start the meta lines block

        if lines_to_remove:
            return True, lines_to_remove  # skip the line and continue

        return False, lines_to_remove  # don't skip the line and continue

    def _upload_image(self, local_path: str, blocks: List[Dict[str, Any]]) -> None:
        """Upload an image to S3 and add it to the blocks.

        Args:
            local_path (str): Path to the image.
            blocks (List[Dict[str, Any]]): List of Notion blocks.
        """
        s3_key = os.path.join(*os.path.normpath(local_path).split(os.sep)[-2:])  # noqa: WPS221
        public_url = self.bucket.upload_file(local_path, s3_key)
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

    def markdown_to_blocks(  # noqa: WPS231,C901,WPS221,WPS234
        self,
        markdown: str,
    ) -> tuple[List[Dict[str, Any]], str, str, str]:
        """
        Convert basic Markdown text to Notion blocks. Support headings, paragraphs, bullet points.

        Args:
            markdown (str): Markdown text to convert.

        Returns:
            List[Dict[str, Any]]: List of Notion blocks.
        """
        lines = markdown.splitlines()
        blocks: List[Dict[str, Any]] = []
        lines_to_remove = False
        first_heading = True
        title = ""
        arxiv_url = ""
        published_date = "2022-01-01"

        for line in lines:
            line = line.rstrip()

            # Check if the line is a meta line
            skip_line, lines_to_remove = self._remove_meta_lines(line, lines_to_remove)
            if skip_line:
                continue

            if first_heading and line.startswith("## "):
                first_heading = False
                title = line[3:]
                continue

            if line.startswith("**ArXiv URL:**"):
                arxiv_url = line.split("**ArXiv URL:**")[1].strip()
                continue

            if line.startswith("**Published Date:**"):
                published_date = line.split("**Published Date:**")[1].strip()
                continue

            # Parse images
            local_path = resolve_image_path(line, self.project_root)
            if local_path:
                self._upload_image(local_path, blocks)
                continue

            # Parse headings
            if self._parse_heading(line, blocks):
                continue

            # Parse bullet points
            if line.startswith("- ") or line.startswith("* "):
                # Bullet list item
                blocks.append(
                    {
                        "object": "block",
                        "type": "bulleted_list_item",
                        "bulleted_list_item": {"rich_text": self._parse_rich_text(line[2:])},
                    },
                )
            elif line == "":
                continue
            else:
                # Parse paragraphs
                blocks.append(
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {"rich_text": self._parse_rich_text(line)},
                    },
                )
        return blocks, arxiv_url, published_date, title

    def upload_markdown_file(self, file_path: str) -> str:  # noqa: WPS210
        """
        Read the markdown file, convert to Notion blocks, and upload as a new page.

        Args:
            file_path (str): Path to the markdown file.

        Returns:
            str: URL of the created Notion page.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            markdown = file.read()

        blocks, arxiv_url, published_date, title = self.markdown_to_blocks(markdown)
        properties = {
            "Category": {"multi_select": [{"name": "Image Editing"}]},
            "Status": {"select": {"name": "Inbox"}},
            "Arxiv": {"url": arxiv_url},
            "Published": {"date": {"start": published_date}},
        }
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


# if __name__ == "__main__":
    # uploader = MarkdownToNotionUploader()
    # uploader.upload_markdown_file("site/_reports/01-2024/Diffusion_Model_Compression_for_Image-to-Image_Translation.md")
