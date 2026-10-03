"""
DUCK TYPING 
    Duck typing is a Python concept where the type/class of an object is less important than the methods or behavior it has

    if an object has the method we need, we can use it , not required to check exact class
"""
# Simple example
class Duck:
    def speak(self):
        return "Quack!"
    
class Dog:
    def speak(self):
        return "Woof!"
    

def make_sound(animal):
    return animal.speak()

duck = Duck()
dog = Dog()

# print(make_sound(duck))
# print(make_sound(dog))
"""
output:
     Quack
     Woof
Here, make_sound() doesn't care whether the object is Duck or a Dog
it only cares that the object has this method:
    speak()
Duck typing meaning
    in Strongly class-based thinking, you may ask
        is this object Duck?
    in duck typing, Python ask:
        Can this ibject do what I need?
    example:
        animal.speak()
    Pythin doesn't care about the exact class name
    it only check: Does the object have speak() method ?
"""


"""
Duck typing and Polymorphism 
    Duck typing is closely related to polymorphism
    Polymorphism means ---> same method name, different behavior

Duck typing is one Python wat to achieve Polymorphism
"""
class CSVReader:
    def read(self):
        return "Reading CSV file"
    

class ExcelReader:
    def read(self):
        return "Reading Excel file"

class SQLReader:
    def read(file):
        return "Reading SQL database"
    
def load_data(reader):
    return reader.read()

# print(load_data(CSVReader))
# print(load_data(ExcelReader))
# print(load_data(SQLReader))


"""
Why Duck Typing useful
    Duck typing helps to write flexible code
"""
# instead of this 
def load_data(reader):
    if isinstance(reader, CSVReader):
        return reader.read_csv()
    elif isinstance(reader, ExcelReader):
        return reader.read_excel()
    elif isinstance(reader, SQLReader):
        return reader.read_sql()
    
# write this 
def load_data(reader):
    return reader.read()


"""
Duck typing in built-in Python
    Python uses duck typing a lot
"""
# print(len("hello"))
# print(len([1, 2, 3]))
# print(len({"a": 1, "b": 2}))
# str, list, dict are different types, but they are support len()


"""
Duck typing error Example:
    if an object does not have the required method, Python gives an error
""" 
class Duck:
    def speak(self):
        return "Quack!"


class Rock:
    pass


def make_it_speak(obj):
    return obj.speak()
# print(make_it_speak(Duck()))
# print(make_it_speak(Rock()))


"""
Safer Duck typing with hasattr
    sometimes you can check before calling the method
"""

class Duck:
    def speak(self):
        return "Quack!"


class Rock:
    pass


def make_it_speak(obj):
    if hasattr(obj, "speak"):
        return obj.speak()
    return "This object cannot speak."


# print(make_it_speak(Duck()))
# print(make_it_speak(Rock()))

"""
Python style: EAFP
    EAFP means --> easier to Ask Forgiveness than Permission
"""
def make_it_speak(obj):
    try:
        return obj.speak()
    except AttributeError:
        return "This object cannot speak."
# print(make_it_speak(Duck()))
# print(make_it_speak(Rock()))


"""
Duck typing with inheritance
    Dog is connected to Animal
"""
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"
# with duck typing
class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep!"
def make_it_speak(obj):
    return obj.speak()



# real example
class CSVLoader:
    def load(self):
        return "Loading data from CSV"


class DatabaseLoader:
    def load(self):
        return "Loading data from database"


class APILoader:
    def load(self):
        return "Loading data from API"


class DataPipeline:
    def __init__(self, loader):
        self.loader = loader

    def run(self):
        data = self.loader.load()
        return f"Pipeline started: {data}"


pipeline1 = DataPipeline(CSVLoader())
pipeline2 = DataPipeline(DatabaseLoader())
pipeline3 = DataPipeline(APILoader())

print(pipeline1.run())
print(pipeline2.run())
print(pipeline3.run())