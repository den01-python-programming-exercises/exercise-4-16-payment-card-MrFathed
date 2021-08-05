class PaymentCard:
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def __str__(self):
        return "The card has a balance of {} pounds.".format(self.balance)

    def eat_affordably(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_heartily(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def add_money(self, amount):
        if amount >= 0:
            self.balance += amount
            if self.balance > 150.0:
                self.balance = 150.0