"""
A sequence is a collection of items stored in order
main types:
    String (str)
    Lists (list)
    Tuples (tuple)
"""

# String , String squence is Immutable
name = "Diyorbek"
print(f'Full name is {name}')
print(f"people often call {name[0:5]}")
#name[0] = 'A' it is wrong
print(name)

# Lists 
"""
a List is a collection of items (can be different data types)
List is mutable
"""
numbers = [1, 2, 3, 4, 5]
mixed = [20, 'ALi', True]
print(numbers)
numbers[1] = 100
print(numbers)
# common opertations in List
# 1- append() adding element 
num = []
num.append(20)
num.append(10)
num.append(30)
print(num)
# 2 - remove() removing element
num.remove(10)
print(num)

# Tuple , A tuple is a list but immutable
coords = (10, 20, 30, 40)
print(coords[0])


