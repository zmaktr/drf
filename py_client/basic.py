import requests

# endpoint = "https://httpbin.org/#/Status_codes/get_status__codes/dsfsdf_"
endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, params={"abc": "parms data"}, json={"key": "value"})

print(get_response.text)
print(get_response.json())
print(get_response.status_code) 