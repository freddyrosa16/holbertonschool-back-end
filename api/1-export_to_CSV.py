#!/usr/bin/python3
"""
Given a specific API, returns information about the user's TODO list progress
"""
import csv
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
    with open("{}.csv".format(argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([argv[1], user.get("username"), todo.get("completed"),
                          todo.get("title")]) for todo in todos]
