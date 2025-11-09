# advanced lists and tuples 
numbers = [1,2,4,5,3,6,10]
numbers.sort()
print (numbers)
numbers.reverse()
print(numbers)
numbers.extend([12,50])
print(numbers)
print(numbers.count(1))
print(numbers.index(2))
numbers.clear()
print(numbers)
#list comprehensions
#Create list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)

#Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#Convert to uppercase
names = ["sunny", "raju", "omni"]
upper_names = [n.upper() for n in names]
print(upper_names)


#nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])     
print(matrix[1][2])   


# tuples in real use
student = ("Sunny", 21, "AI/ML")
name, age, course = student
print(name)
print(age)
print(course)



