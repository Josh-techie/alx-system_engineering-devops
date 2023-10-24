#!/usr/bin/python3
"""Returns TODO list progress for a given employee ID."""
import requests
import sys

def get_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(url).json()

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos = requests.get(url).json()

    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)

    return user, completed_tasks, total_tasks

def display_progress(user, completed_tasks, total_tasks):
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task["title"]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    user, completed_tasks, total_tasks = get_todo_progress(employee_id)
    display_progress(user, completed_tasks, total_tasks)
