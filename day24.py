# Day 24 – Tiny CLI todo app that saves tasks to a file

FILE = "tasks.txt"


def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")


def add_task(tasks):
    text = input("New task: ").strip()
    if text:
        tasks.append(text)
        print("Added.")
    else:
        print("Empty task ignored.")


def remove_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Remove task number: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n1) List  2) Add  3) Remove  4) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Bye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()