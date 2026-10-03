from Validator import Validator
from Person import Person
from Course import Course 

class Student(Person):
    total_students = 0

    def __init__(self, name, email, student_id):
        super().__init__(name, email)

        self.__student_id = None
        self.student_id = student_id

        self.__enrollments = []
        
        Student.total_students += 1

    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self, student_id):
        Validator.validate_not_empty(student_id, 'student_id')
        self.__student_id = student_id

    def enroll(self, course):
        if not isinstance(course, Course):
            raise ValueError("Only Course object can be added")
        self.__enrollments.append(course)

    def drop_course(self, course):
        if course not in self.__enrollments:
            raise ValueError("course is not enrolled")
        self.__enrollments.pop(course)

    def show_course(self):
        print(f"{self.name} Enrolled Courses:")
        for course in self.__enrollments:
            print(f"{course}")

    def get_role(self):
        return "Student"
    
    def get_total_spent(self):
        total = 0

        for enrollement in self.__enrollments:
            if enrollement.status == 'Active':
                total += enrollement.payment.amount

    @classmethod
    def get_total_students(cls):
        return cls.total_students

