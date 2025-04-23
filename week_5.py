# Base class
class Superhero:
    def _init_(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        print(f"{self.name} protects {self.city} using {self.power}!")

    def action(self):
        print(f"{self.name} uses their special power!")

# Subclass with polymorphism
class FlyingHero(Superhero):
    def _init_(self, name, power, city, flight_speed):
        super()._init_(name, power, city)
        self.flight_speed = flight_speed

    def action(self):
        print(f"{self.name} takes off flying at {self.flight_speed} mph to save the day!")


#polymophysm 
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving...")

class Plane(Vehicle):
    def move(self):
        print("Flying...")

class Boat(Vehicle):
    def move(self):
        print("Sailing...")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:v.move()

