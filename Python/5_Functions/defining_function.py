"""
a function is a block of code that performs a specific task
"""

# greeting function 
def greet():
    name = input('What is your name: ')
    print(f'Assalomu alaykum {name}')

# greet()

# even vs odd function 
def check_number():
    number = int(input('Enter a number: '))

    if number%2 == 0:
        print(f"Entered number {number} is even")
    else:
        print(f"Entered {number} is odd")
check_number()