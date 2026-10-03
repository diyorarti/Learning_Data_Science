"""
Function annotations (also called type hits) let you specify the expected types:
    Parameters 
    Return value

"""

def function_name(param: type) -> return_type:
    pass

def add(a:int, b:int) -> int:
    return a+b
 
print(add(2,3))