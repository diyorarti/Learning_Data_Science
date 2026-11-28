
class Validator:

    @staticmethod
    def validate_not_empty(value, filed_name):
        if value is None or str(value).strip() == '':
            raise ValueError(f"{filed_name} can't be empty")

    @staticmethod
    def validate_positive_number(value, field_name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number")
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than 0")

    @staticmethod
    def validate_instance(obj, class_type, field_name):
        if not isinstance(obj, class_type):
            raise TypeError(f"{field_name} must be an instance of {class_type.__name__}")

        
class Product:
    def __init__(self, product_id:str, name:str, price:float, stock:int):
        self.__product_id = None
        self.__name = None
        self.__price = None
        self.__stock = None

        product_id = product_id
        self.name = name

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        Validator.validate_not_empty(value, "product_id")
        self.__product_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_not_empty(value, "name")
        self.__name = value

    def update_price(self, new_price):
        Validator.validate_positive_number(new_price, "price")
        self.__price = new_price

    def increase_stock(self, quantity):
        self.__stock += quantity

    def decrease_stock(self, quantity):
        if self.__stock < quantity:
            return ValueError("not enough stcok")
        self.__stock -= quantity

class CardIten:
    def __init__(self, product, quantity):
        self.__product = None
        self.__quantity = None

        self.product = product
        self.quantity = quantity

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        Validator.validate_instance(product, Product, "product")
        self.__product = product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        Validator.validate_positive_number(quantity, "quantity")
        self.__quantity = quantity

    


