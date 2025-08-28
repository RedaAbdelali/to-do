#!/usr/bin/env python3
import os
import json

TASKS_FILE = "tasks.json"

# Colors for black theme
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
GRAY = "\033[90m"
STRIKE = "\033[9m"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def show_tasks(tasks):
    os.system("clear")
    print(f"{GREEN}=== TODO LIST ==={RESET}\n")
    if not tasks:
        print(f"{GRAY}(No tasks yet){RESET}")
    for i, task in enumerate(tasks, 1):
        if task["done"]:
            print(f"{i}. {STRIKE}{GRAY}{task['text']}{RESET}")
        else:
            print(f"{i}. {task['text']}")
    print(
        "\n"
        f"{GRAY}Commands: [a]dd, [c]heck, [u]ncheck, [d]elete, [q]uit{RESET}"
    )

def main():
    tasks = load_tasks()
    while True:
        show_tasks(tasks)
        choice = input("\n> ").strip().lower()
        if choice == "a":
            text = input("New task: ").strip()
            if text:
                tasks.append({"text": text, "done": False})
                save_tasks(tasks)
        elif choice == "c":
            num = input("Task number to check: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]["done"] = True
                    save_tasks(tasks)
        elif choice == "u":
            num = input("Task number to uncheck: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]["done"] = False
                    save_tasks(tasks)
        elif choice == "d":
            num = input("Task number to delete: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    deleted = tasks.pop(idx)
                    print(f"{RED}Deleted: {deleted['text']}{RESET}")
                    save_tasks(tasks)
                    input("Press Enter to continue...")
        elif choice == "q":
            break

if __name__ == "__main__":
    main()
