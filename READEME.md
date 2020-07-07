# What is json? Javascript Object Notation
## Syntax - json is syntax for exchanging data
### where and how? - between a browser and server 

- Json is also used to parse the data from existing files or web browser 
- The data can only be text - hence json is text written in json format
``` bash
- Data types:
a string
a number
an object (json object)
an array
a boolean
null
```
- Where does this syntax derived from javascript?
- Data is in name/value pairs:
``` bash
{"name": "james", "age": "18"}
- data is separated by ,
```

```python
import json

# ENCODING/WRITING from dictionary and writing to jsonfile
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

# We have DECODED/READING our file new_json.json that we created earlier
# We have used dumps(), dump() and load() methods
```