import os

TODO_FILE = "tasks.txt"

def show_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks found!")
        return
    with open(TODO_FILE, "r") as f:
        tasks = f.readlines()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")
    else:
        print("No tasks found!")

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"✅ Task added: {task}")

def delete_task(task_no):
    if not os.path.exists(TODO_FILE):
        print("No tasks file found!")
        return
    with open(TODO_FILE, "r") as f:
        tasks = f.readlines()
    try:
        removed = tasks.pop(task_no - 1)
        with open(TODO_FILE, "w") as f:
            f.writelines(tasks)
        print(f"❌ Task removed: {removed.strip()}")
    except IndexError:
        print("Invalid task number!")

if __name__ == "__main__":
    while True:
        print("\n📋 To-Do App")
        print("1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task(input("Enter task: "))
        elif choice == "3":
            delete_task(int(input("Enter task number: ")))
        elif choice == "4":
            break
        else:
            print("Invalid choice!")