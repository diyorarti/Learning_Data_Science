# Set comprehension
"""
is a concise way to create set: 
    iterating over an existing iterable
    optionally filtering
    optionally transforming 
"""
numbers = [1, 2, 3, 2, 5, 5, 2, 3, 1]

res = {x** 2 for x in numbers}
# print(res) -> {1, 4, 9, 25} , every element appears once 


# real world example
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"] 
# unique names
unique_names = {n for n in names}
# print(unique_names)

"""
👉 Create a set of:
    word lengths
    only for words longer than 5 characters
"""
words = ["apple", "banana", "apple", "cherry", "banana"]

long_words_length = {len(x) for x in words if len(x) > 5}
#print(long_words_length)

"""
🎯 Task
Using set comprehension, create a set of:
    all unique words
    converted to lowercase
    excluding words shorter than 4 letters
"""
sentences = [
    "Python is great",
    "I love coding",
    "Python is powerful"
]
unique_words = {x.lower() for word in sentences for x in word.split() if len(x) >=4 }
# print(unique_words)

