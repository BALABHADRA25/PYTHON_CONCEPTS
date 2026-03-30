import requests
from requests.auth import HTTPBasicAuth

response= requests.get(
    "https://httpbin.org/basic-auth/user/passwd",
    auth=HTTPBasicAuth("user","passwd")
)

print(response.status_code)
print(response.request.headers)