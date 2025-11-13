#Day 10 — File Handling + Error Handling
#Reading and Writing Files
with open("notes.txt", "w") as f:
    f.write("Day 10: learning file handling\n")
    f.write("This text is stored permanently.\n")
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Appended line → no data lost.\n")

with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

#Exception Handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid number entered.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Program finished.")

#Mini Project — Save User Notes
note = input("Enter your note: ")

try:
    with open("mynotes.txt", "a") as f:
        f.write(note + "\n")
    print("Note saved successfully!")
except Exception as e:
    print("Failed to save note:", e)
    


