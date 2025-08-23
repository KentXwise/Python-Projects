# dictionaries are unordered and mutable (changable after creation) collection of key-value pairs

# syntax
# dictionary_name = {key1: value1, key2: value2, key3: value3}

sample_dictionary = {"name": "John", "age": 20, "city": "New York"}
print(sample_dictionary)

# accessing items in a dictionary using the keys
print(sample_dictionary["name"]) # John

# adding new items to a dictionary
sample_dictionary["gender"] = "male"
print(sample_dictionary)

# removing items from a dictionary
del sample_dictionary["age"]
print(sample_dictionary)

# replace items in a dictionary
sample_dictionary["name"] = "Jane"
print(sample_dictionary)