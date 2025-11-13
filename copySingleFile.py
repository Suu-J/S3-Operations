import boto3

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

# move files!
base_source_folder = '' 
destination_folder = '' 

# Within the same s3 bucket
def copy_folder_within_bucket(bucket_name, source_folder, destination_folder):
    print("Creating paginator\n")
    paginator = s3_client.get_paginator('list_objects_v2')
    print("Created paginator\n")
    for page in paginator.paginate(Bucket=bucket_name, Prefix=source_folder):
        print("in paginator\n")#debugging
        for content in page.get('Contents', []):
            print("in page\n")#debugging
            copy_source = {
                'Bucket': bucket_name,
                'Key': content['Key']
            }
            destination_key = content['Key'].replace(source_folder, destination_folder, 1)
            print("copying...\n")
            s3_client.copy(copy_source, bucket_name, destination_key)
            print(f'Copied {content["Key"]} to {destination_key}')

def copy_single_folder(id):
    # using wildcard for example
    source_folder = f'{base_source_folder}month=*/day=*/hour=*/conversation_id={id}/'

    copy_folder_within_bucket(s3_bucket_name, source_folder, destination_folder)

if __name__ == "__main__":
    # filter according to ids
    conversation_id = ''  
    copy_single_folder(conversation_id)