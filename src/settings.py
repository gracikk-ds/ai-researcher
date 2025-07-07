"""Application settings."""

import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Attributes:
        gemini_model_name: Gemini model name.
        site_reports_dir: Site reports directory.
        telegram_token: Telegram bot token.
        telegram_chat_id: Chat ID to send notifications to.
        check_interval_seconds: Interval between checks in seconds.
    """

    model_config = SettingsConfigDict(
        env_file=os.getenv("ENV_FILE_PATH", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
        protected_namespaces=("settings_",),  # Added to resolve the warning
    )

    github_url_template: str = Field(
        "https://gracikk-ds.github.io/ai-researcher/reports/{month_year}/{title}/",
        description="Base GitHub repository URL.",
    )
    gemini_model_name: str = Field("gemini-2.5-pro", description="Gemini model name.")
    site_reports_dir: str = Field("site/_reports", description="Site reports directory.")
    telegram_token: str = Field(..., description="Telegram bot token.")
    telegram_chat_id: int = Field(..., description="Chat ID to send notifications to.")
    check_interval_minutes: int = Field(1, description="Interval between checks in minutes.")  # noqa: WPS432
    notion_token: str = Field(..., description="Notion API token.")
    aws_access_key_id: str = Field(..., description="AWS access key ID.")
    aws_secret_access_key: str = Field(..., description="AWS secret access key.")
    endpoint_url: str = Field(..., description="AWS endpoint URL.")
    s3_bucket: str = Field(..., description="S3 bucket name.")


settings = Settings()  # type: ignore
