## The car Class
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year =  year
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_car = Car('audi', 'a4', 2018)
print(my_car.get_descriptive_name())

## setting a Default Value for an Attribute
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year =  year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
my_car = Car('audi', 'a4', 2018)
print(my_car.get_descriptive_name())
my_car.read_odometer()

## Modifying attribute values

my_car.odometer_reading = 23
my_car.read_odometer()

## Modifying an attribute's value through a Method
## setting a Default Value for an Attribute
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year =  year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage
my_car = Car('audi', 'a4', 2018)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(24)
my_car.read_odometer()