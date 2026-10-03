"""
zip()
    combines mutiple iterables element-wise 
"""

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

results = list(zip(names, scores))
# print(results)
# print(type(results))

res_dict = dict(zip(names, scores))
# print(res_dict)
# for i in res_dict:
#     print(type(i))