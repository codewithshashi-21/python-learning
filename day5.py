#lists and tuples
fruits = ["apple","mango","banana"]
print(fruits)
print("First fruit:",fruits[0])

#Add change or remove
fruits.append("orange")
fruits.remove("apple")
fruits[1] = "grapes"
print ("Updated lis of fruits:" ,fruits)

#list methods
numbers = [5, 1, 8, 3, 9]
print("Length:", len(numbers))
print("Sorted:", sorted(numbers))
print("Sum:", sum(numbers))
numbers.reverse()
print("Reversed:", numbers)

#loop through list
for item in fruits:
    print("Fruit:", item)

#tuples
coordinates = (10, 20, 30)
print("Tuple:", coordinates)
print("Second value:", coordinates[1])
