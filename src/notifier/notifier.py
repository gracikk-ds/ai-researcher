"""Notifier for sending messages via Telegram."""

from typing import Any

import requests
from loguru import logger

from src.settings import Settings


class Notifier:
    """Notifier for sending messages via Telegram."""

    _api_url_template = "https://api.telegram.org/bot{token}/sendMessage"

    def __init__(self, settings: Settings) -> None:
        """Initialize the Notifier.

        Args:
            settings: Settings for the Notifier.
        """
        self.settings = settings

    def send(self, message: str) -> None:
        """
        Send a text message to the configured Telegram chat.

        Args:
            message: Text message to send.
        """
        url = self._api_url_template.format(token=self.settings.telegram_token)
        payload: dict[str, Any] = {"chat_id": self.settings.telegram_chat_id, "text": message}
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            logger.info(f"Notification sent: {message}.")
        except requests.RequestException as exc:
            logger.error(f"Failed to send Telegram message: {exc}.")
