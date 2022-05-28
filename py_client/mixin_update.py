import requests

data = {
    "title" : "changed title mixinUpdates",
    "content" : "new content",
    "price" : 33.33,
}

endpoint = "http://localhost:8000/api/products/mixinupdate/20"

get_response = requests.put(endpoint, json=data)

print(get_response.text)
print(get_response.json)
print(get_response.status_code)