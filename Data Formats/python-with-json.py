import json

# Load JSON file into a variable called "data"
with open("Example1.json") as f:
    data = f.read()

# json_dict is a dictionary, and json.loads takes care of
# placing our JSON data into it.
json_dict = json.loads(data)


# Print the whole json dictionary
print(json_dict)

for k, v in json_dict.items():
    print("-- The key '{0}' has value of '{1}'.".format(str(k), str(v)))
