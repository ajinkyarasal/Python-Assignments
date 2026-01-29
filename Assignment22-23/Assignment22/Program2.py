# #Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)Amount (Account balance)
# The class should contain one class variable:ROI (Rate of Interest), initialized to 10.5
# Define a constructor (_init_ that accepts Name and initial Amount.
# Implement the following instance methods:Display () - displays account holder name and current balance
# Deposit () - accepts an amount from the user and adds it to balance
# Withdraw() - accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest () - calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:

    ROI = 10.5

    def __init__(self,Name,InitialAmount):
        self.Name = Name
        self.Amount = InitialAmount
    
    def Display(self):
        print(f"Account holder {self.Name} current balance is : {self.Amount}")
    
    def Deposit(self,DepositAmount):
        self.Amount += DepositAmount
        print(f"{DepositAmount} deposited successfully.")
        self.Display()

    def Withdraw(self,WithdrawAmount):
        if WithdrawAmount <= self.Amount:
            self.Amount -= WithdrawAmount
            print(f"{WithdrawAmount} debited successfully.")
            self.Display()
        else:
            print("Unable to withdraw. Insufficient Balance.")
    
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
obj1 = BankAccount("John",10000)
obj1.Display()
obj1.Deposit(100)
obj1.Withdraw(200)
obj1.Withdraw(20000)
print("="*80)
obj2 = BankAccount("Jason",20000)
obj2.Display()
obj2.Deposit(1000)
obj2.Withdraw(2000)
obj2.Withdraw(20000)


