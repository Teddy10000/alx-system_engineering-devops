#!/usr/bin/python3
"""Making a request to a rest api accessing the list of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    bUrl = "https://jsonplaceholder.typicode.com/users"
    url = bUrl + "/" + employeeId

    response = requests.get(url)
    eName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_t = []

    for task in tasks:
        if task.get('completed'):
            done_t.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(eName, done, len(tasks)))

    for task in done_t:
        print("\t {}".format(task.get('title')))
