"""
Sets 
    unordered collection
    no duplicates allowed
    mutable
    no indexing because sets are unordered
"""
set1 = {1, 2, 3, 3}
#print(set1)

# add() adding element 
set1.add(4)
#print(set1)

# remove() returns error if element not found
set1.remove(4)
#print(set1)

# discard() safe
set1.discard(5) # no element 5 but still works
#print(set1)

# combining sets
set2 = {3, 4, 5}
print(set1 | set2)