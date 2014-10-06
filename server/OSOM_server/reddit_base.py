import requests
import time

TS = 0
QUERY_INTERVAL = 2

def make_get_request(url,headers=None):
    global TS
    headers = headers or {"User-Agent":"subreddit crawler made by /u/dhishkyaon"}
    while time.time() - TS < QUERY_INTERVAL:
        time.sleep(1)
    TS = time.time()
    return requests.get(url,headers=headers)
