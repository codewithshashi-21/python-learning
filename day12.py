# Day 12 – Advanced OOP (Encapsulation)

class Student:
    def __init__(self, name):
        self.__name = name   # private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 2:
            raise ValueError("Name must have at least 2 characters")
        self.__name = name


# USING THE CLASS (IMPORTANT)

try:
    s = Student("A")              # too short initially
    print(s.get_name())

    s.set_name("Sunny")           # valid update
    print(s.get_name())

    s.set_name("S")               # will raise error

except ValueError as e:
    print("Error:", e)


