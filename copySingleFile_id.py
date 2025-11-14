import boto3

# AWS configuration
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region_name = ''
s3_bucket_name = ''

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    region_name=aws_region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

base_source_prefix = 'base-path/'  
destination_folder = 'targe-path/'  # this destination folder is within the same bucket

# copy objects that match the ID within the source prefix
def copy_objects_with_id(bucket_name, source_prefix, destination_folder, conversation_id):
    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=source_prefix):
        for content in page.get('Contents', []):
            # object key is the full length path
            if conversation_id in content['Key']:
                # the start of the folder name in the key
                folder_name_start_index = content['Key'].find(f'conversation_id={conversation_id}')
                # get the full folder path
                full_folder_path = content['Key'][:content['Key'].find('/', folder_name_start_index)]
                # copied to new dest
                destination_key = content['Key'].replace(full_folder_path, destination_folder + full_folder_path)
                s3_client.copy(
                    {'Bucket': bucket_name, 'Key': content['Key']},
                    bucket_name,
                    destination_key
                )
                print(f'Copied {content["Key"]} to {destination_key}')

def copy_single_conversation_folder(conversation_id):
    copy_objects_with_id(s3_bucket_name, base_source_prefix, destination_folder, conversation_id)

if __name__ == "__main__":
    # the id we are filtering on
    conversation_id = '' 
    copy_single_conversation_folder(conversation_id)
