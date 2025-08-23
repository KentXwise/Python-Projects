class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def bite(self):
        print(f"{self.name} bites someone!")

Kenneth = Dog("Kenneth", 1)
Kent = Dog("Kent", 2)

Kenneth.bark()
Kent.bite()

if Kenneth.age <= 1:
    Kenneth.birthday()
else:
    print("Kenneth is not a puppy!")