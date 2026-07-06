class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. Balance: {self.balance}"

    
    def __str__(self):
        return f"Account owner: {self.owner} | Balance: {self.balance}"


class SavingsAccount(Bankaccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added. New balance: {self.balance}"
        
acc = Bankaccount("Alice", 1000)
print(acc)
print(acc.deposit(500))
print(acc.withdraw(200))
print(acc.withdraw(2000))

sav = SavingsAccount("Alice", 1300, 0.1)
print(sav.add_interest())
