#!/usr/bin/python3
"""Editing employees todo list"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    bURL = "https://jsonplaceholder.typicode.com/users"
    url = bURL + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    tURL = url + "/todos"
    response = requests.get(tURL)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
