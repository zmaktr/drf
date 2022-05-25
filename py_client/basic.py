import requests

# endpoint = "https://httpbin.org"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title":"dell", "content": "hello man", "price":123})
# params={"abc": "parms data"}

print(get_response.text)
print(get_response.json())
print(get_response.status_code) 