# sets are unordered and mutable (changable after creation) collection of unique items
# the elements must be immutable types
# sets can't have duplicate items

# syntax
# set_name = {item1, item2, item3}

sample_set = {1, 2, 3, 4, 5}
print(sample_set)

# adding items to a set
sample_set.add(6)
print(sample_set)

# removing items from a set
sample_set.remove(1)
print(sample_set)

# removing all items from a set
sample_set.clear()

# union, intersection, and difference

# union
sample_set_union1 = {1, 2, 3}
sample_set_union2 = {3, 4, 5}

new_set_union = sample_set_union1 | sample_set_union2 # "|" is the union operator
print(new_set_union) # {1, 2, 3, 4, 5}

# intersection
sample_set_intersection = sample_set_union1 & sample_set_union2 # "&" is the intersection operator
print(sample_set_intersection) # {3}

# difference
sample_set_difference1 = sample_set_union1 - sample_set_union2 # "-" is the difference operator
sample_set_difference2 = sample_set_union2 - sample_set_union1 # "-" is the difference operator
print(sample_set_difference1) # {1, 2}
print(sample_set_difference2) # {4, 5}

# symmetric difference
sample_set_symmetric_difference = sample_set_union1 ^ sample_set_union2 # "^" is the symmetric difference operator
print(sample_set_symmetric_difference) # {1, 2, 4, 5}