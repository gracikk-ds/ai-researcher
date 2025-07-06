"""Gemini Api Client."""

import json
import os
import subprocess  # noqa: S404
from typing import Optional

from dotenv import load_dotenv
from google.cloud import storage  # type: ignore
from loguru import logger

from src.ai_researcher.base_bucket import BaseBucket

load_dotenv()


class GoogleBucket(BaseBucket):  # noqa: WPS214
    """Google Bucket class."""

    def __init__(self, bucket_prefix: str = "pdfs") -> None:
        """Initialize GoogleBucket.

        Args:
            bucket_prefix (str): Prefix to filter files for deletion.
        """
        super().__init__(bucket_prefix)
        self._load_project_id_from_creds()

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

    def _create_bucket(self) -> None:
        """Create a bucket for the Gemini API.

        Raises:
            ValueError: If the bucket cannot be created.
        """
        cmd = f"gsutil mb -l {self.location} -p {self.project} gs://{self.bucket_name}"
        return_code = subprocess.call(cmd, shell=True)  # noqa: S602
        logger.info(f"Return code: {return_code} for bucket={self.bucket_name} creation")
        if return_code != 0:
            raise ValueError("Can not create gs bucket.")

    @property
    def bucket(self) -> storage.Bucket:
        """Get the bucket.

        Returns:
            storage.Bucket: The bucket object.
        """
        if self._bucket is None:
            gs_client = storage.Client(project=self.project)
            bucket = gs_client.bucket(self.bucket_name)
            if bucket.exists():
                self._bucket = bucket
                return self._bucket
            self._create_bucket()
            self._bucket = gs_client.bucket(self.bucket_name)
            return self._bucket
        return self._bucket

    def list_files(self, prefix: Optional[str] = None) -> list:
        """List all files in the bucket, optionally under a prefix.

        Args:
            prefix (Optional[str]): Prefix to filter files.

        Returns:
            list: List of blob names (str).
        """
        blobs = self.bucket.list_blobs(prefix=prefix or self.bucket_prefix)
        return [blob.name for blob in blobs]

    def upload_file(self, local_path: str) -> str:
        """Upload a file to the bucket.

        Args:
            local_path (str): Path to the local file.

        Returns:
            str: The name of the uploaded file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(local_path):
            raise FileNotFoundError(f"File {local_path} does not exist")
        base_name = os.path.basename(local_path)
        destination_blob_name = f"{self.bucket_prefix}/{base_name}"
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_path)
        logger.info(f"Uploaded {local_path} to {destination_blob_name}")
        return f"gs://{self.bucket_name}/{destination_blob_name}"

    def upload_public_file(self, local_path: str) -> str:
        """Upload a file to the bucket.

        Args:
            local_path (str): Path to the local file.

        Returns:
            str: The name of the uploaded file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(local_path):
            raise FileNotFoundError(f"File {local_path} does not exist")
        base_name = os.path.basename(local_path)
        destination_blob_name = f"{self.bucket_prefix}/{base_name}"
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_path)
        logger.info(f"Uploaded {local_path} to {destination_blob_name}")
        return f"https://storage.googleapis.com/{self.bucket_name}/{destination_blob_name}"

    def download_file(self, blob_name: str, local_path: str) -> None:
        """Download a file from the bucket.

        Args:
            blob_name (str): Name of the blob in the bucket.
            local_path (str): Local path to save the file.

        Raises:
            FileNotFoundError: If the blob does not exist in the bucket.
        """
        blob = self.bucket.blob(blob_name)
        if not blob.exists():
            raise FileNotFoundError(f"Blob {blob_name} does not exist in bucket {self.bucket_name}")
        blob.download_to_filename(local_path)
        logger.info(f"Downloaded {blob_name} to {local_path}")

    def remove_file(self, blob_name: str) -> None:
        """Remove a file from the bucket under the current prefix.

        Args:
            blob_name (str): Name of the blob in the bucket to remove (should include prefix if needed).

        Raises:
            FileNotFoundError: If the blob does not exist in the bucket.
        """
        if blob_name.startswith("gs://"):
            blob_name = blob_name.removeprefix(f"gs://{self.bucket_name}/")
        blob = self.bucket.blob(blob_name)
        if not blob.exists():
            raise FileNotFoundError(f"Blob {blob_name} does not exist in bucket {self.bucket_name}")
        blob.delete()
        logger.info(f"Deleted blob {blob_name} from bucket {self.bucket_name}")

    def remove_all_files_in_prefix(self, prefix: Optional[str] = None) -> None:
        """Remove all files under the given prefix (default: current bucket_prefix).

        Args:
            prefix (Optional[str]): Prefix to filter files for deletion.
        """
        prefix_to_use = prefix or self.bucket_prefix
        blobs = list(self.bucket.list_blobs(prefix=prefix_to_use))
        if not blobs:
            logger.info(f"No files found under prefix '{prefix_to_use}' in bucket {self.bucket_name}")
            return
        for blob in blobs:
            blob.delete()
            logger.info(f"Deleted blob {blob.name} from bucket {self.bucket_name}")
