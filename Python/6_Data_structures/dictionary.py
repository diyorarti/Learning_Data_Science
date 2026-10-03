"""
Dictionary 
    key-value pairs 
    keys are unique
    Values can repeat
    Mutable
"""
person = {
    'name':'Ali',
    'age':23,
    'status':'married'
}
#print(person)

# adding
person['city']='Makka'
#print(person)

# upading 
person['age']=30
#print(person)

# pop() removes 
person.pop('status')
#print(person)
del person['age']
#print(person)

# .get() -> hanldes keys withou crushing programm
users = [
    {"name":"Ali", "age":20, "spend":None},
    {"name":"Vali", "age":32, "spend":1500},
    {"name":"G'ani", "age":25},
    {"name":"Nasiba", "age":24, "spend":1200}
]

# cleanind data (removing None)
# cleaned_data = [x for x in users if x['spend'] != None] -> it crushes because third used hasn't spend
cleaned_data = [x for x in users if x.get('spend') != None]
# print(cleaned_data)

"""
Dictionary unpacking
**x, 
    take all key-value pairs from dictionary x and unpack (spread) them
"""

transforming_users = [
    {
        **x,
        "name":x['name'].upper(),
        "Bonus":x['spend'] /20
    }
    for x in cleaned_data
]
# print(transforming_users)

"""
✅ Task:
Create a new list where for each user:
     a new field:
        is_adult = age >= 18
        Change "city" to lowercase
        Do NOT modify the original list
"""
users = [
    {"name": "Alice", "age": 20, "city": "Warsaw"},
    {"name": "Bob", "age": 17, "city": "Krakow"},
]

updated_users = [
    {
        **x,
        "is_adult":x['age']>=18,
        "city":x['city'].lower(),
    }
    for x in users
]
# print(updated_users)

# Grouping nested loop
"""
🎯 Your task
Create a function that returns:
    {
        "Alice": {"total": ?, "orders": ?, "avg": ?},
        "Bob": {"total": ?, "orders": ?, "avg": ?},
    }

⚠️ Rules (important)
    ✅ Only include status == "completed"
    ❌ Ignore rows where amount is None
    📊 Calculate:
        total → sum of amounts
        orders → number of valid orders
        avg → average amount (total / orders)
"""
data = [
    {"order_id": 1, "customer": "Alice", "amount": 250, "status": "completed"},
    {"order_id": 2, "customer": "Bob", "amount": 120, "status": "pending"},
    {"order_id": 3, "customer": "Alice", "amount": 200, "status": "completed"},
    {"order_id": 4, "customer": "Bob", "amount": 80, "status": "completed"},
    {"order_id": 5, "customer": "Alice", "amount": None, "status": "completed"},
    {"order_id": 6, "customer": "David", "amount": 300, "status": "cancelled"},
    {"order_id": 7, "customer": "Bob", "amount": 150, "status": "completed"},
]

def aggregation(data):
    # filtering : amount is None and status == 'completed'
    cleaned_data = list(filter(lambda x: x['amount'] is not None and x['status'] == 'completed', data))
    
    # grouping total amount and total orders for per customer
    result = {}
    for x in cleaned_data:
        customer = x['customer']
        if customer not in result:
            result[customer] = {
                "total":x.get('amount'),
                "orders":1
            }
        else:
            result[customer]['total'] += x['amount']
            result[customer]['orders'] += 1

    # finding avg
    for x in result:
        total = result[x]['total']
        orders = result[x]['orders']
        result[x]['avg'] = total / orders
    return result

res = aggregation(data)
print(res)