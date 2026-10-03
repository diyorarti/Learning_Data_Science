"""
🧪 Problem 2 — Orders Aggregation
🎯 Tasks
        1️⃣ Keep only "completed" orders
        2️⃣ Compute total spending per customer
        3️⃣ Find the customer who spent the most
"""
from functools import reduce
orders = [
    {"customer": "Alice", "amount": 250, "status": "completed"},
    {"customer": "Bob", "amount": 100, "status": "pending"},
    {"customer": "Alice", "amount": 300, "status": "completed"},
    {"customer": "Charlie", "amount": 200, "status": "completed"},
    {"customer": "Bob", "amount": 150, "status": "completed"}
]

def find_most_spend_customer(orders)->tuple:

    total_spendings = {} 
    for order in orders:
        if order['status'] == 'completed':
            customer = order['customer']
            amount = order['amount']
            total_spendings[customer] = total_spendings.get(customer, 0) + amount
    
    return reduce(lambda x, y: x if x[1] > y[1] else y, total_spendings.items())
    
most_spending_customer = find_most_spend_customer(orders)
print(most_spending_customer)