import boto3
import os
from dotenv import load_dotenv 
# loading variables from .env file
load_dotenv() 

# Define your AWS credentials
aws_access_key_id = os.getenv('ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('SECRET_ACCESS_KEY')

# Define the name of the S3 bucket and the file you want to upload
bucket_name = os.getenv('BUCKET_NAME')
region_name = os.getenv('BUCKET_REGION')  
file_name = 'uploads/test.txt'

# Create a Boto3 S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    config=boto3.session.Config(signature_version='s3v4'),
    region_name=region_name
)
# Upload the file to S3
s3.upload_file(file_name, bucket_name, file_name)
print(f'{file_name} uploaded successfully to {bucket_name}.')