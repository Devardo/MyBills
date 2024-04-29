import json
import boto3
from file_dialog_test import open_file_dialog
from get_provider_test2 import get_provider
from parser import (
    extract_text,
    map_word_id,
    extract_table_info,
    get_key_map,
    get_value_map,
    get_kv_map,
)


# Initialize the Textract client
textract = boto3.client('textract')

# Define the S3 bucket 
bucket_name = '6814a-bills'
# object_key = 'Water/Water_July_2020.jpg'

# Select file to upload to S3
file_to_upload = open_file_dialog()
object_name = file_to_upload.split('/')
object_name = object_name[-1]


# Upload file to S3
def upload_to_s3(file_to_upload, bucket_name, object_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the file to the specified bucket and object name
    try:
        s3.upload_file(file_to_upload, bucket_name, object_name)
        print("File uploaded successfully to S3 bucket:", bucket_name)
    except Exception as e:
        print("Error uploading file to S3 bucket:", e)

#upload file to s3
upload_to_s3(file_to_upload, bucket_name, object_name)

def textract_data():
    response = textract.analyze_document(
        Document={
            "S3Object": {
                "Bucket": bucket_name,
                "Name": object_name,
            }
        },
        FeatureTypes=["FORMS", "TABLES"],
    )
    return response

response = textract_data()


word_map = map_word_id(response)

key_map = get_key_map(response, word_map)
value_map = get_value_map(response, word_map)
final_map = get_kv_map(key_map, value_map)

key_value_map = json.dumps(final_map, indent=4)  # indent for pretty printing

# Specify the file path for the key: value pairs
file_path = 'key_value_map.json'

# Write key:value string to text file
with open(file_path, 'w') as file:
    file.write(key_value_map)

# Get lines frm response data
lines = extract_text(response, extract_by="LINE")

# Parse lines for provider
provider = get_provider(lines)