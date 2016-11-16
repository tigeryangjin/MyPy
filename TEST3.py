import json
from pprint import pprint

with open('E:\Downloads\hangout.json', 'r', encoding="utf8") as f:
    data = json.load(f)

pprint(data)
