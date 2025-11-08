import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, description):
    """Add a new task."""
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    print(f"✓ Task added: {description}")


def list_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks yet!")
        return
    print("\n" + "=" * 50)
    for task in tasks:
        status = "✓" if task["completed"] else "○"
        print(f"{status} [{task['id']}] {task['description']}")
    print("=" * 50 + "\n")


def complete_task(tasks, task_id):
    """Mark a task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"✓ Task {task_id} marked as completed!")
            return
    print("Task not found!")


def delete_task(tasks, task_id):
    """Delete a task."""
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(i)
            print(f"✗ Deleted: {deleted['description']}")
            return
    print("Task not found!")


def show_menu():
    """Display the main menu."""
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. List all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Save and exit")
    print("-" * 20)


def main():
    """Main application loop."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("Enter task description: ").strip()
            if description:
                add_task(tasks, description)
            else:
                print("Task description cannot be empty!")

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            list_tasks(tasks)
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                complete_task(tasks, task_id)
            except ValueError:
                print("Invalid input!")

        elif choice == "4":
            list_tasks(tasks)
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            except ValueError:
                print("Invalid input!")

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid option! Please choose 1-5.")


if __name__ == "__main__":
    main()
