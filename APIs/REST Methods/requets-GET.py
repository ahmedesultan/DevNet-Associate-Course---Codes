import requests

url = "https://postman-echo.com/get"
q = {"test": "123"}
headers = {}

response = requests.request("GET", url, headers=headers, params=q)
print(response)
print(response.text)