#!/usr/bin/python3
"""
Using a REST API, for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users" + employee_id)
    data = response.json()
    employee_name = data['name']
    todo_request = requests.get(
        'https://jsonplaceholder.typicode.com/posts?userId=1' + employee_id)
    todos_data = response.json()
    total_todo = str(len(todos_data))
    completed_todos = str(sum(1 for task in todos_data if task['completed']))
    print("Employee " + employee_name + " is done with tasks(" +
          completed_todos + "/" + total_todo + "):")
    for task in todos_data:
        if task['completed']:
            print('\t ' + task['title'])

if __name__ == '__main__':
    pass
