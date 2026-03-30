import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token=token
    
    def __call__(self, request):
        request.headers["Authorization"]=f"Bearer {self.token}"
        return request

TOKEN=""
with requests.Session() as session:
    session.auth = TokenAuth(TOKEN)
    fs= session.get("https://api.github.com/user")
    ss=session.get("https://api.github.com/user")

print(fs.headers)
print(ss.json())