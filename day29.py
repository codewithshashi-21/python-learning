# Day 29 – Clean and structured version of previous API project

import requests
import csv


URL = "https://jsonplaceholder.typicode.com/users"
FILE = "users.csv"


def fetch_users():
    try:
        res = requests.get(URL)
        if res.status_code != 200:
            print("API error.")
            return []
        return res.json()
    except:
        print("Network error.")
        return []


def process_users(users):
    rows = []
    for u in users:
        rows.append([
            u["id"],
            u["name"],
            u["email"],
            u["company"]["name"],
            u["address"]["city"]
        ])
    return rows


def save_users(rows):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Email", "Company", "City"])
        writer.writerows(rows)


def show_users(rows):
    print("\nPreview:")
    for r in rows[:5]:
        print(f"{r[0]} | {r[1]} | {r[3]} | {r[4]}")


def main():
    users = fetch_users()
    if not users:
        return

    rows = process_users(users)
    save_users(rows)
    show_users(rows)


if __name__ == "__main__":
    main()