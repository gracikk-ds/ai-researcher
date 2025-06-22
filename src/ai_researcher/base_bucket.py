"""Abstract base class for bucket storage."""

from abc import ABC, abstractmethod
from typing import Optional

from google.cloud import storage  # type: ignore


class BaseBucket(ABC):
    """Abstract base class for bucket storage."""

    location: str = "us-central1"

    def __init__(self, bucket_prefix: str = "pdfs") -> None:
        """Initialize the base bucket class.

        Args:
            bucket_prefix (str): Prefix to filter files for deletion.
        """
        self.bucket_prefix = bucket_prefix
        self._bucket_name: Optional[str] = None
        self._bucket: Optional[storage.Bucket] = None
        self._creds: Optional[dict] = None
        self.project: Optional[str] = None

    @property
    def full_bucket_path(self) -> str:
        """Get the full bucket path.

        Returns:
            str: The full bucket path.
        """
        return f"gs://{self.bucket_name}/{self.bucket_prefix}"

    @property
    def bucket_name(self) -> str:
        """Get the bucket name.

        Returns:
            str: The bucket name.
        """
        if self._bucket_name is None:
            self._bucket_name = "sd_layer"
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name: str) -> None:
        """Set the bucket name.

        Args:
            bucket_name (str): The bucket name.
        """
        self._bucket_name = bucket_name

    @abstractmethod
    def _load_project_id_from_creds(self) -> None:
        """Load the project id from the credentials."""
        pass

    @abstractmethod
    def list_files(self, prefix: Optional[str] = None) -> list:
        """List all files in the bucket, optionally under a prefix.

        Args:
            prefix (Optional[str]): Prefix to filter files.

        Returns:
            list: List of blob names (str).
        """
        pass

    @abstractmethod
    def upload_file(self, local_path: str) -> str:
        """Upload a file to the bucket.

        Args:
            local_path (str): Path to the local file.

        Returns:
            str: The name of the uploaded file.
        """
        pass

    @abstractmethod
    def download_file(self, blob_name: str, local_path: str) -> None:
        """Download a file from the bucket.

        Args:
            blob_name (str): Name of the blob in the bucket.
            local_path (str): Local path to save the file.
        """
        pass

    @abstractmethod
    def remove_file(self, blob_name: str) -> None:
        """Remove a file from the bucket under the current prefix.

        Args:
            blob_name (str): Name of the blob in the bucket to remove.
        """
        pass

    @abstractmethod
    def remove_all_files_in_prefix(self, prefix: Optional[str] = None) -> None:
        """Remove all files under the given prefix (default: current bucket_prefix).

        Args:
            prefix (Optional[str]): Prefix to filter files for deletion.
        """
        pass
