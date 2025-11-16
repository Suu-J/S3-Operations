import boto3

# copy an S3 folder to a new location within the same bucket
def copy_s3_folder(bucket_name, source_folder_key, destination_folder_key, aws_access_key_id, aws_secret_access_key, aws_region_name):
    s3_client = boto3.client(
        's3',
        region_name=aws_region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # trying to make sure it ends with slash, getting issues otherwise
    if not source_folder_key.endswith('/'):
        source_folder_key += '/'
    if not destination_folder_key.endswith('/'):
        destination_folder_key += '/'

    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=source_folder_key):
        print("outer loop")
        print(page)
        print('\n')
        for obj in page.get('Contents', []):
            print("Inner loop")
            destination_key = obj['Key'].replace(source_folder_key, destination_folder_key, 1)
            copy_source = {
                'Bucket': bucket_name,
                'Key': obj['Key']
            }
            s3_client.copy(copy_source, bucket_name, destination_key)
            print(f'Copied {obj["Key"]} to {destination_key}')

aws_access_key_id = ''
aws_secret_access_key = ''
aws_region_name = ''
s3_bucket_name = ''
source_folder_key = ''
destination_folder_key = ''

copy_s3_folder(
    bucket_name=s3_bucket_name,
    source_folder_key=source_folder_key,
    destination_folder_key=destination_folder_key,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_region_name=aws_region_name
)
