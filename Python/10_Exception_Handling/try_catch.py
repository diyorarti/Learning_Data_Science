"""
It helps to catch error gracefully instead of crushing the program
"""

# zero divition error
def divition(a=int, b=int)-> int:
    return a / b

#print(divition(10,0)) the function is collapsed 

def divition1(a=int, b=int)->int:
    try:
        return a/b
    except:
        return "error happened"
    
print(divition1(10, 0))
print(divition1(10, 3))
