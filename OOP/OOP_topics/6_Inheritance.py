"""
Inheritance 
    creating new class from existing classes

    1. Sinle Inheritance
    2. Multilevel Inheritance
    3. Hierarchical Inheritance

    super()
"""

from abc import ABC, abstractmethod

class UniversityMember(ABC):
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Validator:

    @staticmethod
    def validate_not_empty(value, field_name):
        if value == "" or value is None:
            raise ValueError(f"{field_name} cannot be empty")

    @staticmethod
    def validate_email(email):
        if "@" not in email or "." not in email:
            raise ValueError("Email must contain '@' and '.'")
    
    @staticmethod
    def validate_age(age):
        if age < 16:
            raise ValueError("Age must be greater than or equal to 16")
    
    @staticmethod
    def validate_positive_number(value):
        if value < 0:
            raise ValueError("value must be greater than 0")
    
    @staticmethod
    def validate_gpa(gpa):
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")

class Person(UniversityMember):
    total_people = 0

    def __init__(self, name, email, age, nationality, phone_number):
        self.nationality = nationality

        self._phone_number = None

        self.phone_number = phone_number

        self.__name = None
        self.__age = None
        self.__email = None

        self.name = name
        self.age = age
        self.email = email

        Person.total_people += 1
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if phone_number == "":
            raise ValueError("Phone Number can not be empty")
        self._phone_number = phone_number

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("name can't be empty")
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("age must be greater than 18")
        self.__age = age

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if '@' not in email:
            raise ValueError("email must contain @")
        self.__email = email

    def get_role(self):
        return "Person"
    
    def get_info(self):
        return f"Name {self.name} \n| Email: {self.email} \n| Age: {self.age} \n| Nationality: {self.nationality} \n| Phone: {self.phone_number} \n| Role: {self.get_role()}"
    
    def update_phone_number(self, new_phone):
        if new_phone == "":
            raise ValueError("phon number can not be empty")
        self.phone_number = new_phone

    @classmethod
    def get_total_people(cls):
        return cls.total_people
    
    @staticmethod
    def is_agul(age):
        if age >= 18:
            return True
        else:
            return False

class Student(Person):
    student_count = 0

    def __init__(self, name, email, age, nationality, phone_number, student_id, major, gpa):
        super().__init__(name, email, age, nationality, phone_number)

        self.__student_id = None
        self.__major = None
        self.__gpa = None

        self.student_id = student_id
        self.major = major
        self.gpa = gpa

        Student.student_count += 1

    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self, student_id):
        if len(student_id) > 5 and len(student_id) < 5:
            raise ValueError("student_id must contain 5 characters")
        self.__student_id = student_id

    @property
    def major(self):
        return self.__major
    
    @major.setter
    def major(self, major):
        if major == "":
            raise ValueError("major can not be empty")
        self.__major = major

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, gpa):
        if gpa <0.0 or gpa > 5.0:
            raise ValueError("gpa must be between 1.0 and 5.0")
        self.__gpa = gpa

    def get_role(self):
        return "Student"
    
    def get_info(self):
        full_info = super().get_info() + f"| Student ID: {self.student_id} | Major:{self.major} | GPA:{self.gpa}"
        return full_info
    
    def study(self, hours):
        if hours > 0 :
            return f"{self.name} studied for {hours} hours"
        else:
            raise ValueError("Hour must be greater than 0.0")
    
    def update_gpa(self, new_gpa):
        if new_gpa <0.0 or new_gpa > 5.0:
            raise ValueError("gpa must be between 1.0 and 5.0")
        self.__gpa = new_gpa

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @staticmethod
    def is_honor_student(gpa):
        if gpa >= 3.7:
            return True
        else:
            return False
    
class Professor(Person):
    professor_count = 0

    def __init__(self, name, email, age, nationality, phone_number, employee_id, department, salary):
        super().__init__(name, email, age, nationality, phone_number)
        self.__employee_id = None
        self.__department = None
        self.__salary = None

        self.employee_id = employee_id
        self.department = department
        self.salary = salary

        Professor.professor_count += 1

    @property
    def employee_id(self):
        return self.__employee_id
    
    @employee_id.setter
    def employee_id(self, employee_id):
        if len(employee_id) > 5 and len(employee_id) < 5:
            raise ValueError("student_id must contain 5 characters")
        self.__employee_id = employee_id

    @property
    def department(self):
        return self.__department
    
    @department.setter
    def department(self, department):
        if department == "":
            raise ValueError("department can not be empty")
        self.__department = department

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary <= 0:
            raise ValueError("salary must be greater than 0")
        self.__salary = salary


    def get_role(self):
        return "Professor"
    
    def get_info(self):
        full_info = super().get_info() + f"| Emplyee ID: {self.employee_id} | Department: {self.department} | Salary: {self.salary}"
        return full_info
    
    def teach(self, course_name):
        return f"Dr. {self.name} is teaching {course_name}"
    
    def increase_salary(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        self.salary += amount

    @classmethod
    def get_professor_count(cls):
        return cls.professor_count
    
class AdminStaff(Person):
    def __init__(self, name, email, age, nationality, phone_number, staff_id, position, monthly_salary):
        super().__init__(name, email, age, nationality, phone_number)
        self.__staff_id = None
        self.__position = None
        self.__monthly_salary = None

        self.staff_id = staff_id
        self.position = position
        self.monthly_salary = monthly_salary

    @property
    def staff_id(self):
        return self.__staff_id
    
    @staff_id.setter
    def staff_id(self, staff_id):
        if len(staff_id) > 5 and len(staff_id) < 5:
            raise ValueError("student_id must contain 5 characters")
        self.__staff_id = staff_id

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        if position == "":
            raise ValueError("position can not be empty")
        self.__position = position

    @property
    def monthly_salary(self):
        return self.__monthly_salary
    
    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        if monthly_salary <= 0:
            raise ValueError("monthly salary  must be greater than 0")
        self.__monthly_salary = monthly_salary

    def increase_salary(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.monthly_salary += amount

    def get_role(self):
        return "Admin Staff"
    
    def get_info(self):
        full_info = super().get_info() + f"| Staff ID: {self.staff_id} | Position: {self.position} | Monthly Salary: {self.monthly_salary}"
        return full_info
    
    def work(self):
        return f"{self.name} is working"
    
class TeachingAssistant(Student):
    def __init__(self, name, email, age, nationality, phone_number, student_id, major, gpa, assigned_course, monthly_payment):
        super().__init__(name, email, age, nationality, phone_number, student_id, major, gpa)

        self.__assigned_course = None
        self.__monthly_payment = None

        self.assigned_course = assigned_course
        self.monthly_payment = monthly_payment

    @property
    def assigned_course(self):
        return self.__assigned_course
    
    @assigned_course.setter
    def assigned_course(self, assigned_course):
        if assigned_course == "":
            raise ValueError("assigned_course can not be empty")
        self.__assigned_course = assigned_course
    
    @property
    def monthly_payment(self):
        return self.__monthly_payment
    
    @monthly_payment.setter
    def monthly_payment(self, monthly_payment):
        if monthly_payment <= 0:
            raise ValueError("monthly_payment must be greater than 0")
        self.__monthly_payment = monthly_payment

    def get_role(self):
        return "Teaching Assistant"
    
    def get_info(self):
        info = super().get_info() + f"|Assigned course: {self.assigned_course} |Monthly Salary: {self.monthly_payment} "
        return info
    
    def assist_professor(self, professor_name):
        return f"{self.name} is assisting Professor {professor_name} in {self.assigned_course}"
    
    def increase_payment(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.monthly_payment += amount

class Course:
    course_count = 0

    def __init__(self, course_code, course_name, credits, professor):
        self.__course_code = None
        self.__course_name = None
        self.__credits = None
        self.__professor = None
        self.__students = []

        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.professor = professor

        Course.course_count += 1

    # Getter for course_code
    @property
    def course_code(self):
        return self.__course_code

    # Setter for course_code
    @course_code.setter
    def course_code(self, course_code):
        if course_code == "":
            raise ValueError("Course code cannot be empty.")
        self.__course_code = course_code

    # Getter for course_name
    @property
    def course_name(self):
        return self.__course_name

    # Setter for course_name
    @course_name.setter
    def course_name(self, course_name):
        if course_name == "":
            raise ValueError("Course name cannot be empty.")
        self.__course_name = course_name

    # Getter for credits
    @property
    def credits(self):
        return self.__credits

    # Setter for credits
    @credits.setter
    def credits(self, credits):
        if credits <= 0:
            raise ValueError("Credits must be greater than 0.")

        if not Course.is_valid_credit(credits):
            raise ValueError("Credits must be between 1 and 10.")

        self.__credits = credits

    # Getter for professor
    @property
    def professor(self):
        return self.__professor

    # Setter for professor
    @professor.setter
    def professor(self, professor):
        if not isinstance(professor, Professor):
            raise TypeError("Professor must be an instance of Professor class.")
        self.__professor = professor

    # Instance method
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class.")

        self.__students.append(student)

    # Instance method
    def remove_student(self, student_id):
        for student in self.__students:
            if student.student_id == student_id:
                self.__students.remove(student)
                return

        raise ValueError("Student not found.")

    # Instance method
    def get_course_info(self):
        return (
            f"Course: {self.__course_name} | "
            f"Code: {self.__course_code} | "
            f"Credits: {self.__credits} | "
            f"Professor: {self.__professor.name} | "
            f"Students: {len(self.__students)}"
        )

    # Class method
    @classmethod
    def get_course_count(cls):
        return cls.course_count

    # Static method
    @staticmethod
    def is_valid_credit(credits):
        return 1 <= credits <= 10
    
class UniversitySystem:
    def __init__(self, university_name):
            self.university_name = university_name

            self.__students = []
            self.__prodessors = []
            self.__staff_members = []
            self.__courses = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Only Student object can be added")
        self.__students.append(student)

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise ValueError("Only Professor object can be added")
        self.__prodessors.append(professor)
    
    def add_staff(self, staff):
        if not isinstance(staff, AdminStaff):
            raise ValueError("Only AdminStaff object can be added")
        self.__staff_members.append(staff)

    def add_course(self, course):
        if not isinstance(course, Course):
            raise ValueError("Only Course object can be added")
        self.__courses.append(course)

    def find_student_by_id(self, student_id):
        for student in self.__students:
            if student.student_id == student_id:
                return student
        return None
    
    def find_professor_by_id(self, prof_id):
        for prof in self.__prodessors:
            if prof.employee_id == prof_id:
                return prof
        return None
    
    def show_all_people(self):
        print("Students: ")
        for student in self.__students:
            print(student)

        print("\nProfessors")
        for prof in self.__prodessors:
            print(prof)
        
        print("\nStaff Members:")
        for staff in self.__staff_members:
            print(staff)

    def show_all_courses(self):
        print("Courses:")
        for course in self.__courses:
            print(course)

    def get_system_summary(self):
        return (
            f"University: {self.university_name} | "
            f"Students: {len(self.__students)} | "
            f"Professors: {len(self.__prodessors)} | "
            f"Staff: {len(self.__staff_members)} | "
            f"Courses: {len(self.__courses)}"
        )

system = UniversitySystem('WSB University')

student1 = Student(
    "Ali",
    "ali@gmail.com",
    20,
    "Uzbek",
    "123456789",
    "S101",
    "Data Science",
    3.8
)

student2 = Student(
    "Vali",
    "vali@gmail.com",
    21,
    "Uzbek",
    "987654321",
    "S102",
    "Cybersecurity",
    3.4
)


professor1 = Professor(
    "Dr. Smith",
    "smith@university.com",
    45,
    "Polish",
    "555555555",
    "P201",
    "Artificial Intelligence",
    7000
)

staff1 = AdminStaff(
    "John",
    "john@university.com",
    35,
    "Polish",
    "444444444",
    "A301",
    "Registrar",
    4000
)

ta1 = TeachingAssistant(
    "Sara",
    "sara@gmail.com",
    22,
    "Uzbek",
    "333333333",
    "S103",
    "Software Engineering",
    3.9,
    "Python OOP",
    800
)
course1 = Course("CS101", "Python OOP", 5, professor1)
course2 = Course("DS201", "Machine Learning", 6, professor1)

course1.add_student(student1)
course1.add_student(ta1)
course2.add_student(student2)

system.add_student(student1)
system.add_student(student2)
system.add_student(ta1)
system.add_professor(professor1)
system.add_staff(staff1)
system.add_course(course1)
system.add_course(course2)

print(system.get_system_summary())

print(student1.study(3))
print(professor1.teach("Machine Learning"))
print(staff1.work())
print(ta1.assist_professor("Smith"))

student1.update_gpa(4.0)
professor1.increase_salary(500)
staff1.increase_salary(300)
ta1.increase_payment(200)

print(course1.get_course_info())
print(course2.get_course_info())

members = [student1, professor1, staff1, ta1]

for member in members:
    print(member.get_info())

print(Person.get_total_people())
print(Student.get_student_count())
print(Professor.get_professor_count())
print(Course.get_course_count())