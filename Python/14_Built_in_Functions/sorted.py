"""
sorted()
    returns a sorted list from anuy iterable object 

"""
numbers = [5, 2, 9, 1, 5, 6]
res = sorted(numbers)
# print(res)  # Output: [1, 2, 5, 5, 6, 9]

# important detail: about sorted() vs .sort()
res1 = sorted(numbers) # returns a new list 
res2 = numbers.sort() # modfies original list

# reserve sorting
res3 = sorted(numbers, reverse=True)
# print(res3) # Output: [9, 6, 5, 5, 2, 1]


# sorting dict
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 78}
]
sored_students = sorted(students, key=lambda x: x['score'], reverse=True)
# print(sored_students)

sored_students_names = sorted(students, key=lambda x: x['name'], reverse=True)
# print(sored_students_names)

