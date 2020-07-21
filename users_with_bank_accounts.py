class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = .05
        self.balance = 0

class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.account = BankAccount(int_rate=0.02, balance=0)

    def deposit(self, amount):
        self.account.balance += amount
        return self
    def withdraw(self, amount):
        if self.account.balance <= 0:
            fee = 5
            self.account.balance -= fee
            print("Insufficient Funds: Charging a $5 fee")
        else:
    	    self.account.balance -= amount
        return self
    def display_account_info(self):
        print(f"Name: {self.name} Balance: ${self.account.balance}")
        return self
    def yield_interest(self):
        int_amt = 0
        if self.account.balance > 0:
            int_amt = self.account.balance * self.account.int_rate
            self.account.balance += int_amt
        return self

mark = User('Mark Enders','endersma@gmail.com', '555 NW St')
lacey = User('Lacey McAllister', 'mcallister.lacey@gmail.com', '555 NW St')


mark.deposit(5000).deposit(2000).deposit(4000).withdraw(3000).yield_interest().display_account_info()
lacey.deposit(10000).deposit(12000).withdraw(22000).withdraw(2000).withdraw(1000).withdraw(5000).yield_interest().display_account_info()