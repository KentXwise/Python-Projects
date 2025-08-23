# function is a block of code that performs a specific task
# it is reusable and can be called multiple times
# making programs modular and easier to maintain
# functions make programs more readable and easier to understand

# syntax
# def function_name(parameters):
#     # body of the function # this is the code that will be executed when the function is called
#     # return statement (optional) # this is the value that will be returned when the function is called
#     pass # if you don't want to write the body of the function

# example
def greet(name):
    print(f"Hello, {name}!")

greet("John")
greet("Jane")


# parameters and arguments
# parameters are the variables that are used in the function definition
# arguments are the values that are passed to the function when it is called

# default parameters
# default parameters are the parameters that are given a default value

def add(a, b):
    return a + b

num1 = 10
num2 = 20

total = add(num1, num2)
print(total)

# another samples
def greet(name, city="Level 1 Village"):
    print(f"Hello, {name}! Welcome to {city}.")


greet("John") # city is default parameter
greet("John", "Los Angeles") # city is positional argument

# keyword arguments
# keyword arguments are the arguments that are passed to the function when it is called
# they are identified by the parameter name

greet(name="John", city="Los Angeles") 
greet(city="Los Angeles", name="John") 

# another sample using function with user input
user_name = input("Enter your name to join the game: ")
greet(name=user_name)

# another sample using function for multiplying by itself of a number
def square(number):
    return number * number

total_square = int(input("Enter a number to multiply by itself: "))
print(f"The square of {total_square} is {square(total_square)}")

# another sample using function for adding two numbers
def add(a, b):
    return a + b

num1 = int(input("Enter a number to add: "))
num2 = int(input("Enter another number to add: "))
print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
