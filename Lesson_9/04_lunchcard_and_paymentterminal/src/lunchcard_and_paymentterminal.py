# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):

        if self.balance > amount:
             self.balance -= amount
             return True
        else:
             return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch_cost = 2.50
        if payment >= lunch_cost:
            self.funds += lunch_cost
            self.lunches += 1
            return payment - lunch_cost
        else:
            return payment

    def eat_special(self, payment: float):
        special_cost = 4.30
        if payment >= special_cost:
            self.funds += special_cost
            self.specials += 1
            return payment - special_cost
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch_lunchcard_price = 2.50
   
        if card.subtract_from_balance(lunch_lunchcard_price):
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        special_lunchcard_price = 4.30
        
        if card.subtract_from_balance(special_lunchcard_price):
            self.specials += 1
            return True
        else:
            return False
    
    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        self.funds += card.balance

if __name__ == "__main__":
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    change = exactum.eat_lunch(5)
    print("The change returned was", change)

    # change = exactum.eat_special(4.3)
    # print("The change returned was", change)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    # print("Special lunches sold:", exactum.specials)

    exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)