import json
from pprint import pprint

with open('E:\Downloads\hangout.json', 'r', encoding="utf8") as f:
    data = json.load(f)

print('data:', type(data))

for i in data:
    print(type(i))

for i in data['conversation_state']:
    print(type(i))

print(data['conversation_state'][0]['response_header'])
print(data['conversation_state'][1])
print(data['conversation_state'][2])
