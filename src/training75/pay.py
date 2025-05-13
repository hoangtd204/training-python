from Interfaces.abstract import PaymentMethod



class PaymentByCardCredit(PaymentMethod):
    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        print(f"Payment by card credit: {self.amount}")



amount1=PaymentByCardCredit(100)
amount1.pay()