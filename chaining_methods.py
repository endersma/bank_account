class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self


mark = User('Mark Enders')
lacey = User('Lacey McAllister')
thomas = User('Thomas Enders')

mark.make_deposit(100).make_deposit(500).make_deposit(200).display_user_balance()

lacey.make_deposit(800).make_deposit(500).make_withdrawl(200).make_withdrawl(400).display_user_balance()

thomas.make_deposit(3000).make_withdrawl(1000).make_withdrawl(500).make_withdrawl(100).display_user_balance()
