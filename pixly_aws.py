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


# def create_presigned_url(expiration=3600):
#     """Generate a presigned URL to share an S3 object

#     :param bucket_name: string
#     :param object_name: string
#     :param expiration: Time in seconds for the presigned URL to remain valid
#     :return: Presigned URL as string. If error, returns None.
#     """

#     # Generate a presigned URL for the S3 object

#     s3_client = boto3.client("s3", AWS_REGION,
#                 aws_access_key_id=AWS_ACCESS_KEY_ID,
#                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
#     try:
#         response = s3_client.generate_presigned_url('get_object',
#                                                     Params={'Bucket': AWS_BUCKET_NAME,
#                                                             'Key': "pixly/1f4d8ea7-e9d9-48b7-b70c-819482fb10fb-cover.png"},
#                                                     ExpiresIn=6000)
#         # response = s3_client.generate_presigned_url('get_object',
#         #                                             Params={'Bucket': AWS_BUCKET_NAME,
#         #                                                     'Key': "teamwork.jpeg"},
#         #                                             ExpiresIn=6000)
#     except ClientError as e:
#         logging.error(e)
#         return None

#     # The response contains the presigned URL
#     return response

"""
- Function to upload an image
- ? Helper function to construct the thumbnail/original file url


Maybe in a separate helper file:
- Unique filename generator

"""