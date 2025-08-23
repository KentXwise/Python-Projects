# inheritance is a way to create a new class from an existing class
# the new class is called the child class and the existing class is called the parent class
# the child class inherits the attributes and methods of the parent class
# the child class can add new attributes and methods of its own
# the child class can override the attributes and methods of the parent class

# syntax:
# class ParentClass:
#     def __init__(self, name, age):
#     pass
# class ChildClass(ParentClass):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age)
#         self.gender = gender
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

# child = ChildClass("John", 20, "Male")
# child.display_info()

# child.display_info()

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_vehicle_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model)
        self.year = year
        self.color = color
    
    def display_car_info(self):
        self.display_vehicle_info()
        print(f"Year: {self.year}, Color: {self.color}")

my_car = Car("BMW", "X5", 2020, "Red")
my_car.display_car_info()




