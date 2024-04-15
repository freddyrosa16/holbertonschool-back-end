#!/usr/bin/python3
"""
Given a specific API, returns information about the user's TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    response = requests.get(url)
    todos = response.json()
    completed = [todo for todo in todos if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(completed), len(todos)))
    [print("\t {}".format(todo.get("title"))) for todo in completed]
