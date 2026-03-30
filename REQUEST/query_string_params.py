import requests

response = requests.get("https://api.github.com/search/repositories",
                        params={"q":"language:python","sort":"stars","order":"desc"},)

json_response= response.json()

print(json_response)
