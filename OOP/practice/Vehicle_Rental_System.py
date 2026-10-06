from abc import ABC, abstractmethod

class Validator:

    @staticmethod
    def validate_not_empty(value, field_name):
        if value is None or str(value).strip() == '':
            raise ValueError(f"{field_name} can't be empty")

    @staticmethod
    def validate_positive_number(value, field_name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number")
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than 0")

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

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.validate_not_empty(value, 'brand')
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.validate_not_empty(value, "model")
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validator.validate_positive_number(value, 'year')
        self.__year = self.year

    @property
    def daily_price(self):
        return self.__daily_price

    @daily_price.setter
    def daily_price(self, value):
        Validator.validate_positive_number(value, 'daily_price')
        self.__daily_price = value

    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self, value):
        if type(value) is not bool:
            raise ValueError("is_availabe must be True or False")
        self.__is_available = value

    def get_vehicle_info(self):
        return f"Brad: {self.brand} |Model: {self.model} |Year {self.year} |Daily Price: {self.daily_price} |Available: {self.is_available}"

    def rent(self):
        return f"{self.model} is renking"

    def return_vehicle(self):
        return f"{self.model} is returning"

    @abstractmethod
    def calculate_rental_cost(self, days):
        return self.daily_price * days


class Car(Vehicle):
    def __init__(self, brand, model, year, daily_price, is_available, number_of_doors):
        super().__init__( brand, model, year, daily_price, is_available)
        self.__number_of_doors = None
        self.number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        Validator.validate_positive_number(value, 'number_of_doors')
        self.__number_of_doors = value

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)

    def get_vehicle_type(self):
        return "Car"


car = Car('BMW', 'X7', 2024, 100, False, 4)
print(car.get_vehicle_info())
print(car.get_vehicle_type())
print(car.calculate_rental_cost(10))