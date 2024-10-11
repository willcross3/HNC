class Car:
    instance_count = 0
    def __init__(self, make, model):
        self.make = make        # Public Attribute
        self.__model = model    # __ makes a private attribute
        Car.instance_count += 1
    def start(self):
        print(f"{self.make} {self.__model} is starting...")
    def stock():
        print(f"{Car.instance_count} cars in stock...")

car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")

Car.stock()
car2.start()

