import boto3
import csv

# listing all the files in the bucket
aws_access_key_id = ''
aws_secret_access_key = ''
region_name = ''

bucket_name = ''
folder_path = ''

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)


# listing using paginator
keys = []
paginator = s3.get_paginator('list_objects_v2')
for result in paginator.paginate(Bucket=bucket_name, Prefix=folder_path):
    if 'Contents' in result:
        for obj in result['Contents']:
            keys.append(obj['Key'])

# in this case we only want to display .opus files
opus_files = [key.split('/')[-1].split('.')[0] for key in keys if key.endswith('.opus')]

with open('uploaded_opus_files.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for opus_file in opus_files:
        writer.writerow([opus_file])