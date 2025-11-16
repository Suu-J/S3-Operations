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

base_source_prefix = ''  
destination_folder = ''  

def copy_conversation_folder(bucket_name, base_source_prefix, destination_folder, conversation_id):
    # folder_to_copy = f"conversation_id={conversation_id}/"
    # source_prefix = base_source_prefix + folder_to_copy(
    source_prefix = ''

    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=source_prefix)
    for page in pages:
        for obj in page.get('Contents', []):
            if conversation_id in obj['Key']:
                print(obj['Key'])
                # print(obj)
            '''
            destination_key = destination_folder + content['Key'][len(base_source_prefix):]
            s3_client.copy(
                {'Bucket': bucket_name, 'Key': content['Key']},
                bucket_name,
                destination_key
            )'''
            # print(f'Copied {content["Key"]} to {destination_key}')

if __name__ == "__main__":
    conversation_id = ''  
    copy_conversation_folder(s3_bucket_name, base_source_prefix, destination_folder, conversation_id)





