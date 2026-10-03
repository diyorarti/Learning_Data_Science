"""
Encapsulation means hiding internal data inside a class and controlling access to it through methods or properties

    1.public attributes
    2.protected attributes  _ sinlge under score, mainly used with inheritances
    3.private attributes    __ double under scores

    getter/setter
"""

class Product:
    def __init__(self, name, price, quantity):
        self.__name = None
        self.__price = None
        self.__quantity = None

        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("name can't be empty")
        self.__name = name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("price must be greater than 0")
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise ValueError("quantity can't be negative ")
        self.__quantity = quantity

    def increase_quantity(self, amount):
        if amount > 0:
            self.quantity += amount
        else:
            raise ValueError('invalid amount')

    def decrease_quantity(self, amount):
        if amount > 0 and self.quantity >= amount:
            self.quantity -= amount
        else:
            raise ValueError("invalid amount") 
    
    def get_total_value(self):
        return self.quantity * self.price
    
    def get_info(self):
        return f"Product: {self.name} | Price: {self.price} | Quantity: {self.quantity} | Total Value: {self.get_total_value()}"
    

# product1 = Product("Laptop", 1200, 5)

# product1.increase_quantity(3)
# product1.decrease_quantity(2)

# print(product1.get_info())

