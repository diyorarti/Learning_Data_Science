from Validator import Validator
from Student import Student
from Instructor import Instructor
from Course import Course
from Enrollment import Enrollment

class LearningPlatform:
    def __init__(self, platform_name):
        self.platfrom_name = platform_name

        self.__students = []
        self.__instructors = []
        self.__courses = []
        self.__enrollments = []

    def add_student(self, student):
        Validator.validate_instance(student, Student, 'student')
        self.__students.append(student)
    
    def add_instuctor(self, instructor):
        Validator.validate_instance(instructor, Instructor, 'instructor')
        self.__instructors.append(instructor)
    
    def add_course(self, course):
        Validator.validate_instance(course, Course, "course")
        self.__courses.append(course)
    
    def add_enrollment(self, enrollment):
        Validator.validate_instance(enrollment, Enrollment, "enrollment")
        self.__enrollments.append(enrollment)

    def find_student_by_email(self, email):
        Validator.validate_email(email)
        for student in self.__students:
            if student.email == email:
                return student
        return None
    
    def find_instructor_by_email(self, email):
        Validator.validate_email(email)
        for instructor in self.__instructors:
            if instructor.email == email:
                return instructor
        return None
    
    def find_course_by_title(self, title):
        Validator.validate_not_empty(title, "title")
        for course in self.__courses:
            if course.title == title:
                return course
        
        return None
    
    def show_all_students(self):
        if len(self.__students) == 0:
            print("No students found.")
            return

        for student in self.__students:
            print(student)

    def show_all_instructors(self):
        if len(self.__instructors) == 0:
            print("No instructors found.")
            return

        for instructor in self.__instructors:
            print(instructor)

    def show_all_courses(self):
        if len(self.__courses) == 0:
            print("No courses found.")
            return

        for course in self.__courses:
            print(course)

    def show_all_enrollments(self):
        if len(self.__enrollments) == 0:
            print("No enrollments found.")
            return

        for enrollment in self.__enrollments:
            print(enrollment.get_enrollment_info())

    def get_platform_summary(self):
        return (
            f"Platform: {self.platform_name} | "
            f"Students: {len(self.__students)} | "
            f"Instructors: {len(self.__instructors)} | "
            f"Courses: {len(self.__courses)} | "
            f"Enrollments: {len(self.__enrollments)}"
        )

    
