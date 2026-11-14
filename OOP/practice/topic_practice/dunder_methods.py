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

class Student:
    def __init__(self, student_id, name, age, gpa):
        self.__student_id = None
        self.__name = None
        self.__age = None
        self.__gpa = None
        self.__courses = []

        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa
        

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        Validator.validate_not_empty(value, "Student ID")
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

    # Human readable description
    def __str__(self):
        return f"Student name: {self.name}, ID: {self.student_id}, Age: {self.age}, GPA: {self.gpa}, course: {self.__courses}"

    # developer-friendly descriptio
    def __repr__(self):
        return (
            f"Student(student_id={self.student_id!r}, "
            f"name={self.name!r}, "
            f"age={self.age!r}, "
            f"gpa={self.gpa!r})"
        )

    # comparing students, they are equal when their student IDs match
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.student_id == other.student_id

    # __lt__ compares that is current student's GPA less than other's GPA
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa < other.gpa

    # __gt__ compares that is current student's GPA greater than other's GPA
    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa > other.gpa

    # less than or equal
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa <= other.gpa

    # greater than or equal 
    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa >= other.gpa

    # len ruturn number of completed courses 
    def __len__(self):
        return len(self.__courses) 

    # __getitem__ access a course using index
    def __getitem__(self, key):
        return self.__courses[key]

    # __contains__ check whether a student has completed a course 
    def __contains__(self, item):
        return item in self.__courses

    # __bool__ return True if GPA is at least 3.0
    def __bool__(self):
        return self.gpa >= 3


student1 = Student("S001", "Ali", 22, 2.5)
student2 = Student("S001", "Ali", 22, 4.5)
student3 = Student("S002", "John", 24, 5.0)

student1.add_course("Python")
student1.add_course("Statistics")
student1.add_course("SQL")

print(student1.__lt__(student3))
