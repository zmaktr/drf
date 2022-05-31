import requests
import requests

# endpoint = "https://httpbin.org"
endpoint = "http://localhost:8000/api/products/"

headers = {
    'Authorization': 'token ca57f6d731ff401c373b6524c913f44cb70a7b02'
}

data={
    "title":"peach",
    "price": 2.25
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.text)
print(get_response.json())
print(get_response.status_code) 