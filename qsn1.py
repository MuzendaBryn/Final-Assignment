class Vehicle:
    def describe(self):
        return "This is a vehicle."

class Car(Vehicle):
    def describe(self):
        return "This is a car. It has four wheels and is designed for comfortable travel."

class Bike(Vehicle):
    def describe(self):
        return "This is a bike. It has two wheels and is ideal for quick and efficient transportation."

# Example usage
vehicle = Vehicle()
car = Car()
bike = Bike()

print(vehicle.describe())  # Output: This is a vehicle.
print(car.describe())      # Output: This is a car. It has four wheels and is designed for comfortable travel.
print(bike.describe())     # Output: This is a bike. It has two wheels and is ideal for quick and efficient transportation.
