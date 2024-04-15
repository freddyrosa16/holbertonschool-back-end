#!/usr/bin/python3
"""
Given a specific API, returns information about the user's TODO list progress
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{"task": todo.get("title"),
                                     "completed": todo.get("completed"),
                                     "username": user.get("username")} for todo in todos
                                    if user.get("id") == todo.get("userId")]
                  for user in users}, jsonfile)
