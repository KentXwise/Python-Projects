# a list is an ordered and mutable (changable after creation) collection of items
# unlike tuples, lists are defined using square brackets []

# syntax
#list_name = ["item1", "item2", "item3"]

sample_list = [1, 2, 3, "red", "blue", "green"]
print(sample_list)

# accessing items in a list
# index starts from 0

print(sample_list[4]) # blue

# Append method
# adds a new item to the end of the list

sample_list.append("yellow")
print(sample_list)

# Remove method
sample_list.remove("red")
print(sample_list)

# Retrieve Method
print(sample_list[1:4]) # [2, 3, "blue"]

# Replace Method
# replaces the item at the specified index with the new item

sample_list[0] = "black"
print(sample_list)

# Insert Method
# adds a new item at the specified index

sample_list.insert(0, "white")
print(sample_list)
