# tuples is an ordered and immutable (unchangable after creation) collection of items
# unlike lists, tuples are defined using parentheses
# tuple is useful for storing a fixed size of items

# syntax 
# tuple_name = ("items1", "items2", "items3")

sample_tuple = (1, 2, 3)
print(sample_tuple)

# accessing items in a tuple
# index starts from 0
print(sample_tuple[0]) # 1

# concatenation of tuples
sample_tuple_2 = (4, 5, 6)
new_tuple = sample_tuple + sample_tuple_2
print(new_tuple)