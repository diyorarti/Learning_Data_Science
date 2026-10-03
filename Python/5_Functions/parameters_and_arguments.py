"""
Paramerter -> variable in function definition
Argument -> Value passed to the function
"""

def greet(name): # parameter
    print(name)

#greet('Ali') # Argument 

# positional arguments
def introduce(name, age, title, organazition):
    print(f"{name} is a {age} old {title} at {organazition}")

#introduce("Diyor", 21, 'student', 'WSB University') # orders of arguments matter 

# default argument
def accepting_for_armiy(age1=18, height1=1.70):
    age = int(input('Enter your age: '))
    height = float(input('Enter your height: '))

    if age >= age1 and height >=height1:
        print("You are accepted ")
    else:
        print("You are rejected")

#accepting_for_armiy()

# *args - collects extra arguments into a tuple
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)

# sum_numbers(1, 2, 3, 4, 5)

# **kwargs collects into a dictionary 
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")
#show_info(name='Ali', age=21, is_student=False)

def student_info(name, age=18, *grades, **extra):
    print(f"the student's name is {name}")
    print(f"his age is {age}")
    sum_grades = 0
    for grade in grades:
        sum_grades += grade
    print(f"sum of grades is {sum_grades}")

    for key, value in extra.items():
        print(f"{key} - {value}")

student_info("Ali", 20, 80, 90, 85, city="Tashkent", status="student")