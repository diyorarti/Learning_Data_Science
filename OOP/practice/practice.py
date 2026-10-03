from abc import ABC, abstractmethod
import re

class Validator:
    @staticmethod
    def validate_not_empty(value, field_name):
        if value is None or str(value).strip() == "":
            raise ValueError(f"{field_name} cannot be empty")

    @staticmethod
    def validate_positive_number(value, field_name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number")
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than 0")

    @staticmethod
    def validate_email(email):
        if email is None or str(email).strip() == "":
            raise ValueError("email cannot be empty")
        
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")

class Person(ABC):
    def __init__(self, name, age):
        self.__name = None
        self.__age = None
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_not_empty(value, 'name')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.validate_positive_number(value, 'age')
        self.__age = value

    def get_info(self):
        return f"Name: {self.name} | Age: {self.age}"

    def get_role(self):
        pass


class Student(Person):
    def __init__(self, name, age, id, email):
        super().__init__(name, age)
        self.__id = None
        self.__email = None
        self.id = id
        self.email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        Validator.validate_not_empty(value, 'id')
        self.__id = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        Validator.validate_email(value)
        self.__email = value

    def get_info(self):
        full_info = super().get_info()+ f" | ID: {self.id} | Email: {self.email}"
        return full_info

    def get_role(self):
        return "Student"



student1 = Student("John Doe", 20, "12345", "john.doe@example.com")
print(student1.get_info())  # Output: Name: John Doe | Age: 20 | ID: 12345 | Email:
    