# Write a function is_even() that checks whether a given number is even or odd.

def is_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a number to check if it is even or odd: "))
print(f"The number {number} is {is_even(number)}")

# Write a function factorial() that calculates the factorial of a number using recursion.

# Hint: factorial(5) = 5 × 4 × 3 × 2 × 1 = 120

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# the same as this below 
# def factorial(number):
#     def factorial_recursive(n):
#         if n == 0:
#             return 1
#         return n * factorial_recursive(n - 1)
#     return factorial_recursive(number)

number = int(input("Enter a number to calculate the factorial: "))
print(f"The factorial of {number} is {factorial(number)}")

# Write a function reverse_string() that reverses a given string.

def reverse_string(string):
    return string[::-1]

string = input("Enter a string to reverse: ")
print(f"The reversed string is {reverse_string(string)}")