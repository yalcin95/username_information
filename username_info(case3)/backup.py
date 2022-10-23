import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/users')
y=json.loads(response.text)
username = input("enter username :")
if username == "Bret":
    print(y[0])
if username == "Antonette":
    print(y[1])
if username == "Samantha":
    print(y[2])
if username == "Karianne":
    print(y[3])
if username == "Kamren":
    print(y[4])
if username == "Leopoldo_Corkery":
    print(y[5])
if username == "Elwyn.Skiles":
    print(y[6])
if username == "Maxime_Nienow":
    print(y[7])
if username == "Delphine":
    print(y[8])
if username == "Moriah.Stanton":
    print(y[9])