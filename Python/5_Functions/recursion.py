"""
Recursion is when a function calls itself to solve a problem
Recursive function has two parts:
    Base Case (stopping condition)
        prevents infinite recursion
    Recurcive Case
        Function calls itself with a smaller/simpler input
"""
def countdown(n):
    if n == 0: # base case (stop)
        return
    print(n)
    countdown(n-1) # recursive call

#countdown(10)

def count(n):
    a += 1
    if a == n: # base case
        return n
    print(a)
    count(a) # recursion case
#count(10)

def print_n(n):
    if n == 0:   # base case
        return
    print_n(n - 1)   # recursive call
    print(n)         # print after recursion

#print_n(10)

def test(n):
    if n == 0:
        return
    print(n)
    test(n - 1)
    print(n)

# test(3)