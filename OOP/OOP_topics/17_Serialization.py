"""
Serialization 
    Serialization means converting an object into a format that can be saved or transferred
    Serialization = an object -> storable/transmittable format

    For example: An onject
        student = Student("Ali", 20, 4.5)
    We want:
        1. save it to a file
        2. sent it through an API 
        3. store it in a database
        4. Convert it to JSON
        5. Load it again later

Deserialization 
    Deserialization = stored/transmitted format -> object 
    Example:
        Object -> JSON -> Object

Serialization:   Python object          -→ JSON/file/string/bytes
Deserialization: JSON/file/string/bytes -→ Python object
"""
# simple example
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    
student = Student('Ali', 20, 3.5)
# This object exists only while the program is running. When the program stops, the object disappears from memory. 
# So if we want to save it, we can convert it to a dictionary or JSON.
student_data = {
    "name": student.name,
    "age": student.age,
    "gpa": student.gpa
}

# Serialization using dictionary
class Stundet1:
    def __init__(self, name, age, gpa):
        self.name = name 
        self.age = age
        self.gpa = gpa

    def to_dict(self): # serialization method
        return {
            "name":self.name,
            "age":self.age,
            "gpa":self.gpa
        }
    
    @classmethod
    def from_dict(cls, data): # deserialization method
        return cls(
            name=data['name'],
            age=data['age'],
            gpa=data['gpa']
        )
stundet1 = Stundet1("Vali", 19, 4.2).to_dict()
studnet_data = Stundet1.from_dict(stundet1)


"""
Serialization using JSON 
    JSON is one of the most common formats for serialization 
    JSON means JavaScript Object Notation 
        Widely used in :
            1. APIs
            2. Web applications
            3. Configuration files
            4. Databases
            5. Data exnchange between frontend and backend
    there is a built-in module in Python 
        import json
"""

# Object to JSON
import json

class Stundet3:
    def __init__(self, name, age, gpa):
        self.name = name 
        self.age = age
        self.gpa = gpa
    
    def to_dict(self):
        return {
            "name":self.name,
            "age":self.age,
            "gpa":self.gpa
        }
student3 = Stundet3('Nasiba', 18, 20, 4.5)
stundet3_dict = student3.to_dict()
student_json = json.dumps(stundet3_dict) # json.dumps converts Python dict to JSON string


# JSON to Object 
class Student4:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age 
        self.gpa = gpa 
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gpa": self.gpa
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            age=data['age'],
            gpa=data['gpa']
        )
student_json = '{"name": "Ali", "age": 20, "gpa": 4.5}'
student_dict = json.loads(student_json)
student4 = Student4.from_dict(student_dict)



# Saving Object data to a JSON file 
import json


class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gpa": self.gpa
        }


student1 = Student("Ali", 20, 4.5)

with open("student.json", "w") as file:
    json.dump(student1.to_dict(), file)