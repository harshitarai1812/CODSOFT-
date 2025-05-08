import json

# Load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!\n")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{index}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added!")

# Remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("\nEnter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as complete
def complete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("\nEnter the number of the task to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[index]['task']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as complete")
        print("5. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
