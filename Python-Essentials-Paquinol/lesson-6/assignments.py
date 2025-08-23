# Write a Python program that takes two numbers as input and divides the first number by the second.
# Handle the ZeroDivisionError if the second number is zero.
# hint: use try except block

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# Write a program that takes two numbers as input and performs division.
# Handle both ZeroDivisionError and ValueError.
# hint: use try except block

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")

# Write a program that asks the user to enter a number and prints a confirmation message,
# irrespective of an exception occurs or not, using finally.
# hint: use try except finally block

try:
    num = int(input("Enter a number: "))
    print("You entered: ", num)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("This will always execute, even if an exception is raised")