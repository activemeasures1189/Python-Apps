import json

file = open('users.json')
users = json.load(file)
print(users)