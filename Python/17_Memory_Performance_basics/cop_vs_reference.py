# Referece 
"""
a variable pointing to a location in memory where the data is stored
🏠 Object = a house
📍 Reference = the address of the house

"""
# a is the addres for the list [1, 2, 3] created in memory
a = [1, 2, 3]

# Python doesn't copy the list, instead it copies the address
b = a 
"""
So: 
    a[1,2,4] list -> adress X
    b[1,2,4] list -> adress X
"""

# why it matters? ->
b.append(4) # here, b is not changed , the shared object is changed 
# print(a)
# print(b)

# Correct mental model:
"""
a ──┐
    ├──> [1,2,3]
b ──┘
"""

# immutability
a = 10
b = a # here it created a new object in memory because integers are immutable 
b = 20 # it will not effect a because it will create a new object in memory for b
# print(a)
# print(b)

a = [1,2]
b = a
b = [3,4]
# print(a)
# print(b)

list1 = [1,2,3]
list2 = list1
list2.append(4)
# print(list1)
# print(list2)

# Copy
"""
creating new object in memory, instead of sharing existing one
    two main ways of copying:
        1. Shallow copy: -> create a new outer object but inner objects are still shared
        2. Deep copy: -> create a new outer object and also recursively copy inner objects
"""
# shallow copy
a = [1,2,3]
copy = a.copy() # create a new list in memory
copy.append(4)
# print(a)
# print(copy)

list2D = [[1,2], [3,4]]
shallow_copy = list2D.copy() # created a new list in memory but inner lists are shared 
shallow_copy[0].append(5)
# print(list2D)
# print(shallow_copy)

# deep copp 
import copy

list3d = [[[1,2], [3,4]], [[5,6], [7,8]]]
deep_copy = copy.deepcopy(list3d) # createed a new list in memory and also recursively copy inner lists
deep_copy[0][0].append(9)
# print(list3d)
# print(deep_copy)

"""
🎯 Task

You are given a VERY large dataset:
    data = list(range(10_000_000))   # 10 million numbers

    Compute the sum of squares of EVEN numbers
"""



# Naive approach:
def sum_of_squares_even():
    total = 0
    for i in range(10_000_000):
        if i % 2 == 0:
            total += i ** 2
    return total
# print(sum_of_squares_even())

# Optimized approach:
def sum_of_squares_even_optimized():
    total = sum(x**2  for x in range(10_000_000) if x % 2 == 0 )
    return total
# print(sum_of_squares_even_optimized())
