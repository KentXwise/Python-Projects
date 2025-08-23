# classes are blueprints for creating objects
# class key word is used to create a class

class Car:

    location = "USA"
    
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
    
    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}")
    

bmw = Car("BMW", 2020, "Red")
ferrari = Car("Ferrari", 2021, "Yellow")
bmw.display_info()
ferrari.display_info()

bmw.seats = 4

ferrari.seats = 2
ferrari.speed = 300

print(f"BMW has {bmw.seats} seats")
print(f"Ferrari has {ferrari.seats} seats and its speed is {ferrari.speed}")

print(f"The location of the cars is {bmw.location}")
print(f"The location of the cars is {ferrari.location}")




