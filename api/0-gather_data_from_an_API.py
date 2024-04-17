#!/usr/bin/python3
"""information about his/her todo list progress"""
import requests
import sys


def gather_data_from_API(user_id):
    """
        Retrieves user information and tasks
        from an API based on the given user ID.
    """
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code == 200:
        user_name = response.json()["name"]
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    if response.status_code == 200:
        tasks = response.json()
        number_tasks = len(tasks)
    completed_tasks = []
    for task in tasks:
        if task["completed"]:
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, len(completed_tasks), number_tasks))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))


if __name__ == '__main__':
    """call the funcion"""
    gather_data_from_API(int(sys.argv[1]))
