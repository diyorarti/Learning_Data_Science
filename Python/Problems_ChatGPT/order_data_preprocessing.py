r"""
🎯 Your Task:
Build a Python CLI script that processes this dataset (C:\Users\k\Problem-Solving\Python\Problems_ChatGPT\files\order.json).

✅ 1. Load Data:
    Read JSON file
    Handle:
    File not found
    Invalid JSON

✅ 2. Clean Data:
    Remove records where: damount is None
    Hanle missing keys safely

✅ 3. Filter Data
    Keep only:
        status == "completed"
        amount > 100

✅ 4. Transform Data
    For each order:
        Convert customer → uppercase
    Add new field:
        discounted_amount = amount * 0.9

✅ 5. Aggregation (IMPORTANT 🔥)
    Compute:
        📊 Global stats:
            Total revenue (sum of amounts)
            Average order value
        👤 Per customer:
            Total spent per customer
            Number of orders per customer

    👉 Example:
        {
        "ALICE": {"total": 400, "orders": 2},
        "DAVID": {"total": 300, "orders": 1}
        }

✅ 6. Use Functions
    Split your code:
        load_data()
        clean_data()
        filter_data()
        transform_data()
        aggregate_data()

✅ 7. Use CLI Arguments
    Run:
        python script.py orders.json

✅ 8. Use a Generator (Memory Efficient)
    Create a generator that:
        Yields only completed orders

✅ 9. Sort Results
    Sort customers by:
        Highest total spending

✅ 10. Output (Formatted)
    Print:
        Total revenue: X
        Average order: X
"""
import json

# 1 loading data
def load_data(path):
    try:
        with open(path) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: File not Found")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON")
        return []
data = load_data("Python/Problems_ChatGPT/files/order.json")

# 2 clearning data
def clean_data(data):
    # built-in function filter()
    # cleaned_data = list(
    #     filter(lambda x: x.get('amount') is not None, data)
    # )
    # list comprehension 
    cleaned_data = [x for x in data if x.get('amount') is not None]
    return cleaned_data
cleaned_data = clean_data(data)

# 3 Filtering data
def filter_data(data):
    # built-in function filter()
    filtered_data = list(
        filter(
            lambda x: x.get('status') == 'completed' and x.get('amount') > 100, 
            data
        )
    )
    # list comprehension
    # filtered_data = [x for x in data if x.get('status') == 'completed' and x.get('amount')>100]
    return filtered_data
filtered_data = filter_data(cleaned_data)

# 4 transforming data
def transform_data(data):
    # dict unpacking method-> **x
    return [
        {
            **x,
            "customer":x.get('customer').upper(),
            "discounted_amount ":x.get('amount')*0.9
        }
        for x in data
    ]
transformed_data = transform_data(filtered_data)


# 5 aggregation 
def aggregate(data):
    result = {}
    for x in data:
        customer = x['customer']
        if customer not in result:
            result[customer]={
                "total":x.get('amount'),
                "orders":1
            }
        else:
            result[customer]['total'] += x['amount']
            result[customer]['orders']+= 1
    return result

aggregated_data = aggregate(transformed_data)

def sorting(data):
    return sorted(data.items(), key=lambda x: x[1]['total'], reverse=True)

sorted_customers = sorting(aggregated_data)


def get_element(data):
    top = 1
    for name, info in data:
        yield f"{top} -> {name} - total: {info['total']}, orders:{info['orders']}"
        top += 1

gen = get_element(sorted_customers)
print("Top customers: ")
print(next(gen))
print(next(gen))
print(next(gen))

