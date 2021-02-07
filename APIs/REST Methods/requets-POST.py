import requests

url = "https://postman-echo.com/post"
payload = "Hello Ahmed!"
headers = {'content-type': 'text/plain'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response)
print(response.text)