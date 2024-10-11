class Vehicle:
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        return "The car drives"
class Boat(Vehicle):
    def move(self):
        return "The boat sails"
# Using the abstraction
car = Car()
boat = Boat()
print(car.move())   # Output: The car drives
print(boat.move())  # Output: The boat sails
