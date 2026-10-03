"""
enumerate()
    adds a counter(index) to an iterable.
    returns (index, value)

"""
names = ['Alice', 'Bob', 'Charlie']

res = list(enumerate(names))
# print(res)

# for index, name in enumerate(names):
#     print(f'{index}: {name}')

# # customer start index
# for index, name in enumerate(names, start=1):
#     print(f'{index}: {name}')
