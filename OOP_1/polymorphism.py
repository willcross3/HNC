class Bird: #parent class defines the sound
    def sound(self):
        print("Birds make sound")
    def move(self):
        print("Bird moves")
class Sparrow(Bird): #subclasses can override the parent function
    def sound(self):
        print("Sparrow chirps")
    def move(self): #will only work with object with the type of 'Sparrow'
        print("Sparrow also moves")
        super().move() #calls the parent method to keep the functionality of the parent method but allows me to extend the functionality of subclasses   
class Crow(Bird):
    def sound(self):
        print("Crow caws")
class Parrot(Bird):
    def sound(self):
        print("Parrot talks")



def make_sound(bird):
    bird.sound()


sparrow = Sparrow()
crow = Crow()
parrot = Parrot()

""" make_sound(sparrow)
make_sound(crow)
make_sound(parrot) """

Bird.move(sparrow)
Sparrow.move(sparrow) #calls the subclass with its new functionality
