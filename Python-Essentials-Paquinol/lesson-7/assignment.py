#Create a class called BankAccount.
# It should have:

# A private attribute balance (start with 0).

# A method deposit(amount) to add money.

# A method withdraw(amount) to subtract money (only if enough balance).

# A method get_balance() to return the current balance.

# Hints: Use self.__balance to make balance private (Encapsulation).

# Create an object of BankAccount, deposit 100, withdraw 40, and print the balance.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.owner}'s account.")
        else:
            print(f"Failed to deposit {amount}.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account.")
        else:
            print(f"Failed to withdraw {amount}.")

    def get_balance(self):
        return self.__balance

account = BankAccount("John")
account.deposit(100)
account.withdraw(40)
print(account.get_balance())
