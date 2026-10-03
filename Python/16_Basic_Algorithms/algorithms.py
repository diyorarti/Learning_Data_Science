# Algorithms
"""
Algorithm 
    A step by step procedure to solve a problem
"""

def add(a, b):
    return a + b
"""
1. Take input
2. Add
3. Return result
"""

# Wyh Algorithms matter
"""
Solve problem efficienlty
Write faster code
Pass technical interviews
Work with Large data
"""

# a problem "Find a number in a list"'
# Liner search -> Slow because , it checks one by one
def find(nums, target):
    for x in nums:
        if x == target:
            return True
    return False
# Binary Search -> much faster 
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

# Big-O notation 
"""
Big-O 
    it measures how fast an algorithm grows
    smaller = better
"""

# Type of Algorithms
"""
Searching
    Linear search
    Binary search
Sorting
    Bubble sort 
    Merge Sort
    Quick sort
Recursion
    Functions that call themseles
Greedy Algorithms
    Make the best choice at each step
Graph Algorithms
    used in Maps, Networks, AI
"""
