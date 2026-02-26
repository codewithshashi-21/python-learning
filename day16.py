class Account:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance.")
        self._balance -= amount

    def __str__(self):
        return f"{self._owner} | Balance: {self._balance}"


class SavingsAccount(Account):
    def deposit(self, amount):
        bonus = amount * 0.02
        super().deposit(amount + bonus)


class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount > self._balance + 500:
            raise ValueError("Overdraft limit exceeded.")
        self._balance -= amount


try:
    s = SavingsAccount("Sunny", 1000)
    c = CurrentAccount("Ravi", 500)

    s.deposit(1000)
    print(s)

    c.withdraw(800)
    print(c)

except ValueError as e:
    print("Error:", e)