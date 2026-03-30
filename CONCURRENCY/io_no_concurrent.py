import time
import requests


def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time= time.perf_counter()
    download_all_sites(sites)
    duration= time.perf_counter()-start_time
    print(f"Downloaded {len(sites)} in {duration} seconds.")

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)

def download_site(url, session):
    response= session.get(url)
    print(f"Read {len(response.content)} from url {url}")

if __name__=="__main__":
    main()
