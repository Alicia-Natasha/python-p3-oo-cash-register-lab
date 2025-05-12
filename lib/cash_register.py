#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

          
    def add_item(self, title, price, quantity=1):
        '''accepts a title and a price and increases the total.'''
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        '''applies the discount to the total price.'''
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= int(discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
        
    def void_last_transaction(self):
        '''subtracts the last item from the total.'''
        if self.last_transaction_amount:
            self.total -= self.last_transaction_amount
            self.last_transaction_amount = 0
        
    