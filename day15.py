# Day 15 – Cleaning up classes properly
# Today we make our class feel more natural to use.


class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Initial balance can't be negative")

        self._owner = owner
        self._balance = balance

    # Instead of get_balance(), we use property
    @property
    def balance(self):
        return self._balance

    # Controlled update of balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance can't go negative")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    # What users see when printing
    def __str__(self):
        return f"{self._owner}'s account | Balance: {self._balance}"

    # More detailed representation (mainly for debugging)
    def __repr__(self):
        return f"BankAccount(owner='{self._owner}', balance={self._balance})"


# ---- using it ----

try:
    acc = BankAccount("Sunny", 1000)

    print(acc)              # __str__
    print(repr(acc))        # __repr__

    acc.deposit(500)
    print("After deposit:", acc.balance)

    acc.withdraw(300)
    print("After withdraw:", acc.balance)

    acc.balance = 2000      # using property setter
    print("Manually updated:", acc.balance)

    # Uncomment this to test error
    # acc.balance = -100

except ValueError as e:
    print("Error:", e)