import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/users')
y=json.loads(response.text)
print(y)
username = input("enter username :")
val = None
for i in y:
        if i['username'] == username:
            val = i

print(str(val))



