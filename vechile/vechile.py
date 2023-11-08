'''
24) Exercise: Vehicle Inheritance
You are given a base class `Vehicle`, and you need to create three subclasses: `Car`, `Bicycle`, and `Motorcycle`. Each of these subclasses should inherit from the `Vehicle` class and have their own unique properties and methods.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Here are the details for each class:

1. `Vehicle` (Base Class):
   - Properties:
     - `make` (string) - The make or manufacturer of the vehicle.
     - `model` (string) - The model of the vehicle.
     - `year` (int) - The manufacturing year of the vehicle.
     - `fuel` (float) - The current fuel level in liters.
   - Methods:
     - `__init__(self, make, model, year, fuel)` - Initialize the vehicle with the provided make, model, year, and initial fuel level.
     - `refuel(self, liters)` - Refuel the vehicle with the specified number of liters.
     - `drive(self, distance)` - Simulate driving the vehicle for the given distance in kilometers. This should decrease the fuel level and return the remaining fuel.


'''


class Vehicle:
    def __init__(self,make,model,year,fuel):
        self.make=make
        self.model=model
        self.year=year
        self.fuel=fuel

    def refuel(self, liters):
        self.liter+=liter

    def drive(self,distance):
        self.liter-=distance
        return self.liter
    
    

