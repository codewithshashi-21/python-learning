# Day 30 – Final mini project (API + file + CLI)

import requests
import csv


URL = "https://jsonplaceholder.typicode.com/users"
FILE = "users.csv"


def fetch():
    try:
        res = requests.get(URL, timeout=10)
        if res.status_code != 200:
            print("API error.")
            return []
        return res.json()
    except:
        print("Network error.")
        return []


def convert(data):
    rows = []
    for u in data:
        rows.append([
            u["id"],
            u["name"],
            u["email"],
            u["company"]["name"],
            u["address"]["city"]
        ])
    return rows


def save(rows):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Email", "Company", "City"])
        writer.writerows(rows)


def search(rows, name):
    for r in rows:
        if name.lower() in r[1].lower():
            print(f"{r[0]} | {r[1]} | {r[3]} | {r[4]}")


def main():
    data = fetch()
    if not data:
        return

    rows = convert(data)
    save(rows)

    print("\nData ready. You can search users.")
    
    while True:
        q = input("\nSearch name (or 'exit'): ")
        if q.lower() == "exit":
            break
        search(rows, q)


if __name__ == "__main__":
    main()