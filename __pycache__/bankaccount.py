class BankAccount:
    def __init__(self,bal):
        self.__balance = bal
    
    def deposit(self,cash):
        self.__balance += cash
    
    def withdraw(self,cash):
        if self.__balance >=cash:
            self.__balance -= cash
        else:
            print("Error:Insufficient funds")
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return f"The balance is ${self.__balance:,.2f}"
    