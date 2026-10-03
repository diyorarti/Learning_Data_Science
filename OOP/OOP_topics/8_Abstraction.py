"""
Abtraction means hiding unnecerrary details and showing only important features of an obhject 
    ABC stands for Abstract Base Class

    It is a blueprint for creating class
    Child class inherited from Abstract class must implement abstract methods

"""
from abc import ABC, abstractmethod


class Validator:
    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

    @staticmethod
    def validate_currency(currency):
        if currency == "":
            raise ValueError("Currency cannot be empty")


class Payment(ABC):
    def __init__(self, amount, currency):
        self._amount = None
        self._currency = None

        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        Validator.validate_amount(amount)
        self._amount = amount

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        Validator.validate_currency(currency)
        self._currency = currency

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def refund_payment(self):
        pass

    def get_payment_info(self):
        return f"Amount: {self.amount} | Currency: {self.currency}"


class CreditCardPayment(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def process_payment(self):
        return f"Processing credit card payment of {self.amount} {self.currency}"

    def refund_payment(self):
        return f"Refunding credit card payment of {self.amount} {self.currency}"


class PayPalPayment(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def process_payment(self):
        return f"Processing PayPal payment of {self.amount} {self.currency}"

    def refund_payment(self):
        return f"Refunding PayPal payment of {self.amount} {self.currency}"


class CryptoPayment(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def process_payment(self):
        return f"Processing crypto payment of {self.amount} {self.currency}"

    def refund_payment(self):
        return f"Refunding crypto payment of {self.amount} {self.currency}"


payment1 = CreditCardPayment(100, "USD")
payment2 = PayPalPayment(200, "EUR")
payment3 = CryptoPayment(300, "BTC")

print(payment1.get_payment_info())
print(payment1.process_payment())
print(payment1.refund_payment())

print(payment2.process_payment())
print(payment3.process_payment())