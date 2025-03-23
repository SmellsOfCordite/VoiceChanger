import json
 
def read_JSON(filepath):
    print("Reading from JSON ", str(filepath))
    with open(filepath, 'r') as openfile:
        # Reading from json file
        data = json.load(openfile)
        return data
 

def write_JSON(filepath, data):
    print("Writing (Prettily) to JSON ", str(filepath))
    with open(filepath, mode="w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent = 2)

filepath = "Effect_Sets.json"
data = ""
data = read_JSON(filepath)
write_JSON(filepath,data)

print(data)