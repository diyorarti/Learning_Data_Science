from Validator import Validator

class Lesson:
    def __init__(self, title, duration_minutes):
        self.__title = None
        self.__duration_minutes = None
        self.title = title
        self.duration_minutes = duration_minutes

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        Validator.validate_not_empty(title, "title")
        self.__title = title
    
    @property
    def duration_minutes(self):
        return self.__duration_minutes
    
    @duration_minutes.setter
    def duration_minutes(self, duration_minutes):
        Validator.validate_positive_number(duration_minutes, "duration minutes")
        self.__duration_minutes = duration_minutes
    
    def get_lesson_info(self):
        return f"Title: {self.title} | Duration: {self.duration_minutes} minutes"
    
    def __str__(self):
        return f"Lesson title: {self.t} | Lesson Duration {self.duration_minutes} minutes"
    
    def __repr__(self):
        return f"(Lesson Title: {self.title!r} | Lesson Duration: {self.duration_minutes!r})"
    
    def __eq__(self, other):
        Validator.validate_instance(other, Lesson)
        return self.title == other.title
    