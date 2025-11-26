"""
Simple task list manager using a Python list.
Allows user to add, view, and remove tasks.
"""

tasks = []

while True:
    print("\n=== Task List Manager ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task description: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
    elif choice == "4":
        print("Exiting Task List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
