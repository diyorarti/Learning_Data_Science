# Identity operators (is, is not) are used to check whether the Same object , == compares values, is compares memory(identity)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # return True, because the same values
print(a is b) # return False, because they are stored as different objects

c = a
print(a is c) # return True, because the same objects in memory

print(a is not c) # return False, because the same objects 
print(a is not b) # return True, because they are different objects in memory