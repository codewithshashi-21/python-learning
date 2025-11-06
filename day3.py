#if else statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

 #else if 
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C or below")

#logical operations
x = int(input("Enter a number: "))

if x > 0 and x % 2 == 0:
    print("Positive even number")
elif x > 0 and x % 2 != 0:
    print("Positive odd number")
else:
    print("Negative number")
   
