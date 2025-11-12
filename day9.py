#Function Scope + Lambda Functions
#Variable Scope
x = 10  # global variable

def show():
    x = 5 
    print("Inside function:", x)

show()
print("Outside function:", x)

x = 10

def change():
    global x
    x = 20

change()
print(x) 

#Lambda Functions
#Examples
add = lambda a, b: a + b
print(add(5, 3))

square = lambda x: x ** 2
print(square(4))

#Using Lambda with Built-ins
# map: apply a function to all items
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)



