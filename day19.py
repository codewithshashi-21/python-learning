#"Day 19: Student manager with CLI and delete feature"
import json


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["roll_no"], data["marks"])

    def __str__(self):
        return f"{self.roll_no} - {self.name} | Avg: {self.average():.2f}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def list_all(self):
        if not self.students:
            print("No students available.")
            return
        for s in self.students:
            print(s)

    def find(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                return s
        return None

    def delete(self, roll_no):
        student = self.find(roll_no)
        if student:
            self.students.remove(student)
            return True
        return False

    def save(self, filename):
        data = [s.to_dict() for s in self.students]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = [Student.from_dict(d) for d in data]
        except FileNotFoundError:
            self.students = []


# simple CLI flow

manager = StudentManager()
manager.load("students.json")

while True:
    print("\n1. Add Student")
    print("2. List Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Name: ")
        roll = int(input("Roll No: "))
        marks = list(map(int, input("Marks (space separated): ").split()))
        manager.add(Student(name, roll, marks))
        manager.save("students.json")
        print("Student added.")

    elif choice == "2":
        manager.list_all()

    elif choice == "3":
        roll = int(input("Enter roll number to delete: "))
        if manager.delete(roll):
            manager.save("students.json")
            print("Deleted.")
        else:
            print("Student not found.")

    elif choice == "4":
        manager.save("students.json")
        print("Exiting.")
        break

    else:
        print("Invalid option.")