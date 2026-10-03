"""
Set is a collection of unuque (no duplication) and unordered elements 
"""
nums = {1, 2, 3, 4, 4} # renturns {1, 2, 3, 4} , only one 4
#print(nums)

nums2 = {3, 2, 5, 1} # unordered
#print(nums2)

nums.add(5) # adding elemnts 
print(nums)

nums.remove(2) # removing element , returns error if not found
print(nums)
nums.discard(6) # remiving element, no error if not found


a = {1, 2, 3, 5, 6}
b = {3, 4, 5, 6, 7}
print(a | b) # combining sets

print(a & b) # Intersection, (common elemnts in both sets)