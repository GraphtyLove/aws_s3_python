import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".env")


def delete_file(object_name: str) -> None:
    """
    Delete a object (file) from an AWS S3 bucket.

    :param object_name: The name of the object (file) to delete.
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
    
    print(f"Deleting remote file: {object_name}...")
    
    # Delete the object
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    print("File deleted!")

    return


if __name__ == "__main__":
    delete_file("test2.json")
