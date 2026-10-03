"""
Classes 
    A class is a blueprint for creating objects. 
    Example:
        car design (details)       --> class
        created car from the design--> object

The Types of classes:
    1- Regular class
    2- Abstract class
    3- Parent/Base/Super class
    4- Child/Derived/Sub class
    5- Data class               ---> used to strore data 
    6- Utility class            ---> used to group helper methods together
    7- Final class              ---> complete class, can't be inherited, no child allowed
"""



from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_holder, card_number):
        self.card_holder = card_holder
        self.card_number = card_number
    
    def pay(self, amount):
        return f"{self.card_holder} paid {amount} by Credit Card"
    
class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} by PayPal account {self.email}"
    
class PaymentValidator:

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            return False
        return True 

# Abstractclass
class PlatformUser(ABC):

    @abstractmethod
    def get_role(self):
        pass

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_into(self):
        return f"Name: {self.name} | Age: {self.age}"

class Student(Person):
    def __init(self, name, age, id, email):
        super().__init__(name, email)
        self.id = id
        self.email = email

# Parent class
class User(PlatformUser):
    def __init__(self, name, email):
        self.__name = None
        self.__email = None

        self.name = name
        self.eamil = self.eamil

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name =="":
            raise ValueError("name can't be empty")
        self.__name = name
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if '@' not in email:
            raise ValueError("Email must contain @")
        self.__email = email

    def get_role(self):
        return super().get_role()

    def get_info(self):
        return f"Name: {self.name} | Email: {self.email} | Role: {self.get_role()}"

# Child class
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.__student_id = None
        self.enrolled_courses = []
        self.student_id = student_id

    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self, student_id):
        if student_id == "":
            raise ValueError("student_id can't be empty")
        
    def get_role(self):
        return "Student"
    
    def enroll(self, course):
        self.enrolled_courses.append(course)
        return f"{self.name} enrolled in {course}"
    
# Child class
class Instructor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)
        self.__specialization = None
        self.courses = []
        self.specialization = specialization

    @property
    def specialization(self):
        return self.__specialization
    
    @specialization.setter
    def specialization(self, specialization):
        if specialization == "":
            raise ValueError("specialization can't be empty")
        self.__specialization = specialization

    def get_role(self):
        return "Instructor"
    
    def create_course(self, course_title):
        self.courses.append(course_title)
        return f"{self.name} created course {course_title}"
    
# DataClass
@dataclass
class Course:
    title:str
    category:str
    price:float
    courses: list = field(default_factory=list)

# Utility class
class MathUtilities:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
# Final Class
# method 1 by __init_subclass__
class Certificate:
    def __init__(self, student_name, course_title):
        self.student_name = student_name
        self.course_title = course_title

    def generate_certificate(self):
        return f"Certificate {self.student_name} completed {self.course_title}"
    
    def __init_subclass__(cls, **kwargs):
        raise ValueError("Certificate class cannot be inherited")
    
# method 2 by @final
from typing import final
@final 
class Certificate1:

    def __init__(self, student_name, course_title):
        self.student_name = student_name
        self.course_title = course_title

    def generate_certificate(self):
        return f"Certificate: {self.student_name} completed {self.course_title}."