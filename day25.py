# Day 25 – Reading and writing CSV data

import csv


FILE = "students.csv"


def save_students(data):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Course"])
        writer.writerows(data)


def load_students():
    students = []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        pass
    return students


def add_student(data):
    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")
    data.append([name, age, course])


def list_students(data):
    if not data:
        print("No students yet.")
        return

    for s in data:
        print(f"{s[0]} | Age: {s[1]} | Course: {s[2]}")


def main():
    students = load_students()

    while True:
        print("\n1) Add student")
        print("2) List students")
        print("3) Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student(students)
            save_students(students)

        elif choice == "2":
            list_students(students)

        elif choice == "3":
            save_students(students)
            print("Done.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()