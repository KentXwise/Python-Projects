# Write a program that takes a list of numbers and finds the maximum and minimum values.
# numbers = [10, 25, 8, 99, 3, 67]
# Hint: Use in-built functions min() and max()

my_list = [10, 25, 8, 99, 3, 67]
print(min(my_list))
print(max(my_list))


# Create a dictionary with some student names and their scores. Then, add a new student and
# remove an existing student.
# students = {"Alice": 85, "Bob": 78, "Charlie": 92}
# Hint: Use dictionary methods like .get(), .update(), and .pop()

my_dictionary = {"Alice": 85, "Bob": 78, "Charlie": 92}
my_dictionary["David"] = 88
my_dictionary.pop("Bob")
print(my_dictionary)

# Write a program that counts how many times a specific number appears in a tuple.
# numbers = (2, 5, 3, 5, 8, 5, 10)
# Hint: Use the count() method of tuples

my_tuple = (2, 5, 3, 5, 8, 5, 10)
print(my_tuple.count(5))

# Given two sets of numbers, find:
# 1. Union (all unique elements from both sets)
# 2. Intersection (common elements)
# 3. Difference (elements in the first set but not in the second)
# Hint: Use the union(), intersection(), and difference() methods of sets

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}

union_set = my_set1 | my_set2
print(union_set)

intersection_set = my_set1 & my_set2
print(intersection_set)

difference_set1 = my_set1 - my_set2
difference_set2 = my_set2 - my_set1 # I want to see the difference between the two sets that's why I added this line
print(difference_set1)
print(difference_set2) # just for reference