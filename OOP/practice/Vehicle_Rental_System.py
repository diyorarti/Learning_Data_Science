from abc import ABC, abstractmethod
import re

class Validator:

    @staticmethod
    def validate_not_empty(value, field_name):
        if value is None or str(value).strip() == '':
            raise ValueError(f"{field_name} can't be empty")

    @staticmethod
    def validate_positive_number(value, field_name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number")
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than 0")

    @staticmethod
    def validate_email(email):
        if email is None or str(email).strip() == "":
            raise ValueError("email can't be empty")

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")


    @staticmethod
    def validate_instance(obj, class_type, field_name):
        if not isinstance(obj, class_type):
            raise TypeError(f"{field_name} must be an instance of {class_type.__name__}")

class Vehicle(ABC):
    def __init__(self, brand, model, year, daily_price, is_available):
        self.__brand = None
        self.__model = None
        self.__year = None
        self.__daily_price = None
        self.__is_available = None

        self.brand = brand
        self.model = model
        self.year = year
        self.daily_price = daily_price
        self.is_available = is_available

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.validate_not_empty(value, 'brand')
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.validate_not_empty(value, "model")
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validator.validate_positive_number(value, 'year')
        self.__year = value

    @property
    def daily_price(self):
        return self.__daily_price

    @daily_price.setter
    def daily_price(self, value):
        Validator.validate_positive_number(value, 'daily_price')
        self.__daily_price = value

    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self, value):
        if type(value) is not bool:
            raise ValueError("is_availabe must be True or False")
        self.__is_available = value

    def get_vehicle_info(self):
        return f"Brand: {self.brand} |Model: {self.model} |Year {self.year} |Daily Price: {self.daily_price} |Available: {self.is_available}"

    def rent(self):
        if not self.is_available:
            raise ValueError(f"{self.model} is already rented")
        self.is_available = False

    def return_vehicle(self):
        if self.is_available:
            raise ValueError(F"{self.model} is already available")
        self.is_available = True

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, year, daily_price, is_available, number_of_doors):
        super().__init__( brand, model, year, daily_price, is_available)
        self.__number_of_doors = None
        self.number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        Validator.validate_positive_number(value, 'number_of_doors')
        self.__number_of_doors = value

    def calculate_rental_cost(self, days):
        if days <= 0:
            Validator.validate_positive_number(days, 'Days')
        return self.daily_price * days

    def get_vehicle_type(self):
        return "Car"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, daily_price, is_available, engine_cc):
        super().__init__(brand, model, year, daily_price, is_available)
        self.__engine_cc = None
        self.engine_cc = engine_cc
 
    @property
    def engine_cc(self):
        return self.__engine_cc

    @engine_cc.setter
    def engine_cc(self, value):
        Validator.validate_positive_number(value, 'engine_cc')
        self.__engine_cc = value

    def calculate_rental_cost(self, days):
        if days <= 0:
            Validator.validate_positive_number(days, "days")
        if days >= 7:
            total_price = self.daily_price * days 
            return total_price - (10 / 100 * total_price)
        else:
            return self.daily_price * days

    def get_vehicle_type(self):
        return "Motorcycle"
  
class Customer:
    def __init__(self, name, email, customer_id):
        self.__name = None
        self.__email = None
        self.__customer_id = None
        self.name = name
        self.email = email
        self.customer_id = customer_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Validator.validate_not_empty(name, "name")
        self.__name = name 

    @property
    def email(self):
        return self.__email

    @email.setter 
    def email(self, email):
        Validator.validate_email(email)
        self.__email = email

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        Validator.validate_not_empty(customer_id, "customer_id")
        self.__customer_id = customer_id

    def get_customer_info(self):
        return f"Name: {self.name} | Email: {self.email} | Customer-ID: {self.customer_id}"

    def __str__(self):
        return f"Customer: {self.name} | Customer-ID: {self.customer_id}"

class Rental:
    def __init__(self, customer, vehicle, days):
        Validator.validate_instance(
            customer,
            Customer,
            'customer'
        )
        Validator.validate_instance(
            vehicle,
            Vehicle,
            'vehicle'
        )
        Validator.validate_positive_number(
            days,
            'days'
        )
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.total_cost = 0
        self.status = 'Pending'

    def start_rental(self):
        self.vehicle.rent()

        self.status = 'Active'
        self.total_cost = self.vehicle.calculate_rental_cost(
            self.days
        )

    def complete_rental(self):
        self.vehicle.return_vehicle()
        self.status = 'Completed'

    def get_rental_info(self):
        return (
            f"Customer: {self.customer} |"
            f"Vehicle: {self.vehicle.model} |"
            f"Days: {self.days} |"
            f"Total cost: {self.total_cost} |"
            f"Status: {self.status} |"
        )

class RentalCompany:
    def __init__(self, company_name):
        self.company_name = company_name
        self.__vehicles = []
        self.__customers = []
        self.__rentals = []

    def add_vehicle(self, vehicle):
        Validator.validate_instance(vehicle, Vehicle, 'vehicle')
        self.__vehicles.append(vehicle)

    def add_customer(self, customer):
        Validator.validate_instance(customer, Customer, 'customer')
        self.__customers.append(customer)

    def find_vehicle(self, brand, model):
        for vehicle in self.__vehicles:
            if brand == vehicle.brand and model == vehicle.model:
                return vehicle
        return None

    def show_available_vehicles(self):
        available_vehicles = []

        for vehicle in self.__vehicles:
            if vehicle.is_available:
                available_vehicles.append(vehicle)

        return available_vehicles

    def rent_vehicle(self, rental):
        Validator.validate_instance(rental, Rental, 'rental')
        self.__rentals.append(rental)

    def show_all_rentals(self):
        rentals = []

        for rental in self.__rentals:
            rentals.append(rental.get_rental_info())

        return rentals

    def get_company_summary(self):
        total_available_vehicles = self.show_available_vehicles()
        return f"Company name: {self.company_name} | Vehicles: {len(self.__vehicles)} | Available Vehicles: {total_available_vehicles} | Customers: {len(self.__customers)} | Rentals: {len(self.__rentals)}"

    def __str__(self):
        total_available_vehicles = sum(
            vehicle.is_available
            for vehicle in self.__vehicles
        )

        return (
            f"Company name: {self.company_name} | "
            f"Vehicles: {len(self.__vehicles)} | "
            f"Available Vehicles: {total_available_vehicles} | "
            f"Customers: {len(self.__customers)} | "
            f"Rentals: {len(self.__rentals)}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"brand={self.brand!r}, "
            f"model={self.model!r}, "
            f"year={self.year!r}, "
            f"daily_price={self.daily_price!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False

        return (
            self.brand == other.brand
            and self.model == other.model
            and self.year == other.year
        )

    def __len__(self):
        return len(self.__vehicles)

    def __contains__(self, item):
        return item in self.__vehicles



