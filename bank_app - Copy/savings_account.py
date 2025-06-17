

from accounts import Account

class SavingsAccount(Account):  
    def __init__(self, initial_balance=50000):
        super().__init__()  
        self.balance = initial_balance  
        self.withdrawal_limit = 10000

    def savingsWithdraw(self, amount):
        if amount > self.withdrawal_limit:
            return "Withdrawal amount exceeds the limit."
        if amount > self.balance:
            return "Insufficient balance."
        
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"


savings = SavingsAccount(50000)
savings.savingsWithdraw(10001)
savings.deposit(0)          
