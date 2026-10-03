from abc import ABC, abstractmethod
from Validator import Validator

class Person(ABC): 
    def __init__(self, name, email):
        self.__name = None
        self.__email = None

        self.name = name
        self.email = email

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        Validator.validate_not_empty(name, "name")
        self.__name = name

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        Validator.validate_email(email)
    
    @abstractmethod
    def get_info(self):
        return f"Name: {self.name} | email: {self.email}"
    
    @abstractmethod
    def get_role(self):
        pass


    def __str__(self):
        return f"Name:{self.name} | Email:{self.email}"
    
    def __repr__(self):
        return f"(Name:{self.name!r}, Email:{self.email!r})"
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.email == other.email
