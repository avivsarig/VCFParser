import re
import boto3


def file_from_s3(file_path):
    s3_client = boto3.client("s3")

    pattern = r"s3://([^/]+)/(.+)"
    match = re.match(pattern, file_path)

    if match:
        bucket_name = match.group(1)
        key = match.group(2)

    response = s3_client.get_object(Bucket=bucket_name, Key=key)
    compressed_file = response["Body"]
    return compressed_file
