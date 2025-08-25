from abc import ABC, abstractmethod
# abc = Abstract Base Classes module.
# ABC is the parent class that lets you create abstract classes.
# @abstractmethod is a decorator that marks a method as “must be implemented in subclasses.”

class Vehicle(ABC): #Vehicle is an abstract class

    #abstractmethod: Any vehicle must have a way to go and stop
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle): #Car inherits Vehicle.

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle): #Car inherits Motorcycle.

    def go(self):
        print("You drive the Motorcycle")

    def stop(self):
        print("You stop the Motorcycle")

# 👉 You cannot create an object of Vehicle directly.
# For example, v = Vehicle() ❌ will give an error.
motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

car = Car()
car.go()
car.stop()


