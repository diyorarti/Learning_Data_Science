"""
reduce()
    takes a sequence and reduces it to a single value
    map() -> transforms -> many
    filter() -> slects -> many 
    reduce() -> reduces -> one
    unlike map and filter, reduce should be imported from functools module
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x+y, numbers)
# print(res)

# finding max value in a list
max_value = reduce(lambda x, y: x if x > y else y, numbers)
# print(max_value)

# combine strings 
words = ['Hello', 'Python', 'Programming,', 'coding', 'is', 'fun']
res1 = reduce(lambda x, y: x + " " + y, words)
# print(res1)

# finding max score student
students = [
    {"name": "A", "score": 80},
    {"name": "B", "score": 95}
]

max_score_student = reduce(lambda x, y:x if x['score'] > y['score'] else y, students)
print(max_score_student)


"""
🎯 Tasks:
Get names of customers whose orders are:
    "completed"
    AND amount ≥ 200
"""
orders = [
    {"id": 1, "customer": "Alice", "amount": 250, "status": "completed"},
    {"id": 2, "customer": "Bob", "amount": 100, "status": "pending"},
    {"id": 3, "customer": "Charlie", "amount": 300, "status": "completed"},
    {"id": 4, "customer": "David", "amount": 50, "status": "cancelled"},
    {"id": 5, "customer": "Emma", "amount": 400, "status": "completed"}
]

print(type(orders))