# exceptions are errors that occur during the execution of a program
# they are caused by the user or the programmer
# they are handled using try, except, finally blocks

# common cases of exceptions

# invalid operations
# ex: dividing by zero ( 10 / 0 ) - ZeroDivisionError

# incorrect data types
# ex: trying to add a number to a string ( "10" + 20 ) - TypeError

# accessing non-existent elements
# ex: indexing beyond the length of a list (my_list[100] ) when my_list has only 5 elements - IndexError

# file handling errors
# ex: trying to open a file that doesn't exist ( open("nonexistent.txt") ) - FileNotFoundError


# num = 10
# print("Dividing numbers...")
# result = num / 0
# print("result: ", result)

# try except block
# syntax
# try:
#     # code that may raise an exception
# except Exception as e:
#     # code to handle the exception

# try:
#     num = 10
#     print("Dividing numbers...")
#     result = num / 0
#     print("result: ", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")


# else block

# num = int(input("Enter a number: "))
# print("You entered: ", num)


# try: 
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# else:
#     print("No exceptions were raised.")

# finally block


try:
    num = 10
    print("Dividing numbers...")
    result = num / 0
    print("result: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
finally:
    print("This will always execute, even if an exception is raised")