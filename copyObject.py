import boto3
import pandas as pd

# moving an object to a diff location within bucket

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

found_yes_df = pd.read_csv('found_yes.csv')

source_folder = 'year=2023/'
destination_folder = 'new_folder/' 

def copy_file_within_bucket(bucket_name, source_key, destination_key):
    copy_source = {
        'Bucket': bucket_name,
        'Key': source_key
    }
    s3_client.copy(copy_source, bucket_name, destination_key)

def main():
    for index, row in found_yes_df.iterrows():
        id = row['Conversation ID']
        source_key = f'{source_folder}{id}'
        destination_key = f'{destination_folder}{id}'

        copy_file_within_bucket(s3_bucket_name, source_key, destination_key)
        print(f'Copied {source_key} to {destination_key}')

if __name__ == "__main__":
    main()