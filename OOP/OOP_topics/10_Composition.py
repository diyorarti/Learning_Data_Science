"""
Composition -> Building one class by using objects of other classes.
               Object has another object inside it. THis is "Has a" relationship

            Composition helps to build complex systems by connecting smaller classes together.
            Instead of putting e everythin inside one big class, Divide the system into small classes:
                Car:
                    ├── Engine
                    ├── Wheel
                    ├── Battery
                    └── GPS
        Composition - "Has a" relationship 
            Car has an Engine, 
        Inheritance - "Is a" relationship
            Dog is an Animal
"""
class Battery:
    def charge(self):
        return "Battery is chargin"
    
class Screen:
    def display(self):
        return "Screen is displaying content"

class Laptop:
    def __init__(self):
        self.battery = Battery() # Composition
        self.screeen = Screen() # Composition

    def use_laptop(self):
        return f"{self.battery.charge()} and {self.screeen.display()}"
    
# laptop = Laptop()
# print(laptop.use_laptop())

class Validator:
    @staticmethod
    def validate_name(name):
        if name == "":
            raise ValueError("name can not be empty")
    
    @staticmethod
    def validate_price(price):
        if price <= 0:
            raise ValueError("price must be greater than 0")
    
    @staticmethod
    def validate_product(product):
        if not isinstance(product, Product):
            raise ValueError("product must be an instance of Product")
        
    @staticmethod
    def validate_quantity(quantity):
        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")
    
    @staticmethod
    def validate_cart_item(cart_item):
        if not isinstance(cart_item, CartItem):
            raise ValueError("cart_item must be an instance of CartItem")
        
class Product:
    def __init__(self, name, price):
        self.__name = None
        self.__price = None

        self.name = name
        self.price = price

    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        Validator.validate_name(name)
        self.__name = name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        Validator.validate_price(price)
        self.__price = price

    def get_product_info(self):
        return f"Product: {self.name} | Price: {self.price}"
    
class CartItem:
    def __init__(self, product, quatity):
        self.__product = None
        self.__quantity = None

        self.product = product
        self.quantity = quatity

    @property
    def product(self):
        return self.__product
    
    @product.setter
    def product(self, product):
        Validator.validate_product(product)
        self.__product = product

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        Validator.validate_quantity(quantity)
        self.__quantity = quantity
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def get_cart_item_info(self):
        return f"Cart Items: {self.product.name} {self.quantity} in {self.product.price} price each"
    
class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, cart_item):
        Validator.validate_cart_item(cart_item)
        self.__items.append(cart_item)
    
    def remove_item(self, product_name):
        for item in self.__items:
            if item.product.name == product_name:
                self.__items.remove(item)
                return f"{product_name} removed from cart"

        return f"{product_name} not in cart"
        
    def get_total_cart_price(self):
        total_price = 0
        for item in self.__items:
            total_price += item.get_total_price()

        return total_price

    def show_cart_items(self):
        for item in self.__items:
            print(f"{item.product.name} X {item.quantity} = {item.get_total_price()}")
        
class Customer:
    def __init__(self, name):
        self.__name = None
        self.__cart = ShoppingCart()

        self.name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        Validator.validate_name(name)
        self.__name = name

    @property
    def cart(self):
        return self.__cart
    
    def get_customer_info(self):
        return f"Customer: {self.name}"
    
product1 = Product('Laptop', 1200)
product2 = Product('Mouse', 30)
product3 = Product('Keyboard', 150)

item1 = CartItem(product1, 2)
item2 = CartItem(product2, 3)
item3 = CartItem(product3, 1)

customer = Customer('ALi')

customer.cart.add_item(item1)
customer.cart.add_item(item2)
customer.cart.add_item(item3)

print(customer.get_customer_info())
customer.cart.show_cart_items()

print("Total cart price:", customer.cart.get_total_cart_price())

customer.cart.remove_item("Cup")

print("After removing Mouse:")
customer.cart.show_cart_items()

print("Total cart price:", customer.cart.get_total_cart_price())