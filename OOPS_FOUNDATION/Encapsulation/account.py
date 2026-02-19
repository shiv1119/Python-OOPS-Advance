class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   # private variables 

    @property # This will create read only variables
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

# Usage
acc = BankAccount("12345", 5000)
acc.deposit(2000)
acc.withdraw(1000)
print(acc.balance)  # 6000

# Direct modification blocked
#acc.__balance = 100000  # Does not change actual balance
print(acc.balance) # 6000