# polymorphism is a way to create a new class from an existing class
# polymorphism is the ability to take many forms
# polymorphism allows us to use the same interface for different data types
# polymorphism allows different classes to use the same method name

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model)
        self.year = year
        self.color = color
    
    def show_info(self):
        super().show_info()
        print(f"Year: {self.year}, Color: {self.color}")


vehicle = Vehicle("BMW", "X5")
car = Car("Toyota", "Camry", 2020, "Red")
vehicle.show_info()
car.show_info()






