class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def Deposit(self,a):
        self.balance=self.balance+a
    def Withdraw(self,a):
        self.balance=self.balance-a
    def bankFees(self):
        self.balance=self.balance-((5/100)*self.balance)
    def display(self):
        print("Account number:",self.accountNumber)
        print("Name:",self.name)
        print("Balance:",self.balance,"$")

newAccount=BankAccount(123,"me",2)
newAccount.Withdraw(2)
newAccount.Deposit(3)
newAccount.display()