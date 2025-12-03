import json

data = {
    "name": "Alice",
    "age": 30,
    "cities": ["New York", "London"]
    }

with open('my_data.json', 'w') as file:
    json.dump(data, file, indent=4) # indent for pretty printing
print (data,{})
inm = input("enter a thing: ")
if inm == "":
    data = {
    "name": "Alice",
    "age": 30,
    "cities": ["New York", "London"],
    inm:30 # type: ignore
    }

