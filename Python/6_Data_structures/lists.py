"""
Lists 
    ordered collection
    mutable
    can store different data types
"""

my_list = [20, 'Diyor', 4.9, True]

# adding elements
num_list = [10, 20, 30, 40]
#print(num_list)
num_list.append(50)
#print(num_list)

# adding element to specific splace
numbers = [10, 20, 30, 40]
numbers.insert(1, 1000)
#print(numbers)

# removing elements
number = [10, 20, 30, 40]
number.pop() # remove the last element
#print(numbers)
number.pop(1) # remove the given index element
#print(number)
number.remove(30) # remove the given element
#print(number)


# Copy vs Reference 
a = [1, 2, 3, 4]
b = a.copy()
#print(a)
#print(b)
#print(a == b) # True
#print(a is b) # False



def process_list(nums: list[int]) -> list[int]:
    new_list = []
    for num in nums:
        if num % 2 != 0:
            new_list.append(num * 2)
    
    return new_list

list_num = [1, 2, 3, 4]
#print(process_list(list_num))


# list methods
# 1 append() used to add element to list
nums = [1, 2]
nums.append(3)
#print(nums)

# 2 insert used to add elemnt to specific index of list
nums.insert(0, 120)
#print(nums)

# extend () used to add list (multiple elements)
new_elements = [5, 6, 7]
nums.extend(new_elements)
#print(nums)

# remove () remove elements by value
nums.remove(120)
#print(nums)

# pop remove (last element ) or (chosen index element)
nums.pop() # removes last element 7
#print(nums)
nums.pop(0) # removes first element 1
#print(nums)

# count() counts elemnt occurences 
nums_list = [1, 2, 1, 1, 2, 3, 4, 5, 1]
#print(nums_list.count(1))

# sort() sorts elements
list1 = [3, 1, 2, 10, 9]
list1.sort()
#print(list1)

# reverse() descending soroting 
list1.reverse()
#print(list1)

# clear() removes elements
list1.clear()
print(list1)

