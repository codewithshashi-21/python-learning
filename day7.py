# Dictionaries and Sets
# Creating a dictionary
student = {
    "name": "Sunny",
    "age": 21,
    "course": "AI/ML"
}
print(student["name"])
student["college"] = "Guru Nanak College"
student["age"] = 22
student.pop("course")
for key, value in student.items():
    print(key, ":", value)

# sets
# Creating a set
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)
numbers.add(6)
numbers.remove(3)
evens = {2, 4, 6, 8}
print(numbers.union(evens))
print(numbers.intersection(evens))

