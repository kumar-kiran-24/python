class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount

    def get_balance(self):
        return self.balance
    
accont=BankAccount(10000)
accont.deposite(500)
print(accont.get_balance())

        