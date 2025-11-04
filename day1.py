# Day 1 — Simple python program i have learned today .This contains giving input,converting and simple condition checking.
print("Day1 of python")
name = input("Enter your name: ")
age_input = input("Enter your age: ")
try:
    age = int(age_input)
except ValueError:
    print("Invalid age input. Using age = 0.")
    age = 0
print(f"Name: {name}")
print(f"Age: {age}")
if age >= 18:
    print("Adult —  You can apply for driving license.")
else:
    print("Younger —  You cannot apply for driving license.")

