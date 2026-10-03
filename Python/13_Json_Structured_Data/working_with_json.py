# Converting dict -> JSON 

# data = {'name': "Ali", "age":30}
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

# # converting JSON -> Dict 
# json_data = json.loads(json_str)
# print(type(json_data))


import json
with open("Python/13_Json_Structured_Data/data.json", "r") as f:
    data = json.load(f)

print(data)

data_adding = {
    "users": [
        {"name": "Emma", "score": 88},
        {"name": "Liam", "score": 92},
        {"name": "Olivia", "score": 95}
    ]
}
with open("Python/13_Json_Structured_Data/data.json", "w") as f:
    json.dump(data_adding, f)

with open("Python/13_Json_Structured_Data/data.json", "r") as f:
    data = json.load(f)
print(data)