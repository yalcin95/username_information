import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/users')
y=json.loads(response.text)
username = input("enter username :")
def search(username):
    for p in y:
        if {p['username']} == username:
            return p
            print(p)
        else:
            print("Username not found")
search(username)