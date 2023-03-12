import bankaccount

def main():
    start_bal = float(input("Enter your starting balance: "))
    savings = bankaccount.BankAccount(start_bal)
    
    pay = float(input("How much were you paid this week."))
    print("I will deposit tha into your bankaccount")
    savings.deposit(pay)
    
    print(f"Your account balance is ${savings.get_balance():,.2f}")
    
    cash = float(input("How nmuch would you like to withdraw"))
    print("I will withdraw that from your account. ")
    savings.withdraw(cash)
    
    print(f"Your account balance is ${savings.get_balance():,.2f}")
    
if __name__ == "__main__":
    main()
    