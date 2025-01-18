class BankAccount:
    def __init__(self,account_balance, balance = 0):
        self.account_balance = account_balance
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: {self.account_balance}"
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False     
        else:
            return False    
        
    def display_balance(self):
        return f"Current Balance: {self.account_balance}"
        
