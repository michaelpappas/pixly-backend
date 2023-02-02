import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError
import logging

load_dotenv()

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_BUCKET_NAME = os.environ['AWS_BUCKET_NAME']
AWS_ACCESS_KEY_ID=  os.environ['AWS_ACCESS_KEY_ID']
AWS_REGION = os.environ['AWS_REGION']


def upload_image_to_aws(image, folder_path, file_name):
    """
    Upload image to AWS S3 bucket

    :param image: FileStorage data with image to upload
    :param folder_path: Folder path in bucket to upload to
    :param file_name: File name to upload as
    :return: True if file was uploaded, else False
    """

    s3_client = boto3.client(
        's3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    try:
        s3_client.put_object(
            Body=image,
            Bucket=AWS_BUCKET_NAME,
            Key=f"{folder_path}{file_name}"
        )
    except ClientError as e:
        logging.error(e)
        return False

    return True