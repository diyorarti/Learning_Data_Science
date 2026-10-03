"""
Special / Magic / Dunder Methods in Python OOP
    They are methods that start and end with double underscores:
| Method         | Used for                            |
| -------------- | ----------------------------------- |
| `__init__`     | Initializes object                  |
| `__str__`      | User-friendly string representation |
| `__repr__`     | Developer/debugging representation  |
| `__len__`      | `len(object)`                       |
| `__eq__`       | `object1 == object2`                |
| `__lt__`       | `object1 < object2`                 |
| `__gt__`       | `object1 > object2`                 |
| `__add__`      | `object1 + object2`                 |
| `__sub__`      | `object1 - object2`                 |
| `__mul__`      | `object1 * object2`                 |
| `__getitem__`  | `object[index]`                     |
| `__setitem__`  | `object[index] = value`             |
| `__contains__` | `value in object`                   |
| `__call__`     | `object()`                          |


Simple Memory trick 
__str__      -> print object nicely
__repr__     -> show object for debugging
__len__      -> len(object)
__eq__       -> object1 == object2
__add__      -> object1 + object2
__getitem__  -> object[index]
__contains__ -> value in object

"""
class Validator:
    @staticmethod
    def validate_title(title):
        if title == "":
            raise ValueError("title can not be empty")

    @staticmethod
    def validate_author(author):
        if author == "":
            raise ValueError("author can not be empty")

    @staticmethod
    def validate_pages(pages):
        if pages <= 0:
            raise ValueError("pages must be greater than 0")

    @staticmethod
    def validate_price(price):
        if price <= 0:
            raise ValueError("price must be greater than 0")


class Book:
    def __init__(self, title, author, pages, price):
        self.__title = None
        self.__author = None
        self.__pages = None
        self.__price = None

        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # ---------------- Properties ----------------

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        Validator.validate_title(title)
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        Validator.validate_author(author)
        self.__author = author

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        Validator.validate_pages(pages)
        self.__pages = pages

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        Validator.validate_price(price)
        self.__price = price

    # ---------------- Dunder Methods ----------------

    # 1. __str__
    # Used by print(book)
    def __str__(self):
        return f"Book: {self.title} by {self.author} | Pages: {self.pages} | Price: {self.price}"

    # 2. __repr__
    # Used by repr(book)
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages!r}, {self.price!r})"

    # 3. __len__
    # Used by len(book)
    def __len__(self):
        return self.pages

    # 4. __eq__
    # Used by book1 == book2
    # Books are equal if title and author are the same.
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    # 5. __lt__
    # Used by book1 < book2
    # Compares books by price.
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price

    # 6. __gt__
    # Used by book1 > book2
    # Compares books by price.
    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price > other.price

    # 7. __add__
    # Used by book1 + book2
    # Returns total price of two books.
    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price + other.price

    # 8. __sub__
    # Used by book1 - book2
    # Returns price difference.
    def __sub__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price - other.price

    # 9. __mul__
    # Used by book * number
    # Returns total price if buying multiple copies.
    def __mul__(self, quantity):
        if not isinstance(quantity, int):
            return NotImplemented
        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")
        return self.price * quantity

    # 10. __getitem__
    # Used by book["title"], book["author"], book["pages"], book["price"]
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        elif key == "price":
            return self.price
        else:
            raise KeyError("Invalid key. Use: title, author, pages, or price")

    # 11. __setitem__
    # Used by book["price"] = 50
    def __setitem__(self, key, value):
        if key == "title":
            self.title = value
        elif key == "author":
            self.author = value
        elif key == "pages":
            self.pages = value
        elif key == "price":
            self.price = value
        else:
            raise KeyError("Invalid key. Use: title, author, pages, or price")

    # 12. __contains__
    # Used by "Atomic" in book
    # Checks whether a word exists in the title or author.
    def __contains__(self, value):
        return value.lower() in self.title.lower() or value.lower() in self.author.lower()

    # 13. __call__
    # Used by book()
    def __call__(self):
        return f"{self.title} is written by {self.author} and costs {self.price}."


# ---------------- Testing ----------------

book1 = Book("Atomic Habits", "James Clear", 320, 25)
book2 = Book("Deep Work", "Cal Newport", 280, 30)
book3 = Book("Atomic Habits", "James Clear", 350, 40)

print("1. __str__")
print(book1)

print("\n2. __repr__")
print(repr(book1))

print("\n3. __len__")
print(len(book1))

print("\n4. __eq__")
print(book1 == book2)
print(book1 == book3)

print("\n5. __lt__")
print(book1 < book2)

print("\n6. __gt__")
print(book1 > book2)

print("\n7. __add__")
print(book1 + book2)

print("\n8. __sub__")
print(book1 - book2)

print("\n9. __mul__")
print(book1 * 3)

print("\n10. __getitem__")
print(book1["title"])
print(book1["author"])
print(book1["pages"])
print(book1["price"])

print("\n11. __setitem__")
book1["price"] = 35
book1["pages"] = 330
print(book1)

print("\n12. __contains__")
print("Atomic" in book1)
print("James" in book1)
print("Python" in book1)

print("\n13. __call__")
print(book1())