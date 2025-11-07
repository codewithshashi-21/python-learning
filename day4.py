#loops in python 
# simple for loop example
for i in range (1,6):
    print("Iteration:",i)
# simple while loop program
count = 1
while count<= 5:
    print("count",count)
    count+=1
# Break and continue
for i in range(1,10):
    if i == 5:
        break
    print("stopped at", i)

for i in range(1, 10):
    if i == 5:
        continue
    print("Skipped 5 ->", i)

 #Loop Through String
word = "Python"
for letter in word:
    print(letter)
  
   