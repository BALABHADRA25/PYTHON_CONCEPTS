import requests

response = requests.get("https://api.github.com")

# print(response.content)
# print(type(response.content))

#print(response.text)
#print(type(response.text)) # serlized json

print(response.json()) #    dictionary
print(type(response.json()))

print(response.headers)