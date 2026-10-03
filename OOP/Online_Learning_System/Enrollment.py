from Validator import Validator
from Student import Student
from Course import Course
from Payment.Payments import Payment

class Enrollment:
    def __init__(self, student, course, payment, status):
        self.__student = None
        self.__course = None
        self.__payment = None
        self.__status = "Active"

        self.student = student
        self.course = course
        self.payment = payment
        self.status = status

    @property
    def student(self):
        return self.__student
    
    @student.setter
    def student(self, student):
        Validator.validate_instance(student, Student, 'student')
        self.__student = student
    
    @property
    def course(self):
        return self.__course
    
    @course.setter
    def course(self, course):
        Validator.validate_instance(course, Course, 'course')
        self.__course = course
    
    @property
    def payment(self):
        return self.__payment
    
    @payment.setter
    def payment(self, payment):
        Validator.validate_instance(payment, payment, Payment)
        self.__payment = payment

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = "Active"

    
    def cancel(self):
        self.__status = "Cancelled"
        return "Enrollment cancelled successfully."

    def get_enrollment_info(self):
        return (
            f"Student: {self.student.name} | "
            f"Course: {self.course.title} | "
            f"Payment: {self.payment.amount} {self.payment.currency} | "
            f"Status: {self.status}"
        )
