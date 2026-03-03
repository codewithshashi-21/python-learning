# Day 20 – Working with APIs (making a simple request)

import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        print("User not found or API error.")
        return

    data = response.json()

    print("\nUser Info:")
    print("Username:", data.get("login"))
    print("Name:", data.get("name"))
    print("Public Repos:", data.get("public_repos"))
    print("Followers:", data.get("followers"))
    print("Following:", data.get("following"))


if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    get_github_user(username)