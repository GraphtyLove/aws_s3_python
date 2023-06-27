# Using AWS S3 in Python

If you want to save files to the cloud, you can use AWS S3. This is a quick guide to get you started.

![AWS S3](https://fathomtech.io/blog/using-aws-s3-and-cloudfront-for-fast-static-web-sites/amazon-s3.png)

## What is AWS S3?

AWS S3 (Simple Storage Service) is a scalable object storage service for storing and retrieving any amount of data from anywhere on the web. It is designed to be cheap and scalable. You can read more about it [here](https://aws.amazon.com/s3/).

## How to use it

### 1. Create an AWS account

First, you need to create an AWS account.

*You can do this in the [AWS Management Console](https://aws.amazon.com/console/).*


### 2. Create a S3 bucket

Next, you need to create a bucket. This is where you will store your files. 

*You can do this in the [AWS Management Console](https://aws.amazon.com/console/). You can also do it using the [AWS CLI](https://aws.amazon.com/cli/).*

### 3. Get your Access Keys

You need your access keys (Access Key ID and Secret Access Key) to connect to your S3 bucket. 

*You can do this in the [AWS Management Console](https://aws.amazon.com/console/). You can also do it using the [AWS CLI](https://aws.amazon.com/cli/).*

### 4. Store your secrets

You need to store your secrets in a secure place. To keep things simple, we will use a `.env` file. and load it using the [python-dotenv](https://pypi.org/project/python-dotenv/) package.

Create a `.env` file in the root of your project and add your secrets to it. It should look something like this:

```bash
AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXX
AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXX
S3_BUCKET=XXXXXXXX
```

### 5. Upload a file
To upload a file, you an use the code sample in [upload_file.py](./upload_file.py)

```bash
python3 upload_file.py
```

### 6. Download a file
To download a file, you an use the code sample in [download_file.py](./download_file.py)

```bash
python3 download_file.py
```


### 7. Delete a file
To delete a file, you an use the code sample in [delete_file.py](./delete_file.py)

```bash
python3 delete_file.py
```