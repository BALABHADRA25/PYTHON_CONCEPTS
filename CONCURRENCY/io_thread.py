import time
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

thread_local= threading.local()
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
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site,sites)


def download_site(url):
    session= get_session_for_thread()
    response= session.get(url)
    print(f"Read {len(response.content)} from url {url}")

def get_session_for_thread():
    if not hasattr(thread_local,"session"):
        thread_local.session= requests.Session()
    return thread_local.session

if __name__=="__main__":
    main()
