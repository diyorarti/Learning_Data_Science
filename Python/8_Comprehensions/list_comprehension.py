# List Comprehension
"""
a concise way to create a new list by:
    iterating over an existing iterable
    optionally filtering
    optionally transforming 
"""
# transforming list with comprehension
numbers = [1, 2, 3, 4, 5, 6]
res = [x*2 for x in numbers]
# print(res)

# filtering + transforming list with comprhension
even_nums_squared = [x ** 2 for x in numbers if x % 2 == 0]
# print(even_nums_squared)

# eqauvalent loop 
res = []
for i in numbers:
    if i % 2 == 0:
        res.append(i**2)
# print(res)

# labeling 
labels = ['odd' if x % 2 == 0 else 'even' for x in numbers]
# print(labels)

# nexted list comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
flat = [num for row in matrix for num in row]
# print(flat)

"""
🎯 Task

Using list comprehension, create a list of names of users who:
    are active
    and at least 18 years old
"""
users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False},
    {"name": "Diana", "age": 22, "active": True}
]

activa_over_18_users = [x['name'] for x in users if x['age'] >=18 and x['active']]

"""
🎯 Task

Using list comprehension, create a new list where:
    If the number is positive → square it
    If the number is zero or negative → replace it with "invalid"
"""
numbers = [3, -1, 10, 0, 7, -5, 8]
valid_squared_nums = [x**2 if x > 0 else 'invalid' for x in numbers]
print(valid_squared_nums)

