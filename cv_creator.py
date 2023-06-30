import json

with open('data.json', encoding='utf-8') as json_file:
    json_dict = json.load(json_file)

print(json_dict)