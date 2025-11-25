# saving 
# i should just put the string in variable


import boto3
import csv

aws_access_key_id = ''
aws_secret_access_key = ''
aws_region_name = ''
s3_bucket_name = ''

s3_client = boto3.client(
    's3',
    region_name=aws_region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

print("printing all objects in the S3 bucket\n")

def list_s3_objects(bucket_name):
    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name):
        for content in page.get('Contents', []):
            yield content['Key']

print("making CSV file\n")

def save_to_csv(object_keys, filename='s3_file_list3.csv'):
    with open(filename, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['Filename'])
        for key in object_keys:
            if 'conversation_id=' in key and not key.endswith('.json'):
                filewriter.writerow([key])

def main():
    object_keys = list_s3_objects(s3_bucket_name)
    save_to_csv(object_keys)


if __name__ == "__main__":
    main()