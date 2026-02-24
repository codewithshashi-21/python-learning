# Day 14 – Polymorphism
# Same method name, different behavior depending on the object.


# --- Example 1: Simple overriding ---

class Person:
    def introduce(self):
        return "Just a normal person"


class Student(Person):
    def introduce(self):
        return "I'm a student"


class Teacher(Person):
    def introduce(self):
        return "I'm a teacher"


people = [Person(), Student(), Teacher()]

for p in people:
    print(p.introduce())


print("\n" + "-"*30 + "\n")


# --- Example 2: Real use case (shapes with different area logic) ---

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shapes = [Rectangle(4, 5), Circle(3)]

for s in shapes:
    print("Area:", s.area())


print("\n" + "-"*30 + "\n")


# --- Example 3: Duck typing (no inheritance needed) ---

class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


animals = [Dog(), Cat()]

for a in animals:
    print(a.speak())


print("\n" + "-"*30 + "\n")


# --- Your Task Section (Vehicle example) ---

class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bike(Vehicle):
    def move(self):
        return "Bike is riding"


vehicles = [Vehicle(), Car(), Bike()]

for v in vehicles:
    print(v.move())