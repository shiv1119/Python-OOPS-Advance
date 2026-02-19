import uuid
class Account:
    def __init__(self, name):
        self.__name = name
        self.__account_number = uuid.uuid4()
        self.__balance = 0

    def deposit(self, account_number, amount):
        if self.__account_number == account_number:
            if amount > 0 :
                self.__balance += amount
        else:
            raise ValueError("Deposite amout can not be null")
        
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def get_account_details(self):
        print(f"Account Holder: {self.__name}\nAccount Number: {self.__account_number}\nCurrent Balance: {self.__balance}")


shiv_account = Account("Shiv Nandan Verma")
shiv_account.get_account_details()
shiv_account.deposit(shiv_account.get_account_number(), 15000)
shiv_account.get_account_details()