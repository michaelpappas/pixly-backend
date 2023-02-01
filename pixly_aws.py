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


"""
- Function to upload an image
- ? Helper function to construct the thumbnail/original file url


Maybe in a separate helper file:
- Unique filename generator

"""

# def upload_file(file_name, bucket, object_name=None):
#     """Upload a file to an S3 bucket

#     :param file_name: File to upload
#     :param bucket: Bucket to upload to
#     :param object_name: S3 object name. If not specified then file_name is used
#     :return: True if file was uploaded, else False
#     """

#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = os.path.basename(file_name)

#     # Upload the file
#     s3_client = boto3.client("s3", AWS_REGION,
#                 aws_access_key_id=AWS_ACCESS_KEY_ID,
#                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True
#
#
def upload_profile_photo(file):
    """
    Upload User Profile Photo
    """
    image_file = file
    client = boto3.client('s3',
                        region_name=AWS_REGION,
                        # endpoint_url='https://example.xxx.amazonaws.com',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    try:
        client.put_object(Body=image_file,
                      Bucket=AWS_BUCKET_NAME,
                      Key=f"pixly/images/{image_file.filename}",
                      ContentType=image_file.mimetype)
        print("success!")
    except Exception as e:
        print(e)



