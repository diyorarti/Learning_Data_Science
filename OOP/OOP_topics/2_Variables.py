"""
Variables are used to store data inside classes and objects


1. Instance variables   --> Belong to a specific object
2. Class variables      --> Belong to the class itself
3. Local Variables      --> Exist only inside a method or function
"""

class Student:
    university = "WSB" # class Variable

    def __init__(self, name, age):
        self.name = name           # Instance Variable
        self.age = age             # Instance Variable

    def show_info(self):
        message = "Student info: " # local variable
        return f"{message} {self.name}, {self.age}, {Student.university}"


# student1 = Student('Ali', 20)

# print(student1.university)
# print(student1.show_info())



class BankAccount:
    bank_name = "National Bank" # class variable

    def __init__(self, owner, balance, account_type):
        self.owner = owner                         # instance variable             
        self.balance = balance                     # instance variable
        self.account_type = account_type           # instance variable

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("in suficient balance")
    
    def get_info(self):
        return f"Owner: {self.owner} | Balance: {self.balance} | Type: {self.account_type} | Bank: {self.bank_name}"

account1 = BankAccount("Ali", 500, "Savings")
account2 = BankAccount("Vali", 1000, "Business")

account1.deposit(200)
account2.withdraw(300)

print(account1.get_info())
print(account2.get_info())