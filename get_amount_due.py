import json
from full_response import response
from parser import map_line_id

response_data = response
due_synonyms = ["rate", 'Amount due', "New"]


with open('output.json', 'r') as key_values:
    data = json.load(key_values)

keys = data.keys()

for key in keys:
    if key in due_synonyms:
        total_key = key

print(total_key+':', data[total_key])
