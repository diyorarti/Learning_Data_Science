"""
A dictionary stores data in key-value pairs
"""

person = {
    'name':'Diyorbek',
    'age':21,
    'is_student':True
}
# print(person['name'])

# adding/updating values 
person['height'] = 1.70
# person['age'] = 22
# print(person)

# removing items
person.pop('age')
# print(person)

# .items() used to extract items of dict 

spendings = {
    "Alice": 550,
    "Charlie": 200,
    "Bob": 150,
    'Alice':450
}

# for i in spendings:
#     print(i) # it prints only keys of dict, 

# for i in spendings.items():
#     # print(i) # it prints every single item of dict 

# for item in spendings.items():
#     print(type(item))
#     print(item[1])
# after extrating items of dict, index used to extract elements of item , because now they are tuples

# .get() function 
"""
Behavior:
    if key exits -> returns it's value
    if not -> return default (not error)
"""


# checking an element in dict
my_dict = {
    "name":"Diyorbek",
    "age":21
}
# in checks keys of dict, not values 
# if "Diyorbek" in my_dict:
#     print("Exists")
# else:
#     print("Not exists")

print(my_dict['age'])
