# Example 1: Python JSON to dict
#
# import json
#
# person = '{"name": "Bob", "languages": ["English", "Fench"]}'
# person_dict = json.loads(person)
# print(person_dict['languages'])

# Example 2: Python read JSON file
# import json
#
# # Load JSON file into a variable called "data"
# with open("Example1.json") as f:
#     data = f.read()
#
# # json_dict is a dictionary, and json.loads takes care of placing our JSON data into it.
# json_dict = json.loads(data)
#
# # Print the whole json dictionary
# print(json_dict, '\n')
#
# for k, v in json_dict.items():
#     print("-- The key '{0}' has value of '{1}'.".format(str(k), str(v)))

# Example 3: Python pretty print JSON
# import json
#
# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
#
# # Getting dictionary
# person_dict = json.loads(person_string)
#
# # Pretty Printing JSON string back
# print(json.dumps(person_dict, indent=4, sort_keys=True))
