"""Extract information from a Notion page using the Notion API.

Link to API page: https://www.notion.so/profile/integrations/internal/4332f261-a4c4-4579-8635-14617fae08bc
"""

from typing import Any, Dict, List

import requests

from src.settings import settings


class NotionPageExtractor:
    """
    Class to extract information from a Notion page using the Notion API.

    Attributes:
        api_token (str): Integration token for authenticating with the Notion API.
        base_url (str): Base URL for Notion API endpoints.
        headers (dict): Headers for the Notion API requests.

    Methods:
        get_page(page_id): Returns page properties as a dictionary.
        get_blocks(page_id): Returns a list of blocks (content) for a given page.
        extract_text_from_blocks(blocks): Extracts and concatenates text from blocks.
    """

    def __init__(self) -> None:
        """Initialize with the provided Notion integration token."""
        self.api_token = settings.notion_token
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        }

    def get_page(self, page_id: str) -> Dict[str, Any]:
        """
        Fetch the properties of a Notion page.

        Args:
            page_id (str): The ID of the Notion page.

        Returns:
            dict: Dictionary of page properties.
        """
        url = f"{self.base_url}/pages/{page_id}"
        response = requests.get(url, headers=self.headers, timeout=60)
        response.raise_for_status()
        return response.json()

    def get_blocks(self, page_id: str, page_size: int = 100) -> List[Dict[str, Any]]:
        """
        Retrieve the content blocks of a Notion page.

        Args:
            page_id (str): The ID of the Notion page.
            page_size (int): Number of blocks to fetch per request (max 100).

        Returns:
            list: List of block objects.
        """
        blocks = []
        url = f"{self.base_url}/blocks/{page_id}/children?page_size={page_size}"
        while url:
            response = requests.get(url, headers=self.headers, timeout=60)
            response.raise_for_status()
            data = response.json()
            blocks.extend(data.get("results", []))
            url = data.get("next_cursor")
            if url:
                url = f"{self.base_url}/blocks/{page_id}/children?start_cursor={url}&page_size={page_size}"
        return blocks

    @staticmethod
    def extract_text_from_block(block: Dict[str, Any]) -> str:  # noqa: WPS602
        """
        Extract and concatenate plain text from Notion blocks.

        Args:
            block (Dict[str, Any]): Notion block object.

        Returns:
            str: Concatenated text extracted from the blocks.
        """
        texts = []
        block_type = block.get("type")
        if block_type and block_type in block:
            rich_text = block[block_type].get("rich_text", [])
            for text in rich_text:
                plain_text = text.get("plain_text")
                if plain_text:
                    texts.append(plain_text)  # noqa: WPS220
        return "\n".join(texts)


if __name__ == "__main__":
    PAGE_ID = "228f6f75bb0b8023a7aeced6e6799a89"
    extractor = NotionPageExtractor()

    blocks = extractor.get_blocks(PAGE_ID)
    for block in blocks:
        if block.get("type") == "heading_1":
            header_text = extractor.extract_text_from_block(block)
            print(header_text)
