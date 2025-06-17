class Account:
    def __init__(self,):
        self.balance=0
    
    def withdraw(self,amount):
        if amount>self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        
    def deposit(self,amount):
        self.balance += amount 
        return f"Deposited {amount}. New balance: {self.balance}"
