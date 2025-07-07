"""Provide a class for uploading images to S3."""

import boto3

from src.settings import settings


class S3Uploader:
    """Handle uploading files to an S3-compatible storage.

    Attributes:
        s3_client (boto3.client): The boto3 S3 client instance.
    """

    def __init__(self, folder: str = "reports"):
        """Initialize the S3Uploader with credentials from environment variables.

        Args:
            folder (str): Folder to upload the files to.
        """
        aws_access_key_id = settings.aws_access_key_id
        aws_secret_access_key = settings.aws_secret_access_key
        endpoint_url = settings.endpoint_url
        self.bucket = settings.s3_bucket
        self.folder = folder

        session = boto3.session.Session()
        self.s3_client = session.client(
            service_name="s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            endpoint_url=endpoint_url,
        )

    def get_public_url(self, s3_key: str) -> str:
        """Generate the public URL for a file in the S3 bucket.

        Args:
            s3_key (str): S3 key (path) of the file in the bucket.

        Example of the public URL:
        https://rndml-team-layer.obs.ru-moscow-1.hc.sbercloud.ru:443/reports/figure_2.jpg

        Returns:
            str: Public URL of the file.
        """
        endpoint_url = settings.endpoint_url.removeprefix("https://")
        return f"https://{self.bucket}.{endpoint_url}:443/{s3_key}"

    def upload_file(self, local_path: str, s3_key: str) -> str:
        """Upload a single file to the specified S3 bucket and make it public.

        Args:
            local_path (str): Path to the local file.
            s3_key (str): S3 key (path) where the file will be uploaded.

        Returns:
            str: Public URL of the uploaded file.
        """
        s3_key = f"{self.folder}/{s3_key}"
        self.s3_client.upload_file(local_path, self.bucket, s3_key, ExtraArgs={"ACL": "public-read"})
        return self.get_public_url(s3_key)
