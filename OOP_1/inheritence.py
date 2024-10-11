class Vehicle:   #parent class defines the parameters
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def start(self):
        print(f"{self.make} {self.model} is starting...")
class Car(Vehicle): #subclass inherits parameters
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors
    def open_doors(self):
        print(f"Opening {self.doors} doors.")


car = Car("Honda", "Civic", 4) #create new cars using correct parameters
car1 = Car("Lamborghini", "Aventador", 2)


car1.start() #calling the functions from the class
car1.open_doors()
