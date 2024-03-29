#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    mainUrl = "https://jsonplaceholder.typicode.com/users"
    url = mainUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0 
    done_task = []

    for task in tasks:
        if task.get('completed'):
            done_task.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(employeeName, done, len(tasks)))

    for task in done_task:
        print("\t {}".format(task.get('title')))