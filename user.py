class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)


mark = User('Mark Enders')
lacey = User('Lacey McAllister')
thomas = User('Thomas Enders')

mark.make_deposit(100)
mark.make_deposit(500)
mark.make_deposit(200)
mark.display_user_balance()

lacey.make_deposit(800)
lacey.make_deposit(500)
lacey.make_withdrawl(200)
lacey.make_withdrawl(400)
lacey.display_user_balance()

thomas.make_deposit(3000)
thomas.make_withdrawl(1000)
thomas.make_withdrawl(500)
thomas.make_withdrawl(100)
thomas.display_user_balance()
