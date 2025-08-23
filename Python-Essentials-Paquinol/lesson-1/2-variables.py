name = "John"
age = 20
height = 5.9
is_student = True

print(f"Name: {name},\n Age: {age},\n Height: {height},\n Is Student: {is_student}")
# \n is used to print the variables in a new line

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

a = b = c = 10
print(a, b, c)

name, age, height, is_student = "John", 20, 5.9, True
print(name, age, height, is_student)

a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b) #swapping the values of a and b

