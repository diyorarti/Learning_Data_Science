"""
Object Liefcylce 
    Means the full life of an object from creation to deletion
    Object lifecylce --> how an object os creadred, used, and destroyed
    In Python , the lifecycle usually has 3 main stages:
        1. Object creation 
        2. Object usage
        3. Object destruction / delection

"""
# Basic object lifecycle
class Student:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} object created")
    
    def study(self):
        print(f"{self.name} is studying")
    
    def __del__(self):
        print(f"{self.name} object deleted")
# student1 = Student("Ali")  # object creation
# student1.study()           # object usage
# del student1               # object deletion

"""
Stage 1 Object Creation:
    in object creation:
        1. Creates the object in memory
        2. Initializes the object using __init__
    
"""