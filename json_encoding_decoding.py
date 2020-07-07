# python json module Javascript object notation
# Why - we create an object

import json

# ENCODING from dictionary and writing to jsonfile
car_data = {"name": "tesla", "engine": "electric"}  # dictionary
print(car_data)
# printing the dictionary

print(type(car_data))
# checking the type of dictionary

# print(car_data)

car_data_json_string = json.dumps(car_data)
# json.dumps changes python dict to json str

print(type(car_data_json_string))  # json format changed the type to an string

# Let's create a jsonfile with writing permission
with open("new_json_file.json", "w") as jsonfile:
    # "enter the name of the file", permission type write 'w'

    json.dump(car_data, jsonfile)  # json.dump takes 2 args
    # the first is the dictionary, second file_type jsonfile on this occasion

with open("new_json_file.json") as jsonfile:  # Decoding
    # Reading from the file we just created
    car = json.load(jsonfile)  # storing data from file to car variable
    print(type(car)) # Checking the type of the data again
    print(car['name']) # To get the value stored in key called name
    print(car['engine']) # To get the value of second key value pair

# We have DECODED our file new_json.json that we created earlier
# We have used dumps(), dump() and load() methods