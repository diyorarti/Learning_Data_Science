from abc import ABC, abstractmethod
from Validator import Validator


class Payment:
    def __init__(self, amount, currency):
        self.__amount = None
        self.__currency = None

        self.amount = amount
        self.currency = currency
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        Validator.validate_positive_number(amount, "amount")
        self.__amount = amount

    @property
    def currency(self):
        return self.__currency
    
    @currency.setter
    def currency(self, currency):
        Validator.validate_not_empty(currency, "currency")
        self.__currency = currency

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def refund_patment(self):
        pass

    def get_payment_info(self):
        return f"Payment Amount: {self.amount} | Currency: {self.currency}"
    
    