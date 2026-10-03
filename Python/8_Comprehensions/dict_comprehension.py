# Dict comprehension
"""
a concise way to create a dictionary:
    a loop
    optional filtering
    optional transforming

"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = {f"{x} square": x**2 for x in numbers}
# print(squared)

# Uquivalent (very long)
squared_nums = {}
for x in numbers:
    squared_nums[f"{x} squre "] = x**2
# print(squared_nums)

# filtering + tranforming
even_squared = {x: x**2 for x in numbers if x % 2 == 0}
# print(even_squared)

# even vs odd 
labeling = {x:('even' if x % 2 == 0 else 'odd') for x in numbers}
# print(labeling)

# real world example of comprehension
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30}
]

users_with_ages = {x['name']: x['age'] for x in users}
# print(users_with_ages)

"""
🎯 Task

Using dictionary comprehension, create a dictionary where:
    key → product name
    value → price after 10% discount
    include only products that are in stock
"""
products = [
    {"name": "laptop", "price": 1200, "in_stock": True},
    {"name": "mouse", "price": 25, "in_stock": True},
    {"name": "keyboard", "price": 75, "in_stock": False},
    {"name": "monitor", "price": 300, "in_stock": True}
]
products_in_stock = {x['name']: round(x['price']*0.9, 2) for x in products if x['price'] > 100 and x['in_stock']}
#print(products_in_stock)
"""
Modify your solution so that:
    key → product name
    value → "expensive" if discounted price ≥ 1000, otherwise "cheap"
"""
categorized_products = {name: ('expensive' if price >= 1000 else 'cheap') for name, price in products_in_stock.items()}
# print(categorized_products)

"""
🎯 Task

Using dictionary comprehension, create a dictionary where:
    key → student name
    value → average score
    include only students whose average ≥ 70
"""
students = [
    {"name": "Alice", "scores": [80, 90, 100]},
    {"name": "Bob", "scores": [60, 70]},
    {"name": "Charlie", "scores": [30, 40, 50]},
    {"name": "Diana", "scores": [90, 95]}
]
high_performance_students = {x['name']:sum(x['scores'])/len(x['scores']) for x in students if sum(x['scores'])/len(x['scores']) >=70 }
# print(high_performance_students)

"""
Temporary Variable:
    := -> walrus ooperator 
"""
top_students = {x['name']: avg for x in students if (avg := sum(x['scores']) / len(x['scores'])) >= 70 }
# print(top_students)