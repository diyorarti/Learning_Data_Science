"""
Solid Principles are advanced but very important OOP Design principles
    They help you write code that is:
        - Clean
        - Easy to maintain
        - Easy to extend
        - Less bugy 
        - Professional
    Solid has 5 Principles:
        1. S - Single Responsibilit Principle
        2. O - Open/Closed Principle
        3. L - Liskov Substituion Principle
        4. I - Interaface Segregation Principle
        5. Dependency Inversion Principle

    SOLID Summary Table:
    | Principle                 | Simple meaning                                              |
    | ------------------------- | ----------------------------------------------------------- |
    | S — Single Responsibility | One class should have one main job                          |
    | O — Open/Closed           | Add new behavior without changing old code                  |
    | L — Liskov Substitution   | Child classes should work wherever parent class is expected |
    | I — Interface Segregation | Do not force classes to implement methods they do not need  |
    | D — Dependency Inversion  | Depend on abstractions, not concrete classes                |

"""


"""
1. S - Single Responsibility Principle
    Meaning ---> A class should have one reponsibility
                 A class - one job

"""
# bad example
class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        return "Statistics calculated"

    def save_to_file(self):
        return "Report saved to file"

    def send_email(self):
        return "Report sent by email"
    
# better example
class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        return "Statistics calculated"


class ReportSaver:
    def save_to_file(self, report):
        return "Report saved to file"


class EmailSender:
    def send_email(self, report):
        return "Report sent by email"
    

"""
2. O - Open/Closed Principle
    Meaning --> a class shoud be:
                    - open for extension
                    - closed for modification 
    Simply - You should be able to add new behavior without changing old working code

"""
# bad example 
class PaymentProcessor:
    def pay(self, payment_type, amount):
        if payment_type == "card":
            return f"Paid {amount} by card"
        elif payment_type == "paypal":
            return f"Paid {amount} by PayPal"
# Problem: If we want to add crypto payment, we must change the existing class:, elif payment_type == "crypto":

# better example
class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} by card"


class PayPalPayment:
    def pay(self, amount):
        return f"Paid {amount} by PayPal"


class CryptoPayment:
    def pay(self, amount):
        return f"Paid {amount} by crypto"


class PaymentProcessor:
    def process(self, payment_method, amount):
        return payment_method.pay(amount)
    


"""
3. L - Liskov Substitution Principle
    Meaning --> A class should be replaceable for its parent class without breaking the program
    Simply --> if class B inherits from class A, we should be able to use B whenever A is expected
"""
# good example
class Bird:
    def eat(self):
        return "Eating"


class Sparrow(Bird):
    def eat(self):
        return "Sparrow is eating"


def feed_bird(bird):
    print(bird.eat())


# feed_bird(Bird())
# feed_bird(Sparrow())

# bad example
class Bird:
    def fly(self):
        return "Flying"


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")
    
# Problem A Penguin is a bird, but not all birds can fly.
# So if we write:
def make_bird_fly(bird):
    print(bird.fly())
# This works for normal birds but breaks for penguins.

# better design 
class Bird:
    def eat(self):
        return "Eating"


class FlyingBird(Bird):
    def fly(self):
        return "Flying"


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    pass


"""
4. I - Interface Segregation Principle
    Meaning --> A class should not be forced to implement methods it does not need.

    Simple meaning:
        Do not create one huge interface with too many methods.
        Create smaller, specific interfaces/classes instead.
    Python does not use interfaces exactly like Java, but we can understand this idea with abstract classes.
"""
# bad example
from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass
# Now imagine a robot worker.
class RobotWorker(Worker):
    def work(self):
        return "Robot is working"

    def eat(self):
        raise Exception("Robot does not eat")
# Problem: Robot is forced to implement eat(), even though it does not need it.

# Better design 
from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"


class RobotWorker(Workable):
    def work(self):
        return "Robot is working"
    

"""
5. D - Dependency Inversion Principle
    Meaning 
        High-level classes should not depend dicectly on low-level classes
        They should dpend on abstactions.
        Simple
            Your main class should not be tightly connected to one specific implementation
"""
# bad exampl
class MySQLDatabase:
    def save(self, data):
        return f"Saving {data} to MySQL"


class UserService:
    def __init__(self):
        self.database = MySQLDatabase()

    def save_user(self, user):
        return self.database.save(user)
# Problem: UserService is tightly connected to MySQLDatabase. If later we want to use PostgreSQL or MongoDB, we must modify UserService.

# better example
class MySQLDatabase:
    def save(self, data):
        return f"Saving {data} to MySQL"


class PostgreSQLDatabase:
    def save(self, data):
        return f"Saving {data} to PostgreSQL"


class UserService:
    def __init__(self, database):
        self.database = database

    def save_user(self, user):
        return self.database.save(user)
