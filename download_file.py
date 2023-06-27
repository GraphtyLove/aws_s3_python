import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".env")


def download_file(local_file_desired_path: str, object_name: str) -> str:
    """
    Download a object (file) from an AWS S3 bucket and save it to a local file.

    :param local_file_desired_path: The path to the local file to save the object to.
    :param object_name: The name of the object (file) to download.
    :return: The path to the local file.
    """

    # Load environment variables
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    bucket_name = os.getenv("S3_BUCKET")

    # Raise an error if the environment variables are not found
    if not access_key or not secret_key or not bucket_name:
        raise ValueError("Missing environment variables... Please check your .env file")

    # Initialize the connection to AWS S3
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    
    print(f"Downloading file: {object_name}...")
    
    # Download the object
    s3.download_file(bucket_name, object_name, local_file_desired_path)
    
    print("File downloaded!")
    
    return local_file_desired_path


if __name__ == "__main__":
    file_path = download_file("./data/downloaded_file.json", "test.json")
    print(f"File downloaded to: {file_path}")
