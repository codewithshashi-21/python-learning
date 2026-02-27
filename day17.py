#student management system
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

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

    def find_by_roll(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                return s
        return None


# ---- basic testing ----

manager = StudentManager()

s1 = Student("Sunny", 1, [80, 85, 90])
s2 = Student("Ravi", 2, [70, 75, 72])

manager.add_student(s1)
manager.add_student(s2)

print("All Students:")
manager.list_students()

print("\nSearching for Roll No 2:")
student = manager.find_by_roll(2)

if student:
    print(student)
else:
    print("Student not found")