class BankAccount:
    def __init__(self, name, acct_num, int_rate, balance): 
        self.name = name
        self.acct_num = acct_num
        self.int_rate = .05
        self.account_balance = 0 
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance <= 0:
            fee = 5
            self.account_balance -= fee
            print("Insufficient Funds: Charging a $5 fee")
        else:
    	    self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f"Account: {self.acct_num}, Balance: ${self.account_balance}")
        return self
    def yield_interest(self):
        int_amt = 0
        if self.account_balance > 0:
            int_amt = self.account_balance * self.int_rate
            self.account_balance += int_amt
        return self

mark = BankAccount('Mark Enders', 1234, .05, 0)
lacey = BankAccount('Lacey', 4567, .05, 0)

mark.deposit(5000).deposit(2000).deposit(4000).withdraw(3000).yield_interest().display_account_info()
lacey.deposit(10000).deposit(12000).withdraw(22000).withdraw(2000).withdraw(1000).withdraw(5000).yield_interest().display_account_info()