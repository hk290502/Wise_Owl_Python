# =========================
# Base (Parent) Class
# =========================
class Vehicle:
    # The constructor (__init__) runs automatically
    # when a new Vehicle (or subclass) object is created
    def __init__(self, brand, length, speed):
        # Store the brand of the vehicle (e.g., VW, AirBus)
        self.brand = brand
        
        # Store the physical length of the vehicle
        self.length = length
        
        # Store the speed of the vehicle
        self.speed = speed

    # __str__ defines how the object is displayed
    # when print(object) is called
    def __str__(self):
        # Returns a human-readable string instead of
        # the default memory address
        return f'The speed is {self.speed}'
    
    # A general method that describes any vehicle
    # This is meant to be overridden by subclasses
    def describe(self):
        return "This is a vehicle."
    

# =========================
# Child Class: AirVehicle
# =========================
# AirVehicle inherits from Vehicle
# It automatically gets:
# - __init__
# - __str__
# - describe (until overridden)
class AirVehicle(Vehicle):

    # A method specific only to AirVehicle
    def kW(self):
        # Check if the aircraft speed is exactly 1000
        if self.speed == 1000:
            return 'AirSpeed'
        else:
            return 'Not AirSpeed'
      
    # This method overrides Vehicle.describe()
    # This is polymorphism in action
    def describe(self):
        # Same method name as in Vehicle,
        # but different behavior for AirVehicle objects
        return f"{self.brand} flying at {self.speed} km/h"


# =========================
# Child Class: LandVehicle
# =========================
# LandVehicle also inherits from Vehicle
class LandVehicle(Vehicle):

    # Method specific to LandVehicle
    def size(self):
        # Check the length of the vehicle
        if self.length >= 10:
            return 'Car Length'
        else:
            return 'bruh'
    
    # This method overrides Vehicle.describe()
    # Another polymorphic implementation
    def describe(self):
        return f"{self.brand} driving at {self.speed} km/h"
 

# =========================
# Creating Objects
# =========================

# Create an AirVehicle object
# This automatically calls Vehicle.__init__()
# because AirVehicle does not define its own __init__
a = AirVehicle('AirBus', 1432, 1000)

# Calls Vehicle.__str__()
print(a)              # Output: The speed is 1000

# Calls AirVehicle.kW()
print(a.kW())         # Output: AirSpeed


# Create a LandVehicle object
c = LandVehicle('VW', 6, 160)

# Calls Vehicle.__str__()
print(c)              # Output: The speed is 160

# Calls LandVehicle.size()
print(c.size())       # Output: bruh


# =========================
# Polymorphism Demonstration
# =========================

# Create a list containing different types of vehicles
vehicles = [
    AirVehicle("AirBus", 1432, 1000),
    LandVehicle("VW", 6, 160),
    Vehicle("Generic", 5, 80)
]

# Loop through all vehicles
for v in vehicles:
    # Polymorphism happens here:
    # - If v is AirVehicle → AirVehicle.describe() is called
    # - If v is LandVehicle → LandVehicle.describe() is called
    # - If v is Vehicle     → Vehicle.describe() is called
    print(v.describe())