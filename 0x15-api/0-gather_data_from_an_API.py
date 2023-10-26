#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    try:
        user = requests.get(url + "users/{}".format(employee_id)).json()
        todos = requests.get(url + "todos", params={"userId": employee_id}).json()
        
        if "name" not in user:
            print("Employee not found.")
            sys.exit(1)

        completed = [t.get("title") for t in todos if t.get("completed")]
        
        print("Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed), len(todos)))

        for task in completed:
            print("\t{}".format(task))

    except requests.RequestException as e:
        print("Error making API request:", e)
        sys.exit(1)
