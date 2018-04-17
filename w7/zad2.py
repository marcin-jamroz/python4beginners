import random

class BankAccount:
    
    def __init__(self):
        self.balance = 0
    
    def get_balance(self):
        return self.balance

    def deposit(self, money, with_promo=False):
        p = random.random()
        if p < 0.1 and with_promo is True:
            self.balance += 1
        self.balance += money