import json

with open('data.json', encoding='utf-8') as json_file:
    data_from_json = json.load(json_file)

print(data_from_json)