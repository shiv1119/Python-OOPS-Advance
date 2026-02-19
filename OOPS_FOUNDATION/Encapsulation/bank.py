class BankAccount:

    bank_name = "Punjab National Bank"

    def __init__(self, account_number, owner, balance):
        self.__account_number = account_number
        self.owner = owner
        self.__balance = balance
        self.__password = None
        self.__secret_key = "JS1110"

    #read only property to get account number - getter
    @property
    def account_number(self):
        return self.__account_number
    
    #read only property for balance - getter
    @property
    def balance(self):
        return self.__balance
    
    # deposit method that will deposit an amount to a account
    def deposite(self, amount):
        if amount <= 0:
            raise ValueError("Deposite must be positive")
        self.__balance += amount

    #withdraw method
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient Balance")
        self.__balance -= amount

    @property
    def password(self):
        raise AttributeError("Password is write-only")
    
    @password.setter
    def password(self, pwd):
        if len(pwd) < 8:
            raise ValueError("Password must be at least 8 characters")
        self.__password = pwd

    # Factory method to create the object in flashy style
    @classmethod
    def from_dict(cls, data):
        return cls(data['account_number'], data['owner'], data['balance'])

    # Funstion to revel secret of the owner
    def reveal_secret(self):
        return self.__secret_key
    

# Using Factory method
data = {"account_number": "12345", "owner": "Shiv", "balance": 5000}
acc = BankAccount.from_dict(data)
acc.deposite(2000)
acc.withdraw(1000)

print(acc.balance) # 6000

# print(acc.account_number) # Attribute error as account number is read only
acc.password = "Secure@1234"
# print(acc.password)  # AttributeError: Password is write-only
print(acc.owner)