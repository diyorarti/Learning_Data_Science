"""
🧪 Problem 1 — Data Cleaning + Transformation

🎯 Tasks
1️⃣ Keep only users who:
age ≥ 18
2️⃣ Clean the data:
remove spaces from names
make names lowercase
3️⃣ Extract ONLY emails
and convert them to lowercase
✅ Final Expected Output
['alice@gmail.com', 'charlie@gmail.com']
"""

users = [
    {"name": " Alice ", "age": 25, "email": "ALICE@gmail.com"},
    {"name": "bob", "age": 17, "email": "bob@gmail.com"},
    {"name": "  CHARLIE", "age": 30, "email": "charlie@gmail.com"},
    {"name": "David", "age": 15, "email": "DAVID@gmail.com"}
]

# Solution - 1
def clean_extract_emails(users) -> list:
    # keep only users who are adults
    adult_users = list(filter(lambda x: x['age'] >= 18, users))
    # cleaning the data
    cleaned_users = list(map(lambda x: {
        'name': x['name'].strip().lower(),
        'age':x['age'],
        'email':x['email'].lower()
        }, adult_users))
    # extracting emails
    emails = list(map(lambda x: x['email'], cleaned_users))
    return emails

res = clean_extract_emails(users)
# print(res)

# solution - 2
def clean_extract_emails_v2(users)->list:
    result = []
    for user in users:
        if user['age']>=18:
            user['name'] = user['name'].strip().lower()
            result.append(user['email'].lower())
    return result

res_v2 = clean_extract_emails_v2(users)
print(res_v2)


# best solution 
def clean_extract_emails(users):
    adult_users = list(filter(lambda x: x['age'] >= 18, users))

    cleaned_users = list(map(lambda x: {
        'name': x['name'].strip().lower(),
        'age': x['age'],
        'email': x['email'].lower()
    }, adult_users))

    emails = list(map(lambda x: x['email'], cleaned_users))

    return emails
