#!/usr/bin/python3
"""Accessing an api for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    Url = "https://jsonplaceholder.typicode.com/users"
    url = Url + "/" + employeeId

    data = requests.get(url)
    username = data.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
