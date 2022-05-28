import requests

# endpoint = "https://httpbin.org"
endpoint = "http://localhost:8000/api/products/mixincreate/"

data={
    "title":"plastic bottle",
    "price":2.25
}

get_response = requests.post(endpoint, json=data)

print(get_response.text)
print(get_response.json())
print(get_response.status_code) 