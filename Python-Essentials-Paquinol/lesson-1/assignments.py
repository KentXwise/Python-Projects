# age calculator by asking the user's birth year
current_year = 2025
user_birth_year = int(input("Enter your birth year: "))
age = current_year - user_birth_year

print(f"You are {age} years old in {current_year}")

# custom greeting message
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")

print(f"Hello, {user_first_name} {user_last_name}!\nWelcome to the world of Python!")


# distance converter by asking the user's distance in kilometers (as float).
# convert it using the following formula: 1 miles = 0.621371 kilometers

user_distance_in_kilometers = float(input("Enter your distance in kilometers: "))
user_distance_in_miles = user_distance_in_kilometers * 0.621371
print(f"Your distance in miles is {user_distance_in_miles}")