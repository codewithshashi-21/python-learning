# Day 13 - Inheritance

class Person:
    def __init__(self, name):
        if len(name) < 2:
            raise ValueError("Name too short")
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def details(self):
        return f"{self.name} | Roll No: {self.roll_no}"


class Teacher(Person):
    def introduce(self):
        return f"I am Professor {self.name}"


# ---- using it ----

try:
    s = Student("Sunny", 21)
    print(s.introduce())
    print(s.details())

    t = Teacher("Rao")
    print(t.introduce())

except ValueError as e:
    print("Error:", e)