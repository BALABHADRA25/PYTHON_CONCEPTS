import requests
#from custom_token_auth import TokenAuth
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token= token

    def __call__(self, request):
        request.headers["Authorization"]=f"Bearer {self.token}"
        return request
    

token=""
response= requests.get("https://api.github.com/user",
                       auth=TokenAuth(token))


print(response.status_code)
print(response.content)
print(response.json())
        