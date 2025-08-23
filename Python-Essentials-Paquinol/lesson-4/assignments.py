# write a program that asks the user to enter a number between 1 and 10
# if the number is less than 1 or greater than 10, print "Invalid number
# if the number is between 1 and 10, print "Valid number"

user_number = int(input("Enter a number between 1 and 10: "))
if user_number < 1 or user_number > 10:
    print("Invalid number")
else:
    print("Valid number")


# koan ikaw na bahala unsay trip nimo buhaton diri
# pero dapat naay if, elif, else statement