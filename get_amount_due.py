import json
from full_response import response
from parser import map_line_id

response_data = response
due_synonyms = ["rate"]


def get_rate_key():
    for block in response["Blocks"]:
        if block["BlockType"] == "LINE" and block["Text"].lower() in due_synonyms:
            if block["Relationships"]:
                for relation in block["Relationships"]:
                    if relation["Type"] == "CHILD":
                        relation_id = relation["Ids"][0]
                        print(relation_id)


def get_rate_kv(rate_key):
    for block in response["Blocks"]:
        if block["BlockType"] == "KEY_VALUE_SET":
            if block["Relationships"]:
                for relation in block["Relationships"]:
                    if rate_key in relation["Ids"]:
                        for relation in block["Relationships"]:
                            if relation["Type"] == "VALUE":
                                print (relation["Ids"])



my_key = get_rate_key()

get_rate_kv(my_key)