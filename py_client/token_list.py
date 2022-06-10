import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password\n")

auth_response = requests.post(auth_endpoint, json={"username":username, "password": password })

print(auth_response.text)
print(auth_response.json())
print(auth_response.status_code) 

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {"Authorization": f"token {token}"} # make sure add space between token/bearer and {token}

    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.text)
    print(get_response.json())
    print(get_response.status_code) 
    
    # pagination

