from Person import Person
from Validator import Validator
from Course import Course

class Instructor(Person):
    total_instructors = 0


    def __init__(self, name, email, instructor_id):
        super().__init__(name, email)
        self.__instructor_id = None
        self.instructor_id = instructor_id

        self.__courses = []

        Instructor.total_instructors += 1

    @property
    def instructor_id(self):
        return self.__instructor_id
    
    @instructor_id.setter
    def instructor_id(self, instructor_id):
        Validator.validate_not_empty(instructor_id, 'instructor_id')
        self.__instructor_id = instructor_id

    @property
    def courses(self):
        return self.__courses

    def create_course(self, title, price, category):
        from Course import Course
        course = Course(title, price, category, self)
        self.__courses.append(course)
        return course
    
    def add_course(self, course):
        Validator.validate_instance(course, Course, "course")
        self.__courses.append(course)

    def show_courses(self):
        if not self.courses:
            print("this instructor has no courses yet")
        else:
            for couse in self.__courses:
                print(couse)

    def get_role(self):
        return "Instructor"
    
    @classmethod
    def get_total_instructors(cls):
        return cls.total_instructors
    

