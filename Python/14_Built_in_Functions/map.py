"""
maop(function, iterable)
    aplies the function to every item in an iterable (like list, tuple etc)
    return a map object (an iterator)
"""
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

results = map(square, numbers)
# print(list(results))

# using map() with Lambda function 
restults1 = map(lambda x: x / 2 , numbers)
# print(list(restults1))

# map() with multiple iterables
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
restults2 = map(lambda x, y: x+y, num1, num2)
# print(list(restults2))

names = ['  Alice', 'bob', 'charlie   ']
res_names = list(map(str.strip, names))
# print(res_names)
res_names1 = list(map(lambda x: x.strip().capitalize(), names))
# print(res_names1)
