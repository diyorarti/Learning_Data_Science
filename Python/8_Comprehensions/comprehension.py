# Comprehension
"""
Comprehension 
    is a compact way:
        loop over data
        optionally filter it
        optionally transform it
        and build a new collection
    Advantages:
        they replace common patterns (loop +append)
        they make intent clearer
        they reduce errors
        they are ofter faster
        common in real code

"""

orders = [
    {"customer": "Alice", "items": ["laptop", "mouse"], "total": 1200},
    {"customer": "Bob", "items": ["keyboard"], "total": 150},
    {"customer": "Alice", "items": ["monitor"], "total": 300},
    {"customer": "Charlie", "items": ["mouse", "keyboard"], "total": 200},
]
"""
🎯 Tasks
✅ 1. List Comprehension
    Create a list of totals greater than 200

✅ 2. Set Comprehension
    Create a set of all unique items ordered

✅ 3. Dictionary Comprehension (main part 🔥)
Create a dictionary where:
    key → customer name
    value → total amount spent by that customer
    include only customers whose total spending ≥ 500
"""

# list
top_income_orders_list = [x['total'] for x in orders if x['total']>200]
# print(f"List Comprehension {top_income_orders_list}")

# set
unique_items = {
    item 
        for x in orders 
        for item in x['items']
}
# print(f"List Comprehension {unique_items}")

# Dict 
totals = {}
for order in orders:
    totals[order['customer']] = totals.get(order['customer'], 0)+order['total']
top_customers = {customer:spending for customer, spending in totals.items() if spending>=500}

# print(f"Dict Comprehension {top_customers}")


