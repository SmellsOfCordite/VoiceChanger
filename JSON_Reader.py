import json
 
# Opening JSON file
with open('Effect_Sets.json', 'r') as openfile:
 
    # Reading from json file
    effects = json.load(openfile)
 
print(effects)
print(type(effects))

with open("Effect_Sets.json", mode="w", encoding="utf-8") as write_file:
    json.dump(effects, write_file, indent = 2)
