"""
-*- coding: utf-8 -*-
========================
AWS Lambda
========================
Contributor: Chirag Rathod (Srce Cde)
========================
"""

import json
import boto3
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

# Define the S3 bucket and object key for the invoice PDF
bucket_name = '6814a-bills'
object_key = 'Water/Water_July_2020.jpg'

def textract_data():
    response = textract.analyze_document(
        Document={
            "S3Object": {
                "Bucket": bucket_name,
                "Name": object_key,
            }
        },
        FeatureTypes=["FORMS", "TABLES"],
    )
    return response

response = textract_data()


# raw_text = extract_text(response, extract_by="LINE")
# word_map = map_word_id(response)
# table = extract_table_info(response, word_map)
# key_map = get_key_map(response, word_map)
# value_map = get_value_map(response, word_map)
# final_map = get_kv_map(key_map, value_map)

# key_value_map = json.dumps(final_map, indent=4)  # indent for pretty printing

# # Specify the file path for the key: value pairs
# file_path = 'key_value_map.json'

# # Write key:value string to text file
# with open(file_path, 'w') as file:
#     file.write(key_value_map)

# # file_path2 = 'textract_response.json'

# # for item in response['Blocks']:
# #     if item['BlockType'] == 'KEY_VALUE_SET':
# #         # Write JSON string to text file
# #         with open(file_path2, 'w') as file:
# #             file.write(json.dumps(item, indent=4))


# # file_path3 = "full_response.json"
# # # Write JSON string to text file
# # with open(file_path3, 'w') as file:
# #     file.write(json.dumps(response, indent=4))

# print("Key:Values data has been written to:", file_path)

# print(json.dumps(table))
# print(json.dumps(final_map))
# print(raw_text)

# key_value_map = json.loads(key_value_map)

# print ("Account Number:", key_value_map['Account number'])
# print("Amount Due:", key_value_map['Amount due'])
