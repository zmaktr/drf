import requests

# endpoint = "https://httpbin.org"
endpoint = "http://localhost:8000/api/products/2000/"

get_response = requests.get(endpoint)
# params={"abc": "parms data"}

print(get_response.text)
print(get_response.json())
print(get_response.status_code) 