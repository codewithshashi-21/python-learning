#Functions in Python
def greet():
    print("Hello, welcome back to Python!")

greet()

#Functions with Parameters
def greet_user(name):
    print(f"Hello, {name}! Nice to meet you.")

greet_user("Sunny")

#Return Values
def add(a,b):
    return a+b
result = add (100,200)
print ("Sum is",result)

#Default & Keyword Arguments
def power(base, exp=2):
    return base ** exp

print(power(3))        
print(power(base=2, exp=5))

#Multiple Return Values
def calc_stats(numbers):
    return max(numbers), min(numbers), sum(numbers)/len(numbers)

nums = [4, 7, 1, 9, 3]
high, low, avg = calc_stats(nums)
print("High:", high, "Low:", low, "Avg:", avg)


# Mini project  --> Simple calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    print("Result:", a / b if b != 0 else "Division by zero not allowed")
else:
    print("Invalid operation")
