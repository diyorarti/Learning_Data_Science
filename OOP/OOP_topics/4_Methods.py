"""
method is a function that belongs to a class
    Methods define the behavior of class

Types:
    1. Instance method --> works with objects' data
    2. Class method    --> works with class data 
    3. Static method   --> don't need object and class data
"""

class Student:
    university = "WSB university"
    total_students = 0
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.total_students += 1
    
    # instance method
    def increase_score(self, amount):
        self.score += amount

    # instance method
    def decrease_score(self, amount):
        self.score -= amount

    # instance method
    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    # instance method
    def get_info(self):
        return f"Name: {self.name}| Score: {self.score} | Grade: {self.get_grade()}"

    # class method
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
student1 = Student("Ali", 75)

student1.increase_score(10)
student1.decrease_score(5)

print(student1.get_info())
print(Student.get_total_students())


class Validator:
    # static method
    @staticmethod
    def validate_positive_number(value):
        if value <= 0:
            raise ValueError("Value must be greater than 0")

Validator.validate_positive_number(10)  # No error