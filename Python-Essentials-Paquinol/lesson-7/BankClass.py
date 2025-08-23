class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._transaction_limit = 5000
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0 and amount <= self._transaction_limit:
            self.__balance += amount
            print(f"Deposited {amount} to {self.owner}'s account.")
        else:
            print(f"Failed to deposit {amount} transaction limit exceeded. Maximum deposit is {self._transaction_limit}.")
    
    def withdraw(self, amount):
        if amount <= self.__balance and amount <= self._transaction_limit:
            self.__balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account.")
        else:
            print(f"Failed to withdraw {amount} you don't have enough money or transaction limit exceeded. Maximum withdraw is {self._transaction_limit}.")
        
    def display_balance(self):
        return (f"{self.owner}'s balance is {self.__balance}") # safely get the balance

Kenneth = BankAccount("Kenneth", 1000)
Kenneth.deposit(1000)
Kenneth.withdraw(500)
Kenneth.display_balance()

Kent = BankAccount("Kent", 1000)
Kent.deposit(6000)
Kent.withdraw(9000)
Kent.display_balance()

name = input("Enter your name: ")
Student = BankAccount(name)
Student_deposit = int(input("Enter the amount you want to deposit: "))
Student.deposit(Student_deposit)
Student.display_balance()





