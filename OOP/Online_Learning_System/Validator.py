import re 

class Validator:
    
    @staticmethod 
    def validate_not_empty(value, field_name):
        if value is None or str(value).strip() == "":
            raise ValueError(f"{field_name}cam not be empty")
        
    @staticmethod
    def validate_positive_number(value, field_name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number")
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than 0")
    
    @staticmethod
    def validate_email(email):
        if email is None or str(email).strip() == "":
            raise ValueError("email can not be empty")
        
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        
    @staticmethod
    def validate_rating(rating):
        if not isinstance(rating, (int, float)):
            raise TypeError("rating must be a number")
        
        if rating < 1 or rating > 5:
            raise ValueError("ratig must be between 1 and 5")
        
    @staticmethod
    def validate_instance(obj, class_type, field_name):
        if not isinstance(obj, class_type):
            raise TypeError(f"{field_name} must be an instance of {class_type.__name__}")


