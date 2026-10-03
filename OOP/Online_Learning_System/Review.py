from Validator import Validator
from Student import Student
from Course import Course

class Review:
    def __init__(self, student, course, rating, comment):
        self.__student = None
        self.__course = None
        self.__rating = None
        self.__comment = None

        self.student = student
        self.course = course
        self.rating = rating
        self.comment = comment

    @property
    def student(self):
        return self.__student
    
    @student.setter
    def student(self, student):
        Validator.validate_instance(student, Student, "student")
        self.__student = student

    @property
    def course(self):
        return self.__course
    
    @course.setter
    def course(self, course):
        Validator.validate_instance(course, Course, 'course')
        self.__course = course

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rating):
        Validator.validate_rating(rating)
        self.__rating = rating

    @property
    def comment(self):
        return self.__comment
    
    @comment.setter
    def comment(self, comment):
        Validator.validate_not_empty(comment, "comment")
        self.__comment = comment
    
    def get_review_info(self):
        return (
            f"Student: {self.student.name}",
            f"Course: {self.course.title}",
            f"Rating: {self.rating}"
            f"Comment: {self.comment}"
        )

    def __str__(self):
        return (
            f"{self.student.name} rated "
            f"{self.course.title} {self.rating}/5"
        )

    def __repr__(self):
        return (
            f"Review("
            f"student='{self.student.name}', "
            f"course='{self.course.title}', "
            f"rating={self.rating}, "
            f"comment='{self.comment}'"
            f")"
        )
        
    