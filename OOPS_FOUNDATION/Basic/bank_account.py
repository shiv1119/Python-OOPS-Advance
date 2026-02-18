class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.__balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposite amount should be positive")
        self.__balance  += amount

    def withdraw(self, amount):
        if amount < 1:
            raise ValueError("Withdraw amount can not be negative")
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Account balance low")
    
    def get_balance(self):
        return f"Your current account balance is {self.__balance}"
    
    def __repr__(self):
        return f"BankAccount(account_number='{self.account_number}', balance='{self.__balance}')"
    

account1 = BankAccount("1001AC")
print(account1) #BankAccount(account_number='1001AC', balance='0')
account1.deposit(15000)
print(account1) #BankAccount(account_number='1001AC', balance='15000')

account1.withdraw(1000)
print(account1.get_balance()) #Your current account balance is 14000

#print(account1.__balance) #AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?

print(account1._BankAccount__balance) #NameError: name '_BankAccount__balance' is not defined
