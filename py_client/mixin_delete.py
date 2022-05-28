import requests

# product_id = input("what is the product id you want to delete? \n")
# try:
#     product_id = int(product_id)
# except:
#     product_id = None
#     print(f"this product id is not valid")

# if product_id:
endpoint = "http://localhost:8000/api/products/mixindelete/9"

get_response = requests.delete(endpoint)


# print(get_response.text)
# print(get_response.json())
print(get_response.status_code) 
print(get_response.status_code==204)