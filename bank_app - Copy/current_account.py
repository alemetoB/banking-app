

from accounts import Account

class CurrentAccount(Account):
    def __init__(self, initial_balance=50000):
        super().__init__()  
        self.balance = initial_balance 

currents = CurrentAccount(50000)
currents.deposit(0)  
currents.withdraw(0)  
