# S3 Operations Scripts

Scripts for AWS S3 bucket operations including copying, listing, and managing files.

## File Copying Scripts
- **copySingleFile.py** - Copies a single file/folder within S3
- **copySingleFile_id.py** - Enhanced version for copying files based on conversation IDs
- **copyObject.py** - Copies objects from source to destination folders using CSV input
- **folder_copy.py** - Copies conversation folders within S3
- **folder_copy_id.py** - Improved folder copying with conversation ID filtering
- **transferObj.py** - General S3 folder transfer utility

## File Listing Scripts
- **list_uploaded_files.py** - Lists all .opus files in S3 and saves to CSV
- **createCSV.py** - Lists all S3 objects and saves to CSV
- **createCSV_2.py** - Lists S3 objects filtered by 'conversation_id='
- **createCSV_3.py** - Lists S3 objects filtered by conversation ID, excluding JSON files
- **year2023_list.py** - Lists objects from year=2023 folder

## Requirements
- AWS credentials (access key, secret key)
- boto3 library
- Appropriate S3 bucket permissions

