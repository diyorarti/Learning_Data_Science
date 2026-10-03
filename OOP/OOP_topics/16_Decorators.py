"""
Decorators
    A decorator is something that adds extra behavior to a function or method without changing it's original code directly
    Decorator = adds extra power to a function/method

"""
# @decorator_name
# def my_function():
#     pass


"""
Most Common decorators
| Decorator           | Meaning                      |
| ------------------- | ---------------------------- |
| `@staticmethod`     | Creates a static method      |
| `@classmethod`      | Creates a class method       |
| `@property`         | Creates a getter-like method |
| `@attribute.setter` | Creates a setter method      |

"""
class Student:
    university = "WSB"

    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, new_gpa):
        if 0 <= new_gpa <= 5:
            self.__gpa = new_gpa
        else:
            raise ValueError("Invalid GPA")
    
    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

    @staticmethod
    def is_valid_gpa(gpa):
        return 0 <= gpa <=5
    
"""
@staticmethod 
    a static method doesn't use self, cls.
    it is used when the method is logically related to the class, but it doesn't need object data or class data/
"""
class Student:
    @staticmethod
    def is_valid_gpa(gpa):
        return 0 <= gpa <=5
# print(Student.is_valid_gpa(4.5)) # True
# print(Student.is_valid_gpa(7.0)) # False
# why is this static ? becUSE It doesn't use self.name, self.gpa

"""
@classmethod
    A class method works with the class itself. it uses cls

    @classmethod
        changes the method so it receives the class as the first argument:
    instead of the object: self
"""
class Student:
    university = "WSB"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

Student.change_university("Harvard")
# print(Student.university)


"""
@property 
    allows you to use a method like an attribute.

Notice:
    student.gpa 
        looks like an attribute, but internally it calls the method:
        def gpa(self):
So:
    @property = method that behaves like an attribute
"""
# without @property
class Student:
    def __init__(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

student = Student(4.5)
# print(student.get_gpa())

# with @property
class Student:
    def __init__(self, gpa):
        self.__gpa = gpa

    @property
    def gpa(self):
        return self.__gpa

student = Student(4.5)
# print(student.gpa)

"""
@property with setter
    A setter allows to change a value safely

student.gpa = 4.8
    looks like direct assignment, but Python actually calls:
        @gpa.setter
        def gpa(self, new_gpa):
    So @property helps with encapsulation.

"""
class Student:
    def __init__(self, gpa):
        self.__gpa = gpa

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, new_gpa):
        if 0 <= new_gpa <-5:
            self.__gpa = new_gpa
        else:
            raise ValueError("GPA must be between 0 and 5")
        
student = Student(4.5)
#print(student.gpa)
student.gpa = 4.8
#print(student.gpa)
# student.gpa = 10 # valueError


"""
Custom decorator outside a class
"""
def log_method(func):
    def wrapper(*args, **kwargs):
        print("Method is starting...")
        result = func(*args, **kwargs)
        print("Method finished.")
        return result
    return wrapper
class Student:
    def __init__(self, name):
        self.name = name

    @log_method
    def study(self):
        return f"{self.name} is studying."

student = Student("Ali")
# print(student.study())


"""
Decorators wrop functions
    So a decorator takes a function, modifies/wraps it, and returns a new function.
"""
@log_method
def study(self):
    return f"{self.name} is studying."
# similar to following
study = log_method(study)


"""
Better custom decorator using functools.wraps
    Professional decorators usually use functools.wraps.
"""
from functools import wraps


def log_method(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished method: {func.__name__}")
        return result
    return wrapper

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @log_method
    def deposit(self, amount):
        self.balance += amount
        return self.balance


account = BankAccount("Ali", 1000)

# print(account.deposit(500))


"""
Decorator for Validation 

"""
from functools import wraps


def positive_amount_required(func):
    @wraps(func)
    def wrapper(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return func(self, amount)
    return wrapper

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @positive_amount_required
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @positive_amount_required
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        return self.balance


account = BankAccount(1000)

print(account.deposit(500))
print(account.withdraw(200))

# account.deposit(-100)  # ValueError


"""
Decorator with arguments
    Sometimes the decorator itself needs parameters.
"""
from functools import wraps


def require_min_gpa(min_gpa):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.gpa < min_gpa:
                return "GPA is too low."
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    @require_min_gpa(3.0)
    def apply_for_scholarship(self):
        return f"{self.name} can apply for scholarship."


student1 = Student("Ali", 3.5)
student2 = Student("Vali", 2.5)

# print(student1.apply_for_scholarship())
# print(student2.apply_for_scholarship())

"""
Class decorator
    A decorator can also decorate a whole class.
"""
def add_greeting(cls):
    cls.greet = lambda self: f"Hello, I am {self.name}"
    return cls


@add_greeting
class Student:
    def __init__(self, name):
        self.name = name


student = Student("Ali")
# print(student.greet())


"""
| Decorator        | Use                                                     |
| ---------------- | ------------------------------------------------------- |
| `@staticmethod`  | Method does not need `self` or `cls`                    |
| `@classmethod`   | Method works with class data using `cls`                |
| `@property`      | Makes a method accessible like an attribute             |
| `@x.setter`      | Controls how an attribute is changed                    |
| Custom decorator | Adds reusable behavior like logging, validation, timing |
| Class decorator  | Modifies/enhances a whole class                         |

"""