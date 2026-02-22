#Basic class + object
class Person:
    def __init__(self, name, age):
        self.name = name     
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

p = Person("Sunny", 21)
print(p.greet())
    
#Instance vs Class attributes
class Counter:
    total = 0   

    def __init__(self):
        Counter.total += 1

a = Counter()
b = Counter()
print(Counter.total)   

#Encapsulation (private-ish attribute)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdraw")

    def get_balance(self):
        return self._balance
    
#Inheritance
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

d = Dog()
print(d.speak())   

#Static & Class methods
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"This is {cls.__name__}"

print(MathUtil.add(2,3))
print(MathUtil.info())
    
    