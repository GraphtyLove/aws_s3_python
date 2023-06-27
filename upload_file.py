import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".env")


def upload_file(local_file_path: str, object_name: str) -> None:
    """
    Upload a object (file) to an AWS S3 bucket.

    :param local_file_path: The path to the local file to upload.
    :param object_name: The name to give the object (file) in the bucket.
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
    
    print(f"uploading file: {local_file_path}....")
    
    # Upload local file
    with open(local_file_path, "rb") as file:
      s3.upload_fileobj(file, bucket_name, object_name)

    print("file uploaded!")

    return


if __name__ == "__main__":
    upload_file("./data/test.json", "test2.json")
