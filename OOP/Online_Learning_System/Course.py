from Validator import Validator
from Lesson import Lesson
from Review import Review

class Course:
    total_courses = 0
    
    def __init__(self, title, price, category, instructor):
        self.__title = None
        self.__price = None
        self.__category = None
        self.__instructor = None
        self.__lessons = []
        self.__reviews = []

        self.total_courses += 1

    @property
    def title(self):
        return self.__title 
    
    @title.setter
    def title(self, value):
        Validator.validate_not_empty(value, "Title")
        self.__title = value
    
    @property
    def price(self):
        return self.__price 
    
    @price.setter
    def price(self, value):
        Validator.validate_positive_number(value, "Price")
        self.__price = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        Validator.validate_not_empty(value, "Category")
        self.__category = value

    @property
    def instructor(self):
        return self.__instructor
    
    @instructor.setter
    def instructor(self, value):
        from Instructor import Instructor
        Validator.validate_instance(value, Instructor, "Instructor")
        self.__instructor = value
    
    def add_lesson(self, lesson):
        Validator.validate_instance(lesson, Lesson, "Lesson")
        self.__lessons.append(lesson)
    
    def remove_lesson(self, lesson):
        Validator.validate_instance(lesson, Lesson, "Lesson")
        if lesson in self.__lessons:
            self.__lessons.remove(lesson)
        else:
            return "Lesson not Found in the course"
        
    def add_review(self, review):
        Validator.validate_instance(review, Review, "Review")
        self.__reviews.append(review)

    def get_average_rating(self):
        if len(self.__reviews) == 0:
            return 0
        total_rating = 0

        for review in self.__reviews:
            total_rating += review.rating

        return total_rating / len(self.__reviews)
    
    def get_total_duration(self):
        if len(self.__lessons) == 0:
            return 0
        total_duration = []
        for lesson in self.__lessons:
            total_duration += lesson.duration_minutes

        return total_duration
    
    def get_course_info(self):
        return f"Course Title {self.title} | Instructor: {self.instructor} | Price: {self.price}"
    

    def __str__(self):
        return f"Course Title {self.title} | Instructor: {self.instructor} | Price: {self.price}"
    
    def __repr__(self):
        return f"(Course Title: {self.title!r}, Instructor:{self.instructor!r}, Price:{self.price!r})"
    
    def __len__(self):
        return len(self.__lessons)
    
    def __eq__(self, other):
        Validator.validate_instance(other, Course)
        return self.title == other.title
    
    def __lt__(self, other):
        Validator.validate_instance(other, Course)
        return self.price < other.price

    def __gt__(self, other):
        Validator.validate_instance(other, Course)
        return self.price > other.price

    def __contains__(self, lesson_title):
        for lesson in self.__lessons:
            if lesson.title == lesson_title:
                return True

        return False

    def __getitem__(self, index):
        return self.__lessons[index]

    def __add__(self, other):
        Validator.validate_instance(other, Course)
        return self.price + other.price

    # ---------------- CLASS METHOD ----------------

    @classmethod
    def get_total_courses(cls):
        return cls.total_courses