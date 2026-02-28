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

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        for s in self.students:
            print(s)

    def save_to_file(self, filename):
        data = [s.to_dict() for s in self.students]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = [Student.from_dict(item) for item in data]
        except FileNotFoundError:
            self.students = []


# ---- simple usage ----

manager = StudentManager()

manager.add_student(Student("Sunny", 1, [85, 90, 88]))
manager.add_student(Student("Ravi", 2, [70, 75, 80]))

manager.save_to_file("students.json")

manager.load_from_file("students.json")

print("Students after loading:")
manager.list_students()