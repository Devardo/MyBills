import json
from full_response import response
from parser import map_line_id

response_data = response
due_synonyms = ["rate"]


for block in response["Blocks"]:
        if block["BlockType"] == "LINE" and block["Text"].lower() in due_synonyms:
            if block["Relationships"]:
                for relation in block["Relationships"]:
                    if relation["Type"] == "CHILD":
                        relation_id = relation["Ids"][0]
                        print(relation_id)

