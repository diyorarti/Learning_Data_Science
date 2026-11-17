
class Validator:

    @staticmethod
    def validate_not_empty(value, filed_name):
        if value is None or str(value).strip() == '':
            raise ValueError(f"{filed_name} can't be empty")

class Product:
    def __init__(self, name, price, stock):
        self.__name = None
        self.__price = None
        self.__stock = None

        self.name = name
        self.price = price
        self.stock = stock

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_not_empty(value, "name")
        self.__name = value

    
