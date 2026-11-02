from abc import ABC, abstractmethod

class PaymentGateway(ABC) :
    @abstractmethod
    def process_payment(self, amount) :
        pass

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processed credit card payment of {amount} INR")

class PPPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processed PP Payment of {amount} INR")

credit_card = CreditCardPayment()
pp = PPPayment()

print("Payment started ...")
credit_card.process_payment(100)

print("\nPayment started ...")
pp.process_payment(50)