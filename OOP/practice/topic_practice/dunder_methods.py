import re

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

    @staticmethod
    def validate_email(email):
        if email is None or str(email).strip() == "":
            raise ValueError("email can't be empty")

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")


    @staticmethod
    def validate_instance(obj, class_type, field_name):
        if not isinstance(obj, class_type):
            raise TypeError(f"{field_name} must be an instance of {class_type.__name__}")

class Course:
    pass

class Student:
    def __init__(self, student_id, name, age, gpa, courses):
        self.__student_id = None
        self.__name = None
        self.__age = None
        self.__gpa = None
        self.__courses = []

        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa
        self.courses = courses
        

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        Validator.validate_positive_number(value, "Student ID")
        self.__student_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_not_empty(value, "Name")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.validate_positive_number(value, "age")
        self.__age = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        Validator.validate_positive_number(value, "gpa")
        self.__gpa = value

    def add_course(self, value):
        if value not in self.__courses:
            self.__courses.append(value)
        else:
            raise ValueError(f"{value} is already added ")

    

    