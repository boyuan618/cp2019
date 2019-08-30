class BankAccount:
    
    def __init__(self, actno, balance):
        self.actno = actno
        self.balance = balance
        
    def deposit(self, amt):
        self.balance += amt
        return self.balance
            
    def withdraw(self, amt):
        self.balance -= amt
        return self.balance
    
    def calc_interest(self, year, amt):
        self.balance = int(amt*((1+0.02)**year))
        return self.balance
    
            
    def display(self, actno, balance):
        print(self.actno)
        print(self.balance) 
            