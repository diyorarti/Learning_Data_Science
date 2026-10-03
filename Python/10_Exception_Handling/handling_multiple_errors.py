"""
The types of errors:
    1. ZeroDivisionError
    2. ValueError
    3. TypeError
    4. IndexError
    5. KeyError
    6. AttributeError
    7. FileNotFoundError
    8. NameError
    9. RecursionError
    10. ImportError / ModuleNotFoundError
    11. OverflowError
    12. KeyboardInterrupt
"""

# ZeroDivitionError
try:
    print(10/0)
except ZeroDivisionError:
    print("Can't divide by zero")

# ValueError
try:
    x = int("abc")
except ValueError:
    print("Invalid conversion")

# TypeError
try:
    print("3"/ 3)
except TypeError:
    print("Type mismatched")

# IndexError
try:
    lst = [1, 2, 3, 4]
    print(lst[5])
except IndexError:
    print("Index out of range")

# KeyError
try:
    person = {
        "name":"Ali",
        "Age":20
    }
    print(person['title'])
except KeyError:
    print("Key not found")

# AttributeError
try:
    "hello".append("x")
except AttributeError:
    print("invalid method")

# FileNotFoundError
try:
    open("file.txt")
except FileNotFoundError:
    print("File not found")

# NameError
try:
    print(x)
except NameError:   
    print("Variable not defined")

# RecursionError
def recursive():
    return recursive()
try:    recursive()
except RecursionError:
    print("Maximum recursion depth exceeded")

# ImportError / ModuleNotFoundError
try:
    import non_existent_module
except ImportError:
    print("Module not found")

# OverflowError
import math
try:
    math.exp(1000)
except OverflowError:
    print("Number too large to handle")

# KeyboardInterrupt
# try:    
#     while True:
#         pass            
# except KeyboardInterrupt:
#     print("Process interrupted by user")


# catching multiple errors
try:
    x = int("abc")
    z = 10/0
except (ValueError, ZeroDivisionError) as e:
    print(f"error occurred: {e}")

