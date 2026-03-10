# Day 23 – Simple password generator

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Length must be positive.")

        password = generate_password(length)
        print("\nGenerated Password:", password)

    except ValueError as e:
        print("Error:", e)