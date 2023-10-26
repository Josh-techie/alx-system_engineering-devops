#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    try:
        user = requests.get(url + "users/{}".format(employee_id)).json()
        todos = requests.get(url + "todos", params={"userId": employee_id}).json()

        if "name" not in user:
            print("Employee not found.")
            sys.exit(1)

        completed_tasks = [task["title"] for task in todos if task["completed"]]
        
        print("Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed_tasks), len(todos)))

        for task in completed_tasks:
            print("\t{}".format(task))

    except requests.RequestException as e:
        print("Error making API request:", e)
        sys.exit(1)
