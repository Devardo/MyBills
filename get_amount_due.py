import json
from full_response import response
from parser import map_line_id

due_synonyms = ["rate", 'amount due', "total due"]


def get_amount_due():
    with open('output.json', 'r') as key_values:
        data = json.load(key_values)

    keys = data.keys()

    for key in keys:
        if key.lower() in due_synonyms:
            amount_due = data[key]
            return amount_due
       

    
amount_due = get_amount_due()
print(amount_due)

