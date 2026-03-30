import requests
from requests.exceptions import HTTPError

urls= ["http://github.com", "http://github.com/bala11222"]

def check_urls():
    for url in urls:
        try: 
            response=requests.get(url)
            print(f"The response code is :: {response.status_code}")
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"Http error occured: {http_err}")
        except Exception as err:
            print(f"Other error occured:: {err}")
        else:
            print("Success")

if __name__=="__main__":
    check_urls()