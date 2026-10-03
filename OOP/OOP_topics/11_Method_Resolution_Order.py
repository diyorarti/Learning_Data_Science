"""
Method Resolution Order (MRO)
    MRO means Method Resolution Order, it is the order Python follows when it searches for a method or attribute in a class hierarchy.
    MRO = the order Python uses to find methods/attributes

MRO helps Python decides which method to call when multiple classes have the same method name
    1. Inheritance
    2. Method overriding
    3. Multiple inheritance
    4. super()
    5. Avoiding confusion in large class hierarchies

MRO answers this question:
    "When I call this method, where does Python look first, second, third...?"

RULE:
    1. Python searches from the child class first.
    2. Then it searches parent classes.
    3. In multiple inheritance, Python usually searches left to right.
    4. Use ClassName.mro() to confirm the exact order.
    5. super() calls the next class in the MRO, not always the direct parent.

Pthon searches in following order:
    1. Does Dog(class) has sound() ?
    2. No
    3. Does Animal(class) has sound() ?
    4. Yes, Use Animal.sound()

So, MRO = Dog -> Animal -> object
"""
class Animal:
    def sound(self):
        return "Some animal sound"

class Dog(Animal):
    pass

dog = Dog()
# print(dog.sound())


"""
MRO with method overriding
    Python searches like this 
        1. Does Dog have sound()?
        2. Yes. Use Dog.sound().
        3. Stop searching.
"""
class Animal:
    def sound(self):
        return "Some animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
# print(dog.sound())

# how to see MRO 
# method 1 .mro()
#print(Dog.mro())

# method 2  __mro__
#print(Dog.__mro__)


"""
MRO in Multiple Inheritance
    Multiple inheritance measn one class inherits from more than one parent class

Output:
    Father's skill
    [Child, Father, Mother, object]
Why did Python uses Father.skill() ?
    Because Father class comes first here class Child(Father, Mother):
So Python searches:
    Child -> Father -> Mother -> object
"""
class Father:
    def skill(self):
        return "Father's skill"
class Mother:
    def skill(self):
        return "Mother's skill"
class Child(Father, Mother):
    pass

child = Child()
# print(child.skill())
# print(Child.mro())


"""
Diamont Problem -> The Dianmon problem happens when two parent classes inherit from the same grandparent class

MRO -> D -> B -> C -> A -> object

Python doesn't check A twice, it follows a smart order called C3 Linearization.
Python searches left to rigjt , but it avoids repeating parent classes incorrectly

OUTPUT:
    B
    [D, B, C, A, object]
Python searches:
    1. D: show()? No.
    2. B: show()? Yes.
    3. Use B.show().
    4. Stop.
"""
class A:
    def show(self):
        return "A"

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
# print(d.show())
# print(D.mro())


"""
MRO and super()
    super() calls the next class in the MRO
Output:
    D -> B -> C -> A
    [D, B, C, A, object]
Important: In class B, this line:
    super().show()
does not jump directly to A.
It calls the next class in the MRO after B, which is C.
So the order is: D -> B -> C -> A
This is one of the most important MRO ideas.
"""
class A:
    def show(self):
        return "A"
class B(A):
    def show(self):
        return "B -> " + super().show()
class C(A):
    def show(self):
        return "C -> " + super().show()
class D(B, C):
    def show(self):
        return "D -> " + super().show()
d = D()
# print(d.show())
# print(D.mro())

