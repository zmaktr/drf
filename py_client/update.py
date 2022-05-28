import requests

# endpoint = "https://httpbin.org"
endpoint = "http://localhost:8000/api/products/3/update/"

data = {
    'title':'hello this world',
    'price': 33.33
}

get_response = requests.put(endpoint, json=data)


print(get_response.text)
print(get_response.json())
print(get_response.status_code) 