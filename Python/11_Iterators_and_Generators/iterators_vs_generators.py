"""
Iterator 
    an object that lets you go through elements one by one
    Instead of loading at once, it gives values on demand
"""
# Basic Syntax
nums = [1, 2, 3, 4]
iterator = iter(nums)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

"""
Generator 
    a simpler wat to create iterators
"""
def generate(nums):
    for i in nums:
        yield i

gen = generate(nums)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


"""
🎯 TASK
✅ Step 1 — Generator (IMPORTANT)
    Create a generator function:    
        def valid_transactions(data):
            Rules:
                Yield only transactions where:
                amount is NOT None
                amount > 100
"""
data = [
    {"user": "Alice", "amount": 120},
    {"user": "Bob", "amount": 50},
    {"user": "Alice", "amount": 300},
    {"user": "Bob", "amount": None},
    {"user": "Charlie", "amount": 200},
]

# step -1 Generator
def valid_transactions(data):
    for i in data:
        if i['amount'] is not None and i['amount'] > 100:
            yield i 
# gen = valid_transactions(data)
# print(next(gen))

class Transaction:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.data):
            element = self.data[self.index]
            self.index += 1
            if element['amount'] is not None and element['amount']>100:
                return element
        raise StopIteration
        


# custom_iter = Transaction(data)
# print(next(custom_iter))
# print(next(custom_iter))
# print(next(custom_iter))

"""
🎯 Task: Find First Unique Element (LAZY)
    Write a function :
        It should return the first number that appears only once
⚠️ STRICT RULES (IMPORTANT)
    ❌ You CANNOT use:
        list.count()
        creating full frequency dict first
✅ You MUST use:
    generator OR custom iterator
    lazy evaluation
"""
nums = [2, 3, 4, 1, 2, 3, 5, 4, 5, 6, 7, 9, 10, 3, 4, 6]

def unique_num(nums):

    occurance_count = {}
    for i in nums:
        occurance_count[i] = occurance_count.get(i, 0) + 1

    for i in nums:
        if occurance_count[i] == 1:
            yield i 

# gen = unique_num(nums)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))



"""
"""