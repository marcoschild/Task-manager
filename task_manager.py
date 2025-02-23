import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
        return []

# Function to save tasks to file 
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    description = input("Enter task description: ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    priority = input("Enter taks priority (High/Meduim/Low):").capitalize()

    if priority not in ['High', 'Meduim', 'Low']:
        print("Invalid priority. Setting to Meduim.")
        priority = "Meduim"

        task = {
            "description": description,
            "deadline": deadline,
            "priority": priority,
            "completed":False
        }
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{description}' added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i+1}. {task['description']} (Deadline: {task['deadline']})- Priority: {task['priority']} - Status: {status}")

# Function to mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to mark as completed:"))-1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            save_tasks(tasks)
            print(f"Task{task_number + 1} marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to delete:"))-1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            save_tasks(tasks)
            print(f"Task{task_number + 1} deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number")

#Function to search tasks by description 
def search_tasks(tasks):
    query = input("Enter keyword to search for: ").lower()
    matching_tasks = [task for task in tasks if query in task ["description"].lower()]
    if matching_tasks:
        print("\nSearch Results:")
        for i , task in enumerate(matching_tasks):
            status = "Completed" if task ["completed"] else "Pending"
            print(f"{i+1}.{task['description']} (Deadline: {task['deadline']}) - priority: {task['priority']} - Status: {status}")
    else:
        print("No task found matching that description.")

# Function to sort tasks by deadlines 
def sort_tasks_by_deadline(tasks):
    tasks.sort(key=lambda task:["deadline"])
    print("Tasks sorted by deadline.")
    save_tasks(tasks)

# Function to display overdue tasks
def display_overdue_tasks(tasks):
    overdue_tasks = []
    today = datetime.now().strftime("%Y-%m-%d")
    for task in tasks:
        if not task ["completed"] and task ["deadline"] < today:
            overdue_tasks.append(task)
    if overdue_tasks:
        print("\nOverdue Tasks:")
        for i, taks in enumerate(overdue_tasks):
            print(f"{i+1}.{task['description']} (Deadline: {task['deadline']}")
    else:
        print("No overdue tasks.")

# Main menu function 
def menu():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add a Task")
        print("3. Complete a Task")
        print("4. Delete a Task")
        print("5. Search Task")
        print("6. Sort Tasks by Deadline")
        print("7. View overdue Tasks")
        print("8. Exit")
        choice = input("Enter your choie: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            sort_tasks_by_deadline(tasks)
        elif choice == "7":
            display_overdue_tasks(tasks)
        elif choice == "8":
            print("Exciting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()



                                    
                                                  
 