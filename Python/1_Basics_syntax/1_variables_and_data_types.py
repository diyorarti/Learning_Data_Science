# variable is like labeled box, data can be stored 

# int stores whole numbers 
age = 21
number = 103
print(age)
print(number)

# float stores decimal numbers 
price = 19.20
print(f"the price of apple {price} for a kg")

# str stores sting (data must be inside quotes)
name = 'Diyorbek'
print(f'My name is {name}, but people ofter call me Diyor')

# bool (Boolean) stores True/False 
is_student = True
print(f'is {name} a student ? {is_student}')

# checking data type 
print(type(age))


# problem 1 
'''
Creates 4 variables:
    Your name (string)
    Your age (integer)
    Your height (float)
    Whether you are a student (boolean)
Prints all variables
Prints the type of each variable
'''

my_name = "Diyorbek"
my_age  = 21
my_height = 1.70
student = True
print(f'My name is {my_name}, my age am a {my_age}, am I student? - {student}, my height is {my_height}')

print(type(my_name))
print(type(my_age))
print(type(my_height))
print(type(student))