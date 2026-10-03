from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year, daily_price, is_available):
        self.__brand = None
        self.__model = None
        self.__year = None
        self.__daily_price = None
        self.__is_available = None

        self.brand = brand
        self.model = model
        self.year = year
        self.daily_price = daily_price
        self.is_available = is_available

    