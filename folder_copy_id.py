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


base_source_directory = ''
destination_directory = ''


def find_and_copy_conversation_folder(bucket_name, base_source_directory, destination_directory, conversation_id):

    folder_name = f"conversation_id={conversation_id}/"
    

    paginator = s3_client.get_paginator('list_objects_v2')
    operation_parameters = {'Bucket': bucket_name, 'Prefix': base_source_directory}

    for page in paginator.paginate(**operation_parameters):
        for obj in page.get('Contents', []):
            
            if '/' + folder_name in obj['Key']:
                
                source_key = obj['Key']
                destination_key = destination_directory + source_key[len(base_source_directory):]
                
                s3_client.copy({'Bucket': bucket_name, 'Key': source_key}, bucket_name, destination_key)
                print(f'Copied {source_key} to {destination_key}')


if __name__ == "__main__":
    
    conversation_id = ''
    find_and_copy_conversation_folder(s3_bucket_name, base_source_directory, destination_directory, conversation_id)