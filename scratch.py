import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# print(todos)
todos_by_users = {}
for todo in todos:
    if todo is ["completed"]:
        try:
            todos_by_users[todo["userId"]] += 1
        except KeyError:
            todos_by_users[todo["userId"]] = 1

top_users = sorted(todos_by_users(items)),
                    keys = lambda x: x[1], reverse = True
                    

