"""
Class Design Principles:
    Classes Design Principles are rules or guidlines that help to create clean , useful and maintainable classes
    Advantages:
        - easy to understand
        - easy to maintain
        - easy to extend
        - not too large
        - not too dependent on other classes
    
"""

"""
Principle 1 --> A class should represent one clear idea, a class should usually represent one thing.
    One class -- One clear responsibility
"""
# good example
class Student:
    pass

class BankAccount:
    pass

class Product:
    pass

class DataCleaner:
    pass

class ModelTrainer:
    pass

# bad example:
class StudentBankAccountEmailSystem:
    pass

"""
Principle 2 --> Keep related data and methods together
    This is connected to escapsulation 
    if a class stores data, it should also have methods that work with that data

Example:
    balance is inside BankAccount
    deposit() works with balance
    withdraw() works with balance
"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount


"""
Principle 4 --> USing meaningful class names
    class names should be clear
Python class names usually use PascalCase
"""
# good example
class Student:
    pass

class Employee:
    pass

class Order:
    pass

class DataProcessor:
    pass

class ModelTrainer:
    pass

# bad example
class Thing:
    pass

class Manager:
    pass

class Data:
    pass

class MyClass:
    pass

"""
Principle 4 --> Keep classes small
    A class should not become too large
    if a class has too many reponsibilitiees, split it
"""
# bad example
class MachineLearningProject:
    def load_data(self):
        pass

    def clean_data(self):
        pass

    def train_model(self):
        pass

    def evaluate_model(self):
        pass

    def save_model(self):
        pass

    def send_email_report(self):
        pass

    def create_dashboard(self):
        pass
# better design
class DataLoader:
    pass

class DataCleaner:
    pass

class ModelTrainer:
    pass

class ModelEvaluator:
    pass

class ReportSender:
    pass

class MLPipeline:
    def __init__(self, loader, cleaner, trainer, evaluator):
        self.loader = loader
        self.cleaner = cleaner
        self.trainer = trainer
        self.evaluator = evaluator

"""
Principle 5 --> Use instance variables for object-specific data
    if data is different for each, use instance variables
"""
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

"""
Principle 6 --> Use class variables for shared data
    if data is shared by all ibjects, use class variable
"""
class Student:
    university = "WSB" # is shared by all students.

    def __init__(self, name):
        self.name = name


"""
Principle 7: Protect important data
    Do not allow important data to be changed directly in a dangerous way.
"""
# bad example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

# good example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount


"""
Principle 8 --> Avoid repeating code
    If you repeat the same logic many times, move it into a method or parent class.
"""
# bad example
class Student:
    def show_name(self):
        print(self.name)

class Teacher:
    def show_name(self):
        print(self.name)

# good example
class Person:
    def show_name(self):
        print(self.name)


class Student(Person):
    pass


class Teacher(Person):
    pass


"""
Principle 9: Prefer composition when it is a has-a relationship
    Use inheritance for is-a relationships.
    Use composition for has-a relationships.

Inheritance:
    Dog is an Animal
    Student is a Person
Composition:
    Car has an Engine
    Order has Products
    Student has an Address
"""

class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()
    
    
"""
Principle 10: Make methods do one clear thing
    A method should have one clear purpose.
"""
# good example
class BankAccount:
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def show_balance(self):
        pass

# bad example
def deposit_and_withdraw_and_send_email_and_print_report(self):
    pass


"""
Principle 11: Use clear method names
    Method names should usually be verbs because methods represent actions.
    good method names
        #deposit()
        #withdraw()
        #show_info()
        #calculate_total()
        #validate_gpa()
        #train_model()
        #clean_data()
    bad method names
        data()
        thing()
        process()
        do()
        handle()
"""


"""
Principle 12: Hide unnecessary details
    The user of a class should not need to know how everything works internally.
"""

class DataCleaner:
    def clean(self):
        self._remove_duplicates()
        self._fill_missing_values()
        self._fix_column_names()
        return "Data cleaned"

    def _remove_duplicates(self):
        pass

    def _fill_missing_values(self):
        pass

    def _fix_column_names(self):
        pass

# user only calls
clearer = DataCleaner()
clearer.clean()


"""
Principle 13: Design classes to be easy to extend
    Good class design makes it easy to add new behavior later.
"""
class Payment:
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by card"


class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by PayPal"
    

# bad class design 
class App:
    def __init__(self, data):
        self.data = data

    def load_data(self):
        pass

    def clean_data(self):
        pass

    def train_model(self):
        pass

    def evaluate_model(self):
        pass

    def send_email(self):
        pass

    def save_to_database(self):
        pass

    def create_dashboard(self):
        pass

# better class design 
class DataLoader:
    def load(self):
        pass


class DataCleaner:
    def clean(self, data):
        pass


class ModelTrainer:
    def train(self, data):
        pass


class ModelEvaluator:
    def evaluate(self, model, data):
        pass


class EmailSender:
    def send(self, message):
        pass


class MLPipeline:
    def __init__(self, loader, cleaner, trainer, evaluator):
        self.loader = loader
        self.cleaner = cleaner
        self.trainer = trainer
        self.evaluator = evaluator

    def run(self):
        data = self.loader.load()
        clean_data = self.cleaner.clean(data)
        model = self.trainer.train(clean_data)
        score = self.evaluator.evaluate(model, clean_data)
        return score