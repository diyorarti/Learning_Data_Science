"""
filter()
    is usedto select elements from an iterable based on a condiftion
    map() -> transforms elements of an itable data 
    filter() -> selects elements of an iterable data
"""
def is_even(num):
    if num % 2 == 0:
        return num

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(is_even, num1)
# print(list(even_numbers))


# filter() with lambda function
odd_nums = list(filter(lambda x: x%2 != 0, num1))
# print(odd_nums)


"""
🎯 Task
👉 Create a list of names of students who passed
"""
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 30},
    {"name": "Emma", "score": 92}
]
def is_passed(student):
    return student['score'] >=50
def get_name(student):
    return student['name']

# passed_students = list(map(get_name, filter(is_passed, students)))
# print(passed_students)

"""
🎯 Task 
Create a list of product names whose price is 50 or more.
"""

products = [
    {"name": "Laptop", "price": 800},
    {"name": "Mouse", "price": 20},
    {"name": "Keyboard", "price": 50},
    {"name": "Monitor", "price": 150},
    {"name": "USB Cable", "price": 10}
]

def is_expensive(prducts):
    return prducts['price'] >= 50
def get_product_name(products):
    return products['name']

expensive_products = list(map(get_product_name, filter(is_expensive, products)))
# print(expensive_products)

# solution with lambda function
expensive_products1 = list(map(lambda x: x['name'], filter(lambda x: x['price'] >= 50, products)))
# print(expensive_products1)

