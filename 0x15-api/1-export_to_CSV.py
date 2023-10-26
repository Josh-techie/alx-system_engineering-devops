#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to a CSV file."""
import requests
import csv
import sys


def export_to_csv(employee_id, tasks):
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([employee_id, task['username'],
                             str(task['completed']),
                             task['title']])

    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    try:
        user = requests.get(url + "users/{}".
                            format(employee_id)).json()
        todos = requests.get(url + "todos",
                             params={"userId": employee_id}).json()

        if "name" not in user:
            print("Employee not found.")
            sys.exit(1)
        completed_tasks = [
            {"username": user["username"], "completed": task["completed"],
             "title": task["title"]}
            for task in todos if task["completed"]
        ]

        print("Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed_tasks), len(todos)))

        for task in completed_tasks:
            print("\t{}".format(task["title"]))

        export_to_csv(employee_id, completed_tasks)

    except requests.RequestException as e:
        print("Error making API request:", e)
        sys.exit(1)
