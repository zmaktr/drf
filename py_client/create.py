import requests

# endpoint = "https://httpbin.org"
endpoint = "http://localhost:8000/api/products/"

data={
    "title":"bananas",
    "price":45.25
}

get_response = requests.post(endpoint, json=data)
# params={"abc": "parms data"}

print(get_response.text)
print(get_response.json())
print(get_response.status_code) 